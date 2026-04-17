from django.shortcuts import render

# Create your views here.




def add_student(request):
    if request.method == "post":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        student_id = request.POST.get("student_id")
        gender = request.POST.get("gender ")
        date_of_birth = request.POST.get("date_of_birth")
        student_class  = request.POST.get("student_class ")
        religion = request.POST.get("religion")
        joining_date = request.POST.get("joining_date")
        mobile_number = request.POST.get("mobile_number")
        admission_number  = request.POST.get("admission_number ")
        section = request.POST.get("section")
        student_image = request.FILES.get("student_image")


        #PARENT DATA from the formn 

        father_name = request.POST.get(father_name) 
        father_occupation = request.POST.get(father_occupation) 
        father_mobile = request.POST.get(father_mobile) 
        father_email = request.POST.get(father_email) 
     
        mother_name = request.POST.get(mother_name) 
        fat_occupation = request.POST.get(fat_occupation) 
        father_mobile = request.POST.get(father_mobile) 
        father_email = request.POST.get(father_email) 

    return render(request, "student/add-student.html")

def student_list(request):
    return render(request, "student/students.html")

def edit_student(request):
    return render(request, "student/edit-student.html")

def view_details(request):
    return render(request, "student/student-details.html")
