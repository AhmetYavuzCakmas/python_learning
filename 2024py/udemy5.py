"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number (negatif veya pozitif olabilir):\n"))
"""

"""
def encrypt(plain_text,shift_amount):
    cipher_text= ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print("the encoded text is {}".format(cipher_text))

def decrypt(cipher_text,shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text +=alphabet[new_position]
    print("the decoded text is {}".format(plain_text))

if direction == "encode":
    encrypt(plain_text=text,shift_amount=shift)
elif direction=="decode":
    decrypt(cipher_text=text,shift_amount=shift)

encrypt(plain_text=text,shift_amount=shift)
"""

"""

def sifreleme(text,shift):
    bos_kelime = ""
    for harf in text:
        harf_yer = alphabet.index(harf)
        yeni_yer = shift + harf_yer
        bos_kelime += alphabet[yeni_yer]

print(bos_kelime)
"""

"""
def caesar(start_text,shift_amount,cipher_direction):
    end_text =""
    if cipher_direction == "decode":
            shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print("the {} text is {}".format(cipher_direction,end_text))
caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
"""

"""
country = input("ülke: ")
visits = int(input("kaç kere: "))
list_of_cities = input("hangi şehirler: ")
travel_log = [
    {
        "country":"france",
        "visits": 12,
        "cities": ["paeris","lille","dijon"]
    },
    {
        "country":"germany",
        "visits": 7,
        "cities": ["berlin","hamburg","stuttgart"]
    },
]

def add_new_country (name, times_visited,cities_visited):
    new_country = {}
    new_country["country"]= name
    new_country["visits"]=times_visited
    new_country["cities"]=cities_visited
    travel_log.append(new_country)

add_new_country(country,visits,list_of_cities)
print("ı have been to {} {} times".format(travel_log[2]['country'],travel_log[2]['visits']))
"""

"""

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
item_dict = {}
another = "evet"
while (another == "evet"):
    name = input("isminizi giriniz: ")
    price = input("enter the price for item: ")
    item_dict[name]=price
    another = input("başka var mı fiyat vercek (evet/hayır): ")

prices = list(item_dict.values())
max_price =int(max(prices))

print(logo)
print(max_price)
    
"""

"""
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}
bidding_finished = False
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner =bidder
  print("the winner is {} with a bid of ${} ".format(winner,highest_bid))

while not bidding_finished:
  name = input("what is your name?: ")
  price = int(input("what is your bid? : $"))
  bids[name] = price
  should_continue = input("are there any other bidders? type 'yer or no'.\n")
  if should_continue =="no":
    bidding_finished = True
    find_highest_bidder(bids)
"""

"""
def isim_soyisim(isim,soyisim):
    isim = isim.title()
    soyisim = soyisim.title()
    print("your name: {} and your surname: {}".format(isim,soyisim))

isim_soyisim("ali","cem")



def isim_soyisim(isim,soyisim):
    isim = isim.title()
    soyisim = soyisim.title()
    return "your name: {} and your surname: {}".format(isim,soyisim)

print(isim_soyisim("ali","cem"))
"""

"""
def format_name(f_name,l_name):
    if f_name =="" or l_name == "":
        return "you didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return  "your name: {} and your surname: {}".format(formated_f_name,formated_l_name)

print(format_name(input("adınız nedir: "),input("soyadınız nedir: ")))
"""

"""
def yil_mi(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("artık yıl")
            else:
                print("artık yıl değil")
        else:
            print("artik yil değil")
    else:
        print("artik yil değil")

def ayin_günleri():
    ayin_günleri = [31,28,31,30,31,30,31,31,30,31,30,31]
    if yil_mi == True:
        print("tariniz: {}.{}.{}".format(29,month-1,year))
    else:
        print("tariniz: {}.{}.{}".format(ayin_günleri[month-1],month,year))

    
year = int(input("yil girinz: "))
month = int(input("kaçinci aydasiniz: "))

ayin_günleri()
"""

def yil_mi(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                True
            else:
                False
        else:
            False
    else:
        False
def ayin_günleri(year,month):
    ayin_günleri = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2 and yil_mi(year):
        return 29
    else:
        return ayin_günleri[month-1]

year = int(input("yil: "))
month = int(input("ay: "))
days = ayin_günleri(year,month)
print(days)









