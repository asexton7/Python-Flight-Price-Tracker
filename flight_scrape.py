# import libraries
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Flight

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

flight = Flight(origin, destination, depart_date, return_date)

# open the corresponding browser page to check for updates
kayak = 'https://www.kayak.com/flights/{}-{}/{}/{}{}'.format(origin, destination, depart_date, return_date, type)
browser.get(kayak)

# wait up to 45s for progress bar to indicate all flights loaded
wait = WebDriverWait(browser, 45)
try:
    progressBar_present = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class=\"bar\"][@style=\"transform: translateX(100%);\"]")))
except:
    print("Search took too long, try search again")
    browser.get(kayak)

# get the lowest priced flight on the page
searchResults = browser.find_element_by_xpath("//*[@id=\"searchResultsList\"]")
prices = searchResults.find_elements_by_class_name("price-text")

# iterate through list. keep actual values
price_out = []
for price in prices:
    price_out.append(price.text.replace('$', ''))

# filter out none values
price_out = list(map(int, [price for price in price_out if price.isdigit()]))

# try catch block in case price_out is an empty vector
try:
    cheapest_flight = min(price_out)
    print(cheapest_flight)
except ValueError:
    print("No Flights Found for these dates, try search again with different dates or airports")
