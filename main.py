import db_manager
db = db_manager.mydb("localhost","root","123456")
#print(db.create_student(ID="S161710101",name="张三",sex="male",clas="1617001",profession="计算机科学与技术",college="计算机科学与技术",room="12-10101",phone="1247323764",birthday="199-10-1",password="123456"))
#print(db.create_manager(ID="M1321",name="李四",sex="samale",phone="154756322",password="123456"))
db.init_data()
