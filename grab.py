from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
 
import os
from time import sleep
start_url = 'https://www.instagram.com/USER/saved/COLLECTION_NAME/COLLECTION_ID/' 
username = "USERNAME"
#change this!
index = 1

def filename(ind):
    if ind < 10:
        filename = "000"+str(ind)
    elif ind >= 10 and ind < 100:
        filename = "00"+str(ind)
    elif ind >= 100 and ind < 1000:
        filename = "0"+str(ind)
    elif ind >= 1000:
        filename = str(ind)
    return filename
 
driver = webdriver.Chrome("chromedriver.exe")
 
driver.get(start_url)
sleep(2)
try:
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys(username)
except:
    print("non-permissable login screen, enter credentials manually")
    
wait = input("Logged in?")
go = int(input("how many?"))

next_picture = '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button'

if wait:
    first_click = '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div/div[3]/article/div[1]/div/div[1]/div[2]/a/div[1]/div[2]'
    
    driver.find_element_by_xpath(first_click).click()
    sleep(2)
    
for x in range(0,go-1):
        sleep(1)
        try:
            div = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div/div[1]')
            by = div.screenshot_as_png
            with open("raw_screenshots/"+filename(index)+".png", "wb") as f:
                f.write(by)
            index+=1
            driver.find_element_by_xpath(next_picture).click()
            sleep(2)
        except Exception as e:
            print(e)
            sleep(2)
            try:
                div = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div/div/div[1]')
                by = div.screenshot_as_png
                with open("raw_screenshots/"+filename(index)+".png", "wb") as f:
                    f.write(by)
                index+=1
                driver.find_element_by_xpath(next_picture).click()
                sleep(2)
            except Exception as e:
                print(e)
                index+=1
                driver.find_element_by_xpath(next_picture).click()

    driver.quit()
