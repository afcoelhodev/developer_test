from django.shortcuts import render, redirect
from .models import SurveyQuestionAlternative, SurveyQuestion, Survey, SurveyUserAnswer

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime
from .serializers import SurveyQuestionAlternativeSerializer, SurveyQuestionSerializer, SurveySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    return render (request, 'home.html')


@api_view(['GET'])
def SurveyList(request, format=None, **kwargs):

    alternativas = SurveyQuestionAlternative.objects.all()
    perguntas = SurveyQuestion.objects.all()
    pesquisas = Survey.objects.all()

    alternativas_serializer = SurveyQuestionAlternativeSerializer(alternativas, many=True)
    perguntas_serializer = SurveyQuestionSerializer(perguntas, many=True)
    pesquisas_serializer = SurveySerializer(pesquisas, many=True)

    return Response({
        'alternativas': alternativas_serializer.data,
        'perguntas': perguntas_serializer.data,
        'pesquisas': perguntas_serializer.data,
    })
