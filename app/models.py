from django.db import models
from django.views.generic.dates import timezone_today


class Promo(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128)
    is_active = models.BooleanField(default=False, verbose_name='Активно')
    html = models.TextField()

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=128)
    date = models.DateField(verbose_name='Дата')
    html = models.TextField()

    def save(self, **kwargs):
        if self.id is None:
            self.date = timezone_today()
        super().save(**kwargs)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128)
    image = models.ImageField()
    url = models.URLField(verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Document(models.Model):
    file = models.FileField(verbose_name='Файл')
    name = models.CharField(verbose_name='Название', default='', max_length=128)
    slug = models.SlugField(verbose_name='Идентификатор', unique=True)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return self.name
