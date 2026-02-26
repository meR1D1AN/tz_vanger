from django.db import models
from filer.fields.image import FilerImageField


class SlideItem(models.Model):
    title = models.CharField(
        verbose_name='Название изображения',
        max_length=250,
        help_text='Короткое название или подпись к изображению',
    )
    image = FilerImageField(
        verbose_name='Изображение',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='slide_items',
    )
    order = models.PositiveIntegerField(
        verbose_name='Порядок',
        default=0,
        help_text='Чем меньше цифра, тем выше слайд в списке',
    )
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Элемент слайдера'
        verbose_name_plural = 'Элементы слайдера'
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title
