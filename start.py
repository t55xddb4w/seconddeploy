import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

check=1
while(check>0):
    gChromeOptions = webdriver.ChromeOptions()
    gChromeOptions.add_argument("window-size=1920x1480")
    gChromeOptions.add_argument("disable-dev-shm-usage")
    gDriver = webdriver.Chrome(
        chrome_options=gChromeOptions, executable_path=ChromeDriverManager().install()
    )
    
    gDriver.get("https://index.strongerdc.ml")
    time.sleep(600)
    gDriver.close()
    print("Times Run = ", check)
    check=check+1
