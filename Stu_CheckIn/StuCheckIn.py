 # -*- coding:utf-8 -*-
 """
 详细设计
def StuCheckIn(_stuWechatID,inputStream)
	1. 系统登记考勤认定成功的信息IsSucc部分为True
	2. 未认定成功的学生系统将其保持在一个临时的变量中，直至考勤时间窗口关闭时再写入checkDetail 的数据行
	3. checkinResult一直不写入任何信息
	4. checkinType登记为Auto
	5. 一直未响应考勤系统的学生在考勤窗口关闭之后，将在checkDetail 的数据行增加一条考勤记录
	6. checkinResult 一直不写入任何信息
	7. checkinType登记为Auto
 """
import csv,time
def StuCheckIn(_stuWechatID,inputStream):
	IsSucc = False
	checkinType = Auto
	with open('studentInfo.csv') as csv_student:
		reader = csv.DictReader(csv_student)
		for row in reader:
			if row['WeChatID'] == _stuWechatID:
				ClassID = row['ClassID']
				FeaturePath = row['FeaturePath']
	csv_student.close()
	#根据课程号，找到该课程的名字
	with open('courseInfo.csv') as csv_course:#
		reader = csv.DictReader(csv_course)
		for row in reader:
			if row['CourseName'] == ClassID:
				class_name.append(row['ClassName'])
				CourseID = row['CourseID']
				TeacherID = row['TeacherID']
	csv_course.close()

	if  check_current_queue(TeacherID, CourseID)==True identity(inputStream,FeaturePath) ==True:
		IsSucc = True


def  identity(inputStream,FeaturePath):
	pass

def check_current_queue(TeacherID, CourseID):
	for teacherInfo in Teacher_Queue:
		if  (teacherInfo[0] == TeacherID) and (teacherInfo[1]== CourseID):
		return True

