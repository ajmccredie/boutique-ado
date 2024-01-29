from django import path
from . import views

urlpattern = [
    path('', views.profile, name='profile')
]