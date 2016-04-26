 # -*- coding:utf-8 -*-
 """
Author  :  RayYu
Time :  2016/04/19
详细设计
def StopCheckin(teacherWechatID,CourseID):
	1. 打开teacherInfo.csv文件；
	2. 根据教师微信号，获取该教师的TeacherID；
	3. 打开courseInfo.csv文件；
	4. 根据课程号，获取参加该课程的班级名字；
	5. 打开studentInfo.csv文件；
	6. 根据班名，获取参加该班的学生ID；
	7. 打开该课程的checkinDetail.csv
	8. 对考勤的学生进行考勤认定，未参与考勤的学生，系统将在checkDetail的数据行增加一条缺勤记录
	9. 从全局队列中删除该教师的课程信息
 """
import csv
#停止考勤
def StopCheckin(teacherWechatID,CourseID):
	stuID_List = []
	ClassID_List = []
	#根据教师微信号，找到该教师的教工号
	with open('teacherInfo.csv') as csv_Teacher:
		reader = csv.DictReader(csv_Teacher)
		for row in reader:
			if row['WeChatID'] == teacherWechatID:
				TeacherID = row['TeacherID']
	csv_Teacher.close()
	# 根据课程号，获取参加该课程的班级；
	with open('courseInfo.csv') as csv_course:
		reader = csv.DictReader(csv_course)
		for row in reader:
			if row['CourseID'] == CourseID:
				ClassID_List.append(row['ClassName') 
	csv_course.close()
	#根据班名，获取参加该班的学生ID；
	with open('studentInfo.csv') as csv_stu:
		reader = csv.DictReader(csv_stu)
			for row in reader:
				for class_ID in ClassID_List:
					if row['ClassID'] = class_ID:
						stuID_List.append(row['stuID'])
	csv_stu.close()

	#获取文件名
	File= (TeacherID + '_' + CourseID + '_' + seqID + '_' + 'checkinDetail.csv')

	#对考勤的学生进行考勤认定，未参与考勤的学生，系统将在checkDetail的数据行增加一条缺勤记录
	with open(File,'a') as csvfile:
		reader = csv.reader(csvfile)
		reader.next()
		writer = csv.writer(ccsvfile)
		for row in reader:
			flag = False
			for class_ID in ClassID_List:
				if class_ID == row[0]:
					flag = True
					break
			if flag == True:
				if row[4] == True:
					checkinResult = '出勤'
					row[5] = checkinResult
				else:
					checkinResult = '缺勤'
					row[4] = False
					row[5] = checkinResult
			else:
				CurrentTime=time.strftime('%Y/%m/%d %H:%M:%S')
				writer.writerow([StuID, CurrentTime,'','Auto','False','缺勤'])
   		csvfile.close()
	
	#从全局队列中删除该教师的课程信息
	for teacherInfo in Teacher_Queue:
		flag = 0
		if  (teacherInfo[0] == TeacherID) and (teacherInfo[1]== CourseID):
			Teacher_Queue.pop(flag)
		flag = flag + 1
