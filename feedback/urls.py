from django.urls import path

from .views import *

urlpatterns = [
    path('', post_feedback, name="feedback"),
]
