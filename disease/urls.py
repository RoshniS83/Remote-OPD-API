from django.urls import path
from disease.views import DiseaseAPI

urlpatterns = [
    path('alldisease/', DiseaseAPI.as_view({'get':'list'})),
    path('diseasebyid/<int:pk>/', DiseaseAPI.as_view({'get':'retrieve'})),
    path('createDisease/', DiseaseAPI.as_view({'post':'create'})),
    path('updateDisease/<int:pk>/', DiseaseAPI.as_view({'put': 'update'})),
    path('deleteDisease/<int:pk>/', DiseaseAPI.as_view({'delete': 'destroy'}))

]