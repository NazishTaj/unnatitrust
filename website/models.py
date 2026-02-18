from django.db import models
import uuid


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class StudentRegistration(models.Model):
    # Auto student ID
    student_id = models.CharField(max_length=20, unique=True, blank=True)

    # Student details
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    education = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    dob = models.CharField(max_length=20)

    # Parent details
    father = models.CharField(max_length=100)
    mother = models.CharField(max_length=100)
    Father_Phone = models.CharField(max_length=15)
    Mother_Phone = models.CharField(max_length=15, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    income = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=100)

    # Course
    program = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    reference = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.student_id:
            self.student_id = "STU" + str(uuid.uuid4().hex[:6]).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student_id} - {self.First_Name} {self.Last_Name}"
