# This will work using headless Chrome for any Desktop OS (Windows, MacOS, Linux Desktop)
from selenium import webdriver
import platform
import time

# Gets the path to the right chromedriver
path = "C:/webdriver/chromedriver.exe"

browsers = [
    'chrome'
    ]

client_urls = [
    'www.vetrotech.com'
    ]

sub_pages = [
    '',
    "/fire-resistant-solutions", 
    "/insulation-glass-ei-class", 
    "/radiation-control-glass-ew-class", 
    "/integrity-glass-e-class", 
    "/fire-resistant-systems", 
    "/high-security-solutions", 
    "/attack-resistance-glass", 
    "/bullet-resistant-glass", 
    "/blast-resistant-glass", 
    "/multifunctionality", 
    "/commercial", 
    "/education", 
    "/healthcare", 
    "/hospitality-and-leisure", 
    "/public-and-transport", 
    "/marine", 
    "/partitions", 
    "/skylights", 
    "/windows", 
    "/facade", 
    "/doors", 
    "/floors", 
    "/contraflam-family", 
    "/vetroflam-family", 
    "/pyroswiss-family", 
    "/vetrogard-family", 
    "/polygard-family", 
    "/other-specialty-glass", 
    "/services", 
    "/projects", 
    "/downloads", 
    "/about-us", 
    "/management", 
    "/history", 
    "/sustainability", 
    "/open-positions", 
    "/vetrotech-sales-school", 
    "/volontariat-international-en-entreprise", 
    "/internships-vetrotech-saint-gobain", 
    "/news-and-trends", 
    "/pressroom", 
    "/offices", 
    "/contact-us#no-back", 
    "/vetrogard-attack", 
    "/vetrogard-and-polygard-attack-igu", 
    "/vetrogard-bullet", 
    "/vetrogard-and-polygard-bullet-igu", 
    "/vetrogard-blast", 
    "/vetrogard-and-polygard", 
    "/pyroswiss", 
    "/pyroswiss-stadip", 
    "/vetroflam", 
    "/vetroflam-laminated", 
    "/vetroflam-igu", 
    "/vetroflam-2s", 
    "/contraflam", 
    "/contraflam-mega", 
    "/contraflam-stadip", 
    "/contraflam-igu", 
    "/contraflam-lite", 
    "/contraflam-door-lite", 
    "/polygard-attack", 
    "/vetrogard-and-polygard-attack-igu", 
    "/polygard-bullet", 
    "/vetrogard-and-polygard-bullet-igu", 
    "/vetrogard-and-polygard"
    ]

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("disable-infobars")  # disabling infobars
options.add_argument("--disable-extensions")  # disabling extensions
options.add_argument("--disable-gpu")  # applicable to windows os only
# overcome limited resource problems
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")


complete_urls = [client_url + sub_page for client_url in client_urls for sub_page in sub_pages]
totalheight = 10000

for browser in browsers:
    #insert your code for creating a new webdriver for the given browser
    for complete_url in complete_urls:
        new_sub_pages = complete_url.replace("/", "_")
        driver = webdriver.Chrome(path, options=options)

        desktop = {'output': 'screenshots/global/desktop/' + str(new_sub_pages) + '-desktop.png',
                    'width': 1920,
                    'height': totalheight}
        mobile = {'output': 'screenshots/global/mobile/' + str(new_sub_pages) + '-mobile.png',
                  'width': 680,
                  'height': totalheight}
        #get link
        linkWithProtocol = 'http://' + str(complete_url)

        # set the window size for desktop
        driver.set_window_size(desktop['width'], desktop['height'])
        driver.get(linkWithProtocol)
        time.sleep(2)
        driver.save_screenshot(desktop['output'])

        driver.set_window_size(mobile['width'], mobile['height'])
        driver.get(linkWithProtocol)
        time.sleep(2)
        driver.save_screenshot(mobile['output'])