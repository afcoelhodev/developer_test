from rest_framework import serializers
from .models import SurveyQuestionAlternative, SurveyQuestion, Survey

class SurveyQuestionAlternativeSerializer(serializers.ModelSerializer):

    class Meta:
        model = SurveyQuestionAlternative
        fields = '__all__'


class SurveyQuestionSerializer(serializers.ModelSerializer):
    resposta = SurveyQuestionAlternative.objects.prefetch_related('resposta')

    class Meta:
        model = SurveyQuestion
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    questoes = SurveyQuestion.objects.prefetch_related('pergunta')

    class Meta:
        model = Survey
        fields = '__all__'
