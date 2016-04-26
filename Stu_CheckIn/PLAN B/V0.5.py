# -*- coding: UTF-8 -*-
#版本时间2016/4/19   未封装

import csv
import time

CLASS_QUEUE=[]   #全局队列
CLASS_TIME=100*60 #全局时间

class BaseClass:
     #用于获取教师ID
    def get_TeacherID(self,TeacherWechat):
        csvfile = open('data/teacherInfo.csv', 'rb')
        reader = csv.reader(csvfile)
        reader.next() #忽略第一行

        for line in reader:
            if line[2]==TeacherWechat:  #判断微信是否存在
                csvfile.close()
                return line[0]

        csvfile.close()
        return 'None'    #不存在返回

    #检查教师数据是否匹配
    def check_Data(self,TeacherID,CourseID):
        csvfile = open('data/courseInfo.csv', 'rb')
        reader = csv.reader(csvfile)
        reader.next() #忽略第一行

        for line in reader:
            if (line[2]==TeacherID) and line[0]==CourseID:
                csvfile.close()
                return True

        csvfile.close()
        return False


class StartCheckin(BaseClass):

    #超时清队
    def time_out_pop(self):
        now=time.time()
        for x in CLASS_QUEUE:
            if now>=x[3]+CLASS_TIME:
                del x

    #坚持班级数据发生重叠
    def check_class_data(self,x,Node):
        for i in x:
            for j in Node:
                if i==j: return True;
        return False

    #返回当天的秒数
    def return_second(self,h,m):
        return 3600*h+m*60

    #数据入队
    def data_push(self,TeacherID,CourseID):
        self.time_out_pop() #清除超时队列
        Node=[]  #元素
        csvfile = open('data/courseInfo.csv', 'rb')
        reader = csv.reader(csvfile)
        reader.next() #忽略第一行

        classInfo=[] #班级元素

        for line in reader:
            if (line[2]==TeacherID) and line[0]==CourseID:
                classInfo.append(line[3])

        Node.append(TeacherID)
        Node.append(CourseID)
        Node.append(classInfo)

        #前一个时间窗口发生交叉处理
        for x in CLASS_QUEUE:
           if time.time()-x[3]<CLASS_TIME:   #误操作不进行处理
               if time.time()%365>self.return_second(8,25) and time.time()%365<self.return_second(10,05):
                   if x[3]%365>self.return_second(8,25) and x[3]%365<self.return_second(10,05):
                        continue
               elif time.time()%365>self.return_second(10,25) and time.time()%365<self.return_second(12,05):
                   if x[3]%365>self.return_second(10,25) and x[3]%365<self.return_second(12,05):
                        continue
               elif time.time()%365>self.return_second(14,30) and time.time()%365<self.return_second(16,05):
                   if x[3]%365>self.return_second(14,30) and x[3]%365<self.return_second(16,05):
                        continue
               elif time.time()%365>self.return_second(16,25) and time.time()%365<self.return_second(18,05):
                   if x[3]%365>self.return_second(16,25) and x[3]%365<self.return_second(18,05):
                        continue
               #查重
               if self.check_class_data(x[2],Node[2]): del x



        Node.append(time.time())
        CLASS_QUEUE.append(Node)  #数据插入队列

        csvfile.close()


    def start_checkin(self,TeacherID,CourseID):
        csvfile = open('data/seq.csv', 'r+')
        reader = csv.reader(csvfile)

        count=0
        for line in reader:
            if (line[0]==TeacherID) and (line[0]==TeacherID):
                count=int(line[3]) #考勤seq次数以最后一次为准

        self.data_push(TeacherID,CourseID); #进队列

        count+=1
        data=[TeacherID,CourseID,str(count),time.asctime()]
        writer = csv.writer(csvfile)
        writer.writerows(data)
        csvfile.close()


class StopCheckin(BaseClass):
    def stop_checkin(self,TeacherID,CourseID):
        for x in CLASS_QUEUE:
            if TeacherID==x[0] and CourseID==x[1]:
                del x


