from .models import Subject


def fetch_data_for_subjects_with_more_than_1_teacher():
    context = []
    subjects = Subject.objects.all()

    for subject in subjects:
        data = {}
        data['name'] = subject.name

        teacher_count = subject.teacher_set.count()

        if teacher_count > 1:
            students_count = subject.student_set.count()
            total_minutes = subject.total_duration

            data['teacher_count'] = teacher_count
            data['students_count'] = students_count
            data['total_hours'] = total_minutes / 60

            context.append(data)

    return context
