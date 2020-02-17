from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Student
# Create your views here.


def home(request):
    if request.method =='POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        s = Student(First_name=fname, Email=email)
        s.save()
    return render(request, 'app1/index.html')
