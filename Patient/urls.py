from django.urls import path
from Patient.views import PatientAPI, ExcelReport, WeeklyReport, VillageWiseGenderReport,VillageWiseAgeGroupReport
from django.urls import path
from Patient.views import PatientAPI, ExcelReport, WeeklyReport, VillageWiseGenderReport,VillageWiseAgeGroupReport
from Patient.views import MonthlySummaryReport, SummaryDiseaseWiseWeeklyReport, PatientHistoryAPI
urlpatterns = [
          path('addopdform/', PatientAPI.as_view({'post': 'create'})),
          path('opdforms_paginated/', PatientAPI.as_view({'get': 'list'})),
          path('opdsearch/', PatientAPI.as_view({'get':'search'})),
          path('opdform/<int:pk>/', PatientAPI.as_view({'get': 'retrieve'})),
          path('opdform/<int:pk>/update/', PatientAPI.as_view({'put': 'update'})),
          path('opdform/<int:pk>/partial-update/', PatientAPI.as_view({'patch': 'partial_update'})),
          path('opdform/<int:pk>/delete/', PatientAPI.as_view({'delete': 'destroy'})),
          path('excelreport/', ExcelReport.as_view()),
        #   path('monthly-weekly-report/', MonthlyWeeklyReport.as_view()),
          path('weeklyreport/', WeeklyReport.as_view()),
          path('VillageWiseGenderReport/', VillageWiseGenderReport.as_view()),
          path('VillageWiseAgeGroupReport/', VillageWiseAgeGroupReport.as_view()),
          path('MonthlySummaryReport/', MonthlySummaryReport.as_view()),
          path('SummaryDiseaseWiseWeeklyReport/', SummaryDiseaseWiseWeeklyReport.as_view()),
          path('PatientHistory/', PatientHistoryAPI.as_view()),
]

