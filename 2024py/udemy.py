"""print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")
print('hjytj\"g4vb\"j ty')"""


#print("hello "+input("what is your name? ")) 


"""
num1 = int(input("kaç kere gireceğiniz sayiyi giriniz: "))
i = 0
carpim = 1
while (i< num1):
    num2 = int(input("sayialri giriniz: "))
    carpim *= num2
    i +=1
print(carpim)
"""


"""
sayi = input("sayı giriniz: ")
i = 0
toplam = 0
while (i < len(sayi)):
    rakam = sayi[i]
    toplam += int(rakam)
    i += 1
print(toplam)
"""

"""
age = input("yasinizi giriniz: ")
kalan_omur= 90 -int(age)
kalan_hafta = kalan_omur * 52
print(f'kalan ömrünüzden {kalan_hafta} haftaniz kaldi')

"""

"""
print("Hosgeldiniz Restaurantta. ")
amount =input("ne kadar tuttu? ")
bahsis = input("ne kadar bahşiş vermek istersiniz (12, 15, 20): ")
person = input("kaç kişiye bölelim : ")

hesap = float((float(account) + (int(bahsis) * 0.01)) / int(person))
print("kişi başı ödemeniz gereken tutar {} tl".format(hesap)) 

"""

"""
print("Hosgeldiniz Restaurantta. ")
amount =input("ne kadar tuttu? ")
bahsis = input("ne kadar bahşiş vermek istersiniz (12, 15, 20): ")
person = input("kaç kişiye bölelim : ")

hesap = float((float(amount) + (int(bahsis) * 0.01)) / int(person))
hesap = "{:.2f}".format(hesap) # ondalıklı sayıyı ondalık kısmını 2 basamaklıya çevirdik.
print("kişi başı ödemeniz gereken tutar {} tl".format(hesap)) 

"""

"""
sayi = input("Sayi giriniz: ")
if(int(sayi)>=0):
    if(int(sayi) % 2 == 0):
        print(sayi+" sı çifttir")
    else:
        print(sayi+" sı tek tir")
else:
    print("negatif sayidan büyük sayi giriniz: ")
"""

"""
boy = int(input("boyunuz cm cinsinden giriniz: "))
ucret = 0
if (boy >=120):
    print("boyunuz yeterli uzunlukta")
    age = int(input("yasinizi girniz: "))
    
    if(age<55 and age>45):
        print("ÜCRET: "+str("0")+ "$")
    elif(12<age<=18):
        ucret+=9
        print("ÜCRET: "+str(ucret)+ "$")
    elif (age >18 ):
        ucret +=11
        print("ÜCRET: "+str(ucret)+ "$")
    else:
        ucret +=7
        print("ÜCRET: "+str(ucret)+ "$")
    foto = input("fotoğraf ister misiniz?(y/n) ")
    if(foto == "y"):
        print("ÜCRET: "+str(ucret+3)+ "$")
    else:
        print("ÜCRET: "+str(ucret)+ "$")
else:
    print("boyunuz yetmemektedir.")

"""    

"""
year = int(input("yıl giriniz: "))
print("şimdi girdiğiniz sayının artık yıl olup olmadığını hesaplayacağız.")

if(year % 4 == 0 & year % 100 == 0 & year % 400 == 0): 
    print(str(year) +" yılı artık yıldır")
else:
    print(str(year)+" yılı artık yıl değildir.")
"""

"""
print("Aşk hesaplayıcısı senin aşk puanını hesaplıyor...")
name1 = input("ilk isim: ")
name2 = input("ikinci isim: ")

isim_listesi1 = name1.split()
# İki kelimeyi birleştir
birlesik_isim1 = "".join(isim_listesi1)

isim_listesi2 = name2.split()
# İki kelimeyi birleştir
birlesik_isim2 = "".join(isim_listesi2)


birlesik_isim= birlesik_isim2 + birlesik_isim1
kucuk_isim= birlesik_isim.lower()
t = kucuk_isim.count("t")
r = kucuk_isim.count("r")
u = kucuk_isim.count("u")
e = kucuk_isim.count("e")

ilk_sayi = t+r+u+e

l = kucuk_isim.count("l")
o = kucuk_isim.count("o")
v = kucuk_isim.count("v")
e = kucuk_isim.count("e")

ikinci_sayi = l+o+v+e
love_scor = str(ilk_sayi)+str(ikinci_sayi)
print(kucuk_isim)
print("aşk puanınız : "+love_scor)
"""

"""
isim1 = input("İlk ismi girin: ")
isim2 = input("İkinci ismi girin: ")

birlesik0_isim = isim1.split()
birlesik1_isim = isim2.split()
# İsimleri boşlukla birleştir
birlesik_isim = ''.join([isim1, isim2])

# Sonucu yazdır
print("Birleştirilmiş isim:", birlesik_isim)
"""

"""
# Kullanıcıdan iki kelimeyi tek seferde al
isimler = input("İki kelimeyi aralarında boşluk bırakarak girin: ")

# Girdiyi boşlukla ayırarak iki kelimeye bölelim
isim_listesi = isimler.split()

# İki kelimeyi birleştir
birlesik_isim = "".join(isim_listesi)

# Sonucu yazdır
print("Birleştirilmiş isim:", birlesik_isim)
"""

import random

"""
random_sayi =random.randint(1,50)
print(random_sayi)
"""

"""
sayi =random.random()
print(sayi)
"""

#yazı tura oyunu
"""
tahmin = input("yazı veya tura girniz(yazı için = 1/tura için = 0): ")
rastgele_sayi = random.randint(1,3)
if (rastgele_sayi==int(tahmin)):
    print("siz kazandınız: "+tahmin)
else:
    print("kaybettinşiz çıkan sonuç: "+str(rastgele_sayi))
"""

"""
tahmin = random.randint(1,2)
if (tahmin == 1):
    print("yazı")
else:
    print("tura")
"""

