from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://accounts.google.com")
driver.find_element(By.XPATH,"//input[@id='identifierId']").send_keys("rakeshhn232@gmail.com")
sleep(3)
driver.find_element(By.ID,"identifierNext").click()
sleep(7)
driver.find_element(By.XPATH,"//input[@name='Passwd']").send_keys("Somashekar@186")
sleep(3)
driver.find_element(By.ID,"identifierNext").click()
sleep(3)
driver.close()
driver.quit()