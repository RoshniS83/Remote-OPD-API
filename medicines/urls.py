from django.urls import path
from medicines.views import MedicinesAPI

urlpatterns = [
    path('allmedicines/', MedicinesAPI.as_view({'get': 'list'})),
    path('medicinesbyid/<int:pk>/', MedicinesAPI.as_view({'get': 'retrieve'})),
    path('createmedicines/', MedicinesAPI.as_view({'post': 'create'})),
    path('updatemedicines/<int:pk>/', MedicinesAPI.as_view({'put': 'update'})),
    path('deletemedicines/<int:pk>/', MedicinesAPI.as_view({'delete': 'destroy'}))

]