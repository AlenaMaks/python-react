from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import News, Comment
from .forms import CommentForm, NewsForm


def home(request):
    latest_news = News.objects.order_by('-created_at')[:3]

    return render(request, 'home.html', {'latest_news': latest_news})


def contacts(request):
    return render(request, 'contacts.html')


def news_list(request):
    search = request.GET.get('search', '')
    sort = request.GET.get('sort', 'new')

    news = News.objects.all()

    if search:
        news = news.filter(title__icontains=search)

    news = news.order_by('created_at' if sort == 'old' else '-created_at')

    return render(request, 'news/news_list.html', {
        'news_list': news,
        'search': search,
        'sort': sort
    })


def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    comments = Comment.objects.filter(news=news, is_active=True)

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.user = request.user
            comment.save()

            return redirect('news_detail', news_id=news.id)
    else:
        form = CommentForm()

    return render(request, 'news/news_detail.html', {
        'news': news,
        'comments': comments,
        'form': form
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    comments = Comment.objects.filter(user=request.user)

    return render(request, 'profile.html', {'comments': comments})


@login_required
def create_news(request):
    if not request.user.is_staff:
        return redirect('home')

    if request.method == 'POST':
        form = NewsForm(request.POST)

        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()

            return redirect('news_detail', news_id=news.id)
    else:
        form = NewsForm()

    return render(request, 'news/create_news.html', {'form': form})


@login_required
def edit_news(request, news_id):
    news = get_object_or_404(News, id=news_id)

    if not request.user.is_staff:
        return redirect('home')

    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)

        if form.is_valid():
            form.save()
            return redirect('news_detail', news_id=news.id)
    else:
        form = NewsForm(instance=news)

    return render(request, 'news/edit_news.html', {
        'form': form,
        'news': news
    })


@login_required
def delete_news(request, news_id):
    news = get_object_or_404(News, id=news_id)

    if not request.user.is_staff:
        return redirect('home')

    if request.method == 'POST':
        news.delete()
        return redirect('news_list')

    return render(request, 'news/delete_news.html', {'news': news})