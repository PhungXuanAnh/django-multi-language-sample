from django.contrib import admin
from django.urls import path

from .models import Choice, Question

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
