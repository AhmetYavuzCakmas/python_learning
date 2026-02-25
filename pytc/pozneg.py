"""sayi = input("sayı giriniz: ")

if int(sayi) > 0 :
    print("sayınız pozitif")
elif int(sayi) == 0:
    print("sayınız sıfırdır")
elif int(sayi) < 0:
    print("sayınız negatif")
elif sayi != int(sayi):
    print("girdiğiniz sayi hatalı")"""

"""
sayi = input("sayı giriniz: ")

try:
    sayi = int(sayi)
    if sayi > 0:
        print("sayınız pozitif")
    elif sayi == 0:
        print("sayınız sıfırdır")
    elif sayi < 0:
        print("sayınız negatif")
except ValueError:
    print("Girdiğiniz sayı hatalı")"""

"""
sum = 0

for x in range(1,100,2):
    sum += x
print(sum)

"""

"""
sayi = int(input("kaç yıldız olsun? "))
yildiz = ""

for x in range(1,sayi + 1 ):
    yildiz = yildiz + "*"
    print(yildiz)

hilal = ""

for y in range(sayi,0,-1):
    hilal = y * "*"
    print(hilal)

    """

"""
sayi = int(input("sayı giriniz: "))

asalMi = True
for i in range(2,sayi):
    if (sayi % i == 0):
        asalMi = False
        break

if asalMi == True:
    print("asal")
else:
   print("asal değil")

"""

"""
def factoriyel(sayi):
    fac = 1
    if (sayi < 0):
        print("pozitif sayı girinizi")
    elif ( sayi == 0):
        print("sıfırın faktöriyeli 1 dir.")
    else:
        for i in range(1,sayi + 1):
            fac = fac * i
    print(str(sayi) + " nin factöriyeli" + str(fac) )
sayi = int(input("sayı giriniz: "))
factoriyel(sayi)
"""

"""
cumle = input("cümle giriniz: ")

kelimeler = cumle.split()

kelimeler.sort()
print(kelimeler)

for kelime in kelimeler:
    print(kelime)
"""

"""

print("a"*30)

print(bool(-10))
adi = "yaVuz"
adi1 = "8541236789"
adi2 = "çakmas"
print(adi[::-1])
print(adi.swapcase())
names = ["ali","cem","deniz","kulak"]

full_name = adi + " " + adi1 + " " + adi2
print(full_name)
print(full_name.upper())
print(full_name.capitalize())
print(full_name.title())
print(full_name.swapcase())
print(full_name.lower())
print("--".join(names))
#print(input("adın ne: ").islower())
print(full_name.find("u"))
print(full_name[full_name.lower().find("z"):])
print(full_name.lower().replace("çakmas","ahmet"))
"""
"""
age = input("yaşınızı giriniz: ")
 
if age.isdigit():
    age = int(age)
    age +=1
    print(age)
else:
    print("yaşınızı doğru giriniz...")
"""

"""
user_name = "ahmet"
adi = input("adınızı giriniz: ")

if(adi.lower() == user_name):
    print("başarılı bi şekilde giriş yaptınız.")
else:
    print("kullıcı adınız hatalı...")
"""

"""
age = input("yaşınızı giriniz: ")

if age.isdigit():
    if int(age) > 18:
        print("yaşınız 18 den büyük")
    else:
        print("yaşınız 18 den küçük.")
else:
    print("sayı giriniz lütfen!!!")
"""
"""
scor = input("skor giriniz: ")

if scor.isdigit():
    scor = int(scor)
    if 0<scor and scor<=100:
        if scor<45:
            result="kaldınız"
        elif 45<=scor<55:
            result = "geçer"
        elif 55<=scor<75:
            result = "orta"
        elif 75<=scor<85:
            result = "iyi"
        else:
            result = "pek iyi"
        print(result)
    else:
        print("0-100 arası sayı giriniz:")
else:
    print("sayı giriniz...")
"""

"""
age = input("yaşınızı giriniz: ")

age = int(age) if age.isdigit() else 0
print(f"{'*'*30}\n{age:^30}\n{'*'*30}")
"""
###########################################################

"""
items = [
    "css",
    "html",
    "python",
    "css",
    "django",
    "css",
    "bootstrap",
]

print(len(items))            #eleman sayısı bulma
print(bool(items))           #içinde öge var mı
print("python" in items)     #içinde sorgudaki öge var mı
"""

"""
item = input("dili sorgulatınız: ")
if item in items:
    print("{} dili var".format(item) ) # print(f"{item} dili var")
else:
    print("yok")
"""
"""
print("kaç adet var css: ",items.count("css")) #kaç adet var
print("python index: ", items.index("python")) #kaçıncı index te
print(items.remove("css")) #ilk gördüğü css siliniyor.
print(items.pop())      #liste içindeki son ögeyi çıkar ve gösterir
"""

"""
for i in range(1,100):
    if i % 5 == 0:
         print(i)
"""

"""
isimler ="ahmetyavuz"
for i in enumerate(isimler):
    print(i)   
"""

"""
user = ""
while len(user) <5:
    print("en az 5 karakterli adınızı giriniz:")
    user = input("Adınızı giriniz:")

    print(user)
"""

#short for ve if kullanımı

"""
is_active = True

if is_active:
    user_info = "active"
else:
    user_info = "deactive"
print(user_info)
"""

# YADA

"""
is_active = True
user_info ="active" if is_active else "deactive"
print(user_info) 
"""

#ÖRNEK 

"""
user_index = []

user_info_v1 = [item for item in range(1,10)]
print(user_info_v1)

user_info_v2 = [item * 10 for item in range(1,10)]
print(user_info_v2)

user_info_v3  = [item for item in range(1,10) if item % 2 !=0]
print(user_info_v3)

"""

"""
name = "ahmet"
def greetings():
    print("merhaba {}".format(name))

greetings()
"""

"""
def greetings(name):
    print("merhaba {}".format(name))

greetings("yavuz")
"""