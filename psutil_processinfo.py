#!coding:utf-8

import psutil

print '列出所有进程ID:'
print psutil.pids()

print '实例化一个进程对象:' #tail一个文件，用这个进程进行测试
p = psutil.Process(3110)

print '进程名称:', p.name()
print '进程bin路径:', p.exe()
#print '进程工作绝对路径:', p.cwd()
print '进程状态:', p.status()
print '进程创建时间:', p.create_time()
print '进程uid信息:', p.uids()
print '进程pid信息:', p.gids()
print '进程CPU时间信息:', p.cpu_times()
print 'get进程CPU亲和度:', p.cpu_affinity()
print '进程内存利用率:', p.memory_percent()
print '进程内存rss, vms信息:', p.memory_info()
print '进程IO信息:', p.io_counters()
print '返回打开socket的namedutples列表:', p.connections()
print '返回进程打开的线程数:', p.num_threads()


##Popen类的使用,用Popen运行的应用程序，可以跟踪程序的信息
import psutil
from subprocess import PIPE
p = psutil.Popen(["/usr/bin/python", "-c", "print ('hello')"], stdout = PIPE)
print p.cpu_times() #进程可能已经结束
print p.name()
print p.username()
print p.communicate()


