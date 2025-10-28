from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from app.models import *
from django.db.models import Q
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
def EmpToDept(request):
    QLEDO=Emp.objects.all().select_related('deptno')
    QLEDO=Emp.objects.select_related('deptno').filter(ename='smith')
    QLEDO=Emp.objects.select_related('deptno').filter(sal__gt=0,deptno=20)
    QLEDO=Emp.objects.select_related('deptno').filter(ename__startswith='s')
    QLEDO=Emp.objects.select_related('deptno').filter(hiredate__range=('1980-12-17','1981-02-20'))
    QLEDO=Emp.objects.select_related('deptno').filter(comm__gt=100,ename__contains='a')
    QLEDO=Emp.objects.select_related('deptno').filter(deptno__dname__contains='a',ename__contains='l')
    QLEDO=Emp.objects.select_related('deptno').filter(Q(deptno__dname__contains='R')|(Q(ename__contains='i')))
    QLEDO=Emp.objects.select_related('deptno').filter(Q(sal__lt=1000)|Q(deptno__loc__startswith='C'))
    QLEDO=Emp.objects.select_related('deptno').filter(job='salesman',sal__lte=1400)
    QLEDO=Emp.objects.select_related('deptno').filter(job='manager',deptno=20)
    QLEDO=Emp.objects.select_related('deptno').filter(Q(deptno__loc='Boston')|Q(deptno__dname__contains='a'))
    QLEDO=Emp.objects.select_related('deptno').filter(Q(deptno__loc='Boston')|Q(deptno=40))
    QLEDO=Emp.objects.select_related('deptno').filter(job='clerk')
    QLEDO=Emp.objects.select_related('deptno').filter(mgr=None)
    QLEDO=Emp.objects.select_related('deptno').filter(mgr=None,comm=None,deptno=20)
    QLEDO=Emp.objects.select_related('deptno').filter(mgr=None,comm=None)
    d={'QLEDO':QLEDO}
    return render(request,'EmpToDept.html',d)

def EmpToMgr(request):
    QLEMO=Emp.objects.all().select_related('mgr')
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__ename='blake')
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__ename='jones')
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__ename='blake',mgr__sal__gt=400)
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__sal__lt=2500)
    QLEMO=Emp.objects.select_related('mgr').filter(mgr__hiredate__range=('1980-12-17','1981-02-20'))
    QLEMO=Emp.objects.select_related('mgr').filter(Q(ename__contains='a')|Q(mgr__ename__contains='a'))
    QLEMO=Emp.objects.select_related('mgr').filter(Q(ename__contains='k')|Q(mgr__ename__contains='k'))
    QLEMO=Emp.objects.select_related('mgr').filter(Q(ename__contains='a')|Q(mgr__ename__startswith='j'))
    QLEMO=Emp.objects.select_related('mgr').filter(ename__contains='a',mgr__ename__contains='a')
    QLEMO=Emp.objects.select_related('mgr').filter(Q(sal__lt=1000)|Q(mgr__ename__contains='a'))
    QLEMO=Emp.objects.select_related('mgr').filter(Q(ename='blake')|Q(mgr__ename='blake'))
    QLEMO=Emp.objects.select_related('mgr').filter(ename='blake',mgr__ename='blake')
    QLEMO=Emp.objects.select_related('mgr').filter(deptno=20,mgr__job__contains='a')
    QLEMO=Emp.objects.select_related('mgr').filter(Q(sal__lt=1000)|Q(mgr__sal__gt=2300))
    d={'QLEMO':QLEMO}
    return render(request,'EmpToMgr.html',d)
def EmpToMgrToDept(request):
    QLEMDO=Emp.objects.all().select_related('mgr','deptno')
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(Q(ename__contains='a')|Q(mgr__ename__contains='w')|Q(deptno__dname__contains='l'))
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(sal__gt=300,mgr__ename__contains='a',deptno__loc='D')
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(job='salesman',mgr__sal__gt=2500,deptno__loc__contains='a')
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(sal__gt=300,mgr__ename__contains='a',deptno__deptno__in=(10,20))
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(sal__gt=300,mgr__ename__contains='a',deptno__dname='sales')
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(Q(sal__gt=300)|Q(mgr__ename__contains='a')|Q(deptno__loc='D'))
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(Q(sal__lt=6000)|Q(mgr__job='manager')|Q(deptno__loc='Dallas'))
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(Q(sal__lt=6000)|Q(mgr__job='manager')|Q(deptno__loc='Dallas'))
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(Q(sal__lt=6000)|Q(mgr__job='salesman')|Q(deptno__loc='Dallas'))
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(Q(job='salesman')|Q(mgr__job='manager')|Q(deptno__loc='Dallas'))
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(Q(comm=None)|Q(mgr__job='manager')|Q(deptno__deptno__in=(20,30)))
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(Q(comm=None)|Q(mgr__empno=None)|Q(deptno__loc='Dallas'))
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(job='salesman',mgr__job='manager',deptno__deptno__in=(10,20,30,40))
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(Q(comm=None)|Q(mgr__empno=None)|Q(mgr__ename__contains='a'))
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(Q(comm=None)|Q(mgr__comm=None)|Q(deptno__dname='sales'))
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(Q(ename='clerk')|Q(mgr__comm=None)|Q(deptno__dname='Research'))
    QLEMDO=Emp.objects.select_related('mgr','deptno').filter(ename='clerk',job='salesman',mgr__comm=None,deptno__deptno=10)
    d={'QLEMDO':QLEMDO}
    return render(request,'EmpToMgrToDept.html',d)
