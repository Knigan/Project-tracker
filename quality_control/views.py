from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BugReport, FeatureRequest
from .forms import BugReportForm, FeatureRequestForm
from tasks.models import Project, Task
from django.urls import reverse, reverse_lazy

# Create your views here.

def index(request):
    return render(request, 'quality_control/index.html')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')

def bugreports_list(request):
    bugreports = BugReport.objects.all()
    return render(request, 'quality_control/bugreports_list.html', {'bugreport_list': bugreports})

class BugReportsListView(ListView):
    model = BugReport
    template_name = 'quality_control/bugreports_list.html'

def bugreport_detail(request, bugreport_id):
    bugreport = get_object_or_404(BugReport, id=bugreport_id)
    return render(request, 'quality_control/bugreport_detail.html', {'bugreport': bugreport})

class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bugreport_id'
    template_name = 'quality_control/bugreport_detail.html'

def featurerequests_list(request):
    featurerequests = FeatureRequest.objects.all()
    return render(request, 'quality_control/featurerequests_list.html', {'bugreport_list': featurerequests})

class FeatureRequestsListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/featurerequests_list.html'

def featurerequest_detail(request, featurerequest_id):
    featurerequest = get_object_or_404(BugReport, id=featurerequest_id)
    return render(request, 'quality_control/featurerequest_detail.html', {'featurerequest': featurerequest})   

class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = "featurerequest_id"
    template_name = 'quality_control/featurerequest_detail.html'

def create_bugreport(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugreports_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bugreport_create.html', {'form': form})

class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bugreport_create.html'
    success_url = reverse_lazy('quality_control:bugreports_list')

    def form_valid(self, form):
        form.instance.project = get_object_or_404(Project, pk=self.kwargs['project_id'])
        form.instance.task = get_object_or_404(Task, pk=self.kwargs['task_id'])
        return super().form_valid(form)

def create_featurerequest(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:featurerequests_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/featurerequest_create.html', {'form': form})

class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/featurerequest_create.html'
    success_url = reverse_lazy('quality_control:featurerequests_list')

    def form_valid(self, form):
        form.instance.project = get_object_or_404(Project, pk=self.kwargs['project_id'])
        form.instance.task = get_object_or_404(Task, pk=self.kwargs['task_id'])
        return super().form_valid(form)

def update_bugreport(request, bugreport_id):
    bugreport = get_object_or_404(BugReport, pk=bugreport_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bugreport)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugreport_detail', bugreport_id=bugreport.id)
    else:
        form = BugReportForm(instance=bugreport)
    return render(request, 'quality_control/bugreport_update.html', {'form': form, 'bugreport': bugreport})

class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bugreport_update.html'
    pk_url_kwarg = 'bugreport_id'
    success_url = reverse_lazy('quality_control:bugreports_list')

def update_featurerequest(request, featurerequest_id):
    featurerequest = get_object_or_404(FeatureRequest, pk=featurerequest_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=featurerequest)
        if form.is_valid():
            form.save()
            return redirect('quality_control:featurerequest_detail', featurerequest_id=featurerequest.id)
    else:
        form = BugReportForm(instance=featurerequest)
    return render(request, 'quality_control/featurerequest_update.html', {'form': form, 'featurerequest': featurerequest})

class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/featurerequest_update.html'
    pk_url_kwarg = 'featurerequest_id'
    success_url = reverse_lazy('quality_control:featurerequests_list')

def delete_bugreport(request, bugreport_id):
    bugreport = get_object_or_404(Project, pk=bugreport_id)
    bugreport.delete()
    return redirect('quality_control:bugreports_list')

class BugReportDeleteView(DeleteView):
    model = BugReport
    template_name = 'quality_control/bugreport_confirm_delete.html'
    pk_url_kwarg = 'bugreport_id'
    success_url = reverse_lazy('quality_control:bugreports_list')

def delete_featurerequest(request, featurerequest_id):
    featurerequest = get_object_or_404(Project, pk=featurerequest_id)
    featurerequest.delete()
    return redirect('quality_control:featurerequests_list')

class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    template_name = 'quality_control/featurerequest_confirm_delete.html'
    pk_url_kwarg = 'featurerequest_id'
    success_url = reverse_lazy('quality_control:featurerequests_list')
