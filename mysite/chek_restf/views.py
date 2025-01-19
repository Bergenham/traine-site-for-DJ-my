from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from django.contrib.auth.models import Group
from .serialization import GroupSerializer

@api_view()
def hello_world_view(request: Request) -> Response:
    return Response({'body_say': "I say: Hello World"})

class GroupListView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
