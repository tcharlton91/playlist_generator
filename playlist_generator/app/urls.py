from django.urls import path

from . import views

urlpatterns = [
        path('basic', views.basicView),
        path('library', views.libraryView),
        path('libraryTemp', views.libraryTemplateView),
        path('mix', views.mixView),
        path('recommended', views.recommendedView),
        path('', views.basicView),
        ]
