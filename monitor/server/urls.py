from django.conf.urls import url,include 
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# router.register(r'base', views.UserViewSet)

urlpatterns = [
    url(r'^regist/$', views.regist),
    url(r'^baseinfo/$', views.BaseDatas.as_view()),
    url(r'^topcpu/$', views.TopCpus.as_view()),
    url(r'^topmem/$', views.TopMems.as_view()),
    url(r'^openport/$', views.OpenPorts.as_view()),
    url(r'^openport_list/$', views.UserPortList.as_view()),
    url(r'^shafile/$', views.CheckFielsd.as_view()),
    url(r'^successip/$', views.SuccessIps.as_view()),
    url(r'^faileip/$', views.FaileIps.as_view()),
    url(r'^email_template/$',views.email_template),#test for view the email template
    url(r'^', include(router.urls)),
]
