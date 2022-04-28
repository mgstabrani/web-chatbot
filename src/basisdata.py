import sqlite3
import datetime

#root of path
path = '../test/'

# MEMBUAT BASIS DATA (semua tabel)
# ===================================Asumsi data base pusat=========================================
def createDB():
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()

    cur.executescript("""
        CREATE TABLE IF NOT EXISTS Daftar_Tugas (
            id        TEXT NOT NULL PRIMARY KEY UNIQUE,
            tanggal   DATE,
            matkul    TEXT,
            jenis     TEXT,
            nama      TEXT,
            status    BOOLEAN
        );

        CREATE TABLE IF NOT EXISTS Kata_Penting (
            Text    TEXT NOT NULL UNIQUE
        );
        CREATE TABLE IF NOT EXISTS Kata_Help (
            Text    TEXT NOT NULL UNIQUE
        );
        CREATE TABLE IF NOT EXISTS Kata_Tampil_Deadline  (
            Text    TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS Kata_Task_Selesai (
            Text    TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS Fitur (
            Text    TEXT NOT NULL UNIQUE
        )

        """)
    conn.commit()

def clearDB():
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()

    cur.executescript("""
        DROP TABLE IF EXISTS Daftar_Tugas;
        DROP TABLE IF EXISTS Kata_Penting;
        DROP TABLE IF EXISTS Kata_Help;
        DROP TABLE IF EXISTS Kata_Tampil_Deadline;
        DROP TABLE IF EXISTS Kata_Task_Selesai;
        DROP TABLE IF EXISTS Fitur
        """)
    conn.commit()
    createDB()

def upsert_Daftar_Tugas(id, tanggal, matkul, jenis, nama, status):
    # insert data baru ketika id (PK) unik  atau update data ketika PK sudah ada di data

    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    query = '''INSERT OR IGNORE INTO Daftar_Tugas(id, tanggal, matkul, jenis, nama, status)
    VALUES(?, ?, ?, ?, ?,?)
    ON CONFLICT(id) 
    DO UPDATE SET tanggal =?, matkul =?, jenis =?, nama =?, status =?'''
    value = (id, tanggal, matkul, jenis, nama, status, tanggal, matkul, jenis, nama, status)
    cur.execute(query,value)
    conn.commit()
    conn.close()

def update_Daftar_Tugas(id, tanggal):
    # insert data baru ketika id (PK) unik  atau update data ketika PK sudah ada di data

    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    query = '''UPDATE Daftar_Tugas SET tanggal =? WHERE id = ?'''
    value = (tanggal, id)
    cur.execute(query,value)
    conn.commit()
    conn.close()

def getList_Daftar_Tugas():
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    data =[]
    query = "SELECT id, tanggal, matkul, jenis, nama FROM Daftar_Tugas"
    for kata in cur.execute(query):
        kata = str(kata).replace("('","")
        kata = str(kata).replace("', '","#-#")
        kata = str(kata).replace("')","")
        kata.split("#-#")
        data.append(kata.split("#-#"))

    return data

def getList_Daftar_Tugas_Status(status):
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    data =[]
    query = "SELECT id, tanggal, matkul, jenis, nama FROM Daftar_Tugas WHERE status =?"

    value = (status,)
    for kata in cur.execute(query,value):
        kata = str(kata).replace("('","")
        kata = str(kata).replace("', '","#-#")
        kata = str(kata).replace("')","")
        kata.split("#-#")
        data.append(kata.split("#-#"))

    return data

def getList_Daftar_Tugas_Jenis_Status(jenis,status):
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    data =[]
    query = "SELECT id, tanggal, matkul, jenis, nama FROM Daftar_Tugas WHERE status =? AND jenis =?"

    value = (status,jenis)
    for kata in cur.execute(query,value):
        kata = str(kata).replace("('","")
        kata = str(kata).replace("', '","#-#")
        kata = str(kata).replace("')","")
        kata.split("#-#")
        data.append(kata.split("#-#"))

    return data


def IsInputValid(tanggal,matkul,jenis,nama,status):
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    data =[]
    query = "SELECT id, tanggal, matkul, jenis, nama FROM Daftar_Tugas WHERE status =? AND jenis =? AND nama = ? AND tanggal=? AND matkul =?"

    value = (status,jenis,nama,tanggal,matkul)
    for kata in cur.execute(query,value):
        kata = str(kata).replace("('","")
        kata = str(kata).replace("', '","#-#")
        kata = str(kata).replace("')","")
        kata.split("#-#")
        data.append(kata.split("#-#"))

    return data ==[]

def getList_Daftar_Tugas_tgl(tglMulai, tglSelesai, status):
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    data =[]
    query = "SELECT id, tanggal, matkul, jenis, nama FROM Daftar_Tugas WHERE status =? AND tanggal >= ? AND tanggal <=? ORDER BY tanggal"

    value = (status,tglMulai,tglSelesai)
    for kata in cur.execute(query,value):
        kata = str(kata).replace("('","")
        kata = str(kata).replace("', '","#-#")
        kata = str(kata).replace("')","")
        kata.split("#-#")
        data.append(kata.split("#-#"))

    return data

def getList_Daftar_Tugas_Jenis_tgl(jenis, tglMulai, tglSelesai, status):
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    data =[]
    query = "SELECT id, tanggal, matkul, jenis, nama FROM Daftar_Tugas WHERE status =? AND tanggal >= ? AND tanggal <=? AND jenis =? ORDER BY tanggal"

    value = (status,tglMulai,tglSelesai,jenis)
    for kata in cur.execute(query,value):
        kata = str(kata).replace("('","")
        kata = str(kata).replace("', '","#-#")
        kata = str(kata).replace("')","")
        kata.split("#-#")
        data.append(kata.split("#-#"))

    return data

def getList_Daftar_Tugas_tglMulai(tglMulai, status):
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    data =[]
    query = "SELECT id, tanggal, matkul, jenis, nama FROM Daftar_Tugas WHERE status =? AND tanggal >= ? ORDER BY tanggal"

    value = (status,tglMulai)
    for kata in cur.execute(query,value):
        kata = str(kata).replace("('","")
        kata = str(kata).replace("', '","#-#")
        kata = str(kata).replace("')","")
        kata.split("#-#")
        data.append(kata.split("#-#"))

    return data

def getList_Daftar_Tugas_Jenis_tglMulai(jenis,tglMulai, status):
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    data =[]
    query = "SELECT id, tanggal, matkul, jenis, nama FROM Daftar_Tugas WHERE status =? AND tanggal >= ? AND jenis =? ORDER BY tanggal"

    value = (status,tglMulai,jenis)
    for kata in cur.execute(query,value):
        kata = str(kata).replace("('","")
        kata = str(kata).replace("', '","#-#")
        kata = str(kata).replace("')","")
        kata.split("#-#")
        data.append(kata.split("#-#"))

    return data 

def insert_Kata_Help(kata):
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    query = '''INSERT OR IGNORE INTO Kata_Help(Text) VALUES(?)'''
    value = (kata,)
    cur.execute(query,value)
    conn.commit()
    conn.close()

def getList_Kata_Help():
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    data =[]
    query = '''SELECT * FROM Kata_Help'''
    for kata in cur.execute(query):
        kata = str(kata).replace("('","")
        kata = str(kata).replace("',)","")
        data.append(kata)

    return data

def insert_Kata_penting(kata):
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    query = '''INSERT OR IGNORE INTO Kata_Penting(Text) VALUES(?)'''
    value = (kata,)
    cur.execute(query,value)
    conn.commit()
    conn.close()

def getList_Kata_Penting():
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    data =[]
    query = '''SELECT * FROM Kata_Penting'''
    for kata in cur.execute(query):
        kata = str(kata).replace("('","")
        kata = str(kata).replace("',)","")
        data.append(kata)

    return data

def insert_Kata_Tampil_Deadline(kata):
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    query = '''INSERT OR IGNORE INTO Kata_Tampil_Deadline(Text) VALUES(?)'''
    value = (kata,)
    cur.execute(query,value)
    conn.commit()
    conn.close()

def getList_Kata_Tampil_Deadline():
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    data =[]
    query = '''SELECT * FROM Kata_Tampil_Deadline'''
    for kata in cur.execute(query):
        kata = str(kata).replace("('","")
        kata = str(kata).replace("',)","")
        data.append(kata)

    return data

def insert_Kata_Task_Selesai(kata):
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    query = '''INSERT OR IGNORE INTO Kata_Task_Selesai(Text) VALUES(?)'''
    value = (kata,)
    cur.execute(query,value)
    conn.commit()
    conn.close()

def getList_Kata_Task_Selesai():
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    data =[]
    query = '''SELECT * FROM Kata_Task_Selesai'''
    for kata in cur.execute(query):
        kata = str(kata).replace("('","")
        kata = str(kata).replace("',)","")
        data.append(kata)

    return data

def insert_Fitur(kata):
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    query = '''INSERT OR IGNORE INTO Fitur(Text) VALUES(?)'''
    value = (kata,)
    cur.execute(query,value)
    conn.commit()
    conn.close()

def getList_Fitur():
    conn = sqlite3.connect(path +'BasisData.sqlite')
    cur = conn.cursor()
    data =[]
    query = '''SELECT * FROM Fitur'''
    for kata in cur.execute(query):
        kata = str(kata).replace("('","")
        kata = str(kata).replace("',)","")
        data.append(kata)

    return data

def Insert_standar():
    clearDB()
    kata_penting = ["deadline", "tubes", "tucil", "kuis", "ujian", "pr"]
    kata_help = ["bisa","lakukan","help","command","fitur"]
    kata_tampil_deadline = ["when","deadline","kapan","pada","tanggal", "hari", "minggu","antara", "sejauh","depan"]
    kata_task_selesai = ["done","selesai","sudah"]
    fitur = [
        "Menambahkan task baru",
        "Melihat daftar task",
        "Menampilkan deadline dari suatu task tertentu",
        "Memperbaharui task tertentu",
        "Menandai bahwa suatu task sudah dikerjakan",
        "Memberikan rekomendasi kata"
        ]
    deadline = [
    ["1","22/08/2021","IF2240","tubes","String Matching"],
    ["2","21/07/2021","IF2230","tucil","Normalisasi"],
    ["3","22/05/2021","IF2230","tubes","Index Tuning"]]

    for kata in kata_penting:
        insert_Kata_penting(kata)

    for kata in kata_help:
        insert_Kata_Help(kata)

    for kata in kata_tampil_deadline:
        insert_Kata_Tampil_Deadline(kata)

    for kata in kata_task_selesai:
        insert_Kata_Task_Selesai(kata)

    for kata in fitur:
        insert_Fitur(kata)

    for List in deadline:
        (tgl,bln,th) = List[1].split("/")
        date = datetime.date(int(th),int(bln),int(tgl))
        #print(date)
        upsert_Daftar_Tugas(List[0],date,List[2],List[3],List[4],False)


#DOKUMENTASI
# Insert_standar()
# print( getList_Kata_Help())
# print( getList_Kata_Tampil_Deadline())
# print( getList_Kata_Task_Selesai())
# print( getList_Fitur())
# print(getList_Daftar_Tugas( 0))
# date1 = datetime.date(2021,5,20)
# date2 = datetime.date(2021,8,22)
# print(getList_Daftar_Tugas_tgl(date1,date2,0))
# tgl = "22/08/2021"
# (tgl,bln,th) = tgl.split("/")
# date = datetime.date(int(th),int(bln),int(tgl))
# print(IsInputValid(date,"IF2240","tubes","String Matching",False))
