from django.shortcuts import render
from . import serializers
from rest_framework.views import APIView
from . import models
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class ProsalAPIView(APIView):
    def get_object(self, pk):
        try:
            return models.Proposal.objects.get(pk=pk)
        except models.Proposal.DoesNotExist:
            return Response("Proposal does not exist")
    
    def get(self, request,pk, format= None):
        proposal = self.get_object(pk)
        serializer = serializers.SendProposalSerializers(proposal)
        return Response(serializer.data)
    
    def post(self, request, pk, format = None):
        proposal = self.get_object(pk)
        serializer = serializers.SendProposalSerializers(proposal)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
         proposal = self.get_object(pk)
         proposal.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
    

# def post(self, request, format = None):
#         serializer = serializers.AddPostSerializers(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)