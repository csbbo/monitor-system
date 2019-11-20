from django.contrib.auth.models import User
from rest_framework import serializers

from .models import ServerToken,BaseData,TopCpu,TopMem,OpenPort,UserPorts,CheckFiels,SuccessIp,FaileIp


class UserSerializer(serializers.ModelSerializer):
    """
    用户序列化
    """
    password = serializers.CharField(
        # write_only=True,
        style={'input_type': 'password'}
    )
    class Meta:
        model = User
        fields = ('id','username','email','password')


class BaseDataSerializer(serializers.ModelSerializer):
    """
    基本数据序列化
    """
    # user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = BaseData
        fields = '__all__'

class TopCpuSerializer(serializers.ModelSerializer):
    """
    TopCpu序列化
    """
    class Meta:
        model = TopCpu
        fields = '__all__'

class TopMemSerializer(serializers.ModelSerializer):
    """
    TopMem序列化
    """
    class Meta:
        model = TopMem
        fields = '__all__'

class CheckFielsSerializer(serializers.ModelSerializer):
    """
    CheckFiels序列化
    """
    class Meta:
        model = CheckFiels
        fields = '__all__'

class OpenPortSerializer(serializers.ModelSerializer):
    """
    OpenPort序列化
    """
    class Meta:
        model = OpenPort
        fields = '__all__'

class UserPortsSerializer(serializers.ModelSerializer):
    """
    UserPorts序列化
    """
    class Meta:
        model = UserPorts
        fields = '__all__'

class SuccessIpSerializer(serializers.ModelSerializer):
    """
    成功登陆ip序列化
    """
    class Meta:
        model = SuccessIp
        fields = '__all__'

class FaileIpSerializer(serializers.ModelSerializer):
    """
    成功失败ip序列化
    """
    class Meta:
        model = FaileIp
        fields = '__all__'