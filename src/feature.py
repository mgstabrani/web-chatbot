import matcher
import re

# mungkin kedepannya perlu dipisah si kata2 pentingnya
# kayak ada kata penting untuk jenis tugas,
# ada kata penting untuk jenis pertanyaan, dll
kata_penting = ["deadline", "tubes", "tucil", "kuis", "ujian", "pr"]
kata_help = ["bisa","lakukan","help","command","fitur"]
fitur = [
    "Menambahkan task baru",
    "Melihat daftar task",
    "Menampilkan deadline dari suatu task tertentu",
    "Memperbaharui task tertentu",
    "Menandai bahwa suatu task sudah dikerjakan",
    "Memberikan rekomendasi kata"
    ]

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

    for pattern in kata_penting:
        if (matcher.match(text, pattern)) :
            return "Ada kata penting"

    return "Tidak ditemukan kata penting"