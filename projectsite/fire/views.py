from django.shortcuts import render
from django.views.generic.list import ListView
from fire.models import Locations, Incident, FireStation 
from django.db import connection
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth
from django.db.models import Count
from datetime import datetime


class HomePageView(ListView):
    model = Locations
    context_object_name = 'home'
    template_name = "home.html"
