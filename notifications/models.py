from django.db import models


# Create your models here.
class Notification(models.Model):
    username = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.message
