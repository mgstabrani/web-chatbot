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

#text = "Deadline tubes 3 hari ke depan"


def daftar_katakunci(text):
    data = []
    textlist = text.split(" ")
    for kata in bd.getList_Kata_Penting()[1:]: 
        for i in range(len(textlist)):
            index = matcher.match( textlist[i].lower() ,kata.lower())
            if(index and len(kata)+1 >= len(textlist[i])+1 ):
                data.append(kata)
                break
        if(index):
            break

    for kata in bd.getList_Kata_Tampil_Deadline():
        for i in range(len(textlist)):
            index = matcher.match( textlist[i].lower(),kata.lower())
            if(index):
                data.append(kata)
                

    return data

def ValidasiInput(text):
    if(matcher.match(str(text).lower(),"diundur")):
        return diundurTask(text)
    
    else:
        data = daftar_katakunci(text)
        if len(data) <= 2 and "antara" not in data and "depan" not in data and "deadline" not in data:
            if(len(data)== 1):
                if("tanggal" not in data and "pada" not in data):
                    return """Gunakan kata ["tangal", "pada"] sebelum tanggal"""
                else:
                    return """Gunakan kata ["tubes", "tucil", "kuis", "ujian", "pr"]"""
            else:
                return add(text)

        elif("antara" in data):
            if("tubes" in data):
                return antaraTanggal_Jenis(text,"tubes")
            elif("tucil" in data):
                return antaraTanggal_Jenis(text,"tucil")
            elif("kuis" in data):
                return antaraTanggal_Jenis(text,"kuis")
            elif("ujian" in data):
                return antaraTanggal_Jenis(text,"ujian")
            elif("pr" in data):
                return antaraTanggal_Jenis(text,"pr")
            else:
                return antaraTanggal(text)
          
        elif("depan" in data):
            
            if ("hari" in data):
                if("tubes" in data):
                    return haritask_Jenis(text,"tubes")
                elif("tucil" in data):
                    return haritask_Jenis(text,"tucil")
                elif("kuis" in data):
                    return haritask_Jenis(text,"kuis")
                elif("ujian" in data):
                    return haritask_Jenis(text,"ujian")
                elif("pr" in data):
                    return haritask_Jenis(text,"pr")
                else:
                    return haritask(text)
            elif("minggu" in data):
                if("tubes" in data):
                    return minggutask_Jenis(text,"tubes")
                elif("tucil" in data):
                    return minggutask_Jenis(text,"tucil")
                elif("kuis" in data):
                    return minggutask_Jenis(text,"kuis")
                elif("ujian" in data):
                    return minggutask_Jenis(text,"ujian")
                elif("pr" in data):
                    return minggutask_Jenis(text,"pr")
                else:
                    return minggutask(text)
            else:
                return "-1"

        elif ("deadline" in data):
            if("hari" in data):
                if("tubes" in data):
                    return hariIni_Jenis("tubes")
                elif("tucil" in data):
                    return hariIni_Jenis("tucil")
                elif("kuis" in data):
                    return hariIni_Jenis("kuis")
                elif("ujian" in data):
                    return hariIni_Jenis("ujian")
                elif("pr" in data):
                    return hariIni_Jenis("pr")
                else:
                    return hariIni()
                
            elif("sejauh" in data):
                if("tubes" in data):
                    return sejauhIni_Jenis("tubes")
                elif("tucil" in data):
                    return sejauhIni_Jenis("tucil")
                elif("kuis" in data):
                    return sejauhIni_Jenis("kuis")
                elif("ujian" in data):
                    return sejauhIni_Jenis("ujian")
                elif("pr" in data):
                    return sejauhIni_Jenis("pr")
                else:
                    return sejauhIni()
            else:
                return "-1"
        else:
            return "-1"

def haritask_Jenis(text,jenis):
    found = False
    textlist = text.split(" ")
    for i in range(len(textlist)):
        index = matcher.match( textlist[i].lower() ,"hari")
        if(index):
            found = True
            N = int(textlist[i-1])
            dateEnd =nHariKedepan(N)
            output = "[Menampilkan " + jenis +" "+ str(N) +" hari ke depan]<br>"
            daftar =bd.getList_Daftar_Tugas_Jenis_tgl(jenis,datetime.date.today(),dateEnd,0)
            
            if(len(daftar)== 0):
                return "Tidak ada "+ jenis+ " "+ str(N) +" hari ke depan"
            for tugas in daftar:
                output += "<br>(ID: " +tugas[0] +")" + tugas[1],tugas[2],tugas[3] +"<br>"
            return output

    if(not found):
        return "-1"

def haritask(text):
    found = False
    textlist = text.split(" ")
    for i in range(len(textlist)):
        index = matcher.match( textlist[i].lower() ,"hari")
        if(index):
            found = True
            N = int(textlist[i-1])
            dateEnd =nHariKedepan(N)
            output = "[Menampilkan Tugas " + str(N) +" hari ke depan]<br>"
            daftar =bd.getList_Daftar_Tugas_tgl(datetime.date.today(),dateEnd,0)
            
            if(len(daftar)== 0):
                return "Tidak ada "+ "deadline"+ " "+ str(N) +" hari ke depan"
            for tugas in daftar:
                output += "(ID: " +tugas[0] +") " + tugas[1]+" "+ tugas[2] +" "+tugas[3] +" <br>"
            return output
    if(not found):
        return "-1"

def minggutask(text):
    found = False
    textlist = text.split(" ")
    for i in range(len(textlist)):
        index = matcher.match( textlist[i].lower() ,"minggu")
        if(index):
            found = True
            N = int(textlist[i-1])
            dateEnd =nHariKedepan(N*7)
            output = "[Menampilkan Tugas " + str(N) +" minggu ke depan]<br>"
            daftar =bd.getList_Daftar_Tugas_tgl(datetime.date.today(),dateEnd,0)
            
            if(len(daftar)== 0):
                return "Tidak ada "+ "deadline"+ " "+ str(N) +" minggu ke depan"
            for tugas in daftar:
                output += "(ID: " +tugas[0] +") " + tugas[1]+" "+tugas[2]+" "+tugas[3] +" <br>"
            return output


    if(not found):
        return "-1"

def minggutask_Jenis(text,jenis):
    found = False
    textlist = text.split(" ")
    for i in range(len(textlist)):
        index = matcher.match( textlist[i].lower() ,"minggu")
        if(index):
            found = True
            N = int(textlist[i-1])
            dateEnd =nHariKedepan(N*7)
            output = "[Menampilkan "+jenis +" " + str(N) +" minggu ke depan]<br>"
            daftar =bd.getList_Daftar_Tugas_Jenis_tgl(jenis,datetime.date.today(),dateEnd,0)

            if(len(daftar)== 0):
                return "Tidak ada "+ jenis+ " "+ str(N) +" minggu ke depan"
            for tugas in daftar:
                output += "(ID: " +tugas[0] +")" + tugas[1] + " "+ tugas[2]+ " "+ tugas[3] +"<br>"
            return output

    if(not found):
        return "-1"

def nHariKedepan(N):
    base = datetime.datetime.today()
    date_list = [base + datetime.timedelta(days=x) for x in range(N+1)]
    dateEND = date_list[len(date_list)-1].date()
    return dateEND

def hariIni():
    output = "[Menampilkan tugas"  +" hari ini]<br>"
    daftar =bd.getList_Daftar_Tugas_tgl(datetime.date.today(),datetime.date.today(),False)
    if(len(daftar)== 0):
        return "Tidak ada deadline hari ini"
    for tugas in daftar:
        output += "(ID: " +tugas[0] +") " + tugas[1] +" "+ tugas[2] +" "+tugas[3] +" <br>"
    return output
    
def hariIni_Jenis(jenis):
    output = "[Menampilkan "+jenis +" hari ini]<br>"
    daftar = bd.getList_Daftar_Tugas_Jenis_tgl(jenis,datetime.date.today(),datetime.date.today(),False)
    if(len(daftar)== 0):
        return "Tidak ada deadline "+jenis+" hari ini"
    for tugas in daftar:
        output += "(ID: " +tugas[0] +") " + tugas[1] +" "+tugas[2]+" "+tugas[3] +" <br>"
    return output

def sejauhIni():
    output = "[Menampilkan tugas"  +" sejauh ini]<br>"
    daftar = bd.getList_Daftar_Tugas_tglMulai(datetime.date.today(),False)
    if(len(daftar)== 0):
        return "Tidak ada deadline  sejauh ini"
    for tugas in daftar:
        output += "(ID: " +tugas[0] +") " + tugas[1] +" "+ tugas[2] +" "+ tugas[3] +" <br>"
    return output

def sejauhIni_Jenis(jenis):
    output = "[Menampilkan "+jenis +" sejauh ini]<br>"
    daftar = bd.getList_Daftar_Tugas_Jenis_tglMulai(jenis,datetime.date.today(),False)
    if(len(daftar)== 0):
        return "Tidak ada deadline "+jenis+" sejauh ini"
    for tugas in daftar:
        output += "(ID: " +tugas[0] +") " + tugas[1] +" "+tugas[2] +" "+ tugas[3] +" <br>"
    
    return str(output)

def antaraTanggal(text):
    data = []
    textlist = text.split(" ")
    for i in range(len(textlist)):
        index = matcher.match( textlist[i].lower() ,"antara")
        if(index):
            if len(textlist[i+1]) > 2:
                data.append(textlist[i+1])
                data.append(str(textlist[i+3]).replace("?",""))

            else:
                bulan_int = bulan.get(textlist[i+1].lower())
                tanggal = textlist[i+1] +"/"+ bulan_int +"/"+textlist[i+3]
                data.append(tanggal)

                bulan_int = bulan.get(textlist[i+3].lower())
                tanggal = textlist[i+1] +"/"+ bulan_int +"/"+textlist[i+3]
                data.append(tanggal)

            break
    if (len(data) == 2):
        (tgl,bln,th) = re.split("/", data[0])
        date1 = datetime.date(int(th),int(bln),int(tgl))
        (tgl,bln,th) = re.split("/", data[1])
        date2 = datetime.date(int(th),int(bln),int(tgl))
        daftar =bd.getList_Daftar_Tugas_tgl(date1,date2,False)
        if(len(daftar)== 0):
            return "Tidak ada deadline antara "+  str(date1) +" - "+ str(date2)

        output = "[Menampilkan deadline antara "+  str(date1) +" - "+ str(date2) +"] <br>"
        for tugas in daftar:
            output += "(ID: " +tugas[0] +") " + tugas[1] +" "+ tugas[2] +" "+tugas[3] +" <br>"

        return output

    else:
        return "-1"

def antaraTanggal_Jenis(text, jenis):
    data = []
    textlist = text.split(" ")
    for i in range(len(textlist)):
        index = matcher.match( textlist[i].lower() ,"antara")
        if(index):
            if len(textlist[i+1]) > 2:
                data.append(textlist[i+1])
                data.append(str(textlist[i+3]).replace("?",""))

            else:
                bulan_int = bulan.get(textlist[i+1].lower())
                tanggal = textlist[i+1] +"/"+ bulan_int +"/"+textlist[i+3]
                data.append(tanggal)

                bulan_int = bulan.get(textlist[i+3].lower())
                tanggal = textlist[i+1] +"/"+ bulan_int +"/"+textlist[i+3]
                data.append(tanggal)

            break
    if (len(data) == 2):
        (tgl,bln,th) = re.split("/", data[0])
        date1 = datetime.date(int(th),int(bln),int(tgl))
        (tgl,bln,th) = re.split("/", data[1])
        date2 = datetime.date(int(th),int(bln),int(tgl))
        # rubah rertun list
        output = "[Menampilkan daftar "+ jenis + str(date1) +" - "+ str(date2) +"] <br>"
        daftar = bd.getList_Daftar_Tugas_Jenis_tgl(jenis,date1,date2,False)
        if(len(daftar)== 0):
            return "Tidak ada "+jenis+" antara "+ str(date1) +" - "+ str(date2)

        for tugas in daftar:
            output += "(ID: " +tugas[0] +") " + tugas[1]+" "+tugas[2]+" "+ tugas[3] +" <br>"

        return output
    else:
        return "-1"

def diundurTask(usrMsg):
    found = False
    text = str(usrMsg).split(" ")
    for i in range(len(text)):
        if(matcher.match(text[i],"diundur")):
            
            if(len(text[i+2]) > 2):
                tanggal = text[i+2]
                    
            else:
                bulan_int = bulan.get(text[i+3].lower())
                tanggal = text[i+2] +"/"+ bulan_int +"/"+text[i+4]

            (tgl,bln,th) = re.split("/", tanggal)
            date = datetime.date(int(th),int(bln),int(tgl))
            bd.update_Daftar_Tugas(text[i-1],date)
            found = True
            output = "Deadline Tugas ID "+ text[i-1] +"<br>"
            output += "berhasil diperbarui menjadi " +str(date) +" <br>"
            return output
    if(found == False):
        return "-1"
    
def add(text):
    data = []
    textlist = text.split(" ")
    #jenis  matkul tugas  dan tugas
    for kata in bd.getList_Kata_Penting(): 
        for i in range(len(textlist)):
            index = matcher.match( textlist[i].lower() ,kata.lower())
            if(index):
                data.append(textlist[i+1])
                data.append(str(textlist[i]).lower())
                nama = textlist[i+2]
        
                pada_tgl = ["pada","tanggal"]
                for kata2 in pada_tgl:
                    for k in range(len(textlist[i+2+1:])):
                        index2 = matcher.match( textlist[i+2+k].lower() ,kata2.lower())
                        if(index2):
                            for j in range(k-1):
                                nama += " "+ textlist[i+2+j+1]
                            break
                
                    if(index2):
                        break

                data.append(nama)

                break
        if(index):
            break

    #tanggal Tugas
    for kata in bd.getList_Kata_Tampil_Deadline():
        for i in range(len(textlist)):
            index = matcher.match( textlist[i].lower(),kata.lower())
            if(index):
                if(len(textlist[i+1]) > 2):
                    data.insert(0,textlist[i+1])
                    
                else:
                    bulan_int = bulan.get(textlist[i+2].lower())
                    tanggal = textlist[i+1] +"/"+ bulan_int +"/"+textlist[i+3]
                    data.insert(0,tanggal)       
                break
        if(index is not False):
            break

    if(len(data)== 4):
        (tgl,bln,th) = re.split("/", data[0])
        date = datetime.date(int(th),int(bln),int(tgl))
        N = len(bd.getList_Daftar_Tugas())+1
        bd.upsert_Daftar_Tugas(N,date,data[1],data[2],data[3],False)
        output = "[ ===== Berhasil Ditambahkan =====]<br>"
        output += "(ID: " +str(N) +") " + str(date)+" "+data[1]+" "+data[2]+" "+data[3] +"<br>"
        return output
    else:
        return "-1"


#add(text)
#print( bd.getList_Daftar_Tugas_tglMulai(datetime.date.today(),False))
#print(ValidasiInput(text))
        

        
    
