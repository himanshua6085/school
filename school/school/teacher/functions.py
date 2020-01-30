from .models import Teacher


def fetch_all_students_for_teacher(teacher_name):
    teachers = Teacher.objects.filter(name__icontains=teacher_name)
    students = list()
    data = set()

    for teacher in teachers:
        for subject in teacher.subjects.all():
            for student in subject.student_set.all():
                if student.id not in data:
                    data.add(student.id)
                    students.append(student.name)

    return students


def fetch_students_count_and_salary_sum(monthly_salary):
    annual_salary = monthly_salary * 12
    teachers = Teacher.objects.filter(salary__gte=annual_salary)
    data = set()

    total_salary = 0

    for teacher in teachers:
        total_salary += teacher.salary
        for subject in teacher.subjects.all():
            for student in subject.student_set.all():
                data.add(student.id)

    no_of_students = len(data)
    return (no_of_students, total_salary)
