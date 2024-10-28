from django.db import models

class Review(models.Model):
    company = models.CharField('Компания', max_length=50)
    review  = models.CharField('Отзыв', max_length=250)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
