from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class login(Page):
	'''用户登录界面'''
	url = '/'

	# 定位器
	bgw_login_button_loc = (By.LINK_TEXT,'登录')

	# 进入币港湾登录界面
	def bgw_login(self):
		self.find_element(*self.bgw_login_button_loc).click()
		sleep(1)

	# 定位器
	login_username_loc = (By.ID,'nick')
	login_password_loc = (By.ID,'password')
	login_button_loc = (By.ID,'login_submit')

	# 登录用户名
	def login_username(self,username):
		self.find_element(*self.login_username_loc).send_keys(username)

	# 登录密码
	def login_password(self,password):
		self.find_element(*self.login_password_loc).send_keys(password)

	# 登录按钮
	def login_button(self):
		self.find_element(*self.login_button_loc).click()

	# 定义统一登录入口
	def user_login(self,username='13362185609',password='123321'):
		'''获取的用户名密码登录'''
		self.open()
		self.bgw_login()
		self.login_username(username)
		self.login_password(password)
		self.login_button()
		sleep(1)

	user_error_hint_loc = (By.XPATH,'//*[@id="generalForm"]/div/div[2]/div[1]/label/span[2]')
	pawd_error_hint_loc = (By.CSS_SELECTOR,"#generalForm > div > div.right_form > div:nth-child(2) > label > span.password_error.error")
	user_login_success_loc = (By.CSS_SELECTOR,'body > div.header > div.nav_top > div.nav_top_right > ul > li.users_login > a.nav_usertel')

	# 用户名错误提示
	def user_error_hint(self):
		return self.find_element(*self.user_error_hint_loc).text

	# 密码错误提示
	def pawd_error_hint(self):
		return self.find_element(*self.pawd_error_hint_loc).text

	# 登录成功用户名
	def user_login_success(self):
		return self.find_element(*self.user_login_success_loc).text