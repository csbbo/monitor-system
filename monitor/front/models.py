from django.db import models

# Create your models here.

class UserToken(models.Model):
    token = models.CharField(max_length=100,null=False)
    user = models.OneToOneField('auth.User',related_name='usertoken',on_delete=models.CASCADE)

# 下面表中的真假值代表是否开启邮件通知
class BaseInfoSwitch(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    switch = models.BooleanField(default=True)

class CpuSwitch(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    switch = models.BooleanField(default=True)

class MemSwitch(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    switch = models.BooleanField(default=True)

class PortSwitch(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    switch = models.BooleanField(default=True)

class FileSwitch(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    switch = models.BooleanField(default=True)

class SuccessIpSwitch(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    switch = models.BooleanField(default=True)

class FailIpSwitch(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    switch = models.BooleanField(default=False)
#
##
#
class IntrusionIpSwitch(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    switch = models.BooleanField(default=True)

class IntrusionFileSwitch(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    switch = models.BooleanField(default=True)

class IntrusionNewIpSwitch(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    switch = models.BooleanField(default=True)