import matcher
import re
from deadline import *

# mungkin kedepannya perlu dipisah si kata2 pentingnya
# kayak ada kata penting untuk jenis tugas,
# ada kata penting untuk jenis pertanyaan, dll
kata_penting = ["deadline", "tubes", "tucil", "kuis", "ujian", "pr"]
kata_help = ["bisa","lakukan","help","command","fitur"]
kata_tampil_deadline = ["when","deadline","kapan"]
kata_task_selesai = ["done","selesai","sudah"]
fitur = [
    "Menambahkan task baru",
    "Melihat daftar task",
    "Menampilkan deadline dari suatu task tertentu",
    "Memperbaharui task tertentu",
    "Menandai bahwa suatu task sudah dikerjakan",
    "Memberikan rekomendasi kata"
    ]

def tampilDeadline(usrMsg):
    for i in range(len(deadline)):
        #General untuk tugas
        if(matcher.match(usrMsg,"tugas")):
            if(matcher.match(usrMsg,deadline[i][2].lower())):
                return deadline[i][1]
        #Spesifik, tucil, tubes atau pr
        else:
            if(matcher.match(usrMsg,deadline[i][2].lower()) and matcher.match(usrMsg,deadline[i][3].lower())):
                return deadline[i][1]

    return "Tidak ada deadline itu"

def tandaiTask(usrMsg):
    for i in range(len(deadline)):
        if(matcher.match(usrMsg,deadline[i][0])):
            deadline.pop(i)
            return "Task ditandai selesai"
    return "Task tidak ditemukan"

def help():
    output = "[Fitur]<br>"
    for i in range(len(fitur)):
        output += str(i+1) + ". " + fitur[i] + "<br>"
    output += "<br>"
    output += "[Daftar kata penting]<br>"
    for i in range(len(kata_penting)):
        output += str(i+1) + ". " + kata_penting[i] + "<br>"
    return output

def process(usrMsg):
    text = str(usrMsg).lower()

    #Menampilkan help
    for pattern in kata_help:
        if (matcher.match(text, pattern)) :
            return help()

    #Menandai task selesai
    for pattern in kata_task_selesai:
        if (matcher.match(text, pattern)) :
            return tandaiTask(text)    

    #Menampilkan tanggal deadline suatu task
    for pattern in kata_tampil_deadline:
        if (matcher.match(text, pattern)) :
            return tampilDeadline(text)

    for pattern in kata_penting:
        if (matcher.match(text, pattern)) :
            return "Ada kata penting"

    return "Tidak ditemukan kata penting"