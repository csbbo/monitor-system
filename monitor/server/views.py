from datetime import datetime
import pytz

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status,exceptions

from .serializers import UserSerializer,BaseDataSerializer,TopCpuSerializer,TopMemSerializer,OpenPortSerializer,UserPortsSerializer,CheckFielsSerializer,SuccessIpSerializer,FaileIpSerializer
from .models import ServerToken,ServerToken,BaseData,TopCpu,TopMem,OpenPort,UserPorts,CheckFiels,SuccessIp,FaileIp
from .jwt import md5
from .email import *
from front.models import *

cpu_use_warning = 80
mem_use_warning = 90
process_use_cpu_warning = 10
ip_stay_time = 30
retain_number = 20

class Authtication(object):
    """
    token认证
    """
    def authenticate(self,request):
        token = request.META.get('HTTP_TOKEN')
        token_obj = ServerToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        # On rest framework within these two fields will be assigned to the request, 
        #   the user, the request.auth for later use
        return (token_obj.user,token_obj)    
    def authenticate_header(self,request):
        pass

@csrf_exempt
@api_view(['POST'])
def regist(request):
    ret = {'code':1000}
    serializer = UserSerializer(data=request.data)

    data = request.data.copy()

    if serializer.is_valid():
        if not email_regist(data.get('username'),data.get('email')):
            ret['code'] = 1001
            ret['msg'] = "请输入一个可达的邮箱!!!"
            return Response(ret)

        serializer.save()
        username = serializer.data.get('username')
        user_id = serializer.data.get('id')
        user = User.objects.get(pk=user_id)
        make_token = md5(username)
        token = ServerToken(token=make_token,user=user)
        token.save()
        ret['token'] = make_token
        ret['user'] = serializer.data

        # Initialize the mailbox control
        base = BaseInfoSwitch(user=user)
        base.save()
        base = CpuSwitch(user=user)
        base.save()
        base = MemSwitch(user=user)
        base.save()
        base = PortSwitch(user=user)
        base.save()
        base = FileSwitch(user=user)
        base.save()
        base = SuccessIpSwitch(user=user)
        base.save()
        base = FailIpSwitch(user=user)
        base.save()
        base = IntrusionIpSwitch(user=user)
        base.save()
        base = IntrusionFileSwitch(user=user)
        base.save()
        base = IntrusionNewIpSwitch(user=user)
        base.save()
        
        return Response(ret)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class BaseDatas(APIView):
    """
    基础信息类
    """
    authentication_classes = [Authtication,]
    def post(self,request,format=None):
        user_data = BaseData.objects.filter(user=self.request.user.id).first()
        data = request.data.copy()
        data['user'] = self.request.user.id
        # when cpu usage is greater than 80 percent serious warning
        if float(data['cpu_percent']) > cpu_use_warning:
            intrusion_cpu(cpu_use_warning,self.request.user)
        # when memory usage is greater than 80 percent serious warning
        if float(data['mem_percent']) > mem_use_warning:
            intrusion_mem(mem_use_warning,self.request.user)
        if user_data:
            serializer = BaseDataSerializer(user_data,data=data)
        else:
            serializer = BaseDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TopCpus(APIView):
    """
    消耗cpu最高的进程
    """
    authentication_classes = [Authtication,]
    def post(self,request,format=None):
        cpu_data = TopCpu.objects.filter(user=self.request.user.id)
        data = request.data.copy()
        data['user'] = self.request.user.id
        # when a process usage is greater than 30 percent serious warning
        if float(data.get('cpu_use')) > process_use_cpu_warning:
            intrucsion_process_cpu(process_use_cpu_warning,self.request.user)
        if len(cpu_data) > retain_number:
            cpu_data.first().delete()
        serializer = TopCpuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TopMems(APIView):
    """
    消耗内存最高的进程
    """
    authentication_classes = [Authtication,]
    def post(self,request,format=None):
        mem_data = TopMem.objects.filter(user=self.request.user.id)
        data = request.data.copy()
        data['user'] = self.request.user.id
        if len(mem_data) > retain_number:
            mem_data.first().delete()
        serializer = TopMemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class OpenPorts(APIView):
    """
    检测开放端口
    """
    authentication_classes = [Authtication,]
    def post(self,request,format=None):
        port_data = OpenPort.objects.filter(user=self.request.user.id,port=request.data.get('port')).first()
        data = request.data.copy()
        data['user'] = self.request.user.id
        if port_data:     
            serializer = OpenPortSerializer(port_data,data=data)
        else:
            port_list = UserPorts.objects.filter(user=self.request.user.id).first()
            if port_list:
                email_ports(data.get('port'),data.get('detail'),self.request.user) #remind
            serializer = OpenPortSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserPortList(APIView):
    """
    开放的端口列表
    """
    authentication_classes = [Authtication,]
    def post(self,request,format=None):
        port_data = UserPorts.objects.filter(user=self.request.user.id).first()
        data = request.data.copy()
        data['user'] = self.request.user.id
        if port_data:
            newp = data.get('port_list').split(',')
            oldp = port_data.port_list.split(',')  
            port_of = list(set(oldp)-set(newp)) 
            if port_of:
                for p in port_of:
                    port_del = OpenPort.objects.filter(user=self.request.user.id,port=p).first()
                    email_ports_del(p,self.request.user) #remind
                    port_del.delete()
            serializer = UserPortsSerializer(port_data,data=data)
        else:
            serializer = UserPortsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CheckFielsd(APIView):
    """
    sha256检查文件
    """
    authentication_classes = [Authtication,]
    def post(self,request,format=None):
        file_data = CheckFiels.objects.filter(user=self.request.user.id,filepath=request.data.get('filepath')).first()
        data = request.data.copy()
        data['user'] = self.request.user.id
        if data['filepath'] == '/home/chen/.bash_history':
            if data['sha256'] == 'None':
                intrucsion_file('/home/chen/.bash_history',self.request.user)
        elif data['filepath'] == '/var/log/wtmp':
            if data['sha256'] == 'None':
                intrucsion_file('/var/log/wtmp',self.request.user)
        else:
            if file_data:
                if request.data.get('sha256') != file_data.sha256:
                    email_files(file_data.filepath,self.request.user) #remind
                serializer = CheckFielsSerializer(file_data,data=data)
            else:
                serializer = CheckFielsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'code':1000})

class SuccessIps(APIView):
    """
    登录成功的ip
    """
    authentication_classes = [Authtication,]
    def post(self,request,format=None):
        ip_data = SuccessIp.objects.filter(user=self.request.user.id)
        data = request.data.copy()
        data['user'] = self.request.user.id
        # if an login ip is stay too long serious warning
        login_statu = data['login_statu']
        login_statu = login_statu.split(':')
        if len(login_statu) == 2:
            if int(login_statu[1]) > ip_stay_time:
                intrucsion_loginip(data.get('ip_addr'),ip_stay_time,self.request.user)
        
        if len(ip_data) > retain_number-1:
            # if a new ip is login serious warning
            new_ip = SuccessIp.objects.filter(user=self.request.user.id,ip_addr=data.get('ip_addr')).first()
            if not new_ip:
                intrucsion_newip(data.get('ip_addr'),self.request.user)   
            ipaddr = SuccessIp.objects.filter(user=self.request.user.id,
                ip_addr=request.data.get('ip_addr'),
                login_time=request.data.get('login_time')).first()
            if ipaddr:
                serializer = SuccessIpSerializer(ipaddr,data=data)
            else:
                email_successip(request.data.get('ip_addr'),self.request.user) #remind
                ip_data.first().delete()
                serializer = SuccessIpSerializer(data=data)
        else:
            serializer = SuccessIpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class FaileIps(APIView):
    """
    登录失败的ip
    """
    authentication_classes = [Authtication,]
    def post(self,request,format=None):
        ip_data = FaileIp.objects.filter(user=self.request.user.id)
        data = request.data.copy()
        data['user'] = self.request.user.id
        # deny this ip
        this_ip = FaileIp.objects.filter(user=self.request.user.id,ip_addr=data.get('ip_addr'))
        if len(this_ip) >= 3:
            # ip_was_deny(data['ip_addr'],self.request.user)
            return Response({'code':1004,'ip_addr':data.get('ip_addr')})

        if len(ip_data) > retain_number-1:   
            ipaddr = FaileIp.objects.filter(user=self.request.user.id,
                ip_addr=request.data.get('ip_addr'),
                login_time=request.data.get('login_time')).first()
            if ipaddr:
                serializer = FaileIpSerializer(ipaddr,data=data)
            else:
                email_failip(request.data.get('ip_addr'),self.request.user) #remind
                ip_data.first().delete()
                serializer = FaileIpSerializer(data=data)
        else:
            serializer = FaileIpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#
#email template test
#

from django.shortcuts import render
def email_template(request):
    return render(request,'intrusion_loginip.html')