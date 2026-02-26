from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminMixin

from .models import SlideItem


@admin.register(SlideItem)
class SlideItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'thumb_preview', 'order')
    readonly_fields = ('thumb_preview',)

    def thumb_preview(self, obj):
        if not obj.image_id:
            return '—'
        return format_html(
            '<img src="{}" alt="{}" style="max-height:80px;object-fit:cover;">',
            obj.image.url,
            obj.title,
        )

    thumb_preview.short_description = 'Превью'
