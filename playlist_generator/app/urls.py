from django.urls import path

from . import views

urlpatterns = [
        path('basic', views.basicView),
        path('', views.basicView),
        ]
