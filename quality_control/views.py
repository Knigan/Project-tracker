from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BugReport, FeatureRequest
from .forms import BugReportForm, FeatureRequestForm
from tasks.models import Project, Task
from django.urls import reverse, reverse_lazy

# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')

class BugReportsListView(ListView):
    model = BugReport
    template_name = 'quality_control/bugs_list.html'

class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bugreport_id'
    template_name = 'quality_control/bugreport_detail.html'

class FeatureRequestsListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/features_list.html'

class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = "feature_request_id"
    template_name = 'quality_control/feature_detail.html'

class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bugreport_create.html'
    success_url = reverse_lazy('quality_control:bugs_list')

    def form_valid(self, form):
        form.instance.project = get_object_or_404(Project, pk=self.kwargs['project_id'])
        form.instance.task = get_object_or_404(Task, pk=self.kwargs['task_id'])
        return super().form_valid(form)


class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_create.html'
    success_url = reverse_lazy('quality_control:features_list')

    def form_valid(self, form):
        form.instance.project = get_object_or_404(Project, pk=self.kwargs['project_id'])
        form.instance.task = get_object_or_404(Task, pk=self.kwargs['task_id'])
        return super().form_valid(form)


class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bugreport_update.html'
    pk_url_kwarg = 'bugreport_id'
    success_url = reverse_lazy('quality_control:bugs_list')

class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_update.html'
    pk_url_kwarg = 'feature_request_id'
    success_url = reverse_lazy('quality_control:features_list')

class BugReportDeleteView(DeleteView):
    model = BugReport
    template_name = 'quality_control/bugreport_confirm_delete.html'
    pk_url_kwarg = 'bugreport_id'
    success_url = reverse_lazy('quality_control:bugs_list')

class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    template_name = 'quality_control/feature_request_confirm_delete.html'
    pk_url_kwarg = 'feature_request_id'
    success_url = reverse_lazy('quality_control:features_list')
