from django.urls import path

from .views import WelcomeView, AboutTokyoView

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('about', AboutTokyoView.as_view(), name='about'),
]
