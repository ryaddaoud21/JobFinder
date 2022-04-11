from .views import add_job, jobdetails , apply_for_job  , edit_job , delete_job
from django.urls import path,include

urlpatterns = [
    path('<int:job_id>/', jobdetails, name='job_details'),
    path('add/', add_job, name='job_add'),
    path('<int:job_id>/apply/', apply_for_job, name='apply_for_job'),
    path('<int:job_id>/edit/', edit_job, name='edit_job'),
    path('<int:job_id>/delete/', delete_job, name='delete_job'),
]