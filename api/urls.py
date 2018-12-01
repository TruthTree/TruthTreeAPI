from django.urls import path

from . import views

app_name = "api"
urlpatterns = [
    # /api/
    path('', views.index, name='index'),
]
