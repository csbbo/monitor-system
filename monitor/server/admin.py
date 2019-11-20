from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(ServerToken)
admin.site.register([
    BaseData,TopCpu,TopMem,OpenPort,
    UserPorts,CheckFiels,SuccessIp,
    FaileIp
])