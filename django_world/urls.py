from django.urls import path
from . import views

# this is a tuple where the views and URLs are connected or mapped
urlpatterns = [
    path('', views.index, name='index'),
]
