from selenium import webdriver

from time import sleep
start_url = 'https://www.instagram.com/USER/saved/COLLECTION_NAME/COLLECTION_ID/' 
#change this!
index = 1

driver = webdriver.Chrome()
 
driver.get(start_url)
wait = input("Logged in?")

next_picture = '/html/body/div[6]/div[1]/div/div/a[2]'

if wait:
    first_click = '//*[@id="react-root"]/section/main/div/div/div[3]/article/div[1]/div/div[1]/div[3]'
    
    driver.find_element_by_xpath(first_click).click()
    for x in range(0,5000):
        try:
            driver.find_element_by_class_name('fXIG0')
        except:
            f = "raw_screenshots/"+str(index)+".png"
            index+=1
            sleep(3)
            driver.save_screenshot(f)
            driver.find_element_by_xpath(next_picture).click()
    driver.quit()
