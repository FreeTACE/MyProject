from django.db import models
from django.urls import reverse

class Category(models.Model):
    """Категория/Тема"""
    name = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL', max_length=100, unique=True)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to='categories/', blank=True, null=True)
    order = models.IntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активна', default=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.slug])


class Lesson(models.Model):
    """Урок"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='lessons', verbose_name='Тема')
    name = models.CharField('Название', max_length=200)
    slug = models.SlugField('URL', max_length=200, unique=True)
    description = models.TextField('Описание', blank=True)
    content = models.TextField('Содержание урока')
    video_url = models.URLField('Ссылка на видео', blank=True)
    order = models.IntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активен', default=True)
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлен', auto_now=True)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['category', 'order', 'created_at']

    def __str__(self):
        return f"{self.category.name} - {self.name}"

    def get_absolute_url(self):
        return reverse('lesson_detail', args=[self.category.slug, self.slug])


class Card(models.Model):
    """Карточка для запоминания"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='cards', verbose_name='Урок')
    question = models.TextField('Вопрос')
    answer = models.TextField('Ответ')
    hint = models.TextField('Подсказка', blank=True)
    order = models.IntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активна', default=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
        ordering = ['lesson', 'order', 'created_at']

    def __str__(self):
        return f"{self.lesson.name} - {self.question[:50]}"