import random
import time

kocokKartu = "ya"

while kocokKartu == "ya":
    print("Selamat datang di permainan Kartu")
    print("Jika kartu kamu lebih dari 21 maka kamu menang")
    print("tetapi jika kartu kamu kurang dari 21 maka kamu kalah")
     
    print("Kocok Kartu...")
    time.sleep(2)
    kartuPertama = random.randint(1,11)
    kartuKedua = random.randint(1,11)

    total = kartuPertama + kartuKedua

    print(f'Kartu Pertama = {kartuPertama}')
    print(f'Kartu Kedua = {kartuKedua}')
    
    if total < 21:
        print("Anda Kalah :)")
    else:
        print("Selamat Anda Menang :)")

    print(f'Total = {total}')

    kocokKartu = input("Bermain lagi? ")

