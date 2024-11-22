from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Exam
from .forms import ExamForm

def add_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_exam')
    else:
        form = ExamForm()
    return render(request, 'add_exam.html', {'form': form})


def query1(request):
    exams = Exam.objects.filter(subject__name="Mathematics").values()
    return JsonResponse(list(exams), safe=False)

def query2(request):
    exams = Exam.objects.filter(subject__name="Mathematics", date="2024-01-15").values('student__last_name')
    return JsonResponse(list(exams), safe=False)

def query3(request):
    exams = Exam.objects.all()[:5].values()
    return JsonResponse(list(exams), safe=False)

def home(request):
    return render(request, 'base.html') 