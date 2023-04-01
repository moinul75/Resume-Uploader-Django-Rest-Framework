from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import status

# Create your views here.
#create api with django rest framework with  APiVIew | Only upload(Post) and view the resume( Get)
class ProfileView(APIView):
    #create post 
    def post(self,request,format=None):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Successfully Uploaded Resume','status':status.HTTP_201_CREATED,'Data':serializer.data})
        return Response(serializer.errors)
    
    #get all the Applying resume 
    def get(self,request,format=None):
        candidates = Profile.objects.all()
        serializer = ProfileSerializer(candidates,many=True)
        return Response({'message':'success','status':status.HTTP_200_OK,'data':serializer.data})
    



