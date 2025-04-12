from django.urls import path

from .views import (WelcomeView,
                    AboutTokyoView,
                    PopularPlacesView,
                    TokyoView,
                    )

urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('about', AboutTokyoView.as_view(), name='about'),
    path('places', PopularPlacesView.as_view(), name='places'),
    path('tokyo', TokyoView.as_view(), name='tokyo'),
]
