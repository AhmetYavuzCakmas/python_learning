import random

"""
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    if(int(n2)!=0):
        return n1 / n2
operations = {
     "+":add,
     "-":subtract,
     "*":multiply,
     "/":divide
}
"""
"""
cevap = "yes"
while(cevap != "no"):
    num1 = int(input("what is the first number? : "))

    for symbol in operations:
        print(symbol)
    operations_symbol = input("pick an operation from the line above: ")
    while( operations_symbol not in operations):
        print("Hatalı seçim yaptınız.")
        operations_symbol = input("pick an operation from the line above: ")
        
    num2 = int(input("what is the second number? : "))

    calculation_function = operations[operations_symbol]
    answer = calculation_function(num1,num2)
    print("{} {} {} = {}".format(num1,operations_symbol,num2,answer))
    cevap = input("devam etmek ister misiniz? (no/yes): ")
"""

"""
def calculator():
  print(logo)

  num1 = float(input("+"))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
"""

"""
def random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose "


  if user_score == computer_score:
    return "Draw "
  elif computer_score == 0:
    return "Lose, opponent has Blackjack "
  elif user_score == 0:
    return "Win with a Blackjack "
  elif user_score > 21:
    return "You went over. You lose "
  elif computer_score > 21:
    return "Opponent went over. You win "
  elif user_score > computer_score:
    return "You win "
  else:
    return "You lose "

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        #new_card = random_card()
        user_cards.append(random_card())#(new_card)
        computer_cards.append(random_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print("your cards: {}, current score: {}".format(user_cards,user_score))
        print("computer's first card :{}".format(computer_cards[0]))


        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            user_should_deal = input("kart çekim için 'y', pass için 'n': ")
            if user_should_deal == "y":
                user_cards.append(random_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(random_card())
        computer_score = calculate_score(computer_cards)


    print("elindeki son kart {} son scorun {}".format(user_cards,user_score))
    print("bilgisayarın son kartı {} son skor {}".format(computer_cards,computer_score))
    print(compare(user_score,computer_score))

while input("tekrardan oynamak ister misin: (y/n)" == "y"):
  
    play_game()

"""

"""
sayi = 1
def sayii():
    sayi = 2
    print("iç {}".format(sayi))

sayii()
print("dış {}".format(sayi))
"""
"""
def foo():
    i = 100
    return i
 
foo()
"""

"""
print("Sayı Tahmin Etme Oyununa Hoşgeldiniz.(0-100)")

pc_guess = random.randint(0,101)

zorluk = input("kolay mı zor olsun: ")
if zorluk == "kolay":
    sayi= 10
    while(0<sayi):
      guess = int(input("tahmin ettiğiniz sayıyı giriniz: "))
            
        
      if guess<pc_guess:
          print("tahmininizi yükseltin")
      elif pc_guess<guess:
          print("tahmininizi azaltın")
      else:
          print("tebrikler tahmininiz doğru çıktı: {}".format(guess))
          break
      sayi -=1
      print("kalan hakkınız: {}".format(sayi))
      if sayi == 0:
        print("tahmin hakkınız bitmiştir.")
        print("tahmin edilecek sayı: {}".format(pc_guess))

elif zorluk == "zor":
    sayi= 5
    while(0<sayi):
      guess = int(input("tahmin ettiğiniz sayıyı giriniz: "))
        
      if guess<pc_guess:
          print("tahmininizi yükseltin")
      elif pc_guess<guess:
          print("tahmininizi azaltın")
      else:
          print("tebrikler tahmininiz doğru çıktı: {}".format(guess))
          break
      sayi -=1
      print("kalan hakkınız: {}".format(sayi))
      if sayi == 0:
        print("tahmin hakkınız bitmiştir.")
        print("tahmin edilecek sayı: {}".format(pc_guess))
else:
    print("zorluk seviyesini doğru gir.")
"""

"""
EASY_LEVEL_TUNRS = 10
HARD_LEVEL_TUNRS = 5

def check_answer(guess,answer,turns):
    if guess>answer:
        print("too high")
        return turns -1 
    elif guess< answer:
        print("too low")
        return - 1
    else:
        print("you got it. the answer was {}".format(answer))

def set_difficulty():
    level =input("choose a difficulty. type 'easy' or 'hard': ")
    if level =="easy":
        return EASY_LEVEL_TUNRS
    else:
        return HARD_LEVEL_TUNRS
def game():
  print("welcome to the number guessing game.")
  print("1-100 arası sayı tahmini yapınız: ")
  answer = random.randint(1,101)
  print("pssst, the correct answer is {}".format(answer))
  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print("You have {} attempts remaining to guess the number.".format(turns))

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()
"""
"""
def a():
    for i in range(1,20):
        print(i)
a()
"""

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)
mutate([1,2,7,8,65,89])



 #MİLLİ PİYANGO BİLETLİ UYGULAMA random
#KULLANICI RASTEGEL 11 SAYI GİRİSN BUNULARIN BİR TC OLUPN OLMADIĞINIA KARAR VER
