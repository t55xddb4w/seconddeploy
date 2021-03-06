import time
import os

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary #We import this so we can specify the Firefox browser binary location

weburl = os.getenv('WEB_URL')
FF_options = webdriver.FirefoxOptions()
FF_profile = webdriver.FirefoxProfile()
FF_options.add_argument("-headless")
FF_profile.update_preferences()

check=1
while(check>0):
    driver = webdriver.Firefox(options=FF_options, firefox_profile=FF_profile, executable_path=os.environ.get("GECKODRIVER_PATH"), firefox_binary=FirefoxBinary(os.environ.get("FIREFOX_BIN")))
    driver.get("https://icanhazip.com")
    ipaddr = driver.page_source
    print(ipaddr)
    time.sleep(10)
    driver.close()
    print("Times Run = ", check)
    check=check+1
