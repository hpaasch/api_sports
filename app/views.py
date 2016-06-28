from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from rest_framework import generics  # listAPI basic view

import json  # built in python library. we use to convert dict to str (.dumps, .loads)
from app.models import Player
from app.serializers import PlayerSerializer

# Create your views here.

class XPlayerListAPIView(View):  # the most basic view. no forms. no templates. no redirects. data in, data out

    def get(self, request):
        data = list(Player.objects.all().values())  # converted to dicttionary values, and a list
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')  #keyword arg to complete conversion

# class PlayerListAPIView(generics.ListAPIView):
class PlayerListAPIView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer   #this is a class i'm going to Create


# class PlayerDetailAPIView(generics.RetrieveAPIView):  # note that it's not DetailAPIView

class PlayerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):  # note that it's not DetailAPIView
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer   #this is a class i'm going to Create
