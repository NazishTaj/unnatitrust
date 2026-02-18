from django.shortcuts import render
from website.models import Gallery
from django.shortcuts import render, redirect
from website.models import StudentRegistration

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def university(request):
    return render(request, 'university.html')

def registration(request):
    return render(request, 'registration.html')


def contact(request):
    return render(request, 'contact.html')

def termsandconditions(request):
    return render(request, 'terms.html')

def privacypolicy(request):
    return render(request, 'privacypolicy.html')




def gallery(request):
    images = Gallery.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery.html', {'images': images})



def student_registration(request):
    if request.method == "POST":
        student = StudentRegistration.objects.create(
            First_Name=request.POST.get("First_Name"),
            Last_Name=request.POST.get("Last_Name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            gender=request.POST.get("gender"),
            education=request.POST.get("education"),
            category=request.POST.get("category"),
            country=request.POST.get("country"),
            dob=request.POST.get("dob"),
            father=request.POST.get("father"),
            mother=request.POST.get("mother"),
            Father_Phone=request.POST.get("fphone"),
            Mother_Phone=request.POST.get("mphone"),
            occupation=request.POST.get("occupation"),
            income=request.POST.get("income"),
            address=request.POST.get("address"),
            state=request.POST.get("state"),
            program=request.POST.get("program"),
            course=request.POST.get("course"),
            reference=request.POST.get("reference"),
        )
        return render(request, "success.html", {"student": student})

    return render(request, "registration.html")


def success_page(request):
    return render(request, "success.html")


