from django.urls import path

from . import views

urlpatterns = [
        path('basic', views.basicView),
        path('base', views.baseView),
        path('library', views.libraryView),
        path('libraryTemp', views.libraryTemplateView),
        path('mix', views.mixView),
        path('mixTemp', views.mixTemplateView),
        path('recommended', views.recommendedView),
        path('', views.basicView),
        ]
