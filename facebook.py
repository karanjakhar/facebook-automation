import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


email = input('Enter email id : ')
passwd = input('Enter password : ')


driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')
print('page loaded')
driver.find_element(By.XPATH,'//*[@id="email"]').send_keys(email)
print('email is done')
driver.find_element(By.XPATH,'//*[@id="pass"]').send_keys(passwd)
print('pass is done')

driver.find_element(By.XPATH,'//*[@id="loginbutton"]').click()
print('login is done')

#driver.execute_script("var elems = document.getElementsByClassName('UFILikeLink _4x9- _4x9_ _48-k');for(var i= 0;i<elems.length;i++){elems[i].click();}");
print('scrolled first')
i = 2
scroll_pause_time = 5
last_height = driver.execute_script("return document.body.scrollHeight ")

while True:
    time.sleep(scroll_pause_time)
    driver.execute_script("window.scroll(0,document.body.scrollHeight);")
    #time.sleep(10)
    #driver.execute_script("var elems = document.getElementsByClassName('UFILikeLink _4x9- _4x9_ _48-k');function sleep(seconds){var waitUntil = new Date().getTime() + seconds*1000;while(new Date().getTime() < waitUntil) true;}for(var i= 0;i<elems.length;i++){sleep(15);elems[i].click();}");
    print('scrolled : ',i," time.")
    i += 1
    new_height = driver.execute_script(" return document.body.scrollHeight ")
    if new_height == last_height :
        print(" last page ")
        break
    else :
        last_height = new_height
        
    
    

#print("scroll is done")
#driver.execute_script("var elems = document.getElementsByClassName('UFILikeLink _4x9- _4x9_ _48-k');for(var i= 0;i<elems.length;i++){elems[i].click();}");

