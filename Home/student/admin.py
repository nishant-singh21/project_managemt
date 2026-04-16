from django.contrib import admin

# Register your models here.
from django.contrib import admin 
from .models import Student 

@admin.register(Student)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    search_fields = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    list_filter = ('father_name', 'mother_name')

@admin.register(student)
class StudentAdmin (admin.ModelAdmin):
    
    