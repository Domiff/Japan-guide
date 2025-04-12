from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View


class WelcomeView(View):
    def get(self, request):
        # if request.method == 'GET':
        #     url = reverse(request.path)
        #     return redirect(url)
        return render(request, 'welcome_japan/welcome.html')


class AboutTokyoView(View):
    def get(self, request):
        return render(request, 'welcome_japan/about_tokyo.html')
