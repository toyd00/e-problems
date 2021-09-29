from django.contrib import admin
from .models import Subject, Problem, Choice


admin.site.register(Subject)
admin.site.register(Problem)
admin.site.register(Choice)