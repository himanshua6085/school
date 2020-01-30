from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entities', views.entities, name='entities'),
    path('problem_statements', views.problem_statements, name='problem_statements'),
    path('q1', views.q1, name='q1'),
    path('q2', views.q2, name='q2'),
    path('q3', views.q3, name='q3'),
    path('q4', views.q4, name='q4'),
]