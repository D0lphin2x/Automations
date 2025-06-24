from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime

# Configure Edge options, make a new folder to put an edge profile to bypass okta/duo
# Still need to confirm for the first time around
options = Options()
options.add_argument("--user-data-dir=PATH/TO/YOUR/AUTOMATION/PROFILE")

# Download msedgedriver, needed for the automation service, put the path to where you downloaded here
service = Service("PATH/TO/YOUR/")

# Launch Edge
driver = webdriver.Edge(service=service, options=options)

# Go to Workday login page
driver.get("REPLACEWITHYOURJOB.com")

# Calculates what day
today_index = datetime.today().weekday()  # 0 = Monday, 6 = Sunday
print((today_index + 1) * 8) # used for later, if working different hours each day change the 8
input() # Comment these out after first run
driver.quit() #Comment these out after first run

#FOR FIRST TIME ONLY, Enter username, password, okta/duo verification as normal
# Afterwards go into terminal and press enter, it should close edge, then comment out the two lines above
# and uncomment the block of code below

##### Works if you already have a profile, if first time comment this part out

# initial = WebDriverWait(driver, 15)
# login = initial.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Next"]')))
# login.click()

# # After first time input password
# password_input = initial.until(EC.presence_of_element_located((By.ID, 'input80')))
# password_input.send_keys("PASSWORD")

# login2 = initial.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="submit" and @value="Verify"]')))
# login2.click()

# wait = WebDriverWait(driver, 60)
# element = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Time"]')))
# element.click()

# wait1 = WebDriverWait(driver, 15)
# element1 = wait1.until(EC.element_to_be_clickable((By.XPATH, f'//button[@aria-label="This Week ({(today_index + 1) * 8} Hours)"]')))
# element1.click()

# wait2 = WebDriverWait(driver, 10)
# element2 = wait2.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Actions"]')))
# element2.click()
# time.sleep(1)

# wait3 = WebDriverWait(driver, 10)
# element3 = wait3.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and text()="Enter Time by Type"]')))
# element3.click()

# # Now wait for input boxes to load
# try:
#     inputs = WebDriverWait(driver, 30).until(
#         EC.presence_of_all_elements_located((By.XPATH, '//input[@data-automation-id="numericInput"]'))
#     )
#     print(f"\u2705 Found {len(inputs)} input boxes.")
# except:
#     print("\u274C Could not find time entry inputs. Maybe 'Enter Time by Type' didn't finish loading?")
#     driver.quit()
#     exit()

# today_index = datetime.today().weekday()  # 0 = Monday, 6 = Sunday
# print(today_index)
# if today_index >= 5:
#     print("\u2705 Weekend — no need to log time.")
# else:
#     input_index = today_index + 2  # Skipping Sat & Sun inputs
#     target_input = inputs[input_index]

#     # Activate the cell first by clicking its parent td
#     td = target_input.find_element(By.XPATH, './ancestor::td')
#     driver.execute_script("arguments[0].scrollIntoView(true);", td)
#     time.sleep(0.5)
#     td.click()
#     time.sleep(0.3)

#     # Now send input
#     target_input.send_keys(Keys.COMMAND + "a")
#     target_input.send_keys("8")
#     print("\u2705 Entered 8 hours.")

# wait4 = WebDriverWait(driver, 10)
# element4 = wait4.until(EC.element_to_be_clickable((By.XPATH, '//button[@title="Save and Close"]')))
# element4.click()

# time.sleep(5)
# driver.quit()
#####
