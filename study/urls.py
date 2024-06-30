from django.urls import path

from .apps import StudyConfig
from .views import StudyCreateAPIView, StudyListAPIView, StudyUpdateAPIView, StudyDestroyAPIView, StudyRetrieveAPIView

app_name = StudyConfig.name

urlpatterns = [
    path('study/create/', StudyCreateAPIView.as_view(), name='study_create'),  # Создание
    path('study/', StudyListAPIView.as_view(), name='study_list'),  # Список
    path('study/<int:pk>/update', StudyUpdateAPIView.as_view(), name='study_update'),  # Редактирование
    path('study/<int:pk>/delete', StudyDestroyAPIView.as_view(), name='study_delete'),  # Удаление
    path('study/<int:pk>/', StudyRetrieveAPIView.as_view(), name='study_retrieve'),  # Просмотр
]
