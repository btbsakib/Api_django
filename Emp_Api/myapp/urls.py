from django.urls import path
from myapp import views

urlpatterns = [
 
   path('myapi/', views.api_list),
   path('apidetails/<int:pk>/', views.api_detail),
   path('myleave/', views.leave_list),
   path('leavedetails/<int:pk>/', views.leave_detail),
   path('getvacstatus/<int:pk>/', views.get_vacation_status),
   path('getvacationcount/<int:pk>/', views.get_vacation_count),
   path('getallvacationofemp/<int:pk>/', views.get_all_about),

]