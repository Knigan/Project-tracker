from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Task
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProjectForm, TaskForm
from django.urls import reverse, reverse_lazy

# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/index.html')

class ProjectsListView(ListView):
    model = Project
    template_name = 'tasks/projects_list.html'

class ProjectDetailView(DetailView):
    model = Project
    pk_url_kwarg = 'project_id'
    template_name = 'tasks/project_detail.html'

class TaskDetailView(DetailView):
    model = Task
    pk_url_kwarg = 'task_id'
    template_name = 'tasks/task_detail.html'

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'tasks/project_create.html'
    success_url = reverse_lazy('tasks:projects_list')

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/add_task.html'

    def form_valid(self, form):
        form.instance.project = get_object_or_404(Project, pk=self.kwargs['project_id'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('tasks:project_detail', kwargs={'project_id': self.kwargs['project_id']})

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'tasks/project_update.html'
    pk_url_kwarg = 'project_id'
    success_url = reverse_lazy('tasks:projects_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    pk_url_kwarg = 'task_id'
    
    def get_success_url(self):
        return reverse_lazy('tasks:task_detail', kwargs={'project_id': self.object.project.id, 'task_id': self.object.id})

class ProjectDeleteView(DeleteView):
    model = Project
    pk_url_kwarg = 'project_id'
    success_url = reverse_lazy('tasks:projects_list')
    template_name = 'tasks/project_confirm_delete.html'

class TaskDeleteView(DeleteView):
    model = Task
    pk_url_kwarg = 'task_id'

    def get_success_url(self):
        return reverse_lazy('tasks:project_detail', kwargs={'project_id': self.object.project.id})