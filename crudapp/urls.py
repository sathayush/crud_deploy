from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter(trailing_slash=False)
router.register('student', StudentViewset)



urlpatterns=[
    path('', include(router.urls)),
#     # path('student_post/',StudentPostView.as_view()),
#     # path('student_get/',StudentGetView.as_view()),
#     # path('student_update/<int:id>/',StudentUpdateView.as_view()),
#     # path('student_delete/<int:id>/',StudentDeleteView.as_view()),

]
