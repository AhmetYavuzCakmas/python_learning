import random
import math

"""
word_list = ["armut", "tantuni", "televizyon", "karavan", "muz", "kertenkele"]
random_word = random.choice(word_list)
word_len = len(random_word)
bos_kelime = "_" * word_len
print("kelime:  " + "_ " * word_len)

tahminler = []  # Kullanıcının yaptığı doğru tahminlerin listesi
yanlis_tahmin_sayisi = 0

while yanlis_tahmin_sayisi < 6 and "_" in bos_kelime:
    tahmin = input("harf giriniz: ").lower()

    if tahmin in tahminler:
        print("Bu harfi zaten tahmin ettiniz.")
        continue

    tahminler.append(tahmin)
    
    if tahmin in random_word:
        for i in range(len(random_word)):
            if random_word[i] == tahmin:
                bos_kelime = bos_kelime[:i] + tahmin + bos_kelime[i+1:]
        print("Tebrikler, doğru tahmin!")
    else:
        yanlis_tahmin_sayisi += 1
        print("Yanlış tahmin!")
    
    print("Kelime Durumu:", bos_kelime)
    print("Kalan Yanlış Tahmin Hakkı:", 6 - yanlis_tahmin_sayisi)

if "_" not in bos_kelime:
    print("Tebrikler, kelimeyi doğru tahmin ettiniz:", random_word)
else:
    print("Maalesef, kelimeyi bulamadınız. Doğru kelime:", random_word)
"""

"""
def greeting(name):
    print("hi, how are you {}".format(name))

greeting("yavuz")
"""
"""
h = int(input("yükseklik giriniz: "))
w = int(input("genişlik giriniz: "))
def paint_calm():
    need_paint = math.ceil((h*w)/5)
    print("ihtiyacınız olan boya kutu sayısı: {} ".format(need_paint))
paint_calm()    
"""


"""
def asal_sayi_bulma():
    sayi = int(input("sayı giriniz [1-100]: "))
    i = 2
    if not 0<sayi<=100:
        print("sayınızı 1 ila 100 aralığında seçiniz.")
    else:
        while (i <sayi):
            if sayi % i == 0:
                print("{} sayısı asal değildir".format(sayi))
                break
            else:
                print("{} sayısı asaldır.".format(sayi))
                break

            i += 1

asal_sayi_bulma()
"""

"""
def asal_sayi(number):
    is_prime = True
    for i in range(2,number):
        if number % i==0:
            is_prime = False

    if is_prime :
        print("sayınız asal sayıdır")
    else:
        print("sayınız asal değildir.")

n = int(input("sayı giriniz: "))
asal_sayi(number=n) 
"""
