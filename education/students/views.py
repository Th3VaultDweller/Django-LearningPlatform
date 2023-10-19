from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Create your views here.


class StudentRegistrationView(CreateView):
    """Used for registering students for a course"""

    template_name = "students/student/registration.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("stident_course_list")

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd["username"], password=cd["password1"])
        login(self.request, user)
        return result
