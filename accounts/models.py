from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    job_title = models.CharField(max_length=30,blank=False)
    
