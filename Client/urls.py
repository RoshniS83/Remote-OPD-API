from django.urls import path

from Client.views import ClientAPI

urlpatterns = [
          path('allclients/', ClientAPI.as_view({'get': 'list'})),
          path('clientdetails/<int:pk>/', ClientAPI.as_view({'get': 'retrieve'})),
          path('addclient/', ClientAPI.as_view({'post': 'create'})),
          path('updateclient/<int:pk>/', ClientAPI.as_view({'put': 'update'})),
          path('partialupdateclient/<int:pk>/', ClientAPI.as_view({'patch': 'partial_update'})),
          path('deleteclient/<int:pk>/', ClientAPI.as_view({'delete': 'destroy'})),

]
