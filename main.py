from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\\Users\\janns\\PycharmProjects\\chromedriver.exe")
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

driver.fullscreen_window()

for n in range(10**10):
    cookie.click()

driver.quit()
