 # -*- coding:utf-8 -*-
 """
 详细设计
def StopCheckin(teacherWechatID,CourseID):
	1) 打开teacherInfo.csv文件；
	2) 找到匹配WechatID和teacherWechatID的教师信息，获取到该教师的TeacherID；
	3) 从全局队列中删除该教师的课程信息
 """
import csv
#停止考勤
def StopCheckin(teacherWechatID,CourseID):
	#根据教师微信号，找到该教师的教工号
	with open('teacherInfo.csv') as csv_Teacher:
		reader = csv.DictReader(csv_Teacher)
		for row in reader:
			if row['WeChatID'] == teacherWechatID:
				TeacherID = row['TeacherID']
	csv_Teacher.close()
	#从全局队列中删除该教师的课程信息
	for teacherInfo in Teacher_Queue:
		flag = 0
		if  (teacherInfo[0] == TeacherID) and (teacherInfo[1]== CourseID):
			Teacher_Queue.pop(flag)
		flag = flag + 1
