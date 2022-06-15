import imp
from jobs.models import Job
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from accounts.models import User
from django import db

@receiver(m2m_changed, sender=Job.Tags.through)
def send_mails_to_matched_users(sender, instance, action, **kwargs):
    if action == 'post_add':
        #send email logic
        tags=instance.Tags.all()
        users = User.objects.filter(tags__in=tags)
        users_emails=[]
        for user in users:
            users_emails.append(user.email)
        users_emails=list(set(users_emails))
        print(users_emails)
        send_mail("Job Portal",
         f"Hello job seekers , this job matches your tags, you can apply",
         "job_portal@gmail.com",
         ['passant@gmail.com'])
        

       
        
