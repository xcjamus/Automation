#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/8/15 14:31
# @Author : jamus
# @File   : withdrawPage.py

from selenium.webdriver.common.by import By
from .base import Page
from .myAccountButtonPage import myAccountButton
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class withdraw(Page):
    '''用户提现界面'''
    url = '/'

    bgw_withdraw_button_loc = (By.CSS_SELECTOR,'#right_content > div > dl > dt.rig2_top > div.overview_title > div.con_btn > button.butom-iput.withdraw')

    # 进入提现页面
    def bgw_into_withdraw(self):
        myAccountButton(self.driver).bgw_into_view_account()
        self.find_element(*self.bgw_withdraw_button_loc).click()
        sleep(2)

    bgw_balance_loc = (By.CLASS_NAME,'color_font')
    bgw_withdraw_account_loc = (By.ID,'amount')
    bgw_withdraw_all_loc = (By.CLASS_NAME,'withdraw_all')
    bgw_withdraw_password_loc = (By.ID,'payPassword')
    bgw_withdraw_apply_button_loc = (By.CSS_SELECTOR,'#body > div.trade_wrap > div.withdraw > div > div:nth-child(6) > div > a')

    # 币港湾用户余额
    def bgw_user_balance(self):
        return self.find_element(*self.bgw_balance_loc).text

    # 输入提现金额
    def bgw_withdraw_amount(self,amount):
        self.find_element(*self.bgw_withdraw_account_loc).send_keys(amount)

    # 全部提现
    def bgw_withdraw_all(self):
        self.find_element(*self.bgw_withdraw_all_loc).click()

    # 输入交易密码
    def bgw_withdraw_password(self,password):
        self.find_element(*self.bgw_withdraw_password_loc).send_keys(password)

    # 立即提现
    def bgw_withdraw_now(self):
        self.find_element(*self.bgw_withdraw_apply_button_loc).click()

    # 定义统一的提现入口
    def bgw_withdraw(self,amount,password):
        self.bgw_into_withdraw()
        sleep(1)
        self.bgw_withdraw_amount(amount)
        self.bgw_withdraw_password(password)
        self.bgw_withdraw_now()
        sleep(1)

    # 定义统一的全部提现入口
    def bgw_all_withdraw(self,password=''):
        self.bgw_into_withdraw()
        self.bgw_withdraw_all()
        self.bgw_withdraw_password(password)
        self.bgw_withdraw_now()

    # 提现金额、交易密码错误提示
    withdraw_error_hint_loc = (By.CSS_SELECTOR,'#toast > span')

    def withdraw_error_hint(self):
        return self.find_element(*self.withdraw_error_hint_loc).text

    # 提现成功提示
    withdraw_succ_loc = (By.CSS_SELECTOR,'body > div.trade_result > div.trade_result_content > p:nth-child(1)')

    def withdraw_succ_hint(self):
        element = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.withdraw_succ_loc))
        return element.text


