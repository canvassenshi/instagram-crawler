from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"



class Bot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox(options=options)

	def login(self):
		bot = self.bot
		bot.get("https://www.instagram.com/")
		time.sleep(3)
		email = bot.find_element(By.NAME, "username")
		password = bot.find_element(By.NAME, "password")
		email.clear()
		password.clear()
		email.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(10)
		bot.find_element(By.CLASS_NAME, "_ac8f").click()
		time.sleep(10)
		bot.find_element(By.CLASS_NAME, "_a9_1").click()

	def like_post(self):
		bot = self.bot
		x = 0
		y = 585.5
		for i in range(5):
			bot.execute_script(f"window.scrollTo({x}, {y})")
			like_btn = bot.find_element(By.CLASS_NAME, "x1n2onr6")
			like_btn.click()
			time.sleep(3)
			x += 400
			y += 585.5

user = Bot(username, password)
user.login()
user.like_post()