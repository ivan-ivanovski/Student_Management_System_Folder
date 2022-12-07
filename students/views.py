from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student
from .form import StudentForm
# Create your views here.

def index(req):
    return render(req,'students/index.html',{
        'students':Student.objects.all()
    } )

def view_student(req,id):
    student = Student.objects.get(pk=id) #pk e nacin preko koj django dava i vrakja referencu t.e kako id u sql 
    return HttpResponseRedirect(reverse('index')) # reverse e vekje postoecka funkcija preku koja se izbegnuva hardcodding na url view

def add(req):
    if req.method =='POST':
        form = StudentForm(req.POST)
        if form.is_valid():
            new_sn = form.cleaned_data['student_number']
            new_fn = form.cleaned_data['first_name']
            new_ln = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_fos = form.cleaned_data['study_field']
            new_sgpa = form.cleaned_data['gpa']

            new_student = Student(
                student_number = new_sn,
                first_name = new_fn,
                last_name = new_ln,
                email = new_email,
                study_field= new_fos,
                gpa = new_sgpa
            )
            new_student.save()
            return render(req, 'students/add.html',{
                'form':StudentForm(), 
                'success':True
                })
        else:
            form = StudentForm()
    return render(req, 'students/add.html',{
        'form':StudentForm()
        })

def edit(req,id):
    if req.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(req.POST, instance=student)
        if form.is_valid():
            form.save();
            return render(req, 'students/edit.html',{
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(req,'students/edit.html',{
        'form':form
    })
def delete(req,id):
    if req.method =="POST":
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
