# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.


# def homePageView(request):
#     return HttpResponse(" HI WE ARE LEARNING DJANGO")

class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"
