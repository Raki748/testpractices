from time import sleep

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
url="https://www.facebook.com/campaign/landing.php?campaign_id=14884913640&extra_1=s%7Cc%7C550525804944%7Cb%7Cfacebook%20%27%7C&placement=&creative=550525804944&keyword=facebook%20%27&partner_id=googlesem&extra_2=campaignid%3D14884913640%26adgroupid%3D128696220912%26matchtype%3Db%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-327195741349%26loc_physical_ms%3D9299111%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMI-PvdkeHc-gIVTR0rCh3wjwlMEAAYASAAEgJKgPD_BwE"
driver.get(url)
driver.find_element(By.NAME,"firstname").send_keys("Rakesh")
sleep(3)
driver.find_element(By.CSS_SELECTOR,"[aria-label='Surname']").send_keys("Rocky")
sleep(3)
driver.find_element(By.NAME,"reg_email__").send_keys("9972198661")
sleep(3)
driver.find_element(By.CSS_SELECTOR,"#password_step_input").send_keys("RakeshRock")
sleep(10)
dropdwn = driver.find_element(By.CSS_SELECTOR,"#day")
dob = Select(dropdwn)
dob.select_by_index(17)
sleep(10)
dropdwn1 = driver.find_element(By.CSS_SELECTOR,"#month")
dob1 = Select(dropdwn1)
dob1.select_by_visible_text("Dec")
sleep(20)
dropdwnyear = driver.find_element(By.XPATH,"//select[@id='year']")
dob2 = Select(dropdwnyear)
dob2.select_by_index(27)
sleep(12)
driver.find_element(By.XPATH,"(//input[@type='radio'])[2]").click()
sleep(15)
driver.find_element(By.NAME,"websubmit").click()
sleep(4)
driver.quit()
driver.close()

