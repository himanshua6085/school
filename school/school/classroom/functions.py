from .models import Classroom


def fetch_all_with_subjects_and_teachers():
    map = {}

    classrooms = []
    map['classrooms'] = classrooms

    for class_room in Classroom.objects.all():
        classroom = {}
        classrooms.append(classroom)

        classroom['name'] = class_room.name

        subjects = set()
        classroom['subjects'] = subjects

        teachers = set()
        classroom['teachers'] = teachers

        for subject in class_room.subject_set.all():
            for teacher in subject.teacher_set.all():
                teachers.add(teacher.name)
            subjects.add(subject.name)

    return map
