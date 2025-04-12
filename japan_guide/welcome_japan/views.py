from django.shortcuts import render
from django.views.generic import View


class WelcomeView(View):
    def get(self, request):
        return render(request, 'welcome_japan/welcome.html')


class AboutTokyoView(View):
    def get(self, request):
        return render(request, 'welcome_japan/about_japan.html')


class PopularPlacesView(View):
    def get(self, request):
        return render(request, 'welcome_japan/popular_places.html')


class TokyoView(View):
    def get(self, request):
        return render(request, 'welcome_japan/tokyo.html')