from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
sleep(5)
# driver.switch_to.frame("iframeResult")  # Need to take x path of parent frame
driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='iframeResult']"))  # Need to take x path of parent frame
# driver.switch_to.frame(0)
driver.switch_to.frame(1)
sleep(5)
driver.find_element(By.XPATH, "//a[@id='nav_search_btn']").click()
sleep(5)
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//a[@id='getwebsitebtn']").click()
sleep(5)
driver.quit()
driver.close()


