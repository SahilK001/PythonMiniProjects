from selenium import webdriver
from getpass import getpass

uid  = input("Enter your uid")
password = getpass("enter your password")

driver = webdriver.Chrome("C:\\Web Driver\chromedriver.exe")
driver.get("https://cuchd.blackboard.com//")

# Step 1 Enter the UID(Unique Identity)
uid_textbox = driver.find_element_by_id("user_id")
uid_textbox.send_keys(uid)

# Step 2 Enter to next step
# Step 3 Enter the password
password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(password)

# Step 4 Final step to submit
next_button1 = driver.find_element_by_id("entry-login")
next_button1.submit()
