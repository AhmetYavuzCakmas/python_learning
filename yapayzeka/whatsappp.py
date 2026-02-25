from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/users/Downloads/chromedriver.exe")
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
for i in range(5):
    msg_box = driver.find_element_by_xpath("//div[@class='_2A8P4']//div[@contenteditable='true']")
    msg_box.send_keys(message)
    send_button = driver.find_element_by_xpath("//span[@data-icon='send']")
    send_button.click()
    time.sleep(1)