'''
	Designed to combat the growing number of Roblox bot accounts spamming on group walls.
	The only way to encourage your community to post on the group wall and keep them safe without lots of 
	manual moderation is to use a bot to fight back.
	
	None of the data scraped from the Roblox website is stored, it is simply read and forgotten.

	The creator is not responsible for anything that goes wrong. Use at your own risk, edit at your own risk.
	I recommend using a throw away account, creating a bot role within your group with only delete permissions
	
	DO NOT SHARE THIS FILE WITH ANYONE WHILE IT CONTAINS YOUR BOT'S PASSWORD
	
	Supports both chrome or firefox, look at source code.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
import time 
import datetime
import os
import getpass # Invisible password input

# Details
username = input("Account username:")
password = getpass.getpass("Password (hidden):")

group_page = "https://www.roblox.com/groups/group.aspx?gid=997074"
driver_location = "D:\DocumentsHDD\chromedriverfolder\chromedriver.exe"
wait_time = 10

# Unwanted words
blacklist = ["ROBUX", "WIN", "FREE", "FOLLOWERS", "PROFILE", "LOOK", "DONATE", "MORE FOLLOWERS", "PRIZE", "R$", ".COM", ".ME"]

# Run firefox headless 
#options = Options()
#options.add_argument('-headless')
#driver = webdriver.Firefox(firefox_options=options)

# Run chrome headless
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('log-level=3')
driver = webdriver.Chrome(driver_location, chrome_options=options)

# Load login page
print("Loading page")
driver.get("https://www.roblox.com/login")
print("Page loaded")

# Login
print("Logging in")
username_element = driver.find_element_by_id("login-username")
password_element = driver.find_element_by_id("login-password")
username_element.send_keys(username)
password_element.send_keys(password)
time.sleep(1)
driver.find_element_by_id("login-button").click()
print("Logging in, please wait.")
# Page load
time.sleep(5)

# Begin searching
print("Starting search loop")
while True:
	# Webpage to crawl
	driver.get(group_page)
	
	# Find element
	try:
		elem = driver.find_element_by_class_name("AlternatingItemTemplateOdd")
	except:
		print("Couldn't find element")
		time.sleep(wait_time)
		continue
	
	num_of_words = 0
	message = elem.find_element_by_class_name("GroupWall_PostContainer").text.upper()
	for word in blacklist:
			if word in message:
				num_of_words += 1
	
	# If the post contains two or more blacklisted words then delete post
	if num_of_words >= 2:
		print(message)
		try:
			elem.find_element_by_class_name("GroupWall_PostBtns").find_element_by_tag_name("a").click()
		except:
			print("Coudn't find delete button. User may be of a higher permission than bot / username & password may be wrong")
	
	print(str(datetime.datetime.now()))
	time.sleep(wait_time)
	
driver.close()