from django.urls import path

from Patient.views import PatientAPI, ExcelReport

urlpatterns = [
          path('addopdform/', PatientAPI.as_view({'post': 'create'})),
          path('excelreport/', ExcelReport.as_view()),
]
