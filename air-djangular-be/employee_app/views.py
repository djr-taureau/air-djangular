from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employees.objects.all()[:5]


class DepartmentsViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentsSerializer
    queryset = Departments.objects.all()[:5]


class DeptManagerViewSet(viewsets.ModelViewSet):
    serializer_class = DeptManagerSerializer
    queryset = DeptManager.objects.all()[:5]


class DeptEmpViewSet(viewsets.ModelViewSet):
    serializer_class = DeptEmpSerializer
    queryset = DeptEmp.objects.all()[:5]


class SalariesViewSet(viewsets.ModelViewSet):
    serializer_class = SalariesSerializer
    queryset = Salaries.objects.all()[:5]


class TitlesViewSet(viewsets.ModelViewSet):
    serializer_class = TitlesSerializer
    queryset = Titles.objects.all()[:5]
