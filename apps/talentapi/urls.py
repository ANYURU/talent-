from django.urls import path
from .views import endpoints
from apps.talentapi.api.v1.views import snippet_list, snippet_detail

urlpatterns = [
    path('', endpoints),
    path("snippets/", snippet_list),
    path("snippets/<int:pk>/", snippet_detail) 
]
