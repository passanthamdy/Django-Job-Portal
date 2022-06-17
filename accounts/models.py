from django.db import models
from django.contrib.auth.models import AbstractUser
from tags.models import Tag
from datetime import datetime
from django.utils.timezone import now
from django.core.validators import FileExtensionValidator

# # Create your models here.
GENDER = (
    ('MALE', 'male'),
    ('FEMALE', 'Female'),
)
USER_TYPE = (
    ('DEVELOPER', 'Developer'),
    ('COMPANY', 'Company'),
)


class User(AbstractUser):
    user_type = models.CharField(choices=USER_TYPE, max_length=50, default="DEVELOPER")
    allow_notification = models.BooleanField(default=False)
    gender = models.CharField(choices=GENDER, max_length=50, default='FEMALE')
    dob = models.DateField(default=now)
    # Developer fields
    cv = models.FileField(upload_to='user_cvs/', null=True, blank=True,validators=[FileExtensionValidator(allowed_extensions=["pdf"])])
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    # Company Fields
    company_name = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    history = models.ManyToManyField("self", blank=True, null=True)

    def __str__(self):
        return self.username + ' ' + self.user_type
