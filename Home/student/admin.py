from django.contrib import admin


from django.contrib import admin 
from .models import Student ,Parent


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    search_fields = ('father_name', 'mother_name', 'father_mobile', 'mother_mobile')
    list_filter = ('father_name', 'mother_name')

@admin.register(Student)
class StudentAdmin (admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'gender', 'student_id', 'student_class', 'joining_date', 'mobile_number', 'admission_number', 'section')
    list_filter = ('student_class', 'section', 'gender')
    readonly_fields = ['student_image'] #optional make student image feild read-only 




    def student_image(self, obj):
        if obj.student_img:   # <-- must match models.py field name
            return format_html('<img src="{}" width="100" />', obj.student_img.url)
        return "No Image"

