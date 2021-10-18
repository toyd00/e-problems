from django.contrib import admin
from .models import Subject, Problem, Choice, Type


class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 0

class ProblemAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]


admin.site.register(Subject)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Choice)
admin.site.register(Type)