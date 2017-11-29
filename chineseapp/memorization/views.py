from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"
    # def get(self, request, **kwargs):
    #     return render(request, 'home.html', context=None)
class AboutPageView(TemplateView):
    template_name = "about.html"