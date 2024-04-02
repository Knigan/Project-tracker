from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugReportsListView.as_view(), name='bugreports_list'),
    path('bugs/<int:bugreport_id>/', views.BugReportDetailView.as_view(), name='bugreport_detail'),
    path('features/', views.FeatureRequestsListView.as_view(), name='features_list'),
    path('features/<int:feature_request_id>/', views.FeatureRequestDetailView.as_view(), name='feature_detail'),
    path('bugs/project/<int:project_id>/task/<int:task_id>/create', views.BugReportCreateView.as_view(), name='bugreport_create'),
    path('features/project/<int:project_id>/task/<int:task_id>/create', views.FeatureRequestCreateView.as_view(), name='feature_request_create'),
    path('bugs/<int:bugreport_id>/update', views.BugReportUpdateView.as_view(), name='bugreport_update'),
    path('features/<int:feature_request_id>/update', views.FeatureRequestUpdateView.as_view(), name='feature_request_update'),
    path('bugs/<int:bugreport_id>/delete', views.BugReportDeleteView.as_view(), name='bugreport_delete'),
    path('features/<int:feature_request_id>/delete', views.FeatureRequestDeleteView.as_view(), name='feature_request_delete'),
]