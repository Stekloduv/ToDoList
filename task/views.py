from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from task.forms import TaskForm
from task.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'task_list'


class TagListView(generic.ListView):
    model = Tag
    template_name = 'task/tag_list.html'
    context_object_name = 'tag_list'


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = 'task/tag_form.html'
    success_url = reverse_lazy("task:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = 'task/tag_form.html'
    success_url = reverse_lazy("task:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = 'task/tag_confirm_delete.html'
    success_url = reverse_lazy("task:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list")


def toggle_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect('task:task-list')
