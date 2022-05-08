from django.urls import path, include
from .index import index


app_name = '{{ app_name }}'

urlpatterns = [
    path('', index)
]