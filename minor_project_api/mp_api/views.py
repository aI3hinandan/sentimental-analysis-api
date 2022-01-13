from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from . import models
from . import serializers
from rest_framework import views

from .backend.get_data import getRecentNews
from .models import FollowList


class Register(views.APIView):
    def post(self, request: Request):
        username, password = request.query_params['username'], request.query_params['password']
        try:
            user = User.objects.create_user(username=username, password=password)
        except:
            return Response("Please Try again")
        FollowList(user=user, followList="")
        return Response("Success")


class ApiResponse(views.APIView):

    def get(self, request: Request):
        q = request.query_params['query']
        result = getRecentNews(q)
        results = SentimentSerializer(result, many=False).data
        return Response(results)



@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
class Watchlist(views.APIView):
    def post(self, request: Request):
        name = request.query_params['company_name']
        fl = FollowList.objects.get(user=request.user)
        flString = fl.followList
        fl.followList = fl.followList + name
        fl.save()
        return Response("saved")


    def get(self, request: Request):
        try:
            fl = FollowList.objects.get(user=request.user)
        except:
            return Response([])
        #res = {"followList":  fl.followList.split("::")}
        return Response("TODO")