import db_manager
db = db_manager.mydb("localhost","root","123456")
db.init_data()
#print(db.create_student(ID="S1620102",name="张三",sex="male",clas="16201",profession="信息安全",college="16",phone="1247323764",birthday="199-10-1",password="123456"))
#print(db.create_manager(ID="M1321",name="李四",sex="samale",phone="154756322",password="123456"))
#db.create_courise(ID="14",name="ferfr",teacher="T080001",Type="必修",credit=5.5)
[res,re1,flag]=db.search_teacher("name","college='16'")
print(res,re1)
[res,flag]=db.search_student("name,sex","college='16'")
print(res)
#[res,res1,flag] = db.show_grade("S1620102")
#print(res,res1)
#print(db.update_charge("S1620101",20))

