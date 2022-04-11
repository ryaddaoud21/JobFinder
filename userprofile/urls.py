from . import views
from django.urls import  path , include

urlpatterns = [
    path('' , views.dashboard, name= 'dashboard'),
    path('application/<int:application_id>/', views.view_application, name= 'view_application'),
    path('job/<int:job_id>/', views.view_job_dashboard, name='git  '),

]