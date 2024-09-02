from django.urls import path
from camps.views import CampsAPI

urlpatterns = [
    path('allcamps/', CampsAPI.as_view({'get':'list'})),
    path('campsbyid/<int:pk>/', CampsAPI.as_view({'get':'retrieve'})),
    path('createcamps/', CampsAPI.as_view({'post':'create'})),
    path('updatecamps/<int:pk>/', CampsAPI.as_view({'put': 'update'})),
    path('deletecamps/<int:pk>/', CampsAPI.as_view({'delete': 'destroy'}))

]