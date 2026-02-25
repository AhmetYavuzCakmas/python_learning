import random
 
"""
name = input(" isimleri giriniz(boşluklarla giriiniz): ")
names = name.split()
sayi = len(name)
if(sayi == 0):
    print("en az bir isim giriniz")
    input("isim giriniz: ")
else:
    random_index = random.randint(0,sayi-1)
    secilen_kisi = names[random_index]
    print("hesabı ödeyecek: "+secilen_kisi)
"""


"""
line1 = ["| |","| |","| |"]
line2 = ["| |","| |","| |"]
line3 = ["| |","| |","| |"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# Don't change the code above 
# Write your code below this row 


# Write your code above this row 
#Don't change the code below 
letter = position[0].lower()
abc =["a","b","c"]
letter_index = abc.index(letter)
number_index = int(position[1])-1
map[number_index][letter_index]= "|X|"

print("{}\n{}\n{}".format(line1,line2,line3))
"""



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

"""
a0 = rock
a1 = paper
a2 = scissors
"""

"""
games = [rock,paper,scissors]

choose1 = int(input("hangi seçenegi seçmek istersiniz (0 = taş, 1 = kağıt, 2 = makas ): "))
choose = choose1 % 3
pc_choose = random.randint(0,2)
if (choose == 0):
    print("your choose")
    print(games[choose])
elif(choose == 1):
    print("your choose")
    print(games[choose])
else:
    print("your choose")
    print(games[choose])

if (pc_choose == 0):
    print("choose of pc is rock")
    print(games[pc_choose])
elif(pc_choose == 1):
    print("choose of pc is paper")
    print(games[pc_choose])
else:
    print("choose of pc is scissors")
    print(games[pc_choose])


if(choose == 0):
    if(pc_choose == 0):
        print("you are equal")
    elif(pc_choose == 1):
        print("pc won")
    else:
        print("you won")
elif(choose == 1):
    if(pc_choose == 0):
        print("you won")
    elif(pc_choose == 1):
        print("you are equal")
    else:
        print("pc won")
if(choose == 2):
    if(pc_choose == 0):
        print("pc won")
    elif(pc_choose == 1):
        print("you won")
    else:
        print("you are equal")
"""

"""
sayi = int(input("kaç öğrenci gireceksiniz: "))
total_height = 0
i =0
while (i < sayi):
    student_heights = input("boyları cm cinsinden giriniz: ")
    total_height += int(student_heights)
    i += 1
print("toplam uzunlu {} cm.".format(total_height))
ortalama = total_height/sayi
print("ortalama " +str(ortalama))
"""

"""
notlar = [84,56,99,12,75,120,7888]

max = 0
for i in notlar:
    if (i > max):
        max = i
print(max)
"""

"""
sum = 0
for i in range(1,101):
    sum+= i
print(sum)
"""


"""
sayi1 = int(input("başlangiç sayıyı giriniz: "))
sayi2 = int(input("bitiş sayıyı giriniz: "))
cift_toplam = 0
for i in range(sayi1,sayi2):
    if (i%2 == 0):
        cift_toplam += i
print("{} ile {} arasındaki çift sayıların toplamı {} ".format(sayi1,sayi2,cift_toplam))
"""

"""
sayi_son = int(input("nereye kadar toplanmsını istiyorsunz: "))
toplam = 0
for i in range(2,sayi_son+1,2):
    toplam += i
print(toplam)
"""

"""
for i in range(1,100):

    if (i%15 == 0):
        print("fizzbuzz")
    elif(i%5==0):
        print("buzz")
    elif(i%3==0):
        print("fizz")
    else:
        print(i)
"""

"""
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
"""


"""
password = ""
for char in range(1, nr_letters + 1):
   password += random.choice(letters)

for char in range(1, nr_symbols + 1):
   password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
   password += random.choice(numbers)

print(password)

"""
"""
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print("Your password is: {}".format(password))
"""

"""
for i in range(5):
    print("kl")
"""
