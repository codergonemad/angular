from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from emp.models import Departments,Employees
from emp.serializers import DepartmentSerializers,EmployeeSerializers
from django.http.response import JsonResponse

# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments=Departments.objects.all()
        departments_serializer=DepartmentSerializers(departments,many=True)
        return JsonResponse(departments_serializer.data,safe=False)
    
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serializer=DepartmentSerializers(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!",safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer=DepartmentSerializers(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!",safe=False)
        return JsonResponse("Failed to Update.",safe=False)
    
    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully!!",safe=False)


# @csrf_exempt
# def SaveFile(request):
#     file=request.FILES['uploadedFile']   
#     file_name=default_storage.save(file.name,file) 
#     return JsonResponse(file_name,safe=False)
@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees=Employees.objects.all()
        employees_serializer=EmployeeSerializers(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer=EmployeeSerializers(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!",safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employees=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer=EmployeeSerializers(employees,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!",safe=False)
        return JsonResponse("Failed to Update.",safe=False)
    
    elif request.method=='DELETE':
        employees=Employees.objects.get(EmployeeId=id)
        employees.delete()
        return JsonResponse("Deleted Successfully!!",safe=False)
