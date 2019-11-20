from django.db import models
from datetime import datetime

# Create your models here.


class ServerToken(models.Model):

    token = models.CharField(max_length=100,null=False)
    user = models.OneToOneField('auth.User',related_name='token',on_delete=models.CASCADE)

class BaseData(models.Model):
    hostname = models.CharField(max_length=100,null=False)

    boot_time = models.CharField(max_length=100,null=False)
    cpu_count = models.IntegerField(null=False)
    cpu_percent = models.FloatField(null=False)

    mem_total = models.CharField(max_length=100,null=False)
    mem_percent = models.FloatField(null=False)
    mem_used = models.CharField(max_length=100,null=False)
    mem_free = models.CharField(max_length=100,null=False)

    disk_total = models.CharField(max_length=100,null=False)
    disk_percent = models.FloatField(null=False)
    disk_used = models.CharField(max_length=100,null=False)
    disk_free = models.CharField(max_length=100,null=False)
    user = models.OneToOneField('auth.User',related_name='basedata',on_delete=models.CASCADE)

class TopCpu(models.Model):
    cpu_name = models.CharField(max_length=100,null=False)
    cpu_use = models.CharField(max_length=10,null=False)
    user = models.ForeignKey('auth.User',related_name='cpus',on_delete=models.CASCADE)

class TopMem(models.Model):
    mem_name = models.CharField(max_length=100,null=False)
    mem_use = models.CharField(max_length=100,null=False)
    user = models.ForeignKey('auth.User',related_name='mems',on_delete=models.CASCADE)

class OpenPort(models.Model):
    port = models.CharField(max_length=10,null=False)
    detail = models.CharField(max_length=100,null=True)
    user = models.ForeignKey('auth.User',related_name='ports',on_delete=models.CASCADE)

class UserPorts(models.Model):
    port_list = models.CharField(max_length=200,null=False)
    user = models.OneToOneField('auth.User',related_name='port_list',on_delete=models.CASCADE)

class CheckFiels(models.Model):
    filepath = models.CharField(max_length=100,null=False)
    sha256 = models.CharField(max_length=100,null=False)
    user = models.ForeignKey('auth.User',related_name='checkfiles',on_delete=models.CASCADE)

class SuccessIp(models.Model):
    username = models.CharField(max_length=20,null=False)
    terminal_local = models.CharField(max_length=20,null=False)
    ip_addr = models.CharField(max_length=20,null=False)
    week = models.CharField(max_length=10,null=False)
    month = models.CharField(max_length=10,null=False)
    date = models.CharField(max_length=10,null=False)
    login_time = models.CharField(max_length=10,null=False)
    login_statu = models.CharField(max_length=20,null=False)
    user = models.ForeignKey('auth.User',related_name='successip',on_delete=models.CASCADE)

class FaileIp(models.Model):
    username = models.CharField(max_length=20,null=False)
    terminal_local = models.CharField(max_length=20,null=False)
    ip_addr = models.CharField(max_length=20,null=False)
    week = models.CharField(max_length=10,null=False)
    month = models.CharField(max_length=10,null=False)
    date = models.CharField(max_length=10,null=False)
    login_time = models.CharField(max_length=10,null=False)
    login_statu = models.CharField(max_length=20,null=False)
    user = models.ForeignKey('auth.User',related_name='faileip',on_delete=models.CASCADE)

