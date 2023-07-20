from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.student_login, name='login'),
    path('student-register/', views.student_register, name='student_register'),
    path('student-home/', views.student_home, name='student_home'),
    path('student-booking/<int:pk>', views.student_booking, name='student_booking'),
    path('student-booking-history/<int:pk>', views.student_booking_history, name='student_booking_history'),
    path('manager-home/', views.hall_manager_home, name='hall_manager_home'),
    path('logout/', views.logout_user, name='logout'),
]