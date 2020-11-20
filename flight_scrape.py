# import libraries
from time import sleep, strftime
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# setup driver
CHROMEDRIVER_PATH = "D:\\Programming\\ChromeDriver\\chromedriver.exe"
chrome_options = Options()
# chrome_options.headless = True
# chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH , options=chrome_options)


def getPorts():
    # get airport designations
    origin = input("Enter 3 letter origin airport: ")
    while(len(origin) != 3):
        origin=input("Only 3 letter airport codes supported, try again: ")
    destination = input("Enter 3 letter destination airport: ")
    while(len(destination) != 3):
        destination=input("Only 3 letter airport codes supported, try again: ")

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


def getFlightSearchType():
    # request flight type
    type = input("Enter flight type (best, cheapest, or quickest): ")

    while type not in ['best', 'cheapest', 'quickest']:
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
type = getFlightSearchType()

# open the corresponding browser page to check for updates
kayak = 'https://www.kayak.com/flights/{}-{}/{}/{}{}'.format(origin, destination, depart_date, return_date, type)
browser.get(kayak)

# refresh to close pop up, wait for page to refresh
browser.refresh()


wait = WebDriverWait(browser, 15)
progressBar = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "progress-bar")))

loadComplete = WebDriverWait(progressBar, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "Common-Results-ProgressBar theme-dark Hidden")))

print(loadComplete.get_attribute("class"))

# get the lowest priced flight on the page
searchResults = browser.find_element_by_xpath("//*[@id=\"searchResultsList\"]")
prices = searchResults.find_elements_by_class_name("price-text")


sleep(5)
# iterate through list. keep actual values
price_out = []
for price in prices:
    price_out.append(price.text.replace('$', ''))

# filter out none values
price_out = list(map(int, [price for price in price_out if price.isdigit()]))

cheapest_flight = min(price_out)
print(cheapest_flight)
