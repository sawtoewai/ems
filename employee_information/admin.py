from django.contrib import admin
from employee_information.models import Department, Position, Employees, Contract, Job, Recruitment, Payroll, Attendance, Expense

# Register your models here.
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employees)
admin.site.register(Contract)
admin.site.register(Job)
admin.site.register(Recruitment)
admin.site.register(Payroll)
admin.site.register(Attendance)
admin.site.register(Expense)
