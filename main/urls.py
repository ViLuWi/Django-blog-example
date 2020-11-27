from django.urls import path
from .views import *    # import all views from views.py file


urlpatterns = [
    path('', index, name="index"),
    path('register', register, name="register"),
    path('new-post', new_post, name="new_post"),
]