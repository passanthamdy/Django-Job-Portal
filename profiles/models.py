import imp
from django.db import models
from accounts.models import User
from tags.models import Tag
# Create your models here.


class Developer(models.Model):
    developer = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    cv = models.FileField(upload_to='user_cvs/')
    gender=models.CharField(choices=GENDER, max_length=50)
    dob=models.DateField()
    tags = models.ManyToManyField(Tag)
    description = models.TextField()

    def __str__(self):
        return self.developer.username

class Company(models.Model):
    company = models.OneToOneField(
        User, on_delete=models.CASCADE)
    company_name=models.CharField( max_length=50)
    address = models.CharField(max_length=100)
    history= models.ManyToManyField(User)


    def __str__(self):
        return self.company_name