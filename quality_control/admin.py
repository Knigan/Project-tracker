from django.contrib import admin
from .models import BugReport, FeatureRequest

# Register your models here.

@admin.action(description='Mark selected bugreports as "New"')
def bugreport_status_new(modeladmin, request, queryset):
    queryset.update(status="New")

@admin.action(description='Mark selected bugreports as "In progress"')
def bugreport_status_in_progress(modeladmin, request, queryset):
    queryset.update(status="In progress")

@admin.action(description='Mark selected bugreports as "Completed"')
def bugreport_status_completed(modeladmin, request, queryset):
    queryset.update(status="Completed")

@admin.action(description='Mark selected feature requests as "Review"')
def featurerequest_status_review(modeladmin, request, queryset):
    queryset.update(status="Review")

@admin.action(description='Mark selected feature requests as "Accepted"')
def featurerequest_status_accepted(modeladmin, request, queryset):
    queryset.update(status="Accepted")

@admin.action(description='Mark selected feature requests as "Rejected"')
def featurerequest_status_rejected(modeladmin, request, queryset):
    queryset.update(status="Rejected")

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'project', 'task')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    actions = [bugreport_status_new, bugreport_status_in_progress, bugreport_status_completed]


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'project', 'task')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    actions = [featurerequest_status_review, featurerequest_status_accepted, featurerequest_status_rejected]