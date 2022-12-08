from django.urls import path, include
app_name = "v1"
from . import views


urlpatterns = [
    path("v1/", views.index, name='index'),
    # path("v1/snippets/", views.snippet_list),
    # path("v1/snippets/<int:pk>/", views.snippet_detail)
]
