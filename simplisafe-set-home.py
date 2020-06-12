#Source: https://gist.github.com/gyoza/6be7c23c1719fb980d53f749978f1dce [gist.github.com]
# Import packages
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# Using Chrome to access web
# TO INSTALL CHROME: 
driver = webdriver.Chrome(ChromeDriverManager().install())

time.sleep(5) #allows program time to load before running

# Open the website
driver.get('https://webapp.simplisafe.com/#/dashboard [webapp.simplisafe.com]')

# Select the id box
id_box = driver.find_element_by_name('email')

id_box.send_keys('INSERT EMAIL') #This is where you put your SimpliSafe Email

# Find password box
pass_box = driver.find_element_by_name('password')

# Send password
pass_box.send_keys('INSERT PASSWORD') #This is where put in your SimpliSafe Password

# Find login button
driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div[2]/div[5]/button').click()

#Set SimpliSafe to Home
#Need to wait for page to load so make Selenium wait
##Source: https://stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready [stackoverflow.com]; https://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python [stackoverflow.com]

time.sleep(5)
driver.find_element_by_xpath('//*[@id="home-circle"]').click()
