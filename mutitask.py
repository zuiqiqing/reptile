#coding=utf-8
from threading import Thread
from Queue import Queue
from time import sleep
#q是任务队列
#NUM是并发线程总数
#JOBS是有多少任务
q = Queue()
NUM = 2
JOBS = 10
#具体的处理函数，负责处理单个任务
def do_somthing_using(arguments,tup):
    print str(arguments)+tup
#这个是工作进程，负责不断从队列取数据并处理
def working(tup):
    while True:
        arguments = q.get()
        do_somthing_using(arguments, tup)
        sleep(1)
        q.task_done()
#fork NUM个线程等待队列
for i in range(NUM):
    t = Thread(target=working, args=("name"+str(i),))
    t.setDaemon(True)
    t.start()
#把JOBS排入队列
for i in range(JOBS):
    sleep(3)
    q.put(i)
#等待所有JOBS完成
q.join()
