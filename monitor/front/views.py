from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,exceptions
from rest_framework.views import APIView

from .jwt import md5
from .models import UserToken
from server.models import BaseData,TopCpu,TopMem,OpenPort,CheckFiels,SuccessIp,FaileIp
from server.serializers import UserSerializer,BaseDataSerializer,TopCpuSerializer,TopMemSerializer,OpenPortSerializer,CheckFielsSerializer,SuccessIpSerializer,FaileIpSerializer

from .models import *

class Authtication(object):
    """
    token认证
    """
    def authenticate(self,request):
        token = request.META.get('HTTP_TOKEN')
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        # 在rest framework内部会将这两个字段赋值给request.user,request.auth以供后续使用
        return (token_obj.user,token_obj)    
    def authenticate_header(self,request):
        pass


@csrf_exempt
@api_view(['POST'])
def login(request):
    ret = {'code':1000,'msg':None}
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        obj = User.objects.filter(username=username,password=password).first()
    except Exception as e:
        ret['code'] = 1002
        ret['msg'] = '请求异常'
    if obj:
    # if obj and check_password(password_hash,obj.password_hash):
        token = md5(username)
        UserToken.objects.update_or_create(user=obj,defaults={'token':token})
        ret['token'] = token
        ret['username'] = username
        return Response(ret)
    ret['code'] = 1001
    ret['msg'] = '用户名或密码错误'
    return Response(ret)

class BaseInfo(APIView):
    """
    获取服务器基本信息
    """
    authentication_classes = [Authtication,]
    def get(self,request,format=None):
        get_data = BaseData.objects.filter(user=self.request.user.id).first()
        serializer = BaseDataSerializer(get_data)
        return Response(serializer.data)

class TopCpus(APIView):
    """
    获取消耗cpu最高的进程
    """
    authentication_classes = [Authtication,]
    def get(self,request,format=None):
        get_data = TopCpu.objects.filter(user=self.request.user.id)
        serializer = TopCpuSerializer(get_data,many=True)
        return Response(serializer.data)

class TopMems(APIView):
    """
    获取消耗内存最高的进程
    """
    authentication_classes = [Authtication,]
    def get(self,request,format=None):
        get_data = TopMem.objects.filter(user=self.request.user.id)
        serializer = TopMemSerializer(get_data,many=True)
        return Response(serializer.data)

class OpenPorts(APIView):
    """
    获取端口开放信息
    """
    authentication_classes = [Authtication,]
    def get(self,request,format=None):
        get_data = OpenPort.objects.filter(user=self.request.user.id)
        serializer = OpenPortSerializer(get_data,many=True)
        return Response(serializer.data)

class CheckFielsd(APIView):
    """
    获取重要文件变动信息
    """
    authentication_classes = [Authtication,]
    def get(self,request,format=None):
        get_data = CheckFiels.objects.filter(user=self.request.user.id)
        serializer = CheckFielsSerializer(get_data,many=True)
        return Response(serializer.data)

class SuccessIps(APIView):
    """
    获取登录服务器成功ip信息
    """
    authentication_classes = [Authtication,]
    def get(self,request,format=None):
        get_data = SuccessIp.objects.filter(user=self.request.user.id).order_by("-id")
        serializer = SuccessIpSerializer(get_data,many=True)
        return Response(serializer.data)

class FaileIps(APIView):
    """
    获取登录服务器失败ip信息
    """
    authentication_classes = [Authtication,]
    def get(self,request,format=None):
        get_data = FaileIp.objects.filter(user=self.request.user.id).order_by("-id")
        serializer = FaileIpSerializer(get_data,many=True)
        return Response(serializer.data)
        

# 邮箱开启与否
class BaseInfoSwitchStatu(APIView):
    authentication_classes = [Authtication,]
    
    def get(self,request,format=None):
        get_data = BaseInfoSwitch.objects.filter(user=self.request.user.id).first()
        return Response({'email':get_data.switch})
    def put(self,request,format=None):
        get_data = BaseInfoSwitch.objects.filter(user=self.request.user.id).first()
        if get_data.switch == True:
            get_data.switch = False
        else:
            get_data.switch = True
        get_data.save()
        return Response({'email':get_data.switch})

class CpuSwitchStatu(APIView):
    authentication_classes = [Authtication,]
    
    def get(self,request,format=None):
        get_data = CpuSwitch.objects.filter(user=self.request.user.id).first()
        return Response({'email':get_data.switch})
    def put(self,request,format=None):
        get_data = CpuSwitch.objects.filter(user=self.request.user.id).first()
        if get_data.switch == True:
            get_data.switch = False
        else:
            get_data.switch = True
        get_data.save()
        return Response({'email':get_data.switch})

class MemSwitchStatu(APIView):
    authentication_classes = [Authtication,]
    
    def get(self,request,format=None):
        get_data = MemSwitch.objects.filter(user=self.request.user.id).first()
        return Response({'email':get_data.switch})
    def put(self,request,format=None):
        get_data = MemSwitch.objects.filter(user=self.request.user.id).first()
        if get_data.switch == True:
            get_data.switch = False
        else:
            get_data.switch = True
        get_data.save()
        return Response({'email':get_data.switch})

class PortSwitchStatu(APIView):
    authentication_classes = [Authtication,]
    
    def get(self,request,format=None):
        get_data = PortSwitch.objects.filter(user=self.request.user.id).first()
        return Response({'email':get_data.switch})
    def put(self,request,format=None):
        get_data = PortSwitch.objects.filter(user=self.request.user.id).first()
        if get_data.switch == True:
            get_data.switch = False
        else:
            get_data.switch = True
        get_data.save()
        return Response({'email':get_data.switch})

class FileSwitchStatu(APIView):
    authentication_classes = [Authtication,]
    
    def get(self,request,format=None):
        get_data = FileSwitch.objects.filter(user=self.request.user.id).first()
        return Response({'email':get_data.switch})
    def put(self,request,format=None):
        get_data = FileSwitch.objects.filter(user=self.request.user.id).first()
        if get_data.switch == True:
            get_data.switch = False
        else:
            get_data.switch = True
        get_data.save()
        return Response({'email':get_data.switch})

class SuccessIpSwitchStatu(APIView):
    authentication_classes = [Authtication,]
    
    def get(self,request,format=None):
        get_data = SuccessIpSwitch.objects.filter(user=self.request.user.id).first()
        return Response({'email':get_data.switch})
    def put(self,request,format=None):
        get_data = SuccessIpSwitch.objects.filter(user=self.request.user.id).first()
        if get_data.switch == True:
            get_data.switch = False
        else:
            get_data.switch = True
        get_data.save()
        return Response({'email':get_data.switch})

class FailIpSwitchStatu(APIView):
    authentication_classes = [Authtication,]
    
    def get(self,request,format=None):
        get_data = FailIpSwitch.objects.filter(user=self.request.user.id).first()
        return Response({'email':get_data.switch})

    def put(self,request,format=None):
        get_data = FailIpSwitch.objects.filter(user=self.request.user.id).first()
        if get_data.switch == True:
            get_data.switch = False
        else:
            get_data.switch = True
        get_data.save()
        return Response({'email':get_data.switch})

#
##
#
class IntrusionIpSwitchStatu(APIView):
    authentication_classes = [Authtication,]
    
    def get(self,request,format=None):
        get_data = IntrusionIpSwitch.objects.filter(user=self.request.user.id).first()
        return Response({'email':get_data.switch})

    def put(self,request,format=None):
        get_data = IntrusionIpSwitch.objects.filter(user=self.request.user.id).first()
        if get_data.switch == True:
            get_data.switch = False
        else:
            get_data.switch = True
        get_data.save()
        return Response({'email':get_data.switch})

class IntrusionFileSwitchStatu(APIView):
    authentication_classes = [Authtication,]
    
    def get(self,request,format=None):
        get_data = IntrusionFileSwitch.objects.filter(user=self.request.user.id).first()
        return Response({'email':get_data.switch})

    def put(self,request,format=None):
        get_data = IntrusionFileSwitch.objects.filter(user=self.request.user.id).first()
        if get_data.switch == True:
            get_data.switch = False
        else:
            get_data.switch = True
        get_data.save()
        return Response({'email':get_data.switch})

class IntrusionNewIpSwitchStatu(APIView):
    authentication_classes = [Authtication,]
    
    def get(self,request,format=None):
        get_data = IntrusionNewIpSwitch.objects.filter(user=self.request.user.id).first()
        return Response({'email':get_data.switch})

    def put(self,request,format=None):
        get_data = IntrusionNewIpSwitch.objects.filter(user=self.request.user.id).first()
        if get_data.switch == True:
            get_data.switch = False
        else:
            get_data.switch = True
        get_data.save()
        return Response({'email':get_data.switch})