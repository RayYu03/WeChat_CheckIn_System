 # -*- coding:utf-8 -*-
 """
 详细设计
def StartCheckin(teacherWechatID,CourseID):
	1) 记录考勤开始时间，更新Timer；
	2) 设置一个列表记录当前教师课程队列；
	3) 打开teacherInfo.csv文件；
	4) 找到匹配WechatID和teacherWechatID的教师信息，获取到该教师的TeacherID；
	5) 打开courseInfo.csv文件；
	6) 根据课程号，找到该课程的名字
	7) 打开seq.csv文件；
	8) 初始化一个seqID = 1；
	9) 找到该CourseID对应的最新的SeqID,更新seqID；
	10) 将获取到的TeacherID，CourseID，更新过的seqID，考勤开始时间StartTime依次追加到文件seq.csv中；
	11) 将当前教师课程队列存到全局教师课程队列中
	12) 检查Timer，超出上课时间区间的课程清除出队列
	13) 生成<工号>_<课程号>_<考勤序号>_checkinDetail.csv
 
 """
import csv,time

#开始考勤
def StartCheckin(teacherWechatID,CourseID):
	#记录考勤开始时间
	StartTime=time.strftime('%Y/%m/%d %H:%M:%S')
	timeArray = time.strptime(StartTime, '%Y/%m/%d %H:%M:%S')
	timeStamp = time.mktime(timeArray)

	Timer = time.time()+5700
	#设置一个列表记录当前教师课程队列
	TeacInfo = []
	TeacInfo[1] = CourseID
	TeacInfo[3] =  StartTime

	#根据教师微信号，找到该教师的教工号
	with open('teacherInfo.csv') as csv_Teacher:
		reader = csv.DictReader(csv_Teacher)
		for row in reader:
			if row['WeChatID'] == teacherWechatID:
				TeacherID = row['TeacherID']
				TeacInfo[0] = TeacherID
	csv_Teacher.close()			
	#根据课程号，找到该课程的名字
	with open('courseInfo.csv') as csv_course:#
		#记录课程名字
		class_name=[]
		reader = csv.DictReader(csv_course)
		for row in reader:
			if row['CourseID'] ==CourseID:
				class_name.append(row['ClassName'])
			TeacInfo[2] = class_name
	csv_course.close()
	#在Seq.csv中增加一行TeacherID,CourseID,SeqID,StartTime
	with open('seq.csv','a') as csv_Seq:
		writer = csv.writer(csv_Seq)
		reader = csv.reader(csv_Seq)
		seqID = 1
		for row in reader:
			if row1['TeacherID'] = row[0]:
				seqID = row[2]
		writer.writerow([TeacherID,CourseID,seqID,StartTime])	
	csv_Seq.close()
	#将当前教师课程队列存到全局教师课程队列中
	Teacher_Queue.append(TeacInfo)

	#超出上课时间区间的课程清除出队列
	def  check_Timer():
		for teacherInfo in Teacher_Queue:
			flag = 0
			if  teacherInfo[3] < timeStamp:
				Teacher_Queue.pop(flag)
			flag = flag + 1
				
	#生成<工号>_<课程号>_<考勤序号>_checkinDetail.csv
	File= (TeacherID + '_' + CourseID + '_' + seqID + '_' + 'checkinDetail.csv')
	with open(File, 'wb') as csvfile:
		writer = csv.writer(csvfile)
   		writer.writerow(['StuID', 'checkinTime', 'ProofPath','checkinType','IsSucc','checkinResult')
   	csvfile.close()