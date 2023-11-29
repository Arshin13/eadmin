from django.shortcuts import redirect, render

from eadmin.models import Employee,Login

# Create your views here.
def index(request):
    return render(request, 'eadmin/index.html')

def login(request):
    msg=""
    if request.method=="POST":
        uname=request.POST['name']
        password=request.POST['password']

        
        login_user = Login.objects.filter(uname=uname,password=password)
        

        if login_user.exists():
            request.session['login_user_id']=login_user[0].id
            request.session['login_user_name']=login_user[0].uname
            return redirect('details')
        
        else:
            msg="username or password not correct,"

    return render(request,'eadmin/login.html',{'status':msg})

def employee_details(request):
    # Assuming you have a list of employees, pass it to the template
    #employees = [...]  # Replace [...] with your list of employees
    # Sample list of employees
    employees = Employee.objects.all()
    return render(request, 'eadmin/employee_details.html', {'employees': employees})

def edit_employee(request,emp_id):
    # Assuming you have a method to retrieve employee details by ID
    #employee = get_employee_by_id(employee_id)  # Replace with your method
    employee=Employee.objects.get(id=emp_id)
    msg=""
    if request.method=='POST':
        name=request.POST['name']
        department= request.POST['department']

        employee.name=name
        employee.department=department
        employee.save()
        msg="updated successfully"
    context={
        'employee':employee,
        'status':msg
        }    

    return render(request, 'eadmin/edit_employee.html',context)

def add_employee(request):
    msg=""
    if request.method=="POST":
        name=request.POST['emp_name']
        dept=request.POST['emp_department']

        new_employee=Employee(name=name,department=dept)
        new_employee.save()
        msg='employee added successfully'
    return render(request, 'eadmin/add_employee.html',{'status':msg})

def delete_employee(request,emp_id):
    employee=Employee.objects.get(id=emp_id)
    employee.delete()

    return redirect('details')

