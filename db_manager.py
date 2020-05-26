import mysql.connector
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
                        foreign key(college) references college(id))'''
        colge_ch = '''alter table college add constraint f1 
                        foreign key(dean) references teacher(id)'''
        classes =  '''create table class(
                        id varchar(20) primary key,
                        college varchar(20) not null,
                        teacher varchar(20),
                        monitor varchar(20),
                        foreign key(college) references college(id),
                        foreign key(teacher) references teacher(id))'''
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
                        exam_date date,
                        exam_room varchar(20),
                        foreign key(teacher) references teacher(id))'''
        choose = '''create table choose(
                        student varchar(20),
                        course varchar(20),
                        time date not null,
                        score int,
                        foreign key(student) references student(id),
                        foreign key(course) references course(id),
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
                        charge dec(8,2),
                        foreign key(department) references department(id))'''
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
                        foreign key(class) references class(id),
                        foreign key(college) references college(id),
                        foreign key(room) references room(id))'''
        ch2 = '''alter table class add constraint f2 
                        foreign key(monitor) references student(id)'''
        book = '''create table book(
                        id varchar(20) primary key,
                        name varchar(20) not null,
                        type varchar(20),
                        year int,
                        value dec(8,2),
                        sum int not null,
                        avaible int not null,
                        foreign key(type) references college(id))'''
        borrow = '''create table borrow(
                        book varchar(20),
                        person varchar(20),
                        time date not null,
                        deadline date not null,
                        primary key(book,person),
                        foreign key(book) references book(id))'''
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

    # 创建新的学生
    def create_student(self,ID,name,clas,professtion,college,room,password,sex=None,phone=None,birthday=None):
        config = '''inset into student(
            id,name,sex,class,profession,college,room,phone,birthday,password) 
            values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        args = (ID,name,sex,clas,profession,college,room,phone,birthday,password)
        try:
            self.cursor.execute(config,args)
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("insert fails!{}".format(e))
            self.database.rollback()
            flag = False
        return flag

    # 创建新的学院
    def create_college(self,ID,name,profession,dean=None):
        config = '''insert into college(ID,name,profession,dean)
                    values(%s,%s,%s,%s)'''
        args = (ID,name,profession,dean)
        try:
            res = self.cursor.execute(config,args)
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("insert fails!{}".format(e))
            self.database.rollback()
            flag = False
        return flag
    
    # 创建新的管理员
    def create_manager(self,ID,name,password,sex= None,email=None,phone=None,birthday=None):
        a = '''insert into manager(id,name,password,sex,email,phone,birthday) values(%s,%s,%s,%s,%s,%s,%s)'''
        b=(ID,name,password,sex,email,phone,birthday)
        try:
            self.cursor.execute(a,b)
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("insert fails!{}".format(e))
            self.database.rollback()
            flag = False
        return flag
    
    # 创建新的教师
    def create_teacher(self,ID,name,password,sex=None,email=None,phone=None,college=None,birthday=None):
        config = '''insert into teacher(id,name,password,sex,email,phone,college,birthday) values(%s,%s,%s,%s,%s,%s,%s,%s)'''
        args = (ID,name,password,sex,email,phone,college,birthday)
        try:
            res = self.cursor.execute(config,args)
            self.database.commit()
            flag = True
        except mysql.connector.Error as e:
            print("insert fails!{}".format(e))
            self.database.rollback()
            flag = False
        return flag
    # 插入初始数据
    def init_data(self):
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
        self.cursor.execute(config,("1","东区","W0001",150))
        self.cursor.execute(config,("2","东区","W0001",150))
        self.cursor.execute(config,("3","东区","W0001",150))
        self.cursor.execute(config,("4","东区","W0001",150))
        self.cursor.execute(config,("5","东区","W0001",150))
        self.cursor.execute(config,("6","东区","W0002",150))
        self.cursor.execute(config,("7","东区","W0002",150))
        self.cursor.execute(config,("8","东区","W0002",150))
        self.cursor.execute(config,("9","东区","W0002",150))
        self.cursor.execute(config,("10","东区","W0002",150))
        self.cursor.execute(config,("11","东区","W0003",150))
        self.cursor.execute(config,("12","东区","W0003",150))
        self.cursor.execute(config,("13","东区","W0003",150))
        self.cursor.execute(config,("14","东区","W0003",150))
        self.cursor.execute(config,("15","东区","W0003",150))
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
        self.database.commit()
