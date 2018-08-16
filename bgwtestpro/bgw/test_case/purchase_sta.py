#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/8/15 14:26
# @Author : jamus
# @File   : purchase_sta.py

import sys
sys.path.append('./models')
sys.path.append('./page_obj')
sys.path.append('./utils')
from models import myunit,screenshot
from page_obj.loginPage import login
from page_obj.purchasePage import purchase
from utils.mysql_db import DB
import unittest,random

@unittest.skip('')
class purchaseTest(myunit.MyTest):
    '''币港湾购买测试'''
    def user_purchase_verify(self,money=''):
        login(self.driver).user_login()
        purchase(self.driver).bgw_goto_purchase(money)

    def get_mobilecode(self):
        statement = 'select * from bs_auth where mobile = 13362185609'
        rows = DB().query(statement)
        for row in rows:
            return row[3]

    # @unittest.skip('')
    def test_purchase1(self):
        '''购买金额为空'''
        self.user_purchase_verify()
        po = purchase(self.driver)
        self.assertEqual(po.purchase_error_hint(),'请输入您要加入的金额')
        screenshot.insert_img(self.driver, 'purchase_empty.png')

    # @unittest.skip('')
    def test_purchase2(self):
        '''购买金额错误'''
        self.user_purchase_verify(money='99')
        po = purchase(self.driver)
        self.assertEqual(po.purchase_error_hint(), '加入金额只能为100的整数倍')
        screenshot.insert_img(self.driver, 'purchase_error.png')

    # @unittest.skip('')
    def test_purchase3(self):
        '''验证码为空'''
        self.user_purchase_verify(money='1000')
        po = purchase(self.driver)
        po.purchase_mobile(mobilecode='')
        self.assertEqual(po.mobilecode_error_hint(), '验证码不能为空！')
        screenshot.insert_img(self.driver, 'purchase_mobile_empty.png')

    # @unittest.skip('')
    def test_purchase4(self):
        '''验证码格式错误'''
        self.user_purchase_verify(money='1000')
        po = purchase(self.driver)
        mobilecode = random.randint(100,999)
        po.purchase_mobile(mobilecode)
        self.assertEqual(po.mobilecode_error_hint(), '验证码格式有误！')
        screenshot.insert_img(self.driver, 'purchase_mobile_format_error.png')

    # @unittest.skip('')
    def test_purchase5(self):
        '''验证码错误'''
        self.user_purchase_verify(money='1000')
        po = purchase(self.driver)
        mobilecode = random.randint(1000,9999)
        po.purchase_mobile(mobilecode)
        self.assertEqual(po.mobilecode_error_hint(), '手机验证码不正确，请重新验证！')
        screenshot.insert_img(self.driver, 'purchase_mobile_error.png')

    # @unittest.skip('')
    def test_purchase6(self):
        '''购买成功'''
        self.user_purchase_verify(money='1000')
        po = purchase(self.driver)
        po.purchase_join()
        mobilecode = self.get_mobilecode()
        po.purchase_mobile_in(mobilecode)
        po.purchase_mobile_button()
        self.assertIn('币港湾已收到您的申购申请，正在处理中',po.purchase_succ_hint())
        screenshot.insert_img(self.driver, 'purchase_succ.png')

if __name__ == '__main__':
    unittest.main()