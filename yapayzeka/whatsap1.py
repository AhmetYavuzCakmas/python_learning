
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

input("Lütfen QR kodunu taratın ve giriş yapın, ardından bir tuşa basın.")

# Arkadaşınızın ismi
friend_name = "Ömer Faruk"

# Mesajınız
message = "Merhaba, bu otomatik bir mesajdır!"

# Arkadaşınızın sohbet penceresini bulun
search_box = driver.find_element_by_xpath("//div[@contenteditable='true']")
search_box.send_keys(friend_name)
time.sleep(15)

person = driver.find_element_by_xpath("//span[@title='"+friend_name+"']")
person.click()

# Mesaj gönderme işlemini yineleyin
for i in range(100):
    msg_box = driver.find_element_by_xpath("//div[@class='_2A8P4']//div[@contenteditable='true']")
    msg_box.send_keys(message)
    time.sleep(1)
    send_button = driver.find_element_by_xpath("//button[@class='_1E0Oz']")
    send_button.click()