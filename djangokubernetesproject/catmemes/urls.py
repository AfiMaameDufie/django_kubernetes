from django.urls import path
from .views import cat_meme_generator

app_name = 'catmemes'

urlpatterns = [
    path('', cat_meme_generator, name='cat_meme_generator'),
]
