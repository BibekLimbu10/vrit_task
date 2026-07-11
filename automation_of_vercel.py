from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Using chrome browser.
driver=webdriver.Chrome()
time.sleep(2)
#Maximizing the screen. 
driver.maximize_window()
#Opening website
url="https://authorized-partner.vercel.app/"
driver.get(url)
time.sleep(2)
#find get start button
getstart_button=driver.find_element(By.XPATH,"/html/body/div[4]/header/div[1]/div/a[2]/button")
getstart_button.click()
time.sleep(5)
#find terms and conditions marking place
terms_button=driver.find_element(By.XPATH,"//*[@id='remember']")
terms_button.click()
time.sleep(2)
#find continue button
continue_button=driver.find_element(By.XPATH,"/html/body/div[4]/div[4]/div[3]/a/button")
continue_button.click()
time.sleep(5)
#Fill first name
first_name=driver.find_element(By.NAME, "firstName")
first_name.send_keys("Bibek")
time.sleep(2)
#Fill last name
last_name=driver.find_element(By.NAME,"lastName")
last_name.send_keys("Limbu")
time.sleep(2)
#fill email address
email_address=driver.find_element(By.NAME,"email")
email_address.send_keys("sss@yopmail.com")
time.sleep(2)
#find phone number country code
#number_code=driver.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/div/div/div[2]/form/div[2]/div[2]/div/div/div/button/svg")
#line 31 and 32 code is not applicable because the website doesnot contains proper information about the country phone number code.
#fill phone number
phone_number=driver.find_element(By.NAME,"phoneNumber")
phone_number.send_keys("9817340506")
time.sleep(2)
#Fill password
password=driver.find_element(By.NAME,"password")
password.send_keys("Password@123")
time.sleep(2)
#Fill comfirm password
confirm_password=driver.find_element(By.NAME,"confirmPassword")
confirm_password.send_keys("Password@123")
time.sleep(2)
# Click Next Button
next_button=driver.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/div/div/div[2]/form/div[4]/button")
next_button.click()
time.sleep(2)
#fill OPT code but the OPT changes everytime
otp_code=driver.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/div/div/div[2]/div/form/div[1]/div[2]/input")
otp_code.send_keys("129052")
#click verify code button
verify_button=driver.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/div/div/div[2]/div/form/div[2]/button")
verify_button.click()
time.sleep(60)
#fill agency name
agency_name=driver.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/div/div/div[2]/form/div[1]/div[1]/label")
agency_name.send_keys("No_Agency")
time.sleep(2)

#fill your role in agency
role_agency=driver.find_element(By.XPATH,"//*[@id='_r_1_-form-item']")
role_agency.send_keys("Intern")
time.sleep(2)
#fill email address of your agency
email_agency=driver.find_element(By.XPATH,"//*[@id='_r_2_-form-item']")
email_agency.send_keys("agency@yopmail.com")
time.sleep(2)
#fill website link of agency
website_link=driver.find_element(By.XPATH,"//*[@id='_r_3_-form-item']")
website_link.send_keys("www.agency.com")
time.sleep(2)
#fill address of agency
agency_address=driver.find_element(By.XPATH,"//*[@id='_r_4_-form-item']")
agency_address.send_keys("Kathmandu,Nepal")
time.sleep(2)
#scroll bottom to top
driver.execute_script("window.scrollTo(0,0);")
#fill region of operation
region_operation=driver.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/div/div/div[2]/form/div[3]/div[2]/button/div/span")
region_operation.click()
time.sleep(2)
#fill your country name
country_name=driver.find_element(By.XPATH,"//*[@id='radix-_r_6_']/div[1]/input")
country_name.send_keys("Nepal")
time.sleep(2)
#Click your your country name
country_click=driver.find_element(By.XPATH,"//*[@id='radix-_r_6_']/div[2]/div/div/div")
time.sleep(2)
#Click next
next_agency=driver.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/div/div/div[2]/form/div[4]/button[2]")
next_agency.click()
time.sleep(2)
# years of experience
experience=driver.find_element(By.XPATH,"//*[@id='_r_gj_-form-item']")
experience.click()
#choose agency experience
years=driver.find_element(By.XPATH,"//*[@id='_r_gj_-form-item']")
years.send_keys("3 years")
time.sleep(4)
#Number of student recurited annually
student=driver.find_element(By.XPATH,"//*[@id='_r_gl_-form-item']")
student.send_keys("3000")
#focus area of agency
focus_area=driver.find_element(By.XPATH,"//*[@id='_r_gm_-form-item']")
focus_area.send_keys("Undergraduate admissions to Canada.")
time.sleep(3)
#fill success metrics
success_matrics=driver.find_element(By.XPATH,"//*[@id='_r_gn_-form-item']")
success_matrics.send_keys("85%")
time.sleep(2)
#Choose service provided by agency
service=driver.find_element(By.XPATH,"//*[@id='_r_gr_-form-item']")
service.click()
time.sleep(2)
# Click next
next_ae=driver.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/div/div/div[2]/form/div[4]/button[2]")
next_ae.click()
#Enter your registration number
registration=driver.find_element(By.XPATH,"//*[@id='_r_95_-form-item']")
registration.click()
#choose prefered countrty
prefered_country=driver.find_element(By.XPATH,"//*[@id='_r_96_-form-item']/div/span")
prefered_country.click()
time.sleep(2)
# Choosing Australia
country=driver.find_element(By.XPATH,"//*[@id='radix-_r_97_']/div[2]/div/div/div[1]/span")
country.click()
time.sleep(2)
#Choose preferred institution types
types=driver.find_element(By.XPATH,"//*[@id='_r_99_-form-item']")
types.click()
#Certificate details
certificate=driver.find_element(By.XPATH,"//*[@id='_r_9d_-form-item']")
certificate.send_keys("Bachelor in Computer Science")
time.sleep(2)
#Uploading Company registration certificate
registration_agency=driver.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/div/div/div[2]/form/div[3]/div[1]/div/div/div[1]/span")
registration_agency.send_keys(r"c:\Users\bibek\Pictures\Screenshots\brook &  Princess Shuri.png/automation_file.py")
#Uploading educational certificate
file_upload=driver.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/div/div/div[2]/form/div[3]/div[2]/div/div/div[1]/span")
file_upload.send_keys(r"c:\Users\bibek\Pictures\Screenshots\brook &  Princess Shuri.png/automation_file.py")
time.sleep(2)
# Submission of file
submission=driver.find_element(By.XPATH,"/html/body/div[4]/div[4]/div/div/div/div[2]/form/div[3]/div[2]/div/div/div[1]/span")
submission.click()
time.sleep(5)
#To know the process is completed or not
assert "https://authorized-partner.vercel.app/admin/profile" in driver.current_url,"Failed! Logout.Unsuccessful"
time.sleep(2)
driver.quit