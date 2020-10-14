from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student


class GreetingView(View):
    greeting = "<b>First Class Based Views</b>"

    def homepage(self):
        return render(self, 'cbvAPP/homepage.html')

    def get(self, request):
        return HttpResponse(self.greeting)


class StudentListView(ListView):
    model = Student
    # default template_name is student_list.html
    # default contect_object_name is student_list


class StudentDetailView(DetailView):
    model = Student
    # default template_name is student_detail.html
    # default contect_object_name is student


class StudentCreateView(CreateView):
    model = Student
    fields = ('firstName', 'lastName', 'testScore')


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('testScore',)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student')