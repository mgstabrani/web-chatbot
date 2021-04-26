import matcher
import re

# mungkin kedepannya perlu dipisah si kata2 pentingnya
# kayak ada kata penting untuk jenis tugas,
# ada kata penting untuk jenis pertanyaan, dll
kata_penting = ["deadline", "tubes", "tucil", "kuis", "ujian", "pr"]

def process(usrMsg):
    text = str(usrMsg).lower()

    for pattern in kata_penting:
        if (matcher.match(text, pattern)) :
            return "Ada kata penting"

    return "Tidak ditemukan kata penting"