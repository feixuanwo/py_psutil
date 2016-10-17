#!coding:utf-8

from IPy import IP
ip = IP('192.168.0.0/16')
print '输出192.168.0.0/16网段的ip个数:', ip.len()
#for x in ip:
#    print (x)

ip = IP('192.168.1.20')
print ip.reverseNames()
print ip.iptype()
print IP('8.8.8.8').iptype()
print IP('8.8.8.8').int()
print IP('8.8.8.8').strHex()
print IP('8.8.8.8').strBin()
print IP(0x8080808)

#根据IP与掩码生成网段
print (IP('192.168.1.0').make_net('255.255.255.0'))
print (IP('192.168.1.0/255.255.255.0' ,make_net = True))
print (IP('192.168.1.0-192.168.1.255' ,make_net = True))
#通过指定wantprefixlen参数值以定制不同的输出类型的网段
print IP('192.168.1.0/24').strNormal(0)
print IP('192.168.1.0/24').strNormal(1)
print IP('192.168.1.0/24').strNormal(2)
print IP('192.168.1.0/24').strNormal(3)

#ip对象的比较
print IP('10.0.0.0/24') < IP('12.0.0.0/24')
#判断ip地址和网段是否包含于另一个网段中
print '192.168.1.100' in IP('192.168.1.0/24')
print IP('192.168.1.0/24') in IP('192.168.0.0/16')
#判断两个网段是否存在重叠 #存在返回1，不存在返回0
print IP('192.168.0.0/23').overlaps('192.168.1.0/24')
print IP('192.168.0.0/24').overlaps('192.168.2.0')

#example:根据输入的ip或子网返回网络，掩码，广播，反向解析，子网数，ip类型等信息
from IPy import IP

ip_s = raw_input('Please input an IP or net-range:')
ips = IP(ip_s)
if len(ips) > 1:
    print ('net: %s' % ips.net())
    print ('netmask: %s' % ips.netmask())
    print ('broadcast: %s' % ips.broadcast())
    print ('reverse address: %s' % ips.reverseNames()[0])
    print ('subnet: %s' % len(ips))
else:
    print ('reverse address: %s' % ips.reverseNames()[0])

print ('hexadecimal: %s' % ips.strHex())
print ('binary ip: %s' % ips.strBin())
print ('iptype: %s' % ips.iptype())
