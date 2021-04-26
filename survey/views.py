from django.shortcuts import render, redirect
from .models import SurveyQuestionAlternative, SurveyQuestion, Survey, SurveyUserAnswer

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime

def home(request):
    return render (request, 'home.html')
