#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/8/10 16:58
# @Author : jamus
# @File   : myAccountButtonPage.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base import Page
from time import sleep

class myAccountButton(Page):
    '''我的账户按钮小界面'''
    url = '/'

    bgw_my_account_button_loc = (By.LINK_TEXT,'我的账户')
    bgw_view_account_button_loc = (By.LINK_TEXT, '账户总览')
    bgw_discounts_button_loc = (By.LINK_TEXT,'优惠券')
    bgw_plan_manage_button_loc = (By.LINK_TEXT, '计划管理')
    bgw_invite_friends_button_loc = (By.LINK_TEXT, '邀请好友')
    bgw_return_plan_button_loc = (By.LINK_TEXT, '回款计划')
    bgw_bank_card_button_loc = (By.LINK_TEXT, '银行卡')
    bgw_trans_tail_button_loc = (By.LINK_TEXT, '交易明细')
    bgw_secure_center_button_loc = (By.LINK_TEXT, '安全中心')

    # 进入我的账户—账户总览界面
    def bgw_move_to_my_account(self):
        above = self.find_element(*self.bgw_my_account_button_loc)
        ActionChains(self.driver).move_to_element(above).perform()
        sleep(1)
    # 进入账户总览
    def bgw_into_view_account(self):
        self.bgw_move_to_my_account()
        self.find_element(*self.bgw_view_account_button_loc).click()
        sleep(1)
    # 进入优惠券
    def bgw_into_discounts(self):
        self.bgw_move_to_my_account()
        self.find_element(*self.bgw_discounts_button_loc).click()
        sleep(1)
    # 进入计划管理
    def bgw_into_plan_manage(self):
        self.bgw_move_to_my_account()
        self.find_element(*self.bgw_plan_manage_button_loc).click()
        sleep(1)
    # 进入邀请好友
    def bgw_into_invite_friends(self):
        self.bgw_move_to_my_account()
        self.find_element(*self.bgw_invite_friends_button_loc).click()
        sleep(1)
    # 进入回款计划
    def bgw_into_return_plan(self):
        self.bgw_move_to_my_account()
        self.find_element(*self.bgw_return_plan_button_loc).click()
        sleep(1)
    # 进入银行卡
    def bgw_into_bank_card(self):
        self.bgw_move_to_my_account()
        self.find_element(*self.bgw_bank_card_button_loc).click()
        sleep(1)
    # 进入交易明细
    def bgw_into_trans_tail(self):
        self.bgw_move_to_my_account()
        self.find_element(*self.bgw_trans_tail_button_loc).click()
        sleep(1)
    # 进入安全中心
    def bgw_into_secure_center(self):
        self.bgw_move_to_my_account()
        self.find_element(*self.bgw_secure_center_button_loc).click()
        sleep(1)