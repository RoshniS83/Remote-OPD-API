from django.urls import path
from hbcamp.views import HBCampAPI, HBCampExcelSheet, HBCampMonthlyReport

urlpatterns= [
    path("addhbcamp/", HBCampAPI.as_view({'post':'create'})),
    path("getallhbcamp/", HBCampAPI.as_view({'get':'list'})),
    path("hbcamp/<int:pk>/", HBCampAPI.as_view({'get':'retrieve'})),
    path("hbcamp/<int:pk>/update/", HBCampAPI.as_view({'put':'update'})),
    path("hbcamp/<int:pk>/partial-update/", HBCampAPI.as_view({'patch':'partial_update'})),
    path("hbcamp/<int:pk>/delete/", HBCampAPI.as_view({'delete': 'destroy'})),
    path('hbcampExcelsheet/', HBCampExcelSheet.as_view()),
    path('hbcampReport/', HBCampMonthlyReport.as_view())
]