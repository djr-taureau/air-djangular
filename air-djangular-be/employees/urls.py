from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from employees import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)
router.register(r'departments', views.DepartmentsViewSet)
router.register(r'managers', views.DeptManagerViewSet)
router.register(r'department_employees', views.DeptEmpViewSet)
router.register(r'salaries', views.SalariesViewSet)
router.register(r'titles', views.TitlesViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls))
]
