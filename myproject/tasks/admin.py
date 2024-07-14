from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'estado', 'fecha_de_creacion', 'user')
    list_filter = ('estado', 'user')
    search_fields = ('titulo', 'descripcion')
    actions = ['mark_as_completed']

    @admin.action(description='Marcar tareas seleccionadas como completadas.')
    def mark_as_completed(self, request, queryset):
        queryset.update(estado='completed')