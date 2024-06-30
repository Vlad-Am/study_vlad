from rest_framework import generics

from .models import Study
from .serializer import StudySerializer


class StudyListAPIView(generics.ListAPIView):
    """ Отвечает за просмотр списка образовательных модулей"""
    serializer_class = StudySerializer
    queryset = Study.objects.all()


class StudyCreateAPIView(generics.CreateAPIView):
    """ Отвечает за создание сущности образовательного модуля"""
    serializer_class = StudySerializer


class StudyUpdateAPIView(generics.UpdateAPIView):
    """ Отвечает за редактирование сущности образовательного модуля"""
    serializer_class = StudySerializer
    queryset = Study.objects.all()


class StudyRetrieveAPIView(generics.RetrieveAPIView):
    """ Отвечает за просмотр сущности образовательного модуля"""
    serializer_class = StudySerializer
    queryset = Study.objects.all()


class StudyDestroyAPIView(generics.DestroyAPIView):
    """ Отвечает за удаление сущности образовательного модуля"""
    serializer_class = StudySerializer
    queryset = Study.objects.all()
