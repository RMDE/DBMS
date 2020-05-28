## 学生信息管理系统

#### 数据结构
student: id,name,sex,class,profession,college,room,phone,birthday,password

class: id,college,teacher,monitor

teacher: id,name,sex,email,phone,college,birthday,salary,password

course: id,name,type,credit(学分),teacher,schedule,exam-type,exam-date,exam-room

college: id,name,dean(院长),[专业]

choose: student,class,time,score

worker: id,name,sex,phone,birthday,salary,password

department: id,area(区域),manager,capacity(容纳人数)

room: id,department,people,charge(可用电费)

book: id,name,type,author,year,sum,avaible

borrow: book(book-id),person,time,deadline [还书提醒(弹窗)]

manager: id,name,sex,email,phone,birthday,password

#### 功能
1. student:
- show information: id,name,sex,(profession,college,class,room)(不可改),phone,birthday
- show courses: course-id,course-name,type,credit,schedule,[图形化课表(冲突显示)]
- show exam: 显示未有成绩课程的考试
	     course_id,course_name,exam_type(考试，考核),exam_date,exam_room
- show grade: course-name,credit,type,grade
	      绩点 -- 必修平均绩点，所有平均绩点，grade*credit/sum(credit)，显示在顶部
- choose courses: 搜索框 -- course-id,course-name,teacher,college
		  显示课程 -- course_id,course_name,teacher,type,credit,college,schedule,exam_type
		  选课按钮 -- 弹框确定 -- 更新数据库
- charge: 电费 -- 显示的是剩余可用电量，数据库存的是剩余水电费，可充值，1.5元/度，充值后可用电量刷新
- search teacher: 搜索框 -- teacher-name
		  teacher_name,teacher_email,teacher_phone,college,[course]
				可能进一步实现phone或email的copy功能
- borrow book: 搜索框 -- book-name,type
	       book_name,type,year,avaible/sum
	       借阅按键，弹窗确定，并更新数据库
	       如果有欠费，则按借阅后弹出提示无法借书，需先缴费，缴费按钮，取消按钮。
	       缴费 -- book_name,time,deadline,fee
	       确认缴费弹框，缴费后更新欠费区

2. teacher:
- show information: id,name,email,phone,college(不可改),birthday,salary(不可改)
- search course: 搜索框 -- course-id,course-name,teacher,college
	         显示课程 -- course_id,course_name,teacher,type,credit,college,schedule,exam_type
- show self course: course-id,course-name,type,credit,schedule,exam-type
		    点击课程弹出下拉框：查看学生名单、录入成绩、安排考试(安排考试只能选择至少7天后)
		    查看学生名单 -- stu_id,stu_name,stu_class,profession,college,grade(拉条)
		    录入成绩 -- stu_id,stu_name,grade
		    安排考试 -- 下拉框：选择时间，选择地点（直接输入），确定键
		                日历表，可点击，在左侧；右侧时间，7：50~9：50，10：15~12：15，13：50~15：50，16：15~18：15，19：00~21：00
- borrow book: 搜索框 -- book-name,type
	       book_name,type,year,avaible/sum
	       借阅按键，弹窗确定，并更新数据库
	       如果有欠费，则按借阅后弹出提示无法借书，需先缴费，缴费按钮，取消按钮。
	       缴费 -- book_name,time,deadline,fee   老师的借阅期长于学生
	       确认缴费弹框，缴费后更新欠费区

3. worker
- show information: id,name,phone,birthday,salary(不可改)
- show self department: id,area,capacity
			点击宿舍楼下拉框：查看住宿学生名单、录入电费
			查看学生名单 -- stu_id,stu_name,class,profession,college,room
			录入电费 -- room用电量 -- 更新room.charge=charge-1.5*用电量
			最右下角确认键
- search department: 搜索框：id,area,manager
		     department_id,area,manager,capacity

4. manager
- show information: id,name,email,phone,birthday
- search studrnt: 搜索框 -- id,name,profession,college
		  id,name,sex,(college,class,room)(可改),phone  右方删除键，弹出确认框
		  右下方确认修改键
- search teacher: 搜索框 -- id,name,college
		  id,name,email,phone,college(可改),salary(可改)  右方删除键，弹出确认框
		  右下方确认修改键
- search worker: 搜索框 -- id,name
	         id,name,phone,salary(可改)  右方删除键，弹出确认框
