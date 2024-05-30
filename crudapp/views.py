from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all() 
    serializer_class = StudentSerializer 
    # pagination_class=PageNumberPagination    

    

# Create your views here.

# class StudentPostView(generics.GenericAPIView):
#     serializer_class=StudentSerializer

#     def post(self,request):
#         a=StudentSerializer(data=request.data)
#         a.is_valid()
#         b=a.save()
#         return Response(StudentSerializer(b).data)
    

# class StudentGetView(APIView): 
#     def get(self,requset):
#         a=Student.objects.all()
#         return Response(StudentSerializer(a,many=True).data)  


# class StudentUpdateView(generics.GenericAPIView):
#     serializer_class=StudentSerializer 
#     def put(self,request,id):
#         a=Student.objects.get(id=id) 
#         b=StudentSerializer(a,data=request.data)
#         b.is_valid()
#         c=b.save()
#         return Response(StudentSerializer(c).data) 

 

# class StudentDeleteView(generics.GenericAPIView):
#     def delete(self,request,id):
#          a=Student.objects.get(id=id)
#          a.delete()
#          return Response("deleted")
    



