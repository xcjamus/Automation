import unittest
import sys
sys.path.append('./models')
sys.path.append('./page_obj')
from models import myunit,screenshot
from page_obj.loginPage import login
from page_obj.topupPage import topup
from time import sleep
import random

@unittest.skip('')
class topupTest(myunit.MyTest):
    '''币港湾充值测试'''
    def user_topup_verify(self,account=''):
        login(self.driver).user_login()
        topup(self.driver).bgw_topup(account)

    # @unittest.skip('')
    def test_topup1(self):
        '''充值金额为空'''
        self.user_topup_verify()
        po = topup(self.driver)
        self.assertEqual(po.topup_error_hint(),'请填写充值金额')
        screenshot.insert_img(self.driver, 'topup_empty.png')

    # @unittest.skip('')
    def test_topup2(self):
        '''充值金额小于10'''
        account = random.choice('1234567890')
        self.user_topup_verify(account)
        po = topup(self.driver)
        self.assertEqual(po.topup_error_hint(),'充值金额不能低于10元')
        screenshot.insert_img(self.driver, 'topup_less_10.png')

    def test_topup3(self):
        '''充值金额超过单笔最大'''
        self.user_topup_verify(account = '50001')
        po = topup(self.driver)
        sleep(1)
        po.topup_pre()
        self.assertEqual(po.topup_over_once_hint(), '输入金额超过银行的单笔限额！')
        screenshot.insert_img(self.driver, 'topup_over_once.png')

    # @unittest.skip('')
    def test_topup4(self):
        '''充值金额正确'''
        self.user_topup_verify(account = '100')
        po = topup(self.driver)
        sleep(1)
        po.topup_auth(number='123456')
        sleep(3)
        self.assertEqual(po.topup_succ(), '币港湾已收到您的充值申请，正在处理中，请稍等')
        screenshot.insert_img(self.driver, 'topup_succ.png')

if __name__ == '__main__':
	unittest.main()