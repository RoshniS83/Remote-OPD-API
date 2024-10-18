from django.urls import path
from megacamp.views import MegacampAPI, MegacampExcelSheet

urlpatterns = [
	path('addmegacamp/', MegacampAPI.as_view({'post':'create'})),
	path('getallmegacamp', MegacampAPI.as_view({'get':'list'})),
	path('megacampbyid/<int:pk>/', MegacampAPI.as_view({'get':'retrieve'})),
	path('updatemegacamp/<int:pk>', MegacampAPI.as_view({'put':'update'})),
	path('deletemegacamp/<int:pk>', MegacampAPI.as_view({'delete':'destroy'})),
	path('excelsheetmegacamp/', MegacampExcelSheet.as_view()),

]