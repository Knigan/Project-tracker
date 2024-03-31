from django.contrib import admin
from .models import BugReport, FeatureRequest

# Register your models here.

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'project', 'task')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'project', 'task')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'    