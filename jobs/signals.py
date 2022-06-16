from jobs.models import Job
from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from accounts.models import User
from django import db
from notifications.models import Notification


@receiver(m2m_changed, sender=Job.Tags.through)
def send_mails_to_matched_users(sender, instance, action, **kwargs):
    if action == 'post_add':
        # send email logic
        tags = instance.Tags.all()
        users = User.objects.filter(tags__in=tags)
        users_emails = []
        for user in users:
            users_emails.append(user.email)
        users_emails = list(set(users_emails))
        print(users_emails)
        send_mail("Job Portal",
                  f"Hello job seekers , this job matches your tags, you can apply",
                  "job_portal@gmail.com",
                  ['passant@gmail.com'])


@receiver(pre_save, sender=Job)
def send_mails_to_accepted_users(sender, instance, **kwargs):
    if instance.id is not None:
        users_emails = []
        accepted_user = instance.developer

        print(accepted_user.email)
        if accepted_user.id != None:
            users = User.objects.exclude(id=accepted_user.id)

            for user in users:
                users_emails.append(user.email)
            users_emails = list(set(users_emails))
            send_mail("Job Portal",
                      f"GG man you are accepted",
                      "job_portal@gmail.com",
                      [accepted_user.email])
            Notification.objects.create(
                username=accepted_user, message="GG man you are accepted"
            )
            send_mail("Job Portal",
                      f"Sorry guys you not accepted, try again later",
                      "job_portal@gmail.com",
                      users_emails)
