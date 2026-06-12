from django.shortcuts import render
from .models import News
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

from django.shortcuts import render, get_object_or_404

def home(request):
    latest_news = News.objects.order_by('-created_at')[:3]

    return render(
        request,
        'home.html',
        {
            'latest_news': latest_news
        }
    )

def contacts(request):
    return render(request, 'contacts.html')

def news_list(request):
    search = request.GET.get('search', '')
    sort = request.GET.get('sort', 'new')

    news = News.objects.all()

    if search:
        news = news.filter(
            title__icontains=search
        )

    if sort == 'old':
        news = news.order_by('created_at')
    else:
        news = news.order_by('-created_at')

    return render(
        request,
        'news/news_list.html',
        {
            'news_list': news,
            'search': search,
            'sort': sort
        }
    )

def news_detail(request, news_id):
    news = get_object_or_404(
        News,
        id=news_id
    )

    return render(
        request,
        'news/news_detail.html',
        {'news': news}
    )
    
def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')

    else:
        form = UserCreationForm()

    return render(
        request,
        'registration/register.html',
        {
            'form': form
        }
    )