from jobs.models import Job
from django.db.models.signals import m2m_changed,pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from accounts.models import User
from notifications.models import Notification
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
        
        
@receiver(pre_save,sender=Job)   
def send_mails_to_users_and_company(instance,*args,**kwargs):
    print(instance)
    if instance.id is not None:
        if instance.status=="FINISHD":
            job_owner=instance.job_owner
            developer=instance.developer
            if(job_owner.allow_notification == True):
                            job_owner_notification=Notification.objects.create(username=instance.job_owner,message=f"{instance.job_owner.username} Your Job Has Been Finished",created_at="2020-06-17") 
                            send_mail("Job Progress",
                f"Hello Job Owner The Job Status Is Changed To Finish ",
                "job_portal@gmail.com",
                [job_owner.email])
            else:
                         send_mail("Job Progress",
                f"Hello Job Owner You do not allow the Notifications On ",
                "job_portal@gmail.com",
                [job_owner.email])
                         
            if(developer.allow_notification == True):
                            developer_notification=Notification.objects.create(username=instance.developer,message=f"{instance.developer.username} Your Job Has Been Finished",created_at="2020-06-17") 
                            send_mail("Job Progress",
                f"Hello Developer The Job Status Is Changed To Finish ",
                "job_portal@gmail.com",
                [developer.email])
            else:
                         send_mail("Job Progress",
                f"Hello Developer You do not allow the Notifications On ",
                "job_portal@gmail.com",
                [developer.email])            
                         
                            
                            
                

                
           
            
            
            
        
        
         
        

       
        
