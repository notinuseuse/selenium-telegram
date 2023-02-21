#importing the required libraries, 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

'''
    - the time.sleep() functions are used to give some time for the page to load
    successfully so the next command will be able to access the html structure without any errors
    - Login is manual
'''
#when you run this script in linux you might need the chrome webdriver
driver = webdriver.Chrome()

#fetchs the telegram login page
driver.get("https://web.telegram.org/k/")

#just a dummy input so the script will wait until you login and come back and press enter
d = input("press enter after you logged in: ")

#finding the telegram search bar
search_bar = driver.find_element(By.CLASS_NAME, "input-field-input")

#write the channel name 
channel_name = input("write the channel Name: ")

#fetching the channel
search_bar.send_keys(channel_name)
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

#it will get all the members in the channel, its not verified trying changing the class below
# and check 
chatlists = driver.find_elements(By.CLASS_NAME, "row-clickable")

#paste the text you want to send to the extracted users
text = input("write the text you wanna send: ")

d = input()
#it will iterate through the list of users got from the list and perform the below block of code on each
for chat in chatlists:
    time.sleep(3)
    chat.click()
    time.sleep(2)
    #it will find the message option and write the message into it and send it 
    text_message = driver.find_element(By.CLASS_NAME, "input-message-input")
    text_message.send_keys("hello ")
    text_message.send_keys(Keys.ENTER)
    time.sleep(4)
    #this will go one step back and try this same on the second name
    element = driver.find_element(By.CLASS_NAME, "sidebar-close-button")

