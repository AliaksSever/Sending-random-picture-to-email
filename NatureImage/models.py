from django.db import models

class NatureImage(models.Model):
    url = models.URLField(max_length=200, verbose_name='Ссылка')
    width = models.IntegerField(default=0, verbose_name='Ширина')
    height = models.IntegerField(default=0, verbose_name='Высота')
    description = models.CharField(max_length=255, verbose_name='Описание')

    def __str__(self):
        return 'Изображение'

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'