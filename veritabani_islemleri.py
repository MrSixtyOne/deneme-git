import sqlite3

con=sqlite3.connect("dersler.db")
cursor=con.cursor()

def tabloYap():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT, numara INT, ogrenciNotu INT)")

def ekle():
    cursor.execute("INSERT INTO ogrenciler VALUES('Salih Tosun',259173,80)")
    con.commit()

def getir():
    cursor.execute("Select * From ogrenciler")
    veri=cursor.fetchall()
    for i in veri:
        print(i)

tabloYap()
ekle()
getir()
con.close()