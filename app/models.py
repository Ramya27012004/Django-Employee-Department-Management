from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(max_length=10,primary_key=True)
    dname=models.CharField(max_length=20,unique=True)
    loc=models.CharField(max_length=20)
    def __str__(self):
        return str(self.deptno)+self.dname

class Emp(models.Model):
    empno=models.IntegerField(max_length=10)
    ename=models.CharField()
    job=models.CharField()
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    hiredate=models.DateField()
    sal=models.DecimalField(max_digits=8,decimal_places=3)
    comm=models.DecimalField(max_digits=8,decimal_places=4 ,null=True, blank=True)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.ename