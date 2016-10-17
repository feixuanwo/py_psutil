#!coding:utf-8
import psutil

mem = psutil.virtual_memory()
print mem.total, mem.used

#cpu信息
print psutil.cpu_times()
print psutil.cpu_times().user
print psutil.cpu_count()
print psutil.cpu_count(logical=False)

#内存信息
mem = psutil.virtual_memory()
print mem.total
print mem.free
print psutil.swap_memory()

#disk信息
print '获取磁盘完整信息:'
print psutil.disk_partitions()  #

print '获取分区(参数)的使用情况:'
print psutil.disk_usage('/')

print '获取硬盘总的的IO个数，读写信息:'
print psutil.disk_io_counters()

print '获取单个分区的IO个数，读写信息:'
print psutil.disk_io_counters(perdisk = True)

#网络信息
print '获取网络总的IO信息,默认pernic=False'
print psutil.net_io_counters()

print 'pernic=True输出每个网络接口的IO信息'
print psutil.net_io_counters(pernic = True)

#其他系统信息
print '当前登录的用户信息:'
print psutil.users()

print '获取开机时间:'
print psutil.boot_time()
print '将开机时间转换为自然时间格式:'
import datetime
print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
