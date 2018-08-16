#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/8/15 14:27
# @Author : jamus
# @File   : withdraw_sta.py
import sys
sys.path.append('./models')
sys.path.append('./page_obj')
from models import myunit,screenshot
from page_obj.loginPage import login
from page_obj.withdrawPage import withdraw
import unittest,random
from time import sleep

@unittest.skip('')
class withdrawTest(myunit.MyTest):
    '''币港湾提现测试'''

    # 普通提现
    def user_withdraw_verify(self,amount = '',password = ''):
        login(self.driver).user_login()
        withdraw(self.driver).bgw_withdraw(amount,password)

    # 全部提现
    def user_withdraw_all_verify(self,password=''):
        login(self.driver).user_login()
        withdraw(self.driver).bgw_all_withdraw(password)

    # @unittest.skip('')
    def test_withdraw1(self):
        '''提现金额，交易密码为空'''
        self.user_withdraw_verify()
        po = withdraw(self.driver)
        self.assertEqual(po.withdraw_error_hint(),'亲，请输入提现金额')
        screenshot.insert_img(self.driver, 'withdraw_empty.png')

    # @unittest.skip('')
    def test_withdraw2(self):
        '''提现金额正确，交易密码为空'''
        self.user_withdraw_verify(amount= '100')
        po = withdraw(self.driver)
        self.assertEqual(po.withdraw_error_hint(),'亲，请输入交易密码')
        screenshot.insert_img(self.driver, 'withdraw_password_empty.png')

    # @unittest.skip('')
    def test_withdraw3(self):
        '''提现金额为空，交易密码正确'''
        self.user_withdraw_verify(password='123456')
        po = withdraw(self.driver)
        self.assertEqual(po.withdraw_error_hint(), '亲，请输入提现金额')
        screenshot.insert_img(self.driver, 'withdraw_amount_empty.png')

    # @unittest.skip('')
    def test_withdraw4(self):
        '''提现金额错误，交易密码正确'''
        character = random.randint(1,1000)
        print(character)
        amount = '0' + str(character)
        self.user_withdraw_verify(amount = amount, password= '123456')
        po = withdraw(self.driver)
        self.assertEqual(po.withdraw_error_hint(), '提现金额格式不正确')
        screenshot.insert_img(self.driver, 'withdraw_amount_error.png')

    # @unittest.skip('')
    def test_withdraw5(self):
        '''提现金额正确，交易密码错误'''
        self.user_withdraw_verify(amount = '100', password = '12345')
        sleep(2)
        po = withdraw(self.driver)
        self.assertIn('交易密码有误，请重新输入（还有次机会）',po.withdraw_error_hint())
        screenshot.insert_img(self.driver, 'withdraw_amount_empty.png')

    # @unittest.skip('')
    def test_withdraw6(self):
        '''提现金额正确，交易密码正确'''
        self.user_withdraw_verify(amount = '100', password = '123456')
        po = withdraw(self.driver)
        self.assertEqual(po.withdraw_succ_hint(),'币港湾已收到您的提现申请，正在处理中')
        screenshot.insert_img(self.driver,'withdraw_succ.png')

    @unittest.skip('')
    def test_withdraw7(self):
        '''全部提现'''
        self.user_withdraw_all_verify(password='123456')
        po = withdraw(self.driver)
        self.assertEqual(po.withdraw_succ_hint(), '币港湾已收到您的提现申请，正在处理中')
        screenshot.insert_img(self.driver, 'withdraw_succ_all.png')

if __name__ == '__main__':
	unittest.main()



