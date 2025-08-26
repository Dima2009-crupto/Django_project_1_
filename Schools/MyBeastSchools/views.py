from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect


from .forms import SubjectForm, StudentForm
from .models import Subject, Student, Cabinet

# Create your views here.

def index(request):
    context = {
        "products": [
        {
            "name": "Молоко",
            "count": 20
        },
        {
            "name": "Яблуко",
            "count": 143
        },
        {
            "name": "Каштан",
            "count": 35
        },
        {
            "name": "Яйця",
            "count": 1219
        },
    ]}

    return render(request=request, template_name="index.html", context=context)


def add_subject(request):
    if request.method != "POST":
        form = SubjectForm()
        return render(request=request, template_name="add_subject.html", context=dict(form=form))
    
    form = SubjectForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data["name"]
        subject = Subject(name=name)
        subject.save()
        return redirect("get_subjects")
    
    
def get_subjects(request):
    subjects = Subject.objects.all()
    return render(request=request, template_name="subjects.html", context=dict(subjects=subjects))


def get_students(request):
    return render(
        request=request,
        template_name="students.html",
        context=dict(students=Student.objects.all())
    )

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            bio = form.cleaned_data.get("bio")
            cabinet = form.cleaned_data.get("cabinet")
            subjects = form.cleaned_data.get("subjects")

            student = Student(
                first_name=first_name,
                last_name=last_name,
                bio=bio,
                cabinet=cabinet,
            )
            student.subject.set(subjects)
            student.save()
            return redirect("get_students")
        
        return redirect("add_students") 
    
    return render(
        request=request,
        template_name="add_student.html",
        context=dict(form=StudentForm())
    )