from selenium import webdriver
driver = webdriver.Goggle()
driver.get('https://web.whatsapp.com/')
print("Login...\n")

name =input("isim gir: bay hacker")
count = int(input("sayı gir: 10 "))
msg = input("mesajınızı olusturun: merhaba herkese")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msgBox = driver.find_element_by_xpath('//*([@id="main"]/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    msgBox.send_keys(msg)
    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
    sendButton.click()