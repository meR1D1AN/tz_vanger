from django.views.generic import TemplateView

from gallery.models import SlideItem


class SliderPage(TemplateView):
    template_name = 'gallery/landing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = SlideItem.objects.all()
        return context
