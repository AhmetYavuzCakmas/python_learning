import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Driver'ın oluşturulması
service = Service(r"C:\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Sayfanın açılması ve QR kodunun okutulması için beklenmesi
driver.get("https://web.whatsapp.com/")
input("Lütfen QR kodunu okutun ve giriş yapın. Giriş yaptıktan sonra herhangi bir tuşa basın...")

# Mesaj alıcısının seçilmesi
person_name = input("Mesaj göndermek istediğiniz kişinin adını veya grubun adını yazın: ")
search_box = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
search_box.click()
search_box.send_keys(person_name)
time.sleep(1)

# Mesajın yazılması ve gönderilmesi
message = input("Göndermek istediğiniz mesajı yazın: ")
text_box = driver.find_element_by_xpath('//div[@class="_3u328 copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]')
text_box.send_keys(message)
text_box.submit()
