from django.contrib import admin
# from django.db.models.signals import post_save, pre_save
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver
from .models import Inscription

admin.site.register(Inscription)


# @receiver(post_save, sender=Inscription)
# def send_email(sender, instance, **kwargs):

#     "Subject here",
#     "Here is the message.",
#     "from@example.com",
#     ["to@example.com"],
#     fail_silently=False,


    # status = instance.get_status_display()
    # # status.get_variable()
    # # status = dict(instance['status'].choices)[status]

    # # email creation
    # context = {
    #     'date': instance.created_at.strftime(f'%d/%m/%Y'),
    #     'title': instance.title,
    #     'description': instance.description,
    #     'status': status,
    #     'slug': instance.slug,
    #     'link': 'https://pupil.coractium.com/contato/ticket'
    # }
