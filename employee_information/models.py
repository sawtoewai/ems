from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    remark = models.TextField()
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    remark = models.TextField()
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name


class Employees(models.Model):
    code = models.CharField(max_length=100,blank=True) 
    firstname = models.TextField() 
    middlename = models.TextField(blank=True,null= True) 
    lastname = models.TextField() 
    gender = models.TextField(blank=True,null= True) 
    dob = models.DateField(blank=True,null= True) 
    contact = models.TextField() 
    address = models.TextField() 
    email = models.TextField() 
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    date_hired = models.DateField() 
    salary = models.FloatField(default=0) 
    remark = models.TextField()
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.firstname + ' ' +self.middlename + ' '+self.lastname + ' '

class Contract(models.Model):
    name = models.TextField()
    rank = models.TextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    note = models.TextField() 
    status = models.IntegerField()
    remark = models.TextField() 
    create_date = models.DateTimeField(default=timezone.now)
    attachment = models.ImageField(default=None, blank=True)
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Job(models.Model):
    name = models.TextField()
    sequence = models.TextField()
    open_date = models.DateField(default=timezone.now)
    expected_salary = models.TextField()
    note = models.TextField()  
    status = models.IntegerField()  
    create_date = models.DateTimeField(default=timezone.now)
    attachment = models.ImageField(default=None, blank=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Recruitment(models.Model):
    name = models.TextField()
    sequence = models.TextField()
    appointment_date = models.DateField(default=timezone.now)
    note = models.TextField()  
    status = models.IntegerField() 
    create_date = models.DateTimeField(default=timezone.now)
    attachment = models.ImageField(default=None, blank=True)
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Payroll(models.Model):
    name = models.TextField()
    position = models.TextField()
    rank = models.TextField()
    date_of_commence = models.DateTimeField(default=timezone.now)
    basic_salary = models.FloatField(default=0)
    meal_allowance = models.TextField()
    living_cost_allowance = models.TextField()
    traveling_allowance = models.TextField()
    special_allowance = models.TextField()
    overtime = models.TextField()
    ssb_deduction = models.TextField()
    emergency_loan = models.TextField()
    income_tax = models.TextField()
    note = models.TextField()  
    status = models.IntegerField() 
    attachment = models.ImageField(default=None)
    recruitment_id = models.ForeignKey(Recruitment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    name = models.TextField()
    department = models.TextField()
    working_day = models.TextField()
    day_off = models.TextField()
    check_in = models.DateField(default=timezone.now)
    check_out = models.DateField(default=timezone.now)
    remark = models.TextField()
    status = models.IntegerField()
    attachment = models.ImageField(default=None)
    payroll_id = models.ForeignKey(Payroll, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Expense(models.Model):
    department = models.TextField()
    name = models.TextField()
    description = models.TextField()
    payment_type = models.TextField()
    quantity = models.TextField()
    amount = models.TextField()
    note = models.TextField()  
    status = models.IntegerField()  
    create_date = models.DateTimeField(default=timezone.now)
    document = models.ImageField(default=None)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name