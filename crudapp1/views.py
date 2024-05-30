from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class UserPostView(generics.GenericAPIView):
    serializer_class=UserSerializer
    def post(self,request):
        Userdata=UserSerializer(data=request.data)
        Userdata.is_valid()
        x=Userdata.save()
        return Response(UserSerializer(x).data) 