import db_manager
db = db_manager.mydb("localhost","root","123456")
db.init_data()
#db.create_student(ID="S1620102",name="张三",sex="male",clas="16201",profession="信息安全",college="16",phone="1247323764",birthday="199-10-1",password="123456")
#print(db.create_manager(ID="M1321",name="李四",sex="samale",phone="154756322",password="123456"))
#db.create_courise(ID="14",name="ferfr",teacher="T080001",Type="必修",credit=5.5)
[res,flag]=db.show_book("id='1'")
print(res)
