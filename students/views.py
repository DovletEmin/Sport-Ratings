from django.shortcuts import render
from .models import Student, ExerciseResult
from .serializers import StudentSerializer, ExerciseResultSerializer
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']


class ExerciseResultViewSet(viewsets.ModelViewSet):
    queryset = ExerciseResult.objects.all()
    serializer_class = ExerciseResultSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    