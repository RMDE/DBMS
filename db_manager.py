'''
author : RMDE
function : connect the mysql
'''


import mysql.connector
import re

college = ["航空宇航学院","能源与动力学院","自动化学院","电子信息工程学院","机电学院","材料科学与技术学院","民航学院","理学院","经济管理学院","人文与社会科学学院","艺术学院","外国语学院","马克思主义学院","航天学院","国际教育学院","计算机科学与技术学院"]
schedule =["Mon-8:00~9:45","Mon-10:15~12:00","Mon-14:00~15:45","Mon-16:15~18:00","Tue-8:00~9:45","Tue-10:15~12:00","Tue-14:00~15:45","Tue-16:15~18:00","Wed-8:00~9:45","Wed-10:15~12:00","Wed-14:00~15:45","Wed-16:15~18:00","Thu-8:00~9:45","Thu-10:15~12:00","Thu-14:00~15:45","Thu-16:15~18:00","Fri-8:00~9:45","Fri-10:15~12:00","Fri-14:00~15:45","Fri-16:15~18:00"]

class mydb(object):

    # 连接本地数据库并进行初始化
    def __init__(self,host,user,passwd):
        '数据库接口类'
        config={'host':host,
                'user':user,
                'passwd':passwd,
                'port':3306,
                'charset':'utf8',
                'auth_plugin':'mysql_native_password'} # 设置加密规则一致
        try:
            self.database = mysql.connector.connect(**config)
        except mysql.connector.Error as e:
            print("connect fails!{}".format(e))
        self.cursor = self.database.cursor() # 当前游标
        
        #建立数据库info
        self.cursor.execute("drop database if EXISTS info")
        self.cursor.execute("create database info")
        self.cursor.execute("use info")
        #self.cursor.execute("drop table if exists student")
        college = '''create table college(
                        id varchar(20) primary key,
                        name varchar(20) not null,
                        dean varchar(20),
                        profession varchar(50) not null)'''
        teacher = '''create table teacher(
                        id varchar(20) primary key,
                        name varchar(20) not null,
                        sex ENUM("male","female"),
                        email varchar(20),
                        phone varchar(20),
                        college varchar(20),
                        birthday date,
                        salary dec(8,2),
                        password varchar(30) not null,
                        foreign key(college) references college(id) on update cascade)'''
        colge_ch = '''alter table college add constraint f1 
                        foreign key(dean) references teacher(id)'''
        classes =  '''create table class(
                        id varchar(20) primary key,
                        college varchar(20) not null,
                        teacher varchar(20),
                        monitor varchar(20),
                        foreign key(college) references college(id) on update cascade on delete cascade,
                        foreign key(teacher) references teacher(id) on update cascade)'''
        course = '''create table course(
                        id varchar(20) primary key,
                        name varchar(20) not null,
                        type enum("必修","专业选修","文化素质","实践拓展","其他") not null,
                        credit dec(2,1) not null,
                        teacher varchar(20) not null,
                        schedule set("Mon-8:00~9:45","Mon-10:15~12:00","Mon-14:00~15:45","Mon-16:15~18:00",
                                     "Tue-8:00~9:45","Tue-10:15~12:00","Tue-14:00~15:45","Tue-16:15~18:00",
                                     "Wed-8:00~9:45","Wed-10:15~12:00","Wed-14:00~15:45","Wed-16:15~18:00",
                                     "Thu-8:00~9:45","Thu-10:15~12:00","Thu-14:00~15:45","Thu-16:15~18:00",
                                     "Fri-8:00~9:45","Fri-10:15~12:00","Fri-14:00~15:45","Fri-16:15~18:00"),
                        exam_type enum("考试","考查"),
                        exam_date datetime,
                        exam_room varchar(20),
                        foreign key(teacher) references teacher(id) on update cascade)'''
        choose = '''create table choose(
                        student varchar(20),
                        course varchar(20),
                        time datetime not null,
                        score int,
                        foreign key(student) references student(id) on delete cascade on update cascade,
                        foreign key(course) references course(id) on delete cascade,
                        primary key(student,course))'''
        worker = '''create table worker(
                        id varchar(20) primary key,
                        name varchar(20) not null,
                        sex ENUM("male","female"),
                        phone varchar(20),
                        birthday date,
                        salary dec(8,2),
                        password varchar(30) not null)'''
        department = '''create table department(
                        id varchar(20) primary key,
                        area enum("东区","西区","南区","北区") not null,
                        manager varchar(20),
                        capacity int not null,
                        foreign key(manager) references worker(id))'''
        room = '''create table room(
                        id varchar(20) primary key,
                        department varchar(20) not null,
                        people int default 0,
                        charge dec(8,2),
                        foreign key(department) references department(id) on delete cascade)'''
        students = '''create table student(
                        id varchar(20) primary key,
                        name varchar(20) not null,
                        sex ENUM("male","female"),
                        class varchar(20) not null,
                        profession varchar(20) not null,
                        college varchar(20) not null,
                        room varchar(20) not null,
                        phone varchar(20),
                        birthday date,
                        password varchar(30) not null,
                        foreign key(class) references class(id) ,
                        foreign key(college) references college(id),
                        foreign key(room) references room(id) on delete cascade)'''
        ch2 = '''alter table class add constraint f2 
                        foreign key(monitor) references student(id) on delete cascade'''
        book = '''create table book(
                        id varchar(20) primary key,
                        name varchar(20) not null,
                        type varchar(20),
                        author varchar(20),
                        year int,
                        sum int not null,
                        avaible int not null,
                        foreign key(type) references college(id) on update cascade)'''
        borrow = '''create table borrow(
                        book varchar(20),
                        person varchar(20),
                        time date not null,
                        deadline date not null,
                        primary key(book,person),
                        foreign key(book) references book(id) on delete cascade)'''
        manager = '''create table manager(
                        id varchar(20) primary key,
                        name varchar(20) not null,
                        sex ENUM("male","female"),
                        email varchar(20),
                        phone varchar(20),
                        birthday date,
                        password varchar(30) not null)'''
        try:
            self.cursor.execute(college)
            self.cursor.execute(teacher)
            self.cursor.execute(colge_ch)
            self.cursor.execute(classes)
            self.cursor.execute(course)
            self.cursor.execute(worker)
            self.cursor.execute(department)
            self.cursor.execute(room)
            self.cursor.execute(students)
            self.cursor.execute(choose)
            self.cursor.execute(ch2)
            self.cursor.execute(book)
            self.cursor.execute(borrow)
            self.cursor.execute(manager)
            self.database.commit()
        except mysql.connector.Error as e:
            print("create fails!{}".format(e))
            self.database.rollback()
        self.cursor.close()
    
    # 解除数据库关联
    def __del__(self):
        self.database.close()

    # 插入初始数据
    def init_data(self):
        self.cursor = self.database.cursor() # 当前游标
        config='''insert into college(id,name,profession) values(%s,%s,%s)'''
        self.cursor.execute(config,("1","航空宇航","直升机,飞行器,结构工程与力学,空气动力学"))
        self.cursor.execute(config,("2","能源与动力","内流与叶轮机械,强度与振动工程,控制工程"))
        self.cursor.execute(config,("3","自动化","自动控制,电气工程,测试工程,生物医学工程"))
        self.cursor.execute(config,("4","电子信息工程","电子科学与技术,信息与通信工程"))
        self.cursor.execute(config,("5","机电","设计工程,机械制造及其自动化,机械电子工程,航空宇航制造工程,工业设计"))
        self.cursor.execute(config,("6","材料科学与技术","材料加工工程,材料科学,应用化学,核科学与技术"))
        self.cursor.execute(config,("7","民航","空中交通,交通运输,民航工程,飞行技术,土木与机场工程"))
        self.cursor.execute(config,("8","理","数学,应用物理"))
        self.cursor.execute(config,("9","经济管理","管理科学与工程,工商管理,经济"))
        self.cursor.execute(config,("10","人文与社会科学","法律,公共管理"))
        self.cursor.execute(config,("11","艺术","美术,音乐,新闻传播学"))
        self.cursor.execute(config,("12","外国语","英语,日语"))
        self.cursor.execute(config,("13","马克思主义","思想道德修养,中国近现代史,马克思主义基本原理"))
        self.cursor.execute(config,("14","航天","航天系统工程,航天光电信息,航天控制工程"))
        self.cursor.execute(config,("15","国际教育","航空航天,电类,机械与材料,理学,经济与管理"))
        self.cursor.execute(config,("16","计算机科学与技术","计算机科学与技术,信息安全,软件工程,物联网"))
        config = '''insert into teacher(id,name,email,phone,college,birthday,salary,password,sex) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        self.cursor.execute(config,("T010001","张家辉","zjh@xxx.edu.cn","1726482736","1","1966-2-15",10000,"123456","male"))
        self.cursor.execute(config,("T020001","孙酷睿","skr@xxx.edu.cn","1573874382","2","1978-9-27",10000,"123456","male"))
        self.cursor.execute(config,("T030001","陈德观","cdg@xxx.edu.cn","1375674654","3","1978-5-5",10000,"123456","male"))
        self.cursor.execute(config,("T040001","夏简得","xjd@xxx.edu.cn","1578237548","4","1990-7-4",10000,"123456","female"))
        self.cursor.execute(config,("T050001","黄法树","hfs@xxx.edu.cn","1756347856","5","1983-7-30",10000,"123456","male"))
        self.cursor.execute(config,("T060001","王党将","wdj@xxx.edu.cn","1834837483","6","1988-4-1",10000,"123456","male"))
        self.cursor.execute(config,("T070001","叶蓓维","ybw@xxx.edu.cn","1476780237","7","1972-2-18",10000,"123456","female"))
        self.cursor.execute(config,("T080001","蒋峰","jf@xxx.edu.cn","1435386763","8","1980-9-21",10000,"123456","male"))
        self.cursor.execute(config,("T090001","尚夏","sx@xxx.edu.cn","1802375434","9","1990-10-28",10000,"123456","female"))
        self.cursor.execute(config,("T100001","张奋斗","zfd@xxx.edu.cn","1324798753","10","1985-8-14",10000,"123456","male"))
        self.cursor.execute(config,("T110001","王策雅","wcy@xxx.edu.cn","1894728432","11","1988-3-21",10000,"123456","female"))
        self.cursor.execute(config,("T120001","郑世伟","zsw@xxx.edu.cn","1974873634","12","1977-7-7",10000,"123456","male"))
        self.cursor.execute(config,("T130001","赵明端","zmd@xxx.eud.cn","1839247345","13","1979-9-23",10000,"123456","female"))
        self.cursor.execute(config,("T140001","周芙蓉","zfr@xxx.edu.cn","1978324733","14","1982-3-23",10000,"123456","female"))
        self.cursor.execute(config,("T150001","Tony","tony@xxx.edu.cn","1287233789","15","1986-4-19",10000,"123456","male"))
        self.cursor.execute(config,("T160001","陈秉","cb@xxx.edu.cn","1847343298","16","1982-2-5",10000,"123456","male"))
        self.cursor.execute(config,("T160002","何峰","hf@xxx.edu.cn","1847353228","16","1982-7-19",8000,"123456","male"))
        self.cursor.execute(config,("T160003","陈妍","cy@xxx.edu.cn","1847378932","16","1979-8-9",8000,"123456","female"))
        self.cursor.execute(config,("T160004","张而维","zew@xxx.edu.cn","1847926378","16","1990-10-28",7000,"123456","male"))
        config = '''update college set dean=%s where id=%s'''
        self.cursor.execute(config,("T010001","1"))
        self.cursor.execute(config,("T020001","2"))
        self.cursor.execute(config,("T030001","3"))
        self.cursor.execute(config,("T040001","4"))
        self.cursor.execute(config,("T050001","5"))
        self.cursor.execute(config,("T060001","6"))
        self.cursor.execute(config,("T070001","7"))
        self.cursor.execute(config,("T080001","8"))
        self.cursor.execute(config,("T090001","9"))
        self.cursor.execute(config,("T100001","10"))
        self.cursor.execute(config,("T110001","11"))
        self.cursor.execute(config,("T120001","12"))
        self.cursor.execute(config,("T130001","13"))
        self.cursor.execute(config,("T140001","14"))
        self.cursor.execute(config,("T150001","15"))
        self.cursor.execute(config,("T160001","16"))
        config = '''insert into worker(id,name,sex,phone,birthday,salary,password) values(%s,%s,%s,%s,%s,%s,%s)'''
        self.cursor.execute(config,("W0001","孙赫","female","182738478324","1959-3-12",2000,"123456"))
        self.cursor.execute(config,("W0002","陈飞","female","192373843742","1956-6-16",2000,"123456"))
        self.cursor.execute(config,("W0003","周德","female","198324972083","1962-9-9",2000,"123456"))
        self.cursor.execute(config,("W0004","周艳","female","184723894293","1977-3-5",2000,"123456"))
        self.cursor.execute(config,("W0005","孙燕","female","138274346523","1968-4-19",2000,"123456"))
        self.cursor.execute(config,("W0006","何香","female","189545433423","1967-8-20",2000,"123456"))
        self.cursor.execute(config,("W0007","黄文","female","189543423544","1969-7-10",2000,"123456"))
        self.cursor.execute(config,("W0008","叶示分","female","156977432687","1967-9-11",2000,"123456"))
        self.cursor.execute(config,("W0009","王巢","male","198345346546","1968-12-4",2000,"123456"))
        self.cursor.execute(config,("W0010","周礼","female","198278646352","1978-3-21",2000,"123456"))
        self.cursor.execute(config,("W0011","杨怡","female","167632542354","1967-7-24",2000,"123456"))
        self.cursor.execute(config,("W0012","周侠义","male","182472652864","1966-9-12",2000,"123456"))

        config = '''insert into department(id,area,manager,capacity) values(%s,%s,%s,%s)'''
        self.cursor.execute(config,("1","东区","W0001",100))
        self.cursor.execute(config,("2","东区","W0001",100))
        self.cursor.execute(config,("3","东区","W0001",100))
        self.cursor.execute(config,("4","东区","W0001",100))
        self.cursor.execute(config,("5","东区","W0001",100))
        self.cursor.execute(config,("6","东区","W0002",100))
        self.cursor.execute(config,("7","东区","W0002",100))
        self.cursor.execute(config,("8","东区","W0002",100))
        self.cursor.execute(config,("9","东区","W0002",100))
        self.cursor.execute(config,("10","东区","W0002",100))
        self.cursor.execute(config,("11","东区","W0003",100))
        self.cursor.execute(config,("12","东区","W0003",100))
        self.cursor.execute(config,("13","东区","W0003",100))
        self.cursor.execute(config,("14","东区","W0003",100))
        self.cursor.execute(config,("15","东区","W0003",100))
        self.cursor.execute(config,("16","西区","W0004",120))
        self.cursor.execute(config,("17","西区","W0004",120))
        self.cursor.execute(config,("18","西区","W0004",120))
        self.cursor.execute(config,("19","西区","W0004",120))
        self.cursor.execute(config,("20","西区","W0004",120))
        self.cursor.execute(config,("21","西区","W0005",120))
        self.cursor.execute(config,("22","西区","W0005",120))
        self.cursor.execute(config,("23","西区","W0005",120))
        self.cursor.execute(config,("24","西区","W0005",120))
        self.cursor.execute(config,("25","西区","W0005",120))
        self.cursor.execute(config,("26","西区","W0006",120))
        self.cursor.execute(config,("27","西区","W0006",120))
        self.cursor.execute(config,("28","西区","W0006",120))
        self.cursor.execute(config,("29","西区","W0006",120))
        self.cursor.execute(config,("30","西区","W0006",120))
        self.cursor.execute(config,("31","南区","W0007",140))
        self.cursor.execute(config,("32","南区","W0007",140))
        self.cursor.execute(config,("33","南区","W0007",140))
        self.cursor.execute(config,("34","南区","W0007",140))
        self.cursor.execute(config,("35","南区","W0007",140))
        self.cursor.execute(config,("36","南区","W0008",140))
        self.cursor.execute(config,("37","南区","W0008",140))
        self.cursor.execute(config,("38","南区","W0008",140))
        self.cursor.execute(config,("39","南区","W0008",140))
        self.cursor.execute(config,("40","南区","W0008",140))
        self.cursor.execute(config,("41","南区","W0009",140))
        self.cursor.execute(config,("42","南区","W0009",140))
        self.cursor.execute(config,("43","南区","W0009",140))
        self.cursor.execute(config,("44","南区","W0009",140))
        self.cursor.execute(config,("45","南区","W0009",140))
        self.cursor.execute(config,("46","北区","W0010",160))
        self.cursor.execute(config,("47","北区","W0010",160))
        self.cursor.execute(config,("48","北区","W0010",160))
        self.cursor.execute(config,("49","北区","W0010",160))
        self.cursor.execute(config,("50","北区","W0010",160))
        self.cursor.execute(config,("51","北区","W0011",160))
        self.cursor.execute(config,("52","北区","W0011",160))
        self.cursor.execute(config,("53","北区","W0011",160))
        self.cursor.execute(config,("54","北区","W0011",160))
        self.cursor.execute(config,("55","北区","W0011",160))
        self.cursor.execute(config,("56","北区","W0012",160))
        self.cursor.execute(config,("57","北区","W0012",160))
        self.cursor.execute(config,("58","北区","W0012",160))
        self.cursor.execute(config,("59","北区","W0012",160))
        self.cursor.execute(config,("60","北区","W0012",160))
        config = '''insert into room(id,department,people,charge) values(%s,%s,%s,%s)'''
        for i in range(14):
            for j in range(5):
                for k in range(5):
                    room = str(i+1)+"-"+str(j+1)+"0"+str(k+1)
                    self.cursor.execute(config,(room,str(i+1),0,0))
        for i in range(14):
            for j in range(6):
                for k in range(5):
                    room = str(i+16)+"-"+str(j+1)+"0"+str(k+1)
                    self.cursor.execute(config,(room,str(i+16),0,0))
        for i in range(15):
            for j in range(7):
                for k in range(5):
                    room = str(i+31)+"-"+str(j+1)+"0"+str(k+1)
                    self.cursor.execute(config,(room,str(i+31),0,0))
        for i in range(15):
            for j in range(8):
                for k in range(5):
                    room = str(i+46)+"-"+str(j+1)+"0"+str(k+1)
                    self.cursor.execute(config,(room,str(i+46),0,0))
        config = '''update room set people=1 where id="9-101"'''
        self.cursor.execute(config)
        config = '''update room set charge=20.53 where id="9-101"'''
        self.cursor.execute(config)
        config = '''insert into manager(id,name,sex,email,phone,birthday,password) values("M0001","王威风","male","wwf@xxx.man.cn","184325576534","1989-3-7","123456")'''
        self.cursor.execute(config)
        config = '''insert into class(id,college,teacher) values(%s,%s,%s)'''
        for i in range(9):
            cla = "0"+str(i+1)+"201"
            self.cursor.execute(config,(cla,str(i+1),"T0"+str(i+1)+"0001"))
        for i in range(7):
            cla = str(i+10)+"201"
            self.cursor.execute(config,(cla,str(i+10),"T"+str(i+10)+"0001"))
        config = '''insert into student(id,name,sex,class,profession,college,room,phone,birthday,password) values("S1620101","叶曦","female","16201","信息安全","16","9-101","15628472828","1999-7-30","123456")'''
        self.cursor.execute(config)
        config = '''update class set monitor="S1620101" where id="16201"'''
        self.cursor.execute(config)
        config = '''insert into course(id,name,type,credit,teacher,schedule,exam_type) values(%s,%s,%s,%s,%s,%s,%s)'''
        self.cursor.execute(config,("C0001","高等数学","必修",5.5,"T080001","Mon-10:15~12:00,Wed-10:15~12:00,Fri-8:00~9:45","考试"))
        self.cursor.execute(config,("C0002","网络安全","必修",2,"T160001","Tue-8:00~9:45,Fri-8:00~9:45","考试"))
        self.cursor.execute(config,("C0003","嵌入式","专业选修",2,"T160002","Thu-10:15~12:00","考查"))
        self.cursor.execute(config,("C0004","美术鉴赏","文化素质",1.5,"T110001","Fri-14:00~15:45","考查"))
        self.cursor.execute(config,("C0005","操作系统实践","实践拓展",2.5,"T160001","Tue-8:00~9:45,Thu-8:00~9:45","考查"))
        self.cursor.execute(config,("C0006","英语","必修",1.5,"T120001","Wed-16:15~18:00","考试"))
        self.cursor.execute(config,("C0007","操作系统","必修",3.5,"T160002","Mon-14:00~15:45,Wed-8:00~9:45","考试"))
        self.cursor.execute(config,("C0008","数据结构","必修",2,"T160003","Tue-16:15~18:00,Thu-16:15~18:00","考试"))
        self.cursor.execute('''update course set exam_date="2020-6-7 8:00:00" where id="3"''')
        self.cursor.execute('''update course set exam_room="2201" where id="3"''')
        self.cursor.execute('''update course set exam_date="2020-5-25 8:00:00" where id="1"''')
        self.cursor.execute('''update course set exam_room="2301" where id="1"''')
        config = '''insert into choose(student,course,time) values(%s,%s,%s)'''
        self.cursor.execute(config,("S1620101","C0001","2020-1-10 9:23:45"))
        self.cursor.execute(config,("S1620101","C0002","2020-1-12 15:02:12"))
        self.cursor.execute(config,("S1620101","C0003","2020-1-10 9:24:07"))
        self.cursor.execute(config,("S1620101","C0004","2020-1-10 9:24:29"))
        self.cursor.execute(config,("S1620101","C0005","2020-1-10 10:38:22"))
        self.cursor.execute(config,("S1620101","C0006","2020-2-9 12:21:05"))
        self.cursor.execute(config,("S1620101","C0007","2020-2-9 12:21:24"))
        self.cursor.execute('''update choose set score=100 where course="1" and student="S1620101"''')
        config = '''insert into book(id,name,author,type,year,sum,avaible) values(%s,%s,%s,%s,%s,%s,%s)'''
        self.cursor.execute(config,("B000001","高等数学","王五","8",2017,8,6))
        self.cursor.execute(config,("B000002","线性代数","张三","8",2017,5,4))
        self.cursor.execute(config,("B000003","数据结构","刘德峰","16",2016,12,10))
        self.cursor.execute(config,("B000004","操作系统","周赋好","16",2018,8,6))
        self.cursor.execute(config,("B000005","嵌入式","张梁","16",2019,6,5))
        self.cursor.execute(config,("B000006","世界图鉴","孙可望","11",2020,1,0))
        config = '''insert into borrow(book,person,time,deadline) values(%s,%s,%s,%s)'''
        self.cursor.execute(config,("B000001","T080001","2020-4-1","2020-8-1"))
        self.cursor.execute(config,("B000002","T080001","2020-4-1","2020-8-1"))
        self.cursor.execute(config,("B000001","S1620101","2020-3-14","2020-5-14"))
        self.cursor.execute(config,("B000003","T160003","2020-3-16","2020-7-16"))
        self.cursor.execute(config,("B000003","S1620101","2020-5-14","2020-7-14"))
        self.cursor.execute(config,("B000004","T160002","2020-2-29","2020-6-29"))
        self.cursor.execute(config,("B000004","S1620101","2020-5-14","2020-7-14"))
        self.cursor.execute(config,("B000005","T160002","2020-2-29","2020-6-29"))
        self.cursor.execute(config,("B000006","T110001","2020-4-3","2020-8-3"))
        self.database.commit()
        self.cursor.close()

    # 创建新的学生
    def create_student(self,ID,name,clas,profession,college,password,sex=None,phone=None,birthday=None):
        self.cursor = self.database.cursor() # 当前游标
        config = '''select id from room where people<4 limit 1'''
        self.cursor.execute(config)
        res = self.cursor.fetchall()
        room = res[0][0]
        config = '''update room set people=people+1 where id={!r}'''.format(room)
        self.cursor.execute(config)
        config = '''insert into student(
            id,name,sex,class,profession,college,room,phone,birthday,password) 
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        args = (ID,name,sex,clas,profession,college,room,phone,birthday,password)
        try:
            self.cursor.execute(config,args)
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            room = "insert fails!{}".format(e)
            self.database.rollback()
            flag = False
        self.cursor.close()
        return room,flag

    # 创建新的课程
    def create_course(self,ID,name,Type,credit,teacher,schedule=None,exam_type=None,exam_date=None,exam_room=None):
        self.cursor = self.database.cursor() # 当前游标
        config = '''insert into course(id,name,type,credit,teacher,schedule,exam_type,exam_date,exam_room)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        args = (ID,name,Type,credit,teacher,schedule,exam_type,exam_date,exam_room)
        try:
            res = self.cursor.execute(config,args)
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("insert fails!{}".format(e))
            self.database.rollback()
            flag = False
        self.cursor.close()
        return flag

    # 创建新的书籍
    def create_book(self,ID,name,Sum,author=None,Type=None,year=None):
        self.cursor = self.database.cursor() # 当前游标
        a = '''insert into book(id,name,sum,avaible,author,type,year) values(%s,%s,%s,%s,%s,%s,%s)'''
        b=(ID,name,Sum,Sum,author,Type,year)
        try:
            self.cursor.execute(a,b)
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("insert fails!{}".format(e))
            self.database.rollback()
            flag = False
        self.cursor.close()
        return flag
    
    # 创建新的管理员
    def create_manager(self,ID,name,password,sex= None,email=None,phone=None,birthday=None):
        self.cursor = self.database.cursor() # 当前游标
        a = '''insert into manager(id,name,password,sex,email,phone,birthday) values(%s,%s,%s,%s,%s,%s,%s)'''
        b=(ID,name,password,sex,email,phone,birthday)
        try:
            self.cursor.execute(a,b)
            self.database.commit()
            flag = True
            res = None
        except mysql.connector.Error as e:
            res = "insert fails!{}".format(e)
            self.database.rollback()
            flag = False
        self.cursor.close()
        return res,flag
    
    # 创建新的工作人员
    def create_worker(self,ID,name,password,sex= None,phone=None,birthday=None):
        self.cursor = self.database.cursor() # 当前游标
        a = '''insert into worker(id,name,password,sex,phone,birthday) values(%s,%s,%s,%s,%s,%s)'''
        b=(ID,name,password,sex,phone,birthday)
        try:
            self.cursor.execute(a,b)
            self.database.commit()
            flag = True
            res = None
        except mysql.connector.Error as e:
            res = "insert fails!{}".format(e)
            self.database.rollback()
            flag = False
        self.cursor.close()
        return res,flag

    # 创建新的教师
    def create_teacher(self,ID,name,password,sex=None,email=None,phone=None,college=None,birthday=None):
        self.cursor = self.database.cursor() # 当前游标
        config = '''insert into teacher(id,name,password,sex,email,phone,college,birthday) values(%s,%s,%s,%s,%s,%s,%s,%s)'''
        args = (ID,name,password,sex,email,phone,college,birthday)
        try:
            res = self.cursor.execute(config,args)
            self.database.commit()
            flag = True
            res = None
        except mysql.connector.Error as e:
            res = "insert fails!{}".format(e)
            self.database.rollback()
            flag = False
        self.cursor.close()
        return res,flag

    # 查询个人信息
    def show_info(self,ID):
        self.cursor = self.database.cursor() # 当前游标
        # 教师个人信息
        if re.match("T",ID)!=None:
            config = '''select id,name,sex,email,phone,college,birthday,salary from teacher where id={!r}'''.format(ID)
            try:
                self.cursor.execute(config)
                res = self.cursor.fetchall()
                flag = True
            except mysql.connector.Error as e:
                res = "select fails! {}".format(e)
                flag = False
        # 学生个人信息
        elif re.match("S",ID)!=None:
            config = '''select id,name,sex,class,profession,college,room,phone,birthday from student where id={!r}'''.format(ID)
            try:
                self.cursor.execute(config)
                res = self.cursor.fetchall()
                flag = True
            except mysql.connector.Error as e:
                res = "select fails! {}".format(e)
                flag = False
        # 工作人员信息
        elif re.match("W",ID)!=None:
            config = '''select id,name,sex,phone,birthday,salary from worker where id={!r}'''.format(ID)
            try:
                self.cursor.execute(config)
                res = self.cursor.fetchall()
                flag = True
            except mysql.connector.Error as e:
                res = "select fails! {}".format(e)
                flag = False
        # 管理人员信息
        elif re.match("M",ID)!=None:
            config = '''select id,name,sex,email,phone,birthday from manager where id={!r}'''.format(ID)
            try:
                self.cursor.execute(config)
                res = self.cursor.fetchall()
                flag = True
            except mysql.connector.Error as e:
                res = "select fails! {}".format(e)
                flag = False
        self.cursor.close()
        return res,flag
    
    # 显示课程
    def show_course(self,condition=None):
        self.cursor = self.database.cursor() # 当前游标
        config = '''select id,name,teacher,credit,type,schedule,exam_type from course'''
        if condition != None:
            config = config+" where "+condition
        try:
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            flag = True
        except mysql.connector.Error as e:
            res = "select fails! {}".format(e)
            flag = False
        self.cursor.close()
        return res,flag
    
    # 显示书籍
    def show_book(self,condition=None):
        self.cursor = self.database.cursor() # 当前游标
        config = '''select id,name,author,type,year,sum,avaible from book'''
        if condition!=None:
            config = config+" where "+condition
        try:
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            flag = True
        except mysql.connector.Error as e:
            print("select fails! {}".format(e))
            res = None
            flag = False
        self.cursor.close()
        return res,flag
    
    # 显示未考试科目
    def show_test(self,ID):
        self.cursor = self.database.cursor() # 当前游标
        config = '''select id,name,exam_type,exam_date,exam_room
                    from course where id in(
                        select course from choose where 
                            student={!r} and score is NULL)'''.format(ID) 
        try:
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            flag = True
        except mysql.connector.Error as e:
            print("select fails! {}".format(e))
            res = None
            flag = False
        self.cursor.close()
        return res,flag

    # 显示电费
    def show_charge(self,ID):
        self.cursor = self.database.cursor() # 当前游标
        config = '''select area,room.id,charge from department,room 
                    where department.id=room.department and 
                        room.id=(select room from student 
                            where id={!r})'''.format(ID)
        try:
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            flag = True
        except mysql.connector.Error as e:
            print("select fails! {}".format(e))
            res = None
            flag = False
        self.cursor.close()
        return res,flag

    # 显示成绩
    def show_grade(self,ID):
        self.cursor = self.database.cursor() # 当前游标
        config = '''select name,credit,score from course inner join (
                        select score,course from choose where student={!r}) X
                    on course.id=X.course where score is not null'''.format(ID)
        config1 = '''select avg(score) from choose group by student having student={!r}'''.format(ID)
        try:
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            self.cursor.execute(config1)
            res1 = self.cursor.fetchall()
            flag = True
        except mysql.connector.Error as e:
            print("select fails! {}".format(e))
            res = None
            res1 = None
            flag = False
        self.cursor.close()
        return res,res1,flag
    
    # 显示借阅欠费情况
    def show_fee(self,ID):
        self.cursor = self.database.cursor() # 当前游标
        config = '''select name,time,deadline from book inner join(select book,time,deadline from borrow where person={!r}) x on x.book=book.id'''.format(ID)
        try:
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            flag = True
        except mysql.connector.Error as e:
            print("select fails! {}".format(e))
            res = None
            flag=False
        self.cursor.close()
        return res,flag

    # 显示宿舍楼信息
    def show_department(self,ID):
        self.cursor = self.database.cursor() # 当前游标
        config = '''select id,area,capacity from department where manager={!r}'''.format(ID)
        try:
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            flag = True
        except mysql.connector.Error as e:
            print("select fails! {}".format(e))
            res = None
            flag=False
        self.cursor.close()
        return res,flag

    # 显示宿舍房间信息
    def show_room(self,ID):
        self.cursor = self.database.cursor() # 当前游标
        config = '''select id,people,charge from room where department={!r}'''.format(ID)
        try:
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            flag = True
        except mysql.connector.Error as e:
            print("select fails! {}".format(e))
            res = None
            flag=False
        self.cursor.close()
        return res,flag

    # 更新选课记录
    def update_choose(self,student,course):
        self.cursor = self.database.cursor() # 当前游标
        config = '''insert into choose(student,course,time) values(%s,%s,now())'''
        try:
            self.cursor.execute(config,(student,course))
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("insert fails!{}".format(e))
            self.database.rollback()
            flag = False
        self.cursor.close()
        return flag
    
    # 更新借书记录
    def update_borrow(self,person,book):
        self.cursor = self.database.cursor() # 当前游标
        # 判断person是否合法
        if re.match("S",person)!=None:
            config = '''select * from student where id={!r}'''.format(person)
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            if res==[]:
                print("No such person '{}'".format(person))
                self.cursor.close()
                return False
            temp=2
        elif re.match("T",person)!=None:
            config = '''select * from teacher where id={!r}'''.format(person)
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            if res==[]:
                print("No such person '{}'".format(person))
                self.cursor.close()
                return False
            temp=4
        else:
                print("No such person '{}'".format(person))
                self.cursor.close()
                return False
        # 判断书是否还剩
        config = '''select avaible from book where id={!r}'''.format(book)
        self.cursor.execute(config)
        res = self.cursor.fetchall()
        if res==[]:
            print("No such book '{}'".format(book))
            self.cursor.close()
            return false
        elif res[0][0]<1:
            print("The book is not avaible!")
            self.cursor.close()
            return False
        # 写入数据
        config = '''insert into borrow(book,person,time,deadline) values(%s,%s,curdate(),date_add(curdate(),interval %s month))'''
        try:
            self.cursor.execute(config,(book,person,temp))
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("insert fails! {}".format(e))
            self.database.rollback()
            flag = False
        config = '''update book set avaible=avaible-1 where id={!r}'''.format(book)
        try:
            self.cursor.execute(config)
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("update fails! {}".format(e))
            self.database.rollback()
            flag = False
        self.cursor.close()
        return flag

    # 更新电费
    def update_charge(self,ID,add):
        self.cursor = self.database.cursor() # 当前游标
        # 判断传入的是房间号还是学生学号
        if re.match("S",ID)!=None:
            config = '''select room from student where id={!r}'''.format(ID)
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            ID = res[0][0]
        config = '''update room set charge=charge+{} where id={!r}'''.format(add,ID)
        try:
            self.cursor.execute(config)
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("update fails! {}".format(e))
            self.database.rollback()
            flag = False
        self.cursor.close()
        return flag

    # 更新成绩
    def update_grade(self,student,course,score):
        self.cursor = self.database.cursor() # 当前游标
        config = '''update choose set score={} where student={!r} and course={!r}'''.format(score,student,course)
        try:
            self.cursor.execute(config)
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("update fails! {}".format(e))
            self.database.rollback()
            flag = False
        self.cursor.close()
        return flag

    # 更新考试时间及地点
    def update_test(self,ID,time,addr):
        self.cursor = self.database.cursor() # 当前游标
        config = '''update course set exam_date={!r},exam_room={!r} where id={!r}'''.format(time,addr,ID)
        try:
            self.cursor.execute(config)
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("update fails! {}".format(e))
            self.database.rollback()
            flag = False
        self.cursor.close()
        return flag

    # 更新借阅欠费
    def delete_borrow(self,ID):
        self.cursor = self.database.cursor() # 当前游标
        #删除所有已过期借阅
        config = '''delete from borrow where person={!r} and to_days(deadline)<to_days(curdate())'''.format(ID)
        try:
            self.cursor.execute(config)
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("delete fails! {}".format(e))
            self.database.rollback()
            flag = False
        self.cursor.close()
        return flag

    # 搜索教师
    def search_teacher(self,segment,condition=None):
        self.cursor = self.database.cursor() # 当前游标
        config = '''select {} from teacher'''.format(segment)
        if condition!=None:
            config = config+" where "+condition
        courses = []
        try:
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            for teacher in res:
                ID = teacher[0]
                self.cursor.execute('''select name from course where teacher={!r}'''.format(ID))
                course = self.cursor.fetchall()
                courses.append(course)
            flag = True
        except mysql.connector.Error as e:
            print("select fails! {}".format(e))
            res = None
            flag = False
        self.cursor.close()
        return res,courses,flag

    # 搜索学生
    def search_student(self,segment,condition=None):
        self.cursor = self.database.cursor() # 当前游标
        config = '''select {} from student'''.format(segment)
        if condition!=None:
            config = config+" where "+condition
        courses = []
        try:
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            flag = True
        except mysql.connector.Error as e:
            print("select fails! {}".format(e))
            res = None
            flag = False
        self.cursor.close()
        return res,flag

    # 搜索宿舍楼
    def search_department(self,condition=None):
        self.cursor = self.database.cursor() # 当前游标
        config = '''select id,area,manager,capacity from department'''
        if condition!=None:
            config = config+" where "+condition
        courses = []
        try:
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            flag = True
        except mysql.connector.Error as e:
            print("select fails! {}".format(e))
            res = None
            flag = False
        self.cursor.close()
        return res,flag

    # 搜索工作人员
    def search_worker(self,condition=None):
        self.cursor = self.database.cursor() # 当前游标
        config = '''select id,name,phone,salary from worker'''
        if condition!=None:
            config = config+" where "+condition
        courses = []
        try:
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            flag = True
        except mysql.connector.Error as e:
            print("select fails! {}".format(e))
            res = None
            flag = False
        self.cursor.close()
        return res,flag

    # 删除人员
    def delete_person(self,ID):
        self.cursor = self.database.cursor() # 当前游标
        if re.match("S",ID)!=None:
            table = "student"
        elif re.match("T",ID)!=None:
            table = "teacher"
        elif re.match("W",ID)!=None:
            table = "worker"
        config = '''delete from {} where id={!r}'''.format(table,ID)
        try:
            self.cursor.execute(config)
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("delete fails! {}".format(e))
            self.database.rollback()
            flag = False
        self.cursor.close()
        return flag

    # 更新学生信息
    def update_student(self,ID,name,sex,clas,profession,college,phone,birthday):
        self.cursor = self.database.cursor() # 当前游标
        config = '''update student set
            name={!r},sex={!r},class={!r},profession={!r},college={!r},phone={!r},birthday={!r} where id={!r}'''.format
        try:
            self.cursor.execute(config(name,sex,clas,profession,college,phone,birthday,ID))
            self.database.commit()
            res = None
            flag = True
        except mysql.connector.Error as e:
            res = "update fails!{}".format(e)
            self.database.rollback()
            flag = False
        self.cursor.close()
        return res,flag

    # 更新工作人员信息
    def update_worker(self,ID,name,sex,phone,birthday,salary):
        self.cursor = self.database.cursor() # 当前游标
        config = '''update worker set name={!r},sex={!r},phone={!r},birthday={!r},salary={!r} where id={!r}'''.format
        try:
            self.cursor.execute(config(name,sex,phone,birthday,salary,ID))
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("update fails!{}".format(e))
            self.database.rollback()
            flag = False
        self.cursor.close()
        return flag
    
    # 更新教师信息
    def update_teacher(self,ID,name,sex,email,phone,college,birthday,salary):
        self.cursor = self.database.cursor() # 当前游标
        config = '''update teacher set name={!r},sex={!r},email={!r},phone={!r},college={!r},birthday={!r},salary={!r} where id={!r}'''.format
        try:
            self.cursor.execute(config(name,sex,email,phone,college,birthday,salary,ID))
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("update fails!{}".format(e))
            self.database.rollback()
            flag = False
        self.cursor.close()
        return flag

    # 获取ID对应的密码
    def get_passwd(self,ID):
        self.cursor = self.database.cursor() # 当前游标
        if re.match("T",ID):
            table = "teacher"
        elif re.match("W",ID):
            table = "worker"
        elif re.match("M",ID):
            table = "manager"
        elif re.match("S",ID):
            table = "student"
        else:
            self.cursor.close()
            return None,False
        config = '''select password from {} where id={!r}'''.format(table,ID)
        try:
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            flag = True
        except mysql.connector.Error as e:
            print("select fails! {}".format(e))
            res = None
            flag = False
        self.cursor.close()
        return res,flag

    # 获取名字
    def get_name(self,ID):
        self.cursor = self.database.cursor() # 当前游标
        if re.match("T",ID):
            table = "teacher"
        elif re.match("W",ID):
            table = "worker"
        elif re.match("M",ID):
            table = "manager"
        elif re.match("S",ID):
            table = "student"
        else:
            self.cursor.close()
            return None,False
        config = '''select name from {} where id={!r}'''.format(table,ID)
        try:
            self.cursor.execute(config)
            res = self.cursor.fetchall()
            flag = True
        except mysql.connector.Error as e:
            res = "select fails! {}".format(e)
            flag = False
        self.cursor.close()
        return res,flag

        

