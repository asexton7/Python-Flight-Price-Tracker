# import libraries
from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart

# setup driver
browser = webdriver.Firefox()

# get airport designations
origin = input("Enter 3 letter origin airport: ")
destination = input("Enter 3 letter destination airport: ")

# get dates
departure = input("Enter departure date as 'yyyy-mm-dd': ")
return_flight = input("Enter return date as 'yyyy-mm-dd': ")

# request flight type
type = input("Enter flight type (best, cheapest, or quickest): ")
if(type == 'best'):
    type_in = '?sort=bestflight_a'
elif(type == 'cheapest'):
    type_in = '?sort=price_a'
elif(type == 'quickest'):
    type_in = '?sort=duration_a'

# open the corresponding browser page to check for updates
kayak = 'https://www.kayak.com/flights/' + origin + '-' + destination + '/' + departure + '/' + return_flight + type_in
browser.get(kayak)
sleep(5)

try:
    xp_popup_close = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close ")]'
    browser.find_elements_by_xpath(xp_popup_close)[5].click()
except Exception as e:
    pass

prices_x = '//a[@class="booking-link"]/span[@class="price option-text"]'
prices = browser.find_elements_by_xpath(prices_x)
prices_list = [price.text.replace('$', '') for price in prices if price.text != '']
prices_list = list(map(int, prices_list))
print(prices_list)
