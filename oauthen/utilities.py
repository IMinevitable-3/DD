from random import randint 
from django.core.mail import send_mail
from config import settings

def sendmail(to_mail):
    head = "password reset"
    pss = str(randint(1000, 9999))
    message = "your new password" + pss + "\nthis is bot generated email\ndo not reply"
    send_mail(head , message , settings.EMAIL_HOST_USER , [to_mail] )
    return pss 


    