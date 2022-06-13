from distutils import text_file
from django.db import models
from accounts.models import User
from tags.models import Tag
# Create your models here.
STATUS=(
    ('OPEN','Open'),
    ('IN_PROGRESS','In Progress'),
    ('FINISHD','Finished')
)

class Job(models.Model):
    name=models.CharField( max_length=50)
    job_owner=models.ForeignKey("accounts.User", verbose_name="Job Owner",related_name='job_owner', on_delete=models.CASCADE)
    description = models.TextField()
    Tags = models.ManyToManyField("tags.Tag", verbose_name="Job's tags")
    applied_developers = models.ManyToManyField("accounts.User",related_name='developers', verbose_name="Applied Developer",null=True, blank=True)
    developer = models.ForeignKey("accounts.User", verbose_name="Accepted Developer",blank=True,null=True, on_delete=models.SET_NULL)
    status=models.CharField(choices=STATUS, max_length=50)
    creation_time=models.DateTimeField( auto_now=False, auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.name

