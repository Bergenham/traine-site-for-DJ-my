from django.urls import path
from .views import index, bio_user, hzwat, main

app_name = 'requestdataapp'

urlpatterns = [
    path('', main, name='index'),
    path('bio/', bio_user, name='bio_user'),
    path('hzwat/', hzwat, name='hzwat'),
]
