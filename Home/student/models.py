from django.db import models

# Create your models here.
class Parent(models.Model):
    father_name = models.CharField(max_length=100)
    father_occupations = models.CharField(max_length=1000)
    father_mobile = models.CharField(max_length=100)
    father_email = models.EmailField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupations = models.CharField(max_length=1000)
    mother_mobile = models.CharField(max_length=100)
    mother_email = models.EmailField(max_length=100)
    present_addess = models.TextField()
    permanent_addess = models.TextField()

    def __str__(self) -> str:
        return f"(self.father_name) and (self.mother_name)"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id =  models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('male', 'male'), ('female', 'female'), ('other', 'other')])
    date_of_birth = models.DateField()
    student_class = models.CharField(max_length=100)
    religion = models.CharField(max_length=20)
    joining_date = models.DateField()
    mobile_number = models.CharField(max_length=15)
    admission_number = models.CharField(max_length=200)
    section = models.CharField(max_length = 15)
    student_img = models.ImageField(upload_to='student/' , blank = True)
    parent = models.OneToOneField(  Parent, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name}-{self.last_name}")
        super(Student,self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"