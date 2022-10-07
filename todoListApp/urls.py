
from django.urls import path

from todoListApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('<str:id>/delete', views.delete_task, name='delete_task'),
    path('<str:id>/completed', views.completed_task, name='completed_task'),
  
    
    
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
