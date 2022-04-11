from django.contrib import admin
from django.urls import path ,include
from .views import frontpage,signup
from django.contrib.auth.views import LogoutView , LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('userprofile.urls')),
    path('jobs',include('jobs.urls')),
    path('',frontpage, name='frontpage'),
    path('signup/',signup,name ='signup'),
    path('logout/',LogoutView.as_view() , name = 'logout'),
    path('login/', LoginView.as_view(template_name = 'core/login.html') , name ='login' ) ,
]
