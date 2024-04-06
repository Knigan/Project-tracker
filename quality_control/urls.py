from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    #path('bugs/', views.bugreports_list, name='bugreports_list'),
    path('bugs/', views.BugReportsListView.as_view(), name='bugreports_list'),
    #path('bugs/<int:bugreport_id>/', views.bugreport_detail, name='bugreport_detail'),
    path('bugs/<int:bugreport_id>/', views.BugReportDetailView.as_view(), name='bugreport_detail'),
    #path('features/', views.featurerequests_list, name='featurerequests_list'),
    path('features/', views.FeatureRequestsListView.as_view(), name='featurerequests_list'),
    #path('features/<int:featurerequest_id>/', views.featurerequest_detail, name='featurerequest_detail'),
    path('features/<int:featurerequest_id>/', views.FeatureRequestDetailView.as_view(), name='featurerequest_detail'),
    #path('bugs/project/<int:project_id>/task/<int:task_id>/create', views.create_bugreport, name='create_bugreport'),
    path('bugs/project/<int:project_id>/task/<int:task_id>/create', views.BugReportCreateView.as_view(), name='create_bugreport'),
    #path('features/project/<int:project_id>/task/<int:task_id>/create', views.create_featurerequest, name='create_featurerequest'),
    path('features/project/<int:project_id>/task/<int:task_id>/create', views.FeatureRequestCreateView.as_view(), name='create_featurerequest'),
    #path('bugs/<int:bugreport_id>/update', views.update_bugreport, name='update_bugreport'),
    path('bugs/<int:bugreport_id>/update', views.BugReportUpdateView.as_view(), name='update_bugreport'),
    #path('features/<int:featurerequest_id>/update', views.update_featurerequest, name='update_featurerequest'),
    path('features/<int:featurerequest_id>/update', views.FeatureRequestUpdateView.as_view(), name='update_featurerequest'),
    #path('bugs/<int:bugreport_id>/delete', views.delete_bugreport, name='delete_bugreport'),
    path('bugs/<int:bugreport_id>/delete', views.BugReportDeleteView.as_view(), name='delete_bugreport'),
    #path('features/<int:featurerequest_id>/delete', views.delete_featurerequest, name='delete_featurerequest'),
    path('features/<int:featurerequest_id>/delete', views.FeatureRequestDeleteView.as_view(), name='delete_featurerequest'),
]