from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmpForm
from .models import Employee

# Create your views here.


def welcomePage(req):
    return render(req, "emp.html", {"eform": EmpForm(), "emps": Employee.objects.all(),"emp": fetchDummyEmp(),"searchOb":None})

def fetchDummyEmp():
    return Employee(id=0, fname="", lname="", age=0, address="", salary=0.0,email="", country="")

def saveEmployeeInfo(req):
    print('inside save emp...', req.POST['id'])

    if int(req.POST['id'])> 0:
        form = EmpForm(req.POST, instance=Employee.objects.get(id=req.POST['id'])) #check instance then update
    else:
        form = EmpForm(req.POST) #always create

    form.save()
    return redirect('/emp/')

def editEmployeeInfo(req,eid):
    empOb=Employee.objects.filter(id=eid).first()
    print(empOb)
    return render(req, "emp.html", {"eform": EmpForm(), "emps": Employee.objects.all(),"emp": empOb,"searchOb":None})

def deleteEmployeeInfo(req,eid):
    empOb = Employee.objects.filter(id=eid).first()
    empOb.delete()
    return redirect('/emp/')

def searchemp(req):
    print('inside search emp...', req.POST['search'])
    listOfEmps=Employee.objects.filter(fname=req.POST['search']).first()

    return render(req, "emp.html", {"eform": EmpForm(), "emps": Employee.objects.all(), "emp": fetchDummyEmp(),"searchOb":listOfEmps})




