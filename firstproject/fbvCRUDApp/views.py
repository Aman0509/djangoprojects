from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required, permission_required


@login_required
def homepage(request):
    return render(request, 'fbvCRUDApp/homepage.html')


@login_required
def getStudent(request):
    students = Student.objects.all()
    return render(request, 'fbvCRUDApp/index.html', {'students': students})


@login_required
def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/fbvCRUDapp')
    return render(request, 'fbvCRUDApp/create.html', {'form': form})


@login_required
@permission_required('fbvCRUDApp.delete_student')  # You need to define app name and operation with your model class in
# lowercase
def deleteStudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/fbvCRUDapp/getStudent')


''' In below function, for updating fields, we are sending the student object, because of that we have to
create form manually in update.html'''
# def updateStudent(request, id):
#     student = Student.objects.get(id=id)
#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             form.save()
#             return redirect('/fbvCRUDapp/getStudent')
#     return render(request, 'fbvCRUDApp/update.html', {'student': student})


@login_required
def updateStudent(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/fbvCRUDapp/getStudent')
    return render(request, 'fbvCRUDApp/update.html', {'form': form})


def logout(request):
    return render(request, 'fbvCRUDApp/logout.html')