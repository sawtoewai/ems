from django.shortcuts import redirect, render
from django.http import HttpResponse
from employee_information.models import Department, Position, Employees, Contract, Job, Recruitment, Payroll, Attendance, Expense
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Q
from django.core.paginator import Paginator
import json

# Login
def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp),content_type='application/json')

#Logout
def logout_user(request):
    logout(request)
    return redirect('/login')

# Create your views here.
@login_required
def home(request):
    context = {
        'page_title':'Home',
        'employees':employees,
        'total_department':len(Department.objects.all()),
        'total_position':len(Position.objects.all()),
        'total_employee':len(Employees.objects.all()),
        'total_contract':len(Contract.objects.all()),
        'total_job':len(Job.objects.all()),
        'total_recruitment':len(Recruitment.objects.all()),
        'total_payroll':len(Payroll.objects.all()),
        'total_attendance':len(Attendance.objects.all()),
        'total_expense':len(Expense.objects.all()),
    }
    return render(request, 'employee_information/home.html',context)


def about(request):
    context = {
        'page_title':'About',
    }
    return render(request, 'employee_information/about.html',context)

# Departments
def department_search_by(request):
    search = request.GET.get('search')
    if search:    
        departments = Department.objects.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) 
        )
    else:      
        departments = Department.objects.all()
    return render(request, 'employee_information/departments.html', {'departments': departments})

@login_required
def departments(request):
    department_list = Department.objects.all()
    paginator = Paginator(department_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_title':'Departments',
        'departments':page_obj,
    }
    return render(request, 'employee_information/departments.html',context)
@login_required
def manage_departments(request):
    department = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            department = Department.objects.filter(id=id).first()
    
    context = {
        'department' : department
    }
    return render(request, 'employee_information/manage_department.html',context)

@login_required
def save_department(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_department = Department.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],remark = data['remark'],status = data['status'])
        else:
            save_department = Department(name=data['name'], description = data['description'],remark = data['remark'],status = data['status'])
            save_department.save()
        resp['status'] = 'success'
    except Exception:
        resp['status'] = 'failed'
        print(Exception)
        print(json.dumps({"name":data['name'], "description" : data['description'],"remark" : data['remark'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_department(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Department.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_department(request):
    department = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            department = Department.objects.filter(id=id).first()
    
    context = {
        'department' : department
    }
    return render(request, 'employee_information/view_department.html',context)


# Positions
def position_search_by(request):
    search = request.GET.get('search')
    if search:    
        positions = Position.objects.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) 
        )
    else:      
        positions = Position.objects.all()
    return render(request, 'employee_information/positions.html', {'positions': positions})

@login_required
def positions(request):
    position_list = Position.objects.all()
    paginator = Paginator(position_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_title':'Positions',
        'positions':page_obj,
    }
    return render(request, 'employee_information/positions.html',context)

@login_required
def manage_positions(request):
    position = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            position = Position.objects.filter(id=id).first()
    
    context = {
        'position' : position
    }
    return render(request, 'employee_information/manage_position.html',context)

@login_required
def save_position(request):
    data =  request.POST
    resp = {'status':'failed'}
    try:
        if (data['id']).isnumeric() and int(data['id']) > 0 :
            save_position = Position.objects.filter(id = data['id']).update(name=data['name'], description = data['description'],remark = data['remark'],status = data['status'])
        else:
            save_position = Position(name=data['name'], description = data['description'],remark = data['remark'],status = data['status'])
            save_position.save()
        resp['status'] = 'success'
    except Exception:
        resp['status'] = 'failed'
        print(Exception)
        print(json.dumps({"name":data['name'], "description" : data['description'],"remark" : data['remark'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_position(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Position.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_position(request):
    position = {}
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            position = Position.objects.filter(id=id).first()
    
    context = {
        'position' : position
    }
    return render(request, 'employee_information/view_position.html',context)

# Employees
def employee_search_by(request):
    search = request.GET.get('search')
    if search:    
        employees = Employees.objects.filter(
            Q(code__icontains=search) |
            Q(firstname__icontains=search) 
        )
    else:      
        employees = Employee.objects.all()
    return render(request, 'employee_information/employees.html', {'employees': employees})

@login_required
def employees(request):
    employee_list = Employees.objects.all()
    paginator = Paginator(employee_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_title':'Employees',
        'employees':page_obj,
    }
    return render(request, 'employee_information/employees.html',context)

@login_required
def manage_employees(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions
    }
    return render(request, 'employee_information/manage_employee.html',context)

@login_required
def save_employee(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Employees.objects.exclude(id = data['id']).filter(code = data['code'])
    else:
        check  = Employees.objects.filter(code = data['code'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Code Already Exists'
    else:
        try:
            dept = Department.objects.filter(id=data['department_id']).first()
            pos = Position.objects.filter(id=data['position_id']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_employee = Employees.objects.filter(id = data['id']).update(code=data['code'], firstname = data['firstname'],middlename = data['middlename'],lastname = data['lastname'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],department_id = dept,position_id = pos,date_hired = data['date_hired'],salary = data['salary'],remark = data['remark'],status = data['status'])
            else:
                save_employee = Employees(code=data['code'], firstname = data['firstname'],middlename = data['middlename'],lastname = data['lastname'],dob = data['dob'],gender = data['gender'],contact = data['contact'],email = data['email'],address = data['address'],department_id = dept,position_id = pos,date_hired = data['date_hired'],salary = data['salary'],remark = data['remark'],status = data['status'])
                save_employee.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({"code":data['code'], "firstname" : data['firstname'],"middlename" : data['middlename'],"lastname" : data['lastname'],"dob" : data['dob'],"gender" : data['gender'],"contact" : data['contact'],"email" : data['email'],"address" : data['address'],"department_id" : data['department_id'],"position_id" : data['position_id'],"date_hired" : data['date_hired'],"salary" : data['salary'],"remark" : data['remark'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_employee(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Employees.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_employee(request):
    employee = {}
    departments = Department.objects.filter(status = 1).all() 
    positions = Position.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            employee = Employees.objects.filter(id=id).first()
    context = {
        'employee' : employee,
        'departments' : departments,
        'positions' : positions
    }
    return render(request, 'employee_information/view_employee.html',context)

# Contracts
def contract_search_by(request):
    search = request.GET.get('search')
    if search:    
        contracts = Contract.objects.filter(
            Q(name__icontains=search) |
            Q(rank__icontains=search) |
            Q(status__icontains=search) 
        )
    else:      
        contracts = Contract.objects.all()
    return render(request, 'employee_information/contracts.html', {'contracts': contracts})

@login_required
def contracts(request):
    contract_list = Contract.objects.all()
    paginator = Paginator(contract_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_title':'Contracts',
        'contracts':page_obj,
    }
    return render(request, 'employee_information/contracts.html',context)

@login_required
def manage_contracts(request):
    contract = {}
    employee = Employees.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            contract = Contract.objects.filter(id=id).first()
    context = {
        'contract' : contract,
        'employees' : employee
    }
    return render(request, 'employee_information/manage_contract.html',context)

@login_required
def save_contract(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Contract.objects.exclude(id = data['id']).filter(name = data['name'])
    else:
        check  = Contract.objects.filter(name = data['name'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Code Already Exists'
    else:
        try:
            emp = Employees.objects.filter(id=data['employee_id']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_contract = Contract.objects.filter(id = data['id']).update(name = data['name'],rank = data['rank'],start_date = data['start_date'],employee_id = emp,end_date = data['end_date'],note = data['note'],status = data['status'])
            else:
                save_contract = Contract(name = data['name'],rank = data['rank'],start_date = data['start_date'],end_date = data['end_date'],employee_id = emp,note = data['note'],status = data['status'])
                save_contract.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({"name" : data['name'],"rank" : data['rank'],"start_date" : data['start_date'],"end_date" : data['end_date'],"employee_id" : data['employee_id'],"note" : data['note'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_contract(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Contract.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_contract(request):
    contract = {}
    employee = Employees.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            contract = Contract.objects.filter(id=id).first()
    context = {
        'contract' : contract,
        'employee' : employee
    }
    return render(request, 'employee_information/view_contract.html',context)

# Jobs
def job_search_by(request):
    search = request.GET.get('search')
    if search:    
        jobs = Job.objects.filter(
            Q(name__icontains=search) |
            Q(sequence__icontains=search) |
            Q(status__icontains=search) 
        )
    else:      
        jobs = Job.objects.all()
    return render(request, 'employee_information/jobs.html', {'jobs': jobs})

@login_required
def jobs(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_title':'Jobs',
        'jobs':page_obj,
    }
    return render(request, 'employee_information/jobs.html',context)
    
@login_required
def manage_jobs(request):
    job = {}
    departments = Department.objects.filter(status = 1).all()  
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            job = Job.objects.filter(id=id).first()
    context = {
        'job' : job,
        'departments' : departments
    }
    return render(request, 'employee_information/manage_job.html',context)

@login_required
def save_job(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Job.objects.exclude(id = data['id']).filter(name = data['name'])
    else:
        check  = Job.objects.filter(name = data['name'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Code Already Exists'
    else:
        try:
            dept = Department.objects.filter(id=data['department_id']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_job = Job.objects.filter(id = data['id']).update(name = data['name'],sequence = data['sequence'],open_date = data['open_date'],expected_salary = data['expected_salary'],note = data['note'],department_id = dept,status = data['status'])
            else:
                save_job = Job(name = data['name'],sequence = data['sequence'],open_date = data['open_date'],expected_salary = data['expected_salary'],note = data['note'],department_id = dept,status = data['status'])
                save_job.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({"name" : data['name'],"sequence" : data['sequence'],"open_date" : data['open_date'],"expected_salary" : data['expected_salary'],"note" : data['note'],"department_id" : data['department_id'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_job(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Job.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_job(request):
    job = {}
    departments = Department.objects.filter(status = 1).all()  
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            job = Job.objects.filter(id=id).first()
    context = {
        'job' : job,
        'departments' : departments
    }
    return render(request, 'employee_information/view_job.html',context)

# Recruitments
def recruitment_search_by(request):
    search = request.GET.get('search')
    if search:    
        recruitments = Recruitment.objects.filter(
            Q(name__icontains=search) |
            Q(sequence__icontains=search) |
            Q(status__icontains=search) 
        )
    else:      
        recruitments = Recruitment.objects.all()
    return render(request, 'employee_information/recruitments.html', {'recruitments': recruitments})

@login_required    
def recruitments(request):
    recruitment_list = Recruitment.objects.all()
    paginator = Paginator(recruitment_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_title':'Recruitments',
        'recruitments':page_obj,
    }
    return render(request, 'employee_information/recruitments.html',context)
@login_required
def manage_recruitments(request):
    recruitment = {}
    employees = Employees.objects.filter(status = 1).all()  
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            recruitment = Recruitment.objects.filter(id=id).first()
    context = {
        'recruitment' : recruitment,
        'employees' : employees
    }
    return render(request, 'employee_information/manage_recruitment.html',context)

@login_required
def save_recruitment(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Recruitment.objects.exclude(id = data['id']).filter(name = data['name'])
    else:
        check  = Recruitment.objects.filter(name = data['name'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Code Already Exists'
    else:
        try:
            emp = Employees.objects.filter(id=data['employee_id']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_recruitment = Recruitment.objects.filter(id = data['id']).update(name = data['name'],sequence = data['sequence'],appointment_date = data['appointment_date'],note = data['note'],employee_id = emp,status = data['status'])
            else:
                save_recruitment = Recruitment(name = data['name'],sequence = data['sequence'],appointment_date = data['appointment_date'],note = data['note'],employee_id = emp,status = data['status'])
                save_recruitment.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({"name" : data['name'],"sequence" : data['sequence'],"appointment_date" : data['appointment_date'],"note" : data['note'],"employee_id" : data['employee_id'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_recruitment(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Recruitment.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_recruitment(request):
    recruitment = {}
    employees = Employees.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            recruitment = Recruitment.objects.filter(id=id).first()
    context = {
        'recruitment' : recruitment,
        'employees' : employees
    }
    return render(request, 'employee_information/view_recruitment.html',context)

# Payrolls
def payroll_search_by(request):
    search = request.GET.get('search')
    if search:    
        payrolls = Payroll.objects.filter(
            Q(name__icontains=search) |
            Q(note__icontains=search) |
            Q(rank__icontains=search) 
        )
    else:      
        payrolls = Payroll.objects.all()
    return render(request, 'employee_information/payrolls.html', {'payrolls': payrolls})

@login_required
def payrolls(request):
    payroll_list = Payroll.objects.all()
    paginator = Paginator(payroll_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_title':'payrolls',
        'payrolls':page_obj,
    }
    return render(request, 'employee_information/payrolls.html',context)

@login_required
def manage_payrolls(request):
    payroll = {}
    recruitments = Recruitment.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            payroll = Payroll.objects.filter(id=id).first()
    context = {
        'payroll' : payroll,
        'recruitments' : recruitments
    }
    return render(request, 'employee_information/manage_payroll.html',context)

@login_required
def save_payroll(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Payroll.objects.exclude(id = data['id']).filter(name = data['name'])
    else:
        check  = Payroll.objects.filter(name = data['name'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Code Already Exists'
    else:
        try:
            rec = Recruitment.objects.filter(id=data['recruitment_id']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_payroll = Payroll.objects.filter(id = data['id']).update(name=data['name'], position = data['position'],rank = data['rank'],date_of_commence = data['date_of_commence'],basic_salary = data['basic_salary'],meal_allowance = data['meal_allowance'],living_cost_allowance = data['living_cost_allowance'],traveling_allowance = data['traveling_allowance'],special_allowance = data['special_allowance'],recruitment_id = rec,overtime = data['overtime'],ssb_deduction = data['ssb_deduction'],emergency_loan = data['emergency_loan'],income_tax = data['income_tax'],note = data['note'],status = data['status'])
            else:
                save_payroll = Payroll(name=data['name'], position = data['position'],rank = data['rank'],date_of_commence = data['date_of_commence'],basic_salary = data['basic_salary'],meal_allowance = data['meal_allowance'],living_cost_allowance = data['living_cost_allowance'],traveling_allowance = data['traveling_allowance'],special_allowance = data['special_allowance'],recruitment_id = rec,overtime = data['overtime'],ssb_deduction = data['ssb_deduction'],emergency_loan = data['emergency_loan'],income_tax = data['income_tax'],note = data['note'],status = data['status'])
                save_payroll.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({"name":data['name'], "position" : data['position'],"rank" : data['rank'],"date_of_commence" : data['date_of_commence'],"basic_salary" : data['basic_salary'],"meal_allowance" : data['meal_allowance'],"living_cost_allowance" : data['living_cost_allowance'],"traveling_allowance" : data['traveling_allowance'],"special_allowance" : data['special_allowance'],"recruitment_id" : data['recruitment_id'],"overtime" : data['overtime'],"ssb_deduction" : data['ssb_deduction'],"emergency_loan" : data['emergency_loan'],"income_tax" : data['income_tax'],"note" : data['note'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_payroll(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Payroll.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_payroll(request):
    payroll = {}
    recruitments = Recruitment.objects.filter(status = 1).all() 
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            payroll = Payroll.objects.filter(id=id).first()
    context = {
        'payroll' : payroll,
        'recruitments' : recruitments
    }
    return render(request, 'employee_information/view_payroll.html',context)

# Attendances
def attendance_search_by(request):
    search = request.GET.get('search')
    if search:    
        attendances = Attendance.objects.filter(
            Q(name__icontains=search) |
            Q(department__icontains=search) |
            Q(remark__icontains=search) 
        )
    else:      
        attendances = Attendance.objects.all()
    return render(request, 'employee_information/attendances.html', {'attendances': attendances})

@login_required
def attendances(request):
    attendance_list = Attendance.objects.all()
    paginator = Paginator(attendance_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_title':'Attendances',
        'attendances':page_obj,
    }
    return render(request, 'employee_information/attendances.html',context)

@login_required
def manage_attendances(request):
    attendance = {}
    payrolls = Payroll.objects.filter(status = 1).all()
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            attendance = Attendance.objects.filter(id=id).first()
    context = {
        'attendance' : attendance,
        'payrolls' : payrolls
    }
    return render(request, 'employee_information/manage_attendance.html',context)

@login_required
def save_attendance(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Attendance.objects.exclude(id = data['id']).filter(name = data['name'])
    else:
        check  = Attendance.objects.filter(name = data['name'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Code Already Exists'
    else:
        try:
            pay = Payroll.objects.filter(id=data['payroll_id']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_attendance = Attendance.objects.filter(id = data['id']).update(name = data['name'],department = data['department'],working_day = data['working_day'],day_off = data['day_off'],check_in = data['check_in'],check_out = data['check_out'],payroll_id = pay,remark = data['remark'],status = data['status'])
            else:
                save_attendance = Attendance(name = data['name'],department = data['department'],working_day = data['working_day'],day_off = data['day_off'],check_in = data['check_in'],check_out = data['check_out'],payroll_id = pay,remark = data['remark'],status = data['status'])
                save_attendance.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({"name" : data['name'],"department" : data['department'],"working_day" : data['working_day'],"day_off" : data['day_off'],"check_in" : data['check_in'],"check_out" : data['check_out'],"payroll_id" : data['payroll_id'],"remark" : data['remark'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_attendance(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Attendance.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_attendance(request):
    attendance = {}
    payrolls = Payroll.objects.filter(status = 1).all()  
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            attendance = Attendance.objects.filter(id=id).first()
    context = {
        'attendance' : attendance,
        'payrolls' : payrolls
    }
    return render(request, 'employee_information/view_attendance.html',context)

# Expenses
def expense_search_by(request):
    search = request.GET.get('search')
    if search:    
        expenses = Expense.objects.filter(
            Q(name__icontains=search) |
            Q(department__icontains=search) |
            Q(status__icontains=search) 
        )
    else:      
        expenses = Expense.objects.all()
    return render(request, 'employee_information/expenses.html', {'expenses': expenses})

@login_required
def expenses(request):
    expense_list = Expense.objects.all()
    paginator = Paginator(expense_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_title':'Expenses',
        'expenses':page_obj,
    }
    return render(request, 'employee_information/expenses.html',context)

@login_required
def manage_expenses(request):
    expense = {}
    departments = Department.objects.filter(status = 1).all()
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            expense = Expense.objects.filter(id=id).first()
    context = {
        'expense' : expense,
        'departments' : departments
    }
    return render(request, 'employee_information/manage_expense.html',context)

@login_required
def save_expense(request):
    data =  request.POST
    resp = {'status':'failed'}
    if (data['id']).isnumeric() and int(data['id']) > 0:
        check  = Expense.objects.exclude(id = data['id']).filter(name = data['name'])
    else:
        check  = Expense.objects.filter(name = data['name'])

    if len(check) > 0:
        resp['status'] = 'failed'
        resp['msg'] = 'Code Already Exists'
    else:
        try:
            dep = Department.objects.filter(id=data['department_id']).first()
            if (data['id']).isnumeric() and int(data['id']) > 0 :
                save_expense = Expense.objects.filter(id = data['id']).update(name = data['name'],department = data['department'],description = data['description'],payment_type = data['payment_type'],quantity = data['quantity'],amount = data['amount'],note = data['note'],department_id = dep,status = data['status'])
            else:
                save_expense = Expense(name = data['name'],department = data['department'],description = data['description'],payment_type = data['payment_type'],quantity = data['quantity'],amount = data['amount'],note = data['note'],department_id = dep,status = data['status'])
                save_expense.save()
            resp['status'] = 'success'
        except Exception:
            resp['status'] = 'failed'
            print(Exception)
            print(json.dumps({"name" : data['name'],"department" : data['department'],"description" : data['description'],"payment_type" : data['payment_type'],"quantity" : data['quantity'],"amount" : data['amount'],"note" : data['note'],"department_id" : data['department_id'],"status" : data['status']}))
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def delete_expense(request):
    data =  request.POST
    resp = {'status':''}
    try:
        Expense.objects.filter(id = data['id']).delete()
        resp['status'] = 'success'
    except:
        resp['status'] = 'failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")

@login_required
def view_expense(request):
    expense = {}
    departments = Department.objects.filter(status = 1).all()  
    if request.method == 'GET':
        data =  request.GET
        id = ''
        if 'id' in data:
            id= data['id']
        if id.isnumeric() and int(id) > 0:
            expense = Expense.objects.filter(id=id).first()
    context = {
        'expense' : expense,
        'departments' : departments
    }
    return render(request, 'employee_information/view_expense.html',context)