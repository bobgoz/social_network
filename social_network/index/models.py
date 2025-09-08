from django.db import models


class News(models.Model):
    """Модель Новости"""

    title = models.CharField(
        'Название',
        max_length=64,
    )
    content = models.TextField(
        'Описание',
    )
    created_at = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
    )
    update_at = models.DateTimeField(
        'Дата обновления',
        auto_now=True,
    )
    image = models.ImageField(
        'Изображение',
        upload_to='arcticles/%Y/%m/%d/',
        blank=True,
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
