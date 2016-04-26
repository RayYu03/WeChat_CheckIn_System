 # -*- coding:utf-8 -*-
 """
Author  :  RayYu
Time :  2016/04/19
详细设计
def StuCheckIn(_stuWechatID,inputStream)
	1. 记录当前时间
	2. checkinType为Auto
	3. 根据学生微信ID，找到该学生的班级ID，学号，以及样本地址
	4. 根据课程号，找到该课程的名字
	5. 判断当前队列中有无该课程号和教工号当前队列中有该课程号和教工号
	6. 考勤认定
	7. 增加考勤记录
	8. checkinResult一直不写入任何信息
 """
import csv,time
def StuCheckIn(_stuWechatID,inputStream):
	CurrentTime=time.strftime('%Y/%m/%d %H:%M:%S')
	IsSucc = ''
	checkinType = Auto
	proof_path = inputStream

	#根据学生微信ID，找到该学生的班级ID，学号，以及样本地址
	with open('studentInfo.csv') as csv_student:
		reader = csv.DictReader(csv_student)
		for row in reader:
			if row['WeChatID'] == _stuWechatID:
				ClassID = row['ClassID']
				StuID = row['StuID']
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
	#判断当前队列中有无该课程号和教工号当前队列中有该课程号和教工号，并且认真结果为True，IsSucc 为True
	if  check_current_queue(TeacherID, CourseID)==True and identity(inputStream,FeaturePath) ==True:
		IsSucc = True
	#获取文件名	
	File= (TeacherID + '_' + CourseID + '_' + seqID + '_' + 'checkinDetail.csv')
	#增加考勤记录
	with open(File, 'a') as csvfile:
		writer = csv.writer(csvfile)
   		writer.writerow([StuID, CurrentTime, proof_path,checkinType,IsSucc,''])
   	csvfile.close()

#考勤认定模块
def  identity(inputStream,FeaturePath):
	pass
#判断当前队列中有无该课程号和教工号
def check_current_queue(TeacherID, CourseID):
	for teacherInfo in Teacher_Queue:
		if  (teacherInfo[0] == TeacherID) and (teacherInfo[1]== CourseID):
		return True

