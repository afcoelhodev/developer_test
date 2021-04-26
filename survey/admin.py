from django.contrib import admin
from .models import SurveyQuestionAlternative, SurveyQuestion, Survey, SurveyUserAnswer

# Register your models here.

admin.site.register (SurveyQuestionAlternative)
admin.site.register (SurveyQuestion)
admin.site.register (Survey)
admin.site.register (SurveyUserAnswer)
