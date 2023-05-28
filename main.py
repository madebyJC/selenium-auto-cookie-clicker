import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\\Users\\janns\\PycharmProjects\\chromedriver.exe")
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
start_time = time.time()
running = True


def all_store():
    buy_store = driver.find_elements(By.CSS_SELECTOR, "#store div")
    for n in range(len(buy_store), -1, -1):
        try:
            buy_store[n].click()
        except:
            continue


cookie = driver.find_element(By.ID, "cookie")

while True:
    for i in range(0, 500):
        cookie.click()

    for i in range(0, 5):
        all_store()
