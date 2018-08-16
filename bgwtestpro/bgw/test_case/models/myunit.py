import unittest
from .driver import browser

class MyTest(unittest.TestCase):
	def setUp(self):
		self.driver = browser()
		self.driver.maximize_window()
		self.driver.implicitly_wait(10)
		
	def tearDown(self):
		self.driver.quit()