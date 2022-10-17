from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH,"//button[normalize-space()='Click Me']").click()
sleep(5)
# driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()
sleep(3)
driver.get_screenshot_as_file("C:\\Screenshot\\img5.jpg")
driver.quit()
driver.close()