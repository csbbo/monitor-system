from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(UserToken)
admin.site.register([
    BaseInfoSwitch,CpuSwitch,MemSwitch,PortSwitch,
    FileSwitch,SuccessIpSwitch,FailIpSwitch,IntrusionIpSwitch,
    IntrusionFileSwitch,IntrusionNewIpSwitch
])