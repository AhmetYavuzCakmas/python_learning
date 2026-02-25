from selenium import webdriver
import time

# Driver ayarları
driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
print("Lütfen QR kodunu okutun ve giriş yapın.")
input("Giriş yaptıktan sonra herhangi bir tuşa basın...")

# Mesaj atılacak kişiyi seçme
contact = "Ömer Faruk"
search_box = None
while search_box is None:
    try:
        search_box = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
    except:
        time.sleep(10)

search_box.click()
search_box.send_keys(contact)
time.sleep(10)

# Kişiyi seçme
person = None
while person is None:
    try:
        person = driver.find_element_by_xpath(f'//span[@title="{contact}"]')
    except:
        time.sleep(10)

person.click()
time.sleep(10)

# Mesaj gönderme
for i in range(5):
    message_box = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
    message_box.send_keys("Merhaba!")
    time.sleep(10)
    send_button = driver.find_element_by_xpath('//button[@class="_1U1xa"]')
    send_button.click()
    time.sleep(10)

print("Mesajlar başarıyla gönderildi.")
driver.quit()
