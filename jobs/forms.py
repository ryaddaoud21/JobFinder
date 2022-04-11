from django import forms
from .models import Job , Application

class AddJobForm(forms.ModelForm):
    class Meta :
        model = Job
        fields =['title' , 'show_description' , 'long_desctiption']

class ApplicationForm (forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name', 'phone_number','content', 'experience', 'image']