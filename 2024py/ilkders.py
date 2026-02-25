#değişken tanımlama kuralları
#rakam ile başlamaz

"""
x,y,name,isName = (1,5,"yavuz",True)
print(x,y,name)
print(name)
"""


"""
musteriAdi= "taha "
musteriSoyAdi = "polat"
adSoyad = musteriAdi + musteriSoyAdi 
print(musteriSoyAdi,musteriAdi,adSoyad)
"""


"""
x = input("1. sayi: ")
y = input("2. sayi: ")
toplam = int(x) +int(y)
print("toplamınız: "+ str(toplam))
"""


"""
yaricap = input("yarıçapı giriniz: ")
pi = 3.14

daireAlanı   = int(pi * int(yaricap) **2)
dairaCevresi = int(2*pi*int(yaricap))
print("daire alanı: "+str(daireAlanı))
print("dairenin çevresi: "+str(dairaCevresi))
"""


"""
name = "taha"
surname = "polat"

print("your name is {} {}".format(name,surname))
print("my name is {1} {0} ".format(name,surname)) #süslü parantez içine index yazılır
print("my name is {s} {n} ".format(n = name,s = surname))
print("my name is {n} {s} and ı am {a} years old ".format(n = name,s = surname,a = "25"))

print(f"my name is {name} {surname} ")
"""


"""
website = "http://www.sadikturan.com"
course = "Python Kursu: taha polat ile medresede kalıyoruz."

length  = len(course)
reult = len(course)

result = website[7:10]

result = website[length-3:length]
result = website[-3:]

result = course[:15] + course[length-15:]
result = course[-15:]

s = 5
result = website[s+2:]

result = course[::-1]

result = "12345"*5
print(result[::5])
"""


"""
message = " sdafa.  fa.  gegg. g g g.  "

message = message.upper() # tüm harfleri büyük yazar
message = message.lower() # tüm harfleri küçük yazar
message = message.title() #her kelimenin başının büyültür
message = message.capitalize() #cümlenin ilk harfini büyük yazar
message = message.strip() #baştaki ve sondaki boşlukları siler
message = message.split() #dizi halinde kelimeleir ayırır split = bölmek
message = message.split(".") # noktalı kısımlara ayırma
message ="---".join(message) # split ile dizi haline getridiğimiz kelimeleri naısl birleştirir
index = message.find("fa") # fa kelimesinin kaçıncı indekte olduğunu bul
"""


"""
message1 = " sdafa.  fa.  gegg. g g gj.  "
isfound = message1.startswith("s")
isFound = message1.endswith(" ") # sonu neyle bitiyor
print(isfound)
"""


"""
message = "ahmet yavuz çakmas taha polat "

message = message.replace("ahmet","maruf")
message1 = message.replace("a","salih").replace("i","a")
print(message1)
"""


"""
message = message.center(50,"*") #sağdan soldan * koyar toplam 50 karakter den
"""


"""
message = [(5,8),(1,6)]
print(message[0][1])
"""


"""
def yazdir(kelime,adet):
    i = 1
    while ( i<=adet):
        print(kelime)
        i += 1

yazdir("a",5)
"""

"""
def listeEkle(*params):
    liste = []
    for i in params:
        liste.append(i)
    print(liste)

listeEkle("f","fe","rwfwef","fe")
"""

"""
ilkSayi = input("sayı giriniz: ")
sonSayi = input("sayı giriniz: ")
"""

"""
def asalSayiBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2 +1):
        if sayi > 1:
            for i in range(2,sayi):
                if(sayi % i == 0):
                    break
            else:
                print(sayi)

sayi1 = int(input("sayı 1: "))
sayi2 = int(input("sayı 2: "))     

asalSayiBul(sayi1,sayi2)
"""



"""
def tamBolenBulma(sayi):
    list = []
    i = 1
    while(i<=sayi):
        if (sayi % i==0):
            list.append(i)
        i += 1
    print(list)
sayiYeni = int(input("sayı giriniz: "))
tamBolenBulma(sayiYeni)
"""




 