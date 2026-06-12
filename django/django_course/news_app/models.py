from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название'
    )

    content = models.TextField(
        verbose_name='Содержание'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Ссылка на изображение'
    )

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        verbose_name='Новость'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    text = models.TextField(
        max_length=1000,
        verbose_name='Комментарий'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен'
    )

    def __str__(self):
        return f'{self.user.username} - {self.news.title}'
