from django.urls import path,include
from .views import *




urlpatterns=[
    path('user_post/',UserPostView.as_view()),

]