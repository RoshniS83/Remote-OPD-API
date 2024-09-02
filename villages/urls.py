from django.urls import path
from villages.views import VillagesAPI

urlpatterns =  [
    path('allvillages/', VillagesAPI.as_view({'get':'list'})),
    path('villagesbyId/<int:pk>/', VillagesAPI.as_view({'get':'retrieve'})),
    path('villagebyName/<str:name>/',VillagesAPI.as_view({'get':'retrieve_byname'})),
    path('createVillage/', VillagesAPI.as_view({'post':'create'})),
    path('updateVillage/<int:pk>/update', VillagesAPI.as_view({'put': 'update'})),
    path('updateVillage/<int:pk>/partial-update',VillagesAPI.as_view({'patch': 'partial_update'})),
    path('deleteVillage/<int:pk>/', VillagesAPI.as_view({'delete': 'destroy'}))

]

