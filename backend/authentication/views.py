from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from . serializers import *
from rest_framework.response import Response

class ReactView(APIView):
    def get(self,request):
        output = [{"employee": output.employee,
                   "department": output.department}
                   for output in React.objects.all()]
        return Response(output)
    def post(self,request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()#database e save kortese
            return Response(serializer.data)
      

class CheckEmployeeExistenceView(APIView):
    def post(self, request):
        employee_name = request.data.get('employee')

        # Check if employees with the given name exist
        employees = React.objects.filter(employee=employee_name)

        if employees.exists():
            # At least one employee with the given name exists
            department_names = [employee.department for employee in employees]
            response_data = {
                "employee": employee_name,
                "exists": True,
                "departments": department_names,
            }
        else:
            response_data = {"employee": employee_name, "exists": False, "departments": []}

        return Response(response_data)