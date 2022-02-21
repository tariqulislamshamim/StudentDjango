from django.shortcuts import redirect, render
from django.http.response import HttpResponse

from Student.forms import StudentForm
from Student.models import Student


# Create your views here.
def home(request):
    return HttpResponse("Hello World")
def std(request):
    if request.method=="POST":
        form= StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=StudentForm()
    return render(request,'index.html',{'form':form})
def show(request):  
    student = Student.objects.all()  
    return render(request,"show.html",{'student':student})  
