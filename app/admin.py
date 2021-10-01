from django.contrib import admin
from .models import Subject, Problem, Choice


class ChoineInLine(admin.StackedInline):
    model = Choice
    extra = 4

class ProblemAdmin(admin.ModelAdmin):
    inlines = [ChoineInLine]


admin.site.register(Subject)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Choice)