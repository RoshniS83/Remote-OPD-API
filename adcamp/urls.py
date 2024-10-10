from django.urls import path
from adcamp.views import ADCampAPI, ADCampExcelSheet, ADCampMonthlyReport

urlpatterns= [
    path("addadcamp/", ADCampAPI.as_view({'post':'create'})),
    path("getalladcamp/", ADCampAPI.as_view({'get':'list'})),
    path("adcamp/<int:pk>/", ADCampAPI.as_view({'get':'retrieve'})),
    path("adcamp/<int:pk>/update/", ADCampAPI.as_view({'put':'update'})),
    path("adcamp/<int:pk>/partial-update/", ADCampAPI.as_view({'patch':'partial_update'})),
    path("adcamp/<int:pk>/delete/", ADCampAPI.as_view({'delete': 'destroy'})),
    path('adcampExcelsheet/', ADCampExcelSheet.as_view()),
    path('adcampReport/',ADCampMonthlyReport.as_view())
]