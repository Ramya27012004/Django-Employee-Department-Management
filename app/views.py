from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def inset_dept(requst):
    dno=int(input('enter the deptno'))
    dname=input('enter the dname')
    loc=input('enter the loc')
    TDO=Dept.objects.get_or_create(deptno=dno,dname=dname,loc=loc)
    if TDO[1]:
        return HttpResponse('Dept is created')
    else:
        return HttpResponse('dept is alredy exit')
def insert_emp(request):
    empno=int(input('enter the empno:'))
    ename=input('enter the ename:')
    job=input('enter the job:')
    meno=input('enter the mgr:')
    if meno:
        MEO=Emp.objects.get(empno=int(meno))
    else:
        MEO=None
    hiredate=input('enter the date:')
    sal=float(input('enter the sal:'))
    comm=input('enter the comm:')
    if comm:
        comm=float(comm)
    else:
        comm=None
    dn=int(input('enter the number:'))
    DO=Dept.objects.get(deptno=dn)
    TEMPO=Emp.objects.get_or_create(empno=empno,ename=ename,job=job,mgr=MEO,hiredate=hiredate,sal=sal,comm=comm,deptno=DO)
    if TEMPO[1]:
        return HttpResponse('emp is created')
    else:
        return HttpResponse('emp is alredy exit')
def display_dept(request):
    QLDO=Dept.objects.all()
    d={'QLDO':QLDO}
    return render(request,'display_dept.html',d)
def display_emp(request):
    QLEO=Emp.objects.all()
    QLEO=Emp.objects.filter(ename=('allen'))
    QLEO=Emp.objects.filter(ename='smith')
    QLEO=Emp.objects.filter(ename__startswith='s')
    d={'QLEO':QLEO}
    return render(request,'display_emp.html',d)