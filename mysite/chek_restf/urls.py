from django.urls import path
from .views import hello_world_view, GroupListView

app_name = 'chek_restf'

urlpatterns = [
path('h_w/', hello_world_view, name='hello_world_r'),
path('grouplist/', GroupListView.as_view(), name='group_list'),
]