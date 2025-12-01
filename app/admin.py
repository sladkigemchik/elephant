from django.contrib import admin
from .models import Service, Employee, EmployeeService

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_active']
    list_filter = ['is_active']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_active']
    list_filter = ['is_active']

admin.site.register(EmployeeService)