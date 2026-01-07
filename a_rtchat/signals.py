# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from .models import *
# import shortuuid
#
#
# @receiver(pre_save,sender = ChatGroup)
# def set_group_code(sender,instance,**kwargs):
#     if not instance.group_name:
#         instance.group_name = shortuuid.uuid()
