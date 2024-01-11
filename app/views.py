from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def Display_Dept(request):
    EDFO=DeptForms()
    d={'EDFO':EDFO}
    if request.method=='POST':
        EDDO=DeptForms(request.POST)
        if EDDO.is_valid():
            EDDO.save()
            return HttpResponse('data inserted into Dept')


    return render(request,'Insert_Dept.html',d)


def DisplayEmp(request):
    EEFO=EmpForms()
    d={'EEFO':EEFO}
    if request.method=='POST':
        EEDO=EmpForms(request.POST)
        if EEDO.is_valid():
            EEDO.save()
            return HttpResponse('data inserted into Emp')
    return render(request,'Insert_Emp.html',d)
