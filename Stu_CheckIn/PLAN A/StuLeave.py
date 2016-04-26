 # -*- coding:utf-8 -*-
 """
Author :  RayYu
Time :  2016/04/19
 
详细设计
StuLeave(_stuWechatID,inputStream)
{
	1. 记录当前时间
	2. 根据学生微信ID，找到该学生的班级ID，学号，以及样本地址
	3. 根据班级ID，找到该课程的教工号,课程号
	4. 根据教师ID，获取seqID
	5. 获取文件名
	6. 增加考勤记
	7. checkinType登记为Auto
	8. checkinResult写为 “请假
	9. 证据路径填写假条的保存路径
}
 """
import csv,time
def StuCheckIn(_stuWechatID,inputStream):
	#记录当前时间
	CurrentTime=time.strftime('%Y/%m/%d %H:%M:%S')
	IsSucc = ''
	leave = '请假'
	checkinType=Auto
	proof_path = inputStream
	
	#根据学生微信ID，找到该学生的班级ID，学号，以及样本地址
	with open('studentInfo.csv') as csv_student:
		reader = csv.DictReader(csv_student)
		for row in reader:
			if row['WeChatID'] == _stuWechatID:
				ClassID = row['ClassID']
				StuID= row['StuID']
				FeaturePath = row['FeaturePath']
	csv_student.close()

	#根据班级ID，找到该课程的教工号,课程号
	with open('courseInfo.csv') as csv_course:#
		#记录教工号
		class_name=[]
		reader = csv.DictReader(csv_course)
		for row in reader:
			if row['ClassID'] ==ClassID:
				TeacherID = row['TeacherID']
				CourseID = row['CourseID']
	csv_course.close()
	#根据教师ID，获取seqID
	with open('seq.csv') as csv_Seq:
		reader = csv.DictReader(csv_student)
		for row in reader:
			if row['TeacherID'] = TeacherID:
				seqID = row['seqID']
	csv_Seq.close()
	#获取文件名
	File= (TeacherID + '_' + CourseID + '_' + seqID + '_' + 'checkinDetail.csv')
	#增加考勤记录,checkinType登记为Auto,checkinResult写为 “请假”,证据路径填写假条的保存路径
	with open(File, 'a') as csvfile:
		writer = csv.writer(csvfile)
   		writer.writerow([StuID, CurrentTime, proof_path,checkinType,IsSucc,leave])
   	csvfile.close()