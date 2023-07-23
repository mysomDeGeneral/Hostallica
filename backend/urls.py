from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views._login, name='login'),
    path('student-register/', views.student_register, name='student_register'),
    path('halls/', views._hall, name='halls'),
    path('hall/<int:pk>', views._rooms, name='rooms'),
    path('booking/<int:room_id>', views._booking, name='booking'),
    path('manager-home/', views.hall_manager_home, name='hall_manager_home'),
    path('logout/', views.logout_user, name='logout'),
    path('confirmation/', views._confirmation, name='confirmation'),
    path('success/', views.success_view, name='success'),
    
    path('charge/', views.charge, name='charge'),

    #test url
    path('test/', views.test, name='test'),


]

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 