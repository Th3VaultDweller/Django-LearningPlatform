from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Course

# Create your views here.


class ManageCourseListView(ListView):
    """CRUD for managing the course list"""

    model = Course
    template_name = "courses/manage/course/list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
