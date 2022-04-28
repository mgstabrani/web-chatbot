import matcher
import re
import basisdata as db
import addTugas as at

kata_penting = db.getList_Kata_Penting()
kata_help = db.getList_Kata_Help()
kata_tampil_deadline = db.getList_Kata_Tampil_Deadline()
kata_task_selesai = db.getList_Kata_Task_Selesai()

def tampilDeadline(usrMsg):
    deadline = db.getList_Daftar_Tugas_Status(False)
    for i in range(len(deadline)):
        #General untuk tugas
        if matcher.match(usrMsg,"tugas"):
            if matcher.match(usrMsg,deadline[i][2].lower()):
                return deadline[i][1]
        #Spesifik, tucil, tubes atau pr
        else:
            if(matcher.match(usrMsg,deadline[i][2].lower()) and matcher.match(usrMsg,deadline[i][3].lower())):
                return deadline[i][1]

    return "Tidak ada deadline itu"

def tandaiTask(usrMsg):
    deadline = db.getList_Daftar_Tugas_Status(False)
    temp = re.findall(r'\d+', usrMsg)
    id = list(map(int, temp))
    if len(id) > 0:
        id = str(id[0])
    else:
        id = str(-1)
    for i in range(len(deadline)):
        if id == deadline[i][0]:
            db.upsert_Daftar_Tugas(deadline[i][0], deadline[i][1], deadline[i][2], deadline[i][3], deadline[i][4], True)
            return "Task ditandai selesai"
    return "Task tidak ditemukan"

def help():
    fitur = db.getList_Fitur()
    output = "[Fitur] <br>"
    for i in range(len(fitur)):
        output += " " + str(i+1) + ". " + fitur[i] + " <br>"
    output += "<br>"
    output += " [Daftar kata penting] <br>"
    for i in range(len(kata_penting)):
        output += " " + str(i+1) + ". " + kata_penting[i] + " <br>"
    return output

def process(usrMsg):
    result = at.ValidasiInput(usrMsg)
    if result =="-1":
        text = str(usrMsg).lower()

        #Menampilkan help
        for pattern in kata_help:
            if matcher.match(text, pattern) :
                return help()

        #Menandai task selesai
        for pattern in kata_task_selesai:
            if matcher.match(text, pattern) :
                return tandaiTask(text)    

        #Menampilkan tanggal deadline suatu task
        for pattern in kata_tampil_deadline:
            if matcher.match(text, pattern) :
                return tampilDeadline(text)

        kata_penting = db.getList_Kata_Help()
        kata_penting += db.getList_Kata_Tampil_Deadline()
        kata_penting += db.getList_Kata_Task_Selesai()

        kata_input = text.split(" ")
        found = False
        for kata in kata_input:
            for pattern in kata_penting:
                if (
                    kata not in kata_penting
                    and matcher.similarity(pattern, kata) >= 0.75
                ):
                    text = text.replace(kata, pattern)
                    found = True

        if found:
            return "Mungkin maksud kamu:\n" + text

        return "Maaf, pesan tidak dikenali"

    return result