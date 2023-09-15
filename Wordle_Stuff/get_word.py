# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#gets the wordle word and saves it to word.txt

def getword():

    driver = webdriver.Chrome()
    
    #URL
    driver.get("https://word.tips/todays-wordle-answer/")

    time.sleep(2)
    
    data = driver.find_element(By.XPATH, "/html/body").text

    driver.close()

    data = data[data.find("Boost Your Wordle Solving Skills Here"):-1]
    data = data.split()

    word = data[11]

    print(word)

    f = open("Word\word.txt","w")
    f.write(word)
    f.close()

getword()