from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time
driver = webdriver.Chrome()
driver.get("https://web.telegram.org/k/")

"""
n =input('')
element = driver.find_element(By.CLASS_NAME, "c-ripple")
elem.clear()
elem.send_keys("pycon")"""
""""actions = ActionChains(driver)
actions.context_click(element)

actions.perform()
"
"""
"""elem.send_keys(Keys.RETURN)

element.click()
dropdown = Select(driver.find_element_by_id("my-dropdown"))

cn = input("continue : ")



enterelement = driver.find_elements(By.CLASS_NAME, "input-field-input")

enter_element = enterelement[1]
time.sleep(10)

enter_element.send_keys(Keys.BACK_SPACE)
enter_element.send_keys(Keys.BACK_SPACE)
'

#enter_number = driver.find_element(By.NAME, "39843100669469370")

key = input("telegram sent you a code on your mobile: ")"""
d = input("press enter after you logged in ")
cookie = driver.get_cookie("auth_token")
with open("cookie.txt", "w+") as m:
    m.write(str(cookie))



'''
enter_number.send_keys(key)
enter_number.send_keys(Keys.ENTER)

time.sleep(15)'''
search_bar = driver.find_element(By.CLASS_NAME, "input-field-input")

channel_name = input("write the channel Name: ")
search_bar.send_keys(channel_name)
search_bar.send_keys(Keys.ENTER)

time.sleep(10)

button =driver.find_element(By.CLASS_NAME, "chatlist-chat-abitbigger")
button.click()

time.sleep(5)
channel = driver.find_element(By.CLASS_NAME, "content")
channel.click()

while True:
    d = input("class name: ")
    class_name = f"{d}"
    chatlists = driver.find_element(By.CLASS_NAME, class_name)
    try:    
        channel.click()
        break
    except:
        print("didn't worked out")

time.sleep(2)
chatlists.click()
d = input()
print(chatlists)
for chat in chatlists:
    time.sleep(3)
    chat.click()
    time.sleep(2)
    text_message = driver.find_element(By.CLASS_NAME, "input-message-input")
    text = input("write the text")
    text_message.send_keys("hello ")
    text_message.send_keys(Keys.ENTER)


conti = input()