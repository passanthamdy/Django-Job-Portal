from jobs.models import Job
from django.db.models.signals import m2m_changed,pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from accounts.models import User
from notifications.models import Notification
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
        

       
@receiver(pre_save,sender=Job)   
def send_mails_to_users_and_company(instance,*args,**kwargs):
    print(instance)
    if instance.id is not None:
        if instance.status=="FINISHD":
            job_owner=instance.job_owner
            developer=instance.developer
            if job_owner.allow_notification == True:              
                job_owner_notification=Notification.objects.create(username=instance.job_owner,message=f"{instance.job_owner.username} Your Job Has Been Finished",created_at="2020-06-17") 
                send_mail("Job Progress",
                f"Hello {instance.job_owner.username} The Job Status Is Changed To Finish ",
                "job_portal@gmail.com",
                [job_owner.email])
                         
            if developer.allow_notification == True:
                developer_notification=Notification.objects.create(username=instance.developer,message=f"{instance.developer.username} Your Job Has Been Finished",created_at="2020-06-17") 
                send_mail("Job Progress",
                f"Hello {instance.developer.username} The Job Status Is Changed To Finish ",
                "job_portal@gmail.com",
                [developer.email])                    
                            
                            

@receiver(pre_save, sender=Job)
def send_mails_to_accepted_users(sender, instance, **kwargs):
    if instance.id is not None:
        users_emails = []
        accepted_user = instance.developer
        if accepted_user:
            for user in users_emails:
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
           

@receiver(m2m_changed, sender=Job.applied_developers.through)
def send_mails_to_applied_developers(sender, instance, action, **kwargs):
    if action == 'post_add':
        #send email logic
        job_owner_email=instance.job_owner.email
        send_mail("Job Portal",
         f"New developer applied for your {instance.name} job you can accept the qualified one by visiting the job",
         "job_portal@gmail.com",
         [job_owner_email])
                              

                
            
            
            
            
        
        
         
        

     