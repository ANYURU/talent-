from django.urls import path, include
app_name = "v1"
from . import views


urlpatterns = [
    path("v1/", views.index, name='index')
]
