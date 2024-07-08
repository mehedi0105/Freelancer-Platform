from django.shortcuts import render
from rest_framework.views import APIView
from . import models
from .import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.

class JobListAPIView(APIView):
    def get(self, request ,format = None):
        jobs = models.AddJob.objects.all()
        serializer = serializers.AddPostSerializers(jobs, many= True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = serializers.AddPostSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class JobDetailsAPIView(APIView):
    def get_object(self, pk):
        try:
            return models.AddJob.objects.get(pk=pk)
        except models.AddJob.DoesNotExist:
            return Http404
    
    def get(self, request,pk, format= None):
        jobs = self.get_object(pk)
        serializer = serializers.AddPostSerializers(jobs)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        jobs = self.get_object(pk)
        serializer = serializers.AddPostSerializers(jobs, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
         jobs = self.get_object(pk)
         jobs.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
    
class ReveiwListAPIView(APIView):
    def get_object(self, pk):
        try:
            return models.Reveiw.objects.get(pk=pk)
        except models.Reveiw.DoesNotExist:
            return Http404
    
    def get(self, request,pk, format= None):
        reviwe = self.get_object(pk)
        serializer = serializers.ReviewSerializers(reviwe)
        return Response(serializer.data)
    
    def put(self,request,pk,format=None):
        reviwe = self.get_object(pk)
        serializer = serializers.ReviewSerializers(reviwe, data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
         reviwe = self.get_object(pk)
         reviwe.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
    
class AllReveiwListAPIView(APIView):
    def get(self, request ,format = None):
        jobs = models.Reveiw.objects.all()
        serializer = serializers.ReviewSerializers(jobs, many= True)
        return Response(serializer.data)
    
#     def post(self, request, format = None):
#         serializer = serializers.AddPostSerializers(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

