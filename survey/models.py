from django.db import models
from django.urls import reverse
import datetime

# Create your models here.

class SurveyQuestionAlternative(models.Model):
    resposta = models.CharField(max_length=100)

    def __str__(self):
        return self.resposta


class SurveyQuestion(models.Model):
    pergunta = models.CharField(max_length=100, blank=True, null=True)
    resposta = models.ManyToManyField(SurveyQuestionAlternative)

    def __str__(self):
        return self.pergunta


class Survey(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    questoes = models.ManyToManyField(SurveyQuestion)

    def __str__(self):
        return self.titulo


class SurveyUserAnswer(models.Model):
    nome = models.CharField(max_length=300, blank=True, null=True)
    pesquisa = models.ForeignKey(Survey, on_delete=models.CASCADE)
    questao = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    resposta = models.ForeignKey(SurveyQuestionAlternative, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}: {self.pesquisa.titulo} - {self.questao.pergunta}"
