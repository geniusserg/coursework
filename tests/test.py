from selenium import webdriver
import time

if __name__ == "__main__":
    print( "testing started")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://localhost:80/CarConfig.htm")
    time.sleep(3)
    driver.close()
    print( "site opened")