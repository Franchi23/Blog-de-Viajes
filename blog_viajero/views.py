from django.views.generic import TemplateView


class HomeView(TemplateView):               #Vista basada en clases
    template_name="index.html"              