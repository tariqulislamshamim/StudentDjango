'''
Created on Feb 18, 2022

@author: shamim
'''
from django import forms
from Student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields = "__all__"
        
class AbsentForm(forms.Form):
    absdate= forms.DateField()
    period1=forms.CharField()
    period2=forms.CharField()
    period3=forms.CharField()
 
