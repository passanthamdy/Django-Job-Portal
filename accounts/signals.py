from accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail


@receiver(post_save, sender=User)
def send_email_user(sender, instance, created, **kwargs):
    if created:
        #send email logic
        print(instance.username)
        send_mail("Job Portal", f"Hello {instance.username}, please wait for your email confirmation from admin","job_portal@gmail.com",['passant@mail.com'])
        
       
        
