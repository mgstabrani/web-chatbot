import matcher
import re
import basisdata as bd
import datetime

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

text = "ingatkan tubes IF22020 stima pada 30 april 2021"
def add(text):
    data = []
    textlist = text.split(" ")
    #jenis  matkul tugas  dan tugas
    for kata in bd.getList_Kata_Penting(): 
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
    for kata in bd.getList_Kata_Tampil_Deadline():
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
                #print(data)
                break
        if(index is not False):
            break
    #tinggal menambahkan ke  data base
    (tgl,bln,th) = data[0].split("/")
    date = datetime.date(int(th),int(bln),int(tgl))
    bd.upsert_Daftar_Tugas(len(bd.getList_Daftar_Tugas())+1,date,data[1],data[2],data[3],False)


add(text)
        

        
    