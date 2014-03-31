from django.contrib import admin
from models import TraineeTrained


class TraineeTrainingInline(admin.TabularInline):
    model = TraineeTrained


class TrainingAdmin(admin.ModelAdmin):
    fieldsets = [(None,  {'fields': ['date', 'block', 'donor', 'partner', 'module', 'days', 'trainers']
                          }
                  )]
    inlines = [TraineeTrainingInline,]
    list_display = ('date', 'block', 'partner', 'module',)
    search_fields = ['block']
