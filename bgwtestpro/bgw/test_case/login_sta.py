import unittest
import sys
sys.path.append('./models')
sys.path.append('./page_obj')
from models import myunit,screenshot
from page_obj.loginPage import login
import random
from time import sleep

@unittest.skip('跳过测试该类')
class loginTest(myunit.MyTest):
	'''币港湾登录测试'''

	# 测试用户登录
	def user_login_verify(self, username='', password=''):
		login(self.driver).user_login(username, password)
		sleep(1)

	# @unittest.skip('')
	def test_login1(self):
		'''用户名、密码为空登录'''
		self.user_login_verify()
		po = login(self.driver)
		self.assertEqual(po.user_error_hint(), '账号不能为空！')
		screenshot.insert_img(self.driver, 'user_pawd_empty.png')

	# @unittest.skip('')
	def test_login2(self):
		'''用户名正确，密码为空登录'''
		self.user_login_verify(username='13362185609')
		po = login(self.driver)
		self.assertEqual(po.pawd_error_hint(), '密码不能为空！')
		screenshot.insert_img(self.driver, 'pawd_empty.png')

	# @unittest.skip('')
	def test_login3(self):
		'''用户名为空，密码正确'''
		self.user_login_verify(password='123321')
		po = login(self.driver)
		self.assertEqual(po.user_error_hint(), '账号不能为空！')
		screenshot.insert_img(self.driver, 'user_empty.png')

	# @unittest.skip('')
	def test_login4(self):
		'''用户名不匹配'''
		character = random.choice('1234567890')
		username = '13362185609' + character
		self.user_login_verify(username=username, password='123321')
		po = login(self.driver)
		self.assertEqual(po.user_error_hint(), '当前账号不存在，请先注册！')
		screenshot.insert_img(self.driver, 'user_error.png')

	# @unittest.skip('')
	def test_login5(self):
		'''密码长度不匹配'''
		self.user_login_verify(username='13362185609', password='12332')
		po = login(self.driver)
		self.assertEqual(po.pawd_error_hint(), '请输入6-16位密码！')
		screenshot.insert_img(self.driver, 'pawd_short_error.png')

	# @unittest.skip('')
	def test_login6(self):
		'''密码不匹配'''
		self.user_login_verify(username='13362185609', password='1233213')
		po = login(self.driver)
		self.assertEqual(po.pawd_error_hint(), '账号或密码错误！')
		screenshot.insert_img(self.driver, 'pawd_error.png')

	# @unittest.skip('')
	def test_login7(self):
		'''用户名、密码正确'''
		self.user_login_verify(username='13362185609', password='123321')
		sleep(2)
		po = login(self.driver)
		self.assertEqual(po.user_login_success(), '133****5609')
		screenshot.insert_img(self.driver, 'user_pawd_ture.png')

if __name__ == '__main__':
	unittest.main()