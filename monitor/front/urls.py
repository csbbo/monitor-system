from django.conf.urls import url,include 
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# router.register(r'base', views.UserViewSet)

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^base/$', views.BaseInfo.as_view()),
    url(r'^cpu/$', views.TopCpus.as_view()),
    url(r'^mem/$', views.TopMems.as_view()),
    url(r'^ports/$', views.OpenPorts.as_view()),
    url(r'^files/$', views.CheckFielsd.as_view()),
    url(r'^successip/$', views.SuccessIps.as_view()),
    url(r'^faileip/$', views.FaileIps.as_view()),
    ##
    url(r'^base_email/$',views.BaseInfoSwitchStatu.as_view()),  #control cpu mem
    url(r'^cpu_email/$',views.CpuSwitchStatu.as_view()),
    url(r'^mem_email/$',views.MemSwitchStatu.as_view()),
    url(r'^ports_email/$',views.PortSwitchStatu.as_view()),
    url(r'^files_email/$',views.FileSwitchStatu.as_view()),
    url(r'^successip_email/$',views.SuccessIpSwitchStatu.as_view()),
    url(r'^faileip_email/$',views.FailIpSwitchStatu.as_view()),
    ##
    url(r'^intrusionnewip_email/$',views.IntrusionNewIpSwitchStatu.as_view()),
    url(r'^intrusionip_email/$',views.IntrusionIpSwitchStatu.as_view()),
    url(r'^intrusionfile_email/$',views.IntrusionFileSwitchStatu.as_view()),    #control two file
    url(r'^', include(router.urls)),
]
