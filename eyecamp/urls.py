from django.urls import path
from eyecamp.views import EyeCampAPI, EyeCampExcelSheet, EyeCampReport

urlpatterns= [
    path("addeyecamp/", EyeCampAPI.as_view({'post':'create'})),
    path("getalleyecamp/", EyeCampAPI.as_view({'get':'list'})),
    path("eyecamp/<int:pk>/", EyeCampAPI.as_view({'get':'retrieve'})),
    path("eyecamp/<int:pk>/update/", EyeCampAPI.as_view({'put':'update'})),
    path("eyecamp/<int:pk>/partial-update/", EyeCampAPI.as_view({'patch':'partial_update'})),
    path("eyecamp/<int:pk>/delete/", EyeCampAPI.as_view({'delete': 'destroy'})),
    path('eyecampExcelsheet/', EyeCampExcelSheet.as_view()),
    path('eyecampReport/', EyeCampReport.as_view())
]