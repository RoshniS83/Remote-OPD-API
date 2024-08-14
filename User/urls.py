from django.urls import path

from User.views import UserAPI, UserLoginAPI

urlpatterns = [
          path('getallusers/', UserAPI.as_view({'get': 'list'})),
          path('getuserdetails/<int:pk>/', UserAPI.as_view({'get': 'retrieve'})),
          path('adduser/', UserAPI.as_view({'post': 'create'})),
          path('updateuser/<int:pk>/', UserAPI.as_view({'put': 'update'})),
          path('partialupdateuser/<int:pk>/', UserAPI.as_view({'patch': 'partial_update'})),
          path('deleteuser/<int:pk>/', UserAPI.as_view({'delete': 'destroy'})),

          path('auth/login/', UserLoginAPI.as_view()),

]
