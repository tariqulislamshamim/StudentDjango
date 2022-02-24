from datetime import date, datetime
import re
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from Student.forms import AbsentForm, StudentForm
from Student.models import AbsentDate, Student



# Create your views here.
def home(request):
    return render(request,'index.html')
def std(request):
    if request.method=="POST":
        form= StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Hello")
                return redirect('show')
            except:
                pass
    else:
        form=StudentForm()
    return render(request,'addstd.html',{'form':form})
def absent(request):
    if request.method=="POST":
        form= AbsentForm(request.POST) 
        for i in form:
            print(i)
        if form.is_valid():
            
            str= form.cleaned_data['absentroll']
            list1=re.findall(r"[\w']+", str)
            list1 = list(map(int, list1))
            try:
                for i in list1:
                    print(i)
                    std=Student.objects.get(sroll=i)
                    std.sabsent+=1
                    std.save(update_fields=['sabsent'])
                    dateob= AbsentDate(absdate=form.cleaned_data['absdate'],abstudent=std)
                    dateob.save()     
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
