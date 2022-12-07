from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number','first_name','last_name','email','study_field','gpa']
        labels = {
            'student_number' : 'Student Number',
            'first_name' : 'First Name of Student',
            'last_name' : 'Last Name of Student',
            'email' : 'E-mail of student',
            'study_field': 'Field of Study',
            'gpa' : 'GPA'
        }
        widgets = {
            'student_number' : forms.NumberInput(attrs={'class':'form-control border-2 border-dark'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'study_field':forms.TextInput(attrs={'class':'form-control'}),
            'gpa':forms.NumberInput(attrs={'class':'form-control'}),
        }