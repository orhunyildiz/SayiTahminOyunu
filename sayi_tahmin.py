import random
import time

print("""
*************************************

Sayı Tahmin Oyunu

1 ile 1000 arasındaki sayıyı tahmin etmeye çalışın.

10 tahmin hakkınız bulunmaktadır.

*************************************
""")

rastgele_sayi = random.randint(1,1000)
tahmin_hakki = 10

while True:
    tahmin = int(input("Tahmininiz: "))

    if(tahmin < rastgele_sayi):
        print("Bilgiler Sorgulanıyor, Lütfen Bekleyin...")
        time.sleep(2)
        print("Daha yüksek bir sayı girin.")
        tahmin_hakki -= 1
        print("{} tahmin hakkınız kaldı.".format(tahmin_hakki))

    elif(tahmin > rastgele_sayi):
        print("Bilgiler Sorgulanıyor, Lütfen Bekleyin...")
        time.sleep(2)
        print("Daha düşük bir sayı girin.")
        tahmin_hakki -= 1
        print("{} tahmin hakkınız kaldı.".format(tahmin_hakki))

    else:
        print("Bilgiler Sorgulanıyor, Lütfen Bekleyin...")
        time.sleep(2)
        print("Tebrikler! Sayımız",rastgele_sayi)
        break

    if(tahmin_hakki == 0):
        print("Tahmin hakkınız bitti :(\nSayımız {} idi.".format(rastgele_sayi))
        break



