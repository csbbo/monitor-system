from django.conf import settings
import yagmail
from django.template.loader import render_to_string

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

from front.models import *

from_addr = settings.EMAIL_USER
password = settings.EMAIL_PASSWORD
smtp_server = settings.SMTP_SERVER

# format for the sender and subject
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# send email template
def sendemail(recipient,html_template,context,subject):
    to_addr = recipient
    html = render_to_string(html_template,context=context)
    msg = MIMEText(html, 'html', 'utf-8')
    msg['From'] = _format_addr('服务器入侵检测警报系统 <%s>' % from_addr)
    msg['To'] = _format_addr('道友你好 <%s>' % to_addr)
    msg['Subject'] = Header(subject, 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 587) # The default port for the SMTP protocol is 25
    server.starttls()
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
#
# send regist email
#
def email_regist(username,recipient):
    context = {'username':username}
    html_template = 'email_regist.html'
    subject = '欢迎注册服务器入侵检测警报系统'
    try:
        sendemail(recipient,html_template,context,subject)
        return True
    except Exception as e:
        print(e)

#
## remind email
#

# send the email for the port increase
def email_ports(port,detail,recipient):
    port_switch = PortSwitch.objects.filter(user=recipient).first()
    if port_switch.switch == True:
        context = {'port':port,'detail':detail}
        html_template = 'email_port_add.html'
        subject = '服务器端口打开'
        sendemail(recipient.email,html_template,context,subject)

# send the email for the port reduce
def email_ports_del(port,recipient):
    port_switch = PortSwitch.objects.filter(user=recipient).first()
    if port_switch.switch == True:
        context = {'port':port}
        html_template = 'email_port_off.html'
        subject = '服务器端口关闭'
        sendemail(recipient.email,html_template,context,subject)

# send the email for the important file change
def email_files(file_path,recipient):
    file_switch = FileSwitch.objects.filter(user=recipient).first()
    if file_switch.switch == True:
        context = {'filename':file_path}
        html_template = 'email_file_change.html'
        subject = '服务器重要文件异动'
        sendemail(recipient.email,html_template,context,subject)


# send the email for user loggin
def email_successip(loginip,recipient):
    successip_switch = SuccessIpSwitch.objects.filter(user=recipient).first()
    if successip_switch.switch == True:
        context = {'loginip':loginip}
        html_template = 'email_login_sucess.html'
        subject = '用户登录'
        sendemail(recipient.email,html_template,context,subject)

# send the email for user loggin fail
def email_failip(loginip,recipient):
    failip_switch = FailIpSwitch.objects.filter(user=recipient).first()
    if failip_switch.switch == True:
        context = {'loginip':loginip}
        html_template = 'email_login_fail.html'
        subject = '发现失败登录'
        sendemail(recipient.email,html_template,context,subject)

#
# new ip login
#
def intrucsion_newip(ip_addr,recipient):
    intrusion_switch = IntrusionNewIpSwitch.objects.filter(user=recipient).first()
    if intrusion_switch.switch == True:
        context = {'ip_addr':ip_addr}
        html_template = 'intrusion_newip.html'
        subject = '异地登录'
        sendemail(recipient.email,html_template,context,subject)
#
# Below are email warnings judged as intrusions
#

def intrusion_cpu(cpu_use_warning,recipient):
    intrusion_switch = BaseInfoSwitch.objects.filter(user=recipient).first()
    if intrusion_switch.switch == True:
        context = {'cpu_use_warning':cpu_use_warning}
        html_template = 'intrusion_cpu.html'
        subject = '我们发现您的服务器被入侵了!!!'
        sendemail(recipient.email,html_template,context,subject)
        intrusion_switch.switch = False
        intrusion_switch.save()

def intrusion_mem(mem_use_warning,recipient):
    intrusion_switch = BaseInfoSwitch.objects.filter(user=recipient).first()
    if intrusion_switch.switch == True:
        context = {'mem_use_warning':mem_use_warning}
        html_template = 'intrusion_mem.html'
        subject = '我们发现您的服务器被入侵了!!!'
        sendemail(recipient.email,html_template,context,subject)
        intrusion_switch.switch = False
        intrusion_switch.save()

def intrucsion_process_cpu(process_use_cpu_warning,recipient):
    intrusion_switch = CpuSwitch.objects.filter(user=recipient).first()
    if intrusion_switch.switch == True:
        context = {'process_use_cpu_warning':process_use_cpu_warning}
        html_template = 'intrusion_process_cpu.html'
        subject = '我们发现您的服务器被入侵了!!!'
        sendemail(recipient.email,html_template,context,subject)
        intrusion_switch.switch = False
        intrusion_switch.save()

def intrucsion_file(file_path,recipient):
    intrusion_switch = IntrusionFileSwitch.objects.filter(user=recipient).first()
    if intrusion_switch.switch == True:
        context = {'file_path':file_path}
        html_template = 'intrusion_file.html'
        subject = '我们发现您的服务器被入侵了!!!'
        sendemail(recipient.email,html_template,context,subject)
        intrusion_switch.switch = False
        intrusion_switch.save()

def intrucsion_loginip(ip_addr,ip_stay_time,recipient):
    intrusion_switch = IntrusionIpSwitch.objects.filter(user=recipient).first()
    if intrusion_switch.switch == True:
        context = {'ip_addr':ip_addr,'ip_stay_time':ip_stay_time}
        html_template = 'intrusion_loginip.html'
        subject = '我们发现您的服务器被入侵了!!!'
        sendemail(recipient.email,html_template,context,subject)
        intrusion_switch.switch = False
        intrusion_switch.save()

# def ip_was_deny(ip_addr,recipient):
#     context = {'ip_addr':ip_addr,'ip_stay_time':ip_stay_time}
#     html_template = 'intrusion_loginip.html'
#     subject = '服务器入侵检测警报系统启动了自动防御!!!'
#     sendemail(recipient.email,html_template,context,subject)