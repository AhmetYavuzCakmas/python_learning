from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# chromedriver.exe dosyasının yolu
path = r"C:\chromedriver.exe"

# Service objesi oluşturarak chromedriver'ı başlatmak
service = Service(path)
driver = webdriver.Chrome(service=service)

# Whatsapp Web sayfasını açmak
driver.get("https://web.whatsapp.com/")

# QR kodunun okunup sayfanın yüklenmesi için beklemek
input("Giriş yaptıktan sonra herhangi bir tuşa basın...")

# Mesaj gönderilecek kişi ve mesaj metnini belirlemek
person_name = "Ömer"
message = "Hello, John! This message is sent using Python."

# Kişinin adını aramak
search_box = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
search_box.send_keys(person_name)
search_box.submit()

# Kişinin sohbet penceresini açmak
person = driver.find_element_by_xpath(f'//span[@title="{person_name}"]')
person.click()

# Mesaj kutusuna tıklamak ve mesajı göndermek
msg_box = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
msg_box.send_keys(message)
button = driver.find_element_by_xpath('//button[@class="_1U1xa"]')
button.click()
