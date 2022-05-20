from django.db import models
from django.urls import reverse_lazy
# from django.contrib.auth.models import User


class Skill(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Навык')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
        ordering = ['title']


class Language(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Язык')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'
        ordering = ['title']


class Hobby(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Увлечение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Увлечение'
        verbose_name_plural = 'Увлечения'
        ordering = ['title']


class UserProfile(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=150, verbose_name='Отчество')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')
    skill = models.ManyToManyField(Skill)
    language = models.ManyToManyField(Language)
    hobby = models.ManyToManyField(Hobby)

    def get_absolute_url(self):
        return reverse_lazy('view_user', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-created_at']




