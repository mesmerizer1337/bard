from django.contrib import admin
from .models import Todogit

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'status')
    list_filter = ('status', 'due_date')
    search_fields = ('title', 'description')
