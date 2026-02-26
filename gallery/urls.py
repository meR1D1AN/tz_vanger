from django.urls import path

from gallery.apps import GalleryConfig
from gallery.views import SliderPage

app_name = GalleryConfig.name

urlpatterns = [
    path('', SliderPage.as_view(), name='landing'),
]
