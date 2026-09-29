import sqlite3
conn = sqlite3.connect('DevOps.db') #連資料庫=Devops.db
cursor = conn.cursor()
cursor.execute('SELECT * from Student')

records = cursor.fetchall()
print (records)

for i in records[0]:
    print (type(i))


sqlins = """
INSERT into Student (Name, Gender, Birthday)
VALUES ('Susan', 'Female', '1980/07/22');"""
# 將SQ:指令儲存在sqlins變數中

cursor.execute(sqlins) #執行SQL語法
cursor.fetchall() #從資料庫抓出所有資料
conn.commit() #把資料從Python端推回資料庫


sqlupd = """
UPDATE Student SET Name='Judy', 
Birthday='2006/09/12' where Name='Susan';"""

cursor.execute(sqlupd)
cursor.fetchall()
conn.commit()

sqldel = """
DELETE from Student where Name = 'Judy';"""
cursor.execute(sqldel)
cursor.fetchall()
conn.commit()

cursor.execute('SELECT * from Student') #確定資料已更新
check = cursor.fetchall() #確定資料已更新
print (check) #確定資料已更新


cursor.close()
conn.close()
