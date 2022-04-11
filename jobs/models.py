from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=255)
    show_description = models.TextField()
    long_desctiption = models.TextField(blank=True , null=True)
    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job ,related_name='applications', on_delete=models.CASCADE)
    content = models.TextField()
    experience = models.TextField()
    created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    image = models.ImageField(upload_to='Jobseeker')
    def __str__(self):
        return self.job.title


@property
def imageURL(self):
        try:
            url = self.image.url
        except :
            url =''
        return url



