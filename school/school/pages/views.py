from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect

# Create your views here.
from classroom.functions import fetch_all_with_subjects_and_teachers
from django.urls import reverse
from teacher.functions import fetch_all_students_for_teacher, fetch_students_count_and_salary_sum

from subject.functions import fetch_data_for_subjects_with_more_than_1_teacher


def index(request):
    return render(request, 'pages/index.html')


def entities(request):
    return HttpResponseRedirect('admin')


def problem_statements(request):
    return render(request, 'pages/problem_statements.html')


def q1(request):
    context = fetch_all_with_subjects_and_teachers()
    return render(request, 'pages/q1.html', context)


def q2(request):
    key = 'teacher_name'
    if key in request.GET:
        teacher_name = request.GET[key]
        students = fetch_all_students_for_teacher(teacher_name)
        context = {
            'students': students
        }
        return JsonResponse(context)
    else:
        return render(request, 'pages/q2.html')


def q3(request):
    no_of_students, total_salary = fetch_students_count_and_salary_sum(1)
    context = {
        'no_of_students': no_of_students,
        'total_salary': total_salary
    }
    return render(request, 'pages/q3.html', context)


def q4(request):
    data = fetch_data_for_subjects_with_more_than_1_teacher()
    context = {
        'subjects': data
    }
    return render(request, 'pages/q4.html', context)
