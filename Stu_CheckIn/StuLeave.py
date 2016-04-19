 # -*- coding:utf-8 -*-
 """
 详细设计
StuLeave(_stuWechatID,inputStream)
{
	1.系统登记请假学生的信息IsSucc部分为为空
	2.checkinResult写为 “请假”
	3.checkinType登记为Auto
	4.证据路径填写假条的保存路径
	5.时间为当前时间
}
 """
import csv,time
def StuCheckIn(_stuWechatID,inputStream):
	CurrentTime=time.strftime('%Y/%m/%d %H:%M:%S')
	IsSucc = ''
	leave = '请假'
	checkinType=Auto
	proof_path = inputStream
	
	with open('studentInfo.csv') as csv_student:
		reader = csv.DictReader(csv_student)
		for row in reader:
			if row['WeChatID'] == _stuWechatID:
				ClassID = row['ClassID']
				FeaturePath = row['FeaturePath']
	csv_student.close()
	
	File= (TeacherID + '_' + CourseID + '_' + seqID + '_' + 'checkinDetail.csv')
	with open(File, 'a') as csvfile:
		writer = csv.writer(csvfile)
   		writer.writerow(['StuID', 'checkinTime', 'ProofPath','checkinType','IsSucc','checkinResult')
   	csvfile.close()