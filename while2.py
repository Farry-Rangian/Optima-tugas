import random
import time

kocokKartu = "ya"
daftarKartuPertama = []
daftarKartuKedua = []
riwayat = []

print("Selamat datang di permainan Kartu")
print("Jika kartu kamu lebih dari 21 maka kamu menang")
print("tetapi jika kartu kamu kurang dari 21 maka kamu kalah")
print('')

while kocokKartu == "ya": 
    print("Kocok Kartu...")
    time.sleep(2)
    kartuPertama = random.randint(1,13)
    kartuKedua = random.randint(1,13)

    total = kartuPertama + kartuKedua

    print(f'Kartu Pertama = {kartuPertama}')
    daftarKartuPertama.append(kartuPertama)
    print(f'Kartu Kedua = {kartuKedua}')
    daftarKartuKedua.append(kartuKedua)
    
    if total < 21:
        print("Anda Kalah :(")
        riwayat.append("Kalah")
    else:
        print("Selamat Anda Menang :)")
        riwayat.append("Menang")

    print('')
    print(f'Jumlah Kartu = {total}')
    print(f'Riwayat Kartu Pertama : {daftarKartuPertama}')
    print(f'Riwayat Kartu Kedua : {daftarKartuKedua}')
    print(f'Riwayat Permainan : {riwayat}')    

    kocokKartu = input("Bermain lagi (ya/tidak)? ")
    print(' ')

