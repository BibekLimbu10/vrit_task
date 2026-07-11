# importing libraries for api call and random generation
import requests
import random
import string
import re
import os
import subprocess
import signal

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# -- FFmpeg Recording Setup --
RECORDING_FILE = "demo_video.mp4"
ffmpeg_proc = None

def start_recording():
    global ffmpeg_proc
    try:
        import pygetwindow as gw
        import pyautogui
        time.sleep(2)
        screen_w, screen_h = pyautogui.size()
        chrome_win = gw.getWindowsWithTitle("Chrome")[0]
        x = max(0, chrome_win.left)
        y = max(0, chrome_win.top)
        w = min(chrome_win.width, screen_w - x)
        h = min(chrome_win.height, screen_h - y)
    except Exception:
        screen_w, screen_h = 1920, 1080
        x, y, w, h = 0, 0, screen_w, screen_h

    with open("ffmpeg_log.txt", "w") as log:
        ffmpeg_proc = subprocess.Popen(
            ["ffmpeg", "-f", "gdigrab", "-framerate", "10",
             "-offset_x", str(x), "-offset_y", str(y),
             "-video_size", f"{w}x{h}", "-i", "desktop",
             "-c:v", "libx264", "-preset", "ultrafast",
             "-y", RECORDING_FILE],
            stdout=log, stderr=subprocess.STDOUT
        )
    print(f"Recording started -> {RECORDING_FILE}")

def stop_recording():
    global ffmpeg_proc
    if ffmpeg_proc:
        ffmpeg_proc.terminate()
        ffmpeg_proc.wait()
        ffmpeg_proc = None
        print("Recording stopped.")

# creates a temp email inbox using mail.tm api
def create_temp_email():
    base_url = "https://api.mail.tm"
    random_numbers = ''.join(random.choices(string.digits, k=8))
    email = f"test{random_numbers}@web-library.net"
    password = "Temp@123"
    
    # create account on mail.tm
    response = requests.post(f"{base_url}/accounts", json={
        "address": email,
        "password": password
    })
    
    # get token so we can access inbox later
    token_response = requests.post(f"{base_url}/token", json={
        "address": email,
        "password": password
    })
    token = token_response.json()["token"]
    return email, token, base_url

# checking inbox until we get the otp code
def get_otp_from_inbox(token, base_url, wait_time=60):
    headers = {"Authorization": f"Bearer {token}"}
    deadline = time.time() + wait_time
    
    while time.time() < deadline:
        response = requests.get(f"{base_url}/messages", headers=headers)
        messages = response.json().get("hydra:member", [])
        
        if messages:
            latest_msg_id = messages[-1]["id"]
            email_data = requests.get(f"{base_url}/messages/{latest_msg_id}", headers=headers).json()
            
            # look for 6 digit number in email text
            email_text = email_data.get("text", "") or email_data.get("html", "")
            match = re.search(r'\b(\d{6})\b', email_text)
            if match:
                return match.group(1)
        
        time.sleep(3)
    
    return None

# create a fresh email and random phone number every time we run
temp_email, api_token, api_url = create_temp_email()
random_phone = f"98{random.randint(10000000, 99999999)}"

print(f"Using email: {temp_email}")
print(f"Using phone: {random_phone}")

# Using chrome browser with automatic chromedriver management.
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
time.sleep(3)
#Maximizing the screen. 
driver.maximize_window()
#Start recording the demo
start_recording()
#Opening website
url="https://authorized-partner.vercel.app/"
driver.get(url)
time.sleep(3)
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

# Set up Account 
#Fill first name
first_name=driver.find_element(By.NAME, "firstName")
first_name.send_keys("Bibek")
time.sleep(1)
#Fill last name
last_name=driver.find_element(By.NAME,"lastName")
last_name.send_keys("Limbu")
time.sleep(1)
#fill email address (now using dynamic email instead of hardcoded one)
email_address=driver.find_element(By.NAME,"email")
email_address.send_keys(temp_email)
time.sleep(1)
#fill phone number (now using random phone number)
phone_number=driver.find_element(By.NAME,"phoneNumber")
phone_number.send_keys(random_phone)
time.sleep(1)
#Fill password
password=driver.find_element(By.NAME,"password")
password.send_keys("Password@123")
time.sleep(1)
#Fill comfirm password
confirm_password=driver.find_element(By.NAME,"confirmPassword")
confirm_password.send_keys("Password@123")
time.sleep(1)
# Click Next Button
next_button=driver.find_element(By.XPATH,"//button[@type='submit']")
next_button.click()

# now we wait for the otp email to arrive and fetch it automatically
print("Waiting for OTP email...")
otp_value = get_otp_from_inbox(api_token, api_url)

if otp_value is None:
    print("could not get OTP code within 60 seconds")
    stop_recording()
    driver.quit()
    exit()

print(f"OTP received: {otp_value}")

#fill OTP code 
time.sleep(3)
otp_input=driver.find_element(By.XPATH,"//input")
otp_input.send_keys(otp_value)
#click verify code button
verify_button=driver.find_element(By.XPATH,"//button[contains(text(),'Verify Code')]")
verify_button.click()
time.sleep(5)

# Agency Details
print("Filling Agency Details...")
#fill agency name
agency_name=driver.find_element(By.NAME,"agency_name")
agency_name.send_keys("No_Agency")
time.sleep(1)
#fill your role in agency
role_agency=driver.find_element(By.NAME,"role_in_agency")
role_agency.send_keys("Intern")
time.sleep(1)
#fill email address of your agency
email_agency=driver.find_element(By.NAME,"agency_email")
email_agency.send_keys("agency@yopmail.com")
time.sleep(1)
#fill website link of agency
website_link=driver.find_element(By.NAME,"agency_website")
website_link.send_keys("www.agency.com")
time.sleep(1)
#fill address of agency
agency_address=driver.find_element(By.NAME,"agency_address")
agency_address.send_keys("Kathmandu,Nepal")
time.sleep(1)
#scroll to top so the dropdown is visible
driver.execute_script("window.scrollTo(0,0);")
time.sleep(1)
#fill region of operation
region_operation=driver.find_element(By.XPATH,"//button[@role='combobox']")
region_operation.click()
time.sleep(2)
#fill your country name
country_name=driver.find_element(By.XPATH,"//input[@placeholder='Search...']")
country_name.send_keys("Nepal")
time.sleep(2)
#Click your your country name
country_click=driver.find_element(By.XPATH,"//*[text()='Nepal']")
country_click.click()
time.sleep(2)
#close dropdown
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.ESCAPE)
time.sleep(1)
#Click next
next_agency=driver.find_element(By.XPATH,"//button[@type='submit']")
driver.execute_script("arguments[0].scrollIntoView(true);", next_agency)
time.sleep(1)
driver.execute_script("arguments[0].click()", next_agency)
time.sleep(5)

# Professional Experience 
print("Filling Professional Experience...")
# years of experience this combobox needs special handling because react hides the real select
years_combo=driver.find_element(By.XPATH,"//button[@role='combobox']")
years_combo.click()
time.sleep(1)
#choose agency experience
years=driver.find_element(By.XPATH,"//*[text()='3 years']")
years.click()
time.sleep(1)
#this is needed because the actual select is hidden by react and we gotta trigger change event
driver.execute_script("""
    var sel = document.querySelector('select[aria-hidden="true"]');
    if(sel != null) { sel.value = '3'; sel.dispatchEvent(new Event('change', { bubbles: true })); }
""")
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.ESCAPE)
time.sleep(1)

#Number of student recurited annually
student=driver.find_element(By.NAME,"number_of_students_recruited_annually")
student.send_keys("3000")
time.sleep(0.5)
#blur so react knows we typed something
driver.execute_script("arguments[0].blur()", student)
time.sleep(1)
#focus area of agency
focus_area=driver.find_element(By.NAME,"focus_area")
focus_area.send_keys("Undergraduate admissions to Canada.")
time.sleep(0.5)
driver.execute_script("arguments[0].blur()", focus_area)
time.sleep(1)
#fill success metrics
success_matrics=driver.find_element(By.NAME,"success_metrics")
success_matrics.send_keys("85")
time.sleep(0.5)
driver.execute_script("arguments[0].blur()", success_matrics)
time.sleep(1)

#Choose service provided by agency click Visa Processing
driver.execute_script("arguments[0].click()", driver.find_element(By.XPATH,"//*[text()='Visa Processing']"))
time.sleep(1)
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.ESCAPE)
time.sleep(1)

#Click next button
time.sleep(2)
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.ESCAPE)
time.sleep(1)
next_professional=driver.find_element(By.XPATH,"//button[@type='submit']")
driver.execute_script("arguments[0].scrollIntoView(true);", next_professional)
time.sleep(1)
driver.execute_script("arguments[0].click()", next_professional)
time.sleep(8)

# Verification and Preferences 
print("Filling Verification and Preferences...")
#Enter your registration number
registration=driver.find_element(By.NAME,"business_registration_number")
registration.send_keys("REG12345")
time.sleep(1)
#choose prefered country
prefered_country=driver.find_element(By.XPATH,"//button[@role='combobox']")
prefered_country.click()
time.sleep(1)
# Choosing Australia
driver.execute_script("arguments[0].click()", driver.find_element(By.XPATH,"//*[text()='Australia']"))
time.sleep(1)
driver.find_element(By.TAG_NAME,"body").send_keys(Keys.ESCAPE)
time.sleep(1)
#Choose preferred institution types - click Universities
driver.execute_script("arguments[0].click()", driver.find_element(By.XPATH,"//*[text()='Universities']"))
time.sleep(1)
#Certificate details
certificate=driver.find_element(By.NAME,"certification_details")
certificate.send_keys("Bachelor in Computer Science")
time.sleep(1)
#Uploading Company registration certificate
file_inputs=driver.find_elements(By.CSS_SELECTOR,"input[type='file']")
file_inputs[0].send_keys(os.path.abspath("uploads/registration.pdf"))
time.sleep(1)
#Uploading educational certificate
file_inputs[1].send_keys(os.path.abspath("uploads/education.pdf"))
time.sleep(2)
#Click submit
driver.execute_script("arguments[0].click()", driver.find_element(By.XPATH,"//button[@type='submit']"))
time.sleep(8)
#To know the process is completed or not
body_text=driver.find_element(By.TAG_NAME,"body").text
if "Personal Information" in body_text and "Agency Details" in body_text:
    print("Signup completed successfully!")
else:
    print("Signup have failed!")
time.sleep(2)
stop_recording()
driver.quit()
