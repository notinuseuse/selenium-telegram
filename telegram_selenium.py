#importing the required libraries, 
from selenium import webdriver
#the colorama module is used to output colored text in the terminal
from colorama import init, Fore, Back
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
the time module is used to make delays in the middle of the script to give the elements 
enough time to load, although there is a selenium way of doing this, but becoz of some
errors we have used to the time module which is not really for this job but it works.
'''
import time

'''
    - the time.sleep() functions are used to give some time for the page to load
    successfully so the next command will be able to access the html structure without any errors
    - Login is manual
'''
init()

#when you run this script in linux you might need the chrome webdriver
driver = webdriver.Chrome()

#fetchs the telegram login page
driver.get("https://web.telegram.org/k/")


#just a dummy input so the script will wait until you login and come back and press enter
d = input("press enter after you logged in: ")

#finding the telegram search bar
search_bar = driver.find_element(By.CLASS_NAME, "input-field-input")

#write the channel name 
print(Fore.RED, "[WARNING]: Script takes the first group it sees after you type the name so make sure the name is Close to the group name", Fore.RESET)
group_name = input("write the group Name: ")
#fetching the channel
search_bar.send_keys(group_name)
search_bar.send_keys(Keys.ENTER)

#this is a wait because of the speed of my internet,it takes time to fetch the channel name
time.sleep(10)

#it will click the first result that will pop up after writing the name
button = driver.find_element(By.CLASS_NAME, "chatlist-chat-abitbigger")
button.click()

time.sleep(5)

#it will open the side bar of  channel which have the information like users list etc
channel = driver.find_element(By.CLASS_NAME, "content")
channel.click()


time.sleep(2)

#paste the text you want to send to the extracted users
text = input("write the text you wanna send: ")


members = int(input("Number Of Members in the group: "))
time.sleep(10)

#it will get the users of the group one by one and send them the message 
for chat in range(members):
    if chat == 0:
        continue
    time.sleep(4)
    chatlists = driver.find_element(By.XPATH,f'//*[@id="column-right"]/div/div/div[2]/div/div/div[3]/div[2]/div[1]/div/ul/a[{chat}]')
    #wait_2 = WebDriverWait(driver, 10)
    #element = wait_2.until(EC.element_to_be_clickable(chatlists))
    chatlists.click()

    #it will find the message option and write the message into it and send it 
    #text_message = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]')))
    time.sleep(5)
    text_message = driver.find_element(By.XPATH, '//*[@id="column-center"]/div/div[2]/div[4]/div/div[1]/div/div[8]/div[1]/div[1]')
    text_message.send_keys(text)
    text_message.send_keys(Keys.ENTER)
    time.sleep(4)
    #this will go one step back and try this same on the second name
    element = driver.find_element(By.XPATH, '//*[@id="column-center"]/div/div[2]/div[2]/div[1]/button')
    element.click()
    time.sleep(4)


