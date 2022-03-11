import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import *
from .models import *
import requests
import json

def home(request):
  return render(request, 'home.html', {})