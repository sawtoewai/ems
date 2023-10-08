from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('', views.home, name="home-page"),
    path('login/', auth_views.LoginView.as_view(template_name = 'employee_information/login.html',redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout/', views.logout_user, name="logout"),
    path('about', views.about, name="about-page"),

    path('departments', views.departments, name="department-page"),
    path('manage_departments', views.manage_departments, name="manage_departments-page"),
    path('save_department', views.save_department, name="save-department-page"),
    path('delete_department', views.delete_department, name="delete-department"),
    path('view_department/search_by/', views.department_search_by),
    path('view_department', views.view_department, name="view-department-page"),

    path('positions', views.positions, name="position-page"),
    path('manage_positions', views.manage_positions, name="manage_positions-page"),
    path('save_position', views.save_position, name="save-position-page"),
    path('delete_position', views.delete_position, name="delete-position"),
    path('view_position/search_by/', views.position_search_by),
    path('view_position', views.view_position, name="view-position-page"),

    path('employees', views.employees, name="employee-page"),
    path('manage_employees', views.manage_employees, name="manage_employees-page"),
    path('save_employee', views.save_employee, name="save-employee-page"),
    path('delete_employee', views.delete_employee, name="delete-employee"),
    path('view_employee/search_by/', views.employee_search_by),
    path('view_employee', views.view_employee, name="view-employee-page"),

    path('contracts', views.contracts, name="contract-page"),
    path('manage_contracts', views.manage_contracts, name="manage_contracts-page"),
    path('save_contract', views.save_contract, name="save-contract-page"),
    path('delete_contract', views.delete_contract, name="delete-contract"),
    path('view_contract/search_by/', views.contract_search_by),
    path('view_contract', views.view_contract, name="view-contract-page"),

    path('jobs', views.jobs, name="job-page"),
    path('manage_jobs', views.manage_jobs, name="manage_jobs-page"),
    path('save_job', views.save_job, name="save-job-page"),
    path('delete_job', views.delete_job, name="delete-job"),
    path('view_job/search_by/', views.job_search_by),
    path('view_job', views.view_job, name="view-job-page"),

    path('recruitments', views.recruitments, name="recruitment-page"),
    path('manage_recruitments', views.manage_recruitments, name="manage_recruitments-page"),
    path('save_recruitment', views.save_recruitment, name="save-recruitment-page"),
    path('delete_recruitment', views.delete_recruitment, name="delete-recruitment"),
    path('view_recruitment/search_by/', views.recruitment_search_by),
    path('view_recruitment', views.view_recruitment, name="view-recruitment-page"),

    path('payrolls', views.payrolls, name="payroll-page"),
    path('manage_payrolls', views.manage_payrolls, name="manage_payrolls-page"),
    path('save_payroll', views.save_payroll, name="save-payroll-page"),
    path('delete_payroll', views.delete_payroll, name="delete-payroll"),
    path('view_payroll/search_by/', views.payroll_search_by),
    path('view_payroll', views.view_payroll, name="view-payroll-page"),
    
    path('attendances', views.attendances, name="attendance-page"),
    path('manage_attendances', views.manage_attendances, name="manage_attendances-page"),
    path('save_attendance', views.save_attendance, name="save-attendance-page"),
    path('delete_attendance', views.delete_attendance, name="delete-attendance"),
    path('view_attendance/search_by/', views.attendance_search_by),
    path('view_attendance', views.view_attendance, name="view-attendance-page"),

    path('expenses', views.expenses, name="expense-page"),
    path('manage_expenses', views.manage_expenses, name="manage_expenses-page"),
    path('save_expense', views.save_expense, name="save-expense-page"),
    path('delete_expense', views.delete_expense, name="delete-expense"),
    path('view_expense/search_by/', views.expense_search_by),
    path('view_expense', views.view_expense, name="view-expense-page"),
]