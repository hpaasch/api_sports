from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

import json  # built in python library. we use to convert dict to str (.dumps, .loads)

# Create your views here.

class PlayerListAPIView(View):  # the most basic view. no forms. no templates. no redirects. data in, data out

    def get(self, request):
        data = {'name': 'Hope'}
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')  #keyword arg to complete conversion
