import matcher
import re
from feature import kata_penting, kata_help, kata_tampil_deadline, kata_task_selesai,fitur

bulan = {
    "januari": "01",
    "febuari": "02",
    "maret": "03",
    "april": "04",
    "mei":"05",
    "juni":"06",
    "juli":"07",
    "agustus":"08",
    "september":"09",
    "oktober":"10",
    "november":"11",
    "desember":"12"
}

text = "ingatkan tubes IF22020 matem pada 2 april 2021"
def add(text):
    data = []
    textlist = text.split(" ")
    #jenis  matkul tugas  dan tugas
    for kata in kata_penting: 
        for i in range(len(textlist)):
            index = matcher.match( textlist[i].lower() ,kata.lower())
            if(index is not False):
                data.append(textlist[i+1])
                data.append(textlist[i])
                data.append(textlist[i+2])

                textlist.remove(textlist[i])
                textlist.remove(textlist[i])
                textlist.remove(textlist[i])
                break
        if(index is not False):
            break

    #tanggal Tugas
    for kata in kata_tampil_deadline:
        for i in range(len(textlist)):
            index = matcher.match( textlist[i].lower(),kata.lower())
            if(index is not False):
                if(len(textlist[i+1]) > 2):
                    data.insert(0,textlist[i+1])
                    textlist.remove(textlist[i])
                    textlist.remove(textlist[i])
                else:
                    bulan_int = bulan.get(textlist[i+2])
                    tanggal = textlist[i+1] +"/"+ bulan_int +"/"+textlist[i+3]
                    data.insert(0,tanggal)
                    textlist.remove(textlist[i])
                    textlist.remove(textlist[i])
                    textlist.remove(textlist[i])
                    textlist.remove(textlist[i])

                # print(textlist)
                print(data)
                break
        if(index is not False):
            break

    #tinggal menambahkan ke  data base

add(text)
        

        
    