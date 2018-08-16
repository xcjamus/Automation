#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/8/15 18:59
# @Author : jamus
# @File   : purchasePage.py

from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class purchase(Page):
    '''用户购买界面'''
    url = '/'

    # 进入产品列表页
    bgw_pro_list_button_loc = (By.CSS_SELECTOR, 'body > div.header > div.nav_bottom > div > div.header_main_nav > ul > li:nth-child(2) > a')

    def bgw_into_pro_list(self):
        self.find_element(*self.bgw_pro_list_button_loc).click()
        sleep(2)

    # 进入产品详情
    bgw_pro_detail_button_loc = (By.CSS_SELECTOR,'body > div.main > div.main_down > ul:nth-child(1) > li:nth-child(1) > div > div > div.md_btn > a')

    def bgw_pro_detail(self):
        js = 'window.scrollTo(0,200)'
        self.driver.execute_script(js)
        self.find_element(*self.bgw_pro_detail_button_loc).click()
        sleep(1)

    # 购买金额
    bgw_purchase_money_loc = (By.ID,'money')
    bgw_purchase_button_loc = (By.ID,'gotobuy_btn')

    def bgw_purchase_money(self,money):
        self.find_element(*self.bgw_purchase_money_loc).send_keys(money)

    def bgw_purchase_button(self):
        self.find_element(*self.bgw_purchase_button_loc).click()
        sleep(2)

    # 定义统一的购买入口
    def bgw_goto_purchase(self,money):
        self.bgw_into_pro_list()
        self.bgw_pro_detail()
        self.bgw_purchase_money(money)
        self.bgw_purchase_button()

    # 金额输入错误提示
    purchase_error_hint_loc = (By.CSS_SELECTOR,'#toast > span')

    def purchase_error_hint(self):
        return self.find_element(*self.purchase_error_hint_loc).text

    # 购买预下单
    bgw_purchase_join_button_loc = (By.CSS_SELECTOR,'body > div.main > div > div > div.Use_redbtn > a')

    def purchase_join(self):
        js = 'window.scrollTo(0,350)'
        self.driver.execute_script(js)
        self.find_element(*self.bgw_purchase_join_button_loc).click()
        sleep(2)

    # 输入验证码
    bgw_purchase_mobile_loc = (By.ID,'mobileCode')
    bgw_purchase_mobile_button_loc = (By.CSS_SELECTOR,'#alert_listthree_three > div > div.alert_listthree_btnd > a')

    def purchase_mobile_in(self,mobilecode):
        self.find_element(*self.bgw_purchase_mobile_loc).send_keys(mobilecode)
        sleep(5)

    def purchase_mobile_button(self):
        self.find_element(*self.bgw_purchase_mobile_button_loc).click()
        sleep(2)

    # 定义统一的验证码入口
    def purchase_mobile(self,mobilecode):
        self.purchase_join()
        self.purchase_mobile_in(mobilecode)
        self.purchase_mobile_button()

    # 验证码错误提示
    mobilecode_error_hint_loc = (By.CSS_SELECTOR,'#toast > span')

    def mobilecode_error_hint(self):
        return self.find_element(*self.mobilecode_error_hint_loc).text

    # 购买成功提示
    purchase_succ_hint_loc = (By.CSS_SELECTOR,'body > div.con_gmcg > div > div > p:nth-child(1)')

    def purchase_succ_hint(self):
        element = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.purchase_succ_hint_loc))
        return element.text

