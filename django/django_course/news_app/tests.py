from django.test import TestCase
from django.contrib.auth.models import User

from .models import News, Comment

class NewsModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='test12345'
        )

    def test_create_news(self):
        news = News.objects.create(
            title='Тестовая новость',
            content='Текст новости',
            author=self.user
        )
        self.assertEqual(news.title, 'Тестовая новость')


class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='test12345'
        )
        self.news = News.objects.create(
            title='Новость',
            content='Текст',
            author=self.user
        )
        
    def test_create_comment(self):
        comment = Comment.objects.create(
            news=self.news,
            user=self.user,
            text='Комментарий'
        )
        self.assertEqual(comment.text, 'Комментарий')

class ViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='test12345'
        )
        self.news = News.objects.create(
            title='Новость',
            content='Текст',
            author=self.user
        )
        
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_news_list_page(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)
        
    def test_news_detail_page(self):
        response = self.client.get(
            f'/news/{self.news.id}/'
        )
        self.assertEqual(response.status_code, 200)
