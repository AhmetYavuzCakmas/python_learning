import random

"""
word_list = ["armut","tantuni","televizyon","karavan","muz","kertenkele"]
random_word = random.choice(word_list)
word_len = len(random_word)
bos_kelime = []
for i in range(word_len):
    bos_kelime.append("_ ")
print(bos_kelime)
print("kelime:  "+"_ "*word_len)
i = 6

while (i < word_len):
    tahmin = input("harf giriniz: ").lower()
    print("kalan hakknız: "+i)
    for harf in random_word:
        if harf == tahmin:
            bos_kelime[i] = tahmin
        print(bos_kelime)   
    i -=1
print(bos_kelime)

"""


