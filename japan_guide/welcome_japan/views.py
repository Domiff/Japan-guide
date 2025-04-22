from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView

from .models import PlacesModel


class WelcomeView(View):
    def get(self, request):
        return render(request, 'welcome_japan/welcome.html')


class AboutTokyoView(View):
    def get(self, request):
        return render(request, 'welcome_japan/about_japan.html')


class PopularPlacesView(View):
    def get(self, request: HttpRequest):
        context = {
            'places': PlacesModel.objects.get(name='Токио'),
        }
        return render(request, 'welcome_japan/popular_places.html', context=context)


class TokyoView(View):
    def get(self, request):
        return render(request, 'welcome_japan/tokyo.html')
