from datetime import date, datetime
import re
from typing import List
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from Student.forms import AbsentForm,  StudentForm
from Student.models import AbsentDate, Student


from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request,'index.html')
def std(request):
    if request.method=="POST":
        form= StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('show')
            except:
                pass
    else:
        form=StudentForm()
    return render(request,'addstd.html',{'form':form})

@login_required(login_url='login')
def absent(request):
    if request.method=="POST":
        form= AbsentForm(request.POST) 
        if form.is_valid():
            str1= form.cleaned_data['period1']
            str2= form.cleaned_data['period2']
            str3= form.cleaned_data['period3']
            str= str1+','+str2+','+str3
            list1=re.findall(r"[\w']+", str)
            list1 = list(map(int, list1))
            try:
                for i in list1:
                    std=Student.objects.get(sroll=i)
                    std.sabsent+=1
                    std.save(update_fields=['sabsent'])
                    dateob= AbsentDate(absdate=form.cleaned_data['absdate'],abstudent=std)
                    dateob.save()  
                return redirect('show')   
            except:
                pass
    else:
        form=AbsentForm()
    return render(request,'absent.html',{'form':form})

def show(request):  
    student = Student.objects.all()  
    return render(request,"show.html",{'student':student})

def base(request):
    return render(request,'base.html')

def common(request):
    return render(request,'common.html')
def test(request):
    if request.method=="POST":
        list1 = request.POST.get('mytext')
        print(list1)
    return render(request,'test.html')
