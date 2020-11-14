# import libraries
from time import sleep, strftime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart

# setup driver
CHROMEDRIVER_PATH = "D:\\Programming\\ChromeDriver\\chromedriver.exe"
# chrome_options = Options()
# chrome_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH) #, options=chrome_options)


def getPorts():
    # get airport designations
    origin = input("Enter 3 letter origin airport: ")
    while(len(origin) != 3):
        origin = ...
        input("Only 3 letter airport codes supported, try again: ")
    destination = input("Enter 3 letter destination airport: ")
    while(len(destination) != 3):
        destination = ...
        input("Only 3 letter airport codes supported, try again: ")

    return origin, destination


def getDates():
    # get dates
    depart_date = input("Enter departure date as 'yyyy-mm-dd': ")
    while(len(depart_date) != 10):
        depart_date = input("Improper date format, ensure date format is 'yyyy-mm-dd': ")

    return_date = input("Enter return date as 'yyyy-mm-dd': ")
    while(len(return_date) != 10):
        return_date = input("Improper date format, ensure date format is 'yyyy-mm-dd': ")

    return [depart_date, return_date]


def getFlightType():
    # request flight type
    type = input("Enter flight type (best, cheapest, or quickest): ")
    while(type != ('best' or 'cheapest' or 'quickest')):
        type = input("Input was not 'best, cheapest, or quickest', retry: ")
    if(type == 'best'):
        type_in = '?sort=bestflight_a'
    elif(type == 'cheapest'):
        type_in = '?sort=price_a'
    elif(type == 'quickest'):
        type_in = '?sort=duration_a'

    return type_in


# get airports, dates, and flight type
origin, destination = getPorts()
depart_date, return_date = getDates()
type = getFlightType()

# open the corresponding browser page to check for updates
kayak = 'https://www.kayak.com/flights/{}-{}/{}/{}{}'.format(origin, destination, depart_date, return_date, type)
browser.get(kayak)
sleep(5)

# refresh to close pop up
browser.refresh()
