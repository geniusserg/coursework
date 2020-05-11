from selenium import webdriver
import time

if __name__ == "__main__":
    driver = webdriver.Remote()
    driver.maximize_window()
    driver.get("https://localhost:80")
    time.sleep(3)
    driver.close()