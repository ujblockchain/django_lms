from django.shortcuts import render
from django.http import Http404

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from .models import Student 

# Create your views here.
@login_required
def index(request):
    students = Student.objects.all().order_by('-first_name')
    total_students = students.count()
    return render(request, 'students/index.html', {
        'students': students,
        'total_students': total_students
    })
    
def student_detail(request, student_id): 
    try: 
        student = Student.objects.get(id=student_id)
    except: 
        raise Http404("Student not found")
    return render(request, 'students/student_details.html', {
        'firstname': student.first_name, 
        'lastname': student.last_name,
        'age': student.age,
        'is_registered': student.is_registered,
    })
    
def authView(request): 
    if request == "POST": 
        pass
    else: 
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        "form": form
    })
    
    
