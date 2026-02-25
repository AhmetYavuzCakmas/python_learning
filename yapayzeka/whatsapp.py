import time
from selenium import webdriver

# Kullanıcının bilgileri
contact_name = "Ömer Faruk"
message_text = "Merhaba, nasılsın?, şuan mesaj botu yaptım"

# Selenium ayarları
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

# Kullanıcının manuel olarak giriş yapmasını sağlama
while True:
    try:
        chat_name = driver.find_element_by_xpath(f"//span[@title='{contact_name}']")
        chat_name.click()
        break
    except:
        time.sleep(10)

# 5 kez mesaj gönderme
for i in range(100):
    # Mesaj kutusunu bulma ve mesajı yazma
    message_box = driver.find_element_by_xpath("//div[@class='_2A8P4']")
    message_box.send_keys(message_text)

    # Gönderme butonunu bulma ve tıklama
    send_button = driver.find_element_by_xpath("//button[@class='_1E0Oz']")
    send_button.click()

    # 1 saniye bekleme
    time.sleep(1)

# Tarayıcıyı kapatma
driver.quit()