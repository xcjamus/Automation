#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/8/9 16:05
# @Author : jamus
# @File   : topupPage.py

from selenium.webdriver.common.by import By
from .base import Page
from .myAccountButtonPage import myAccountButton
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class topup(Page):
    '''用户充值界面'''
    url = '/'

    bgw_topup_button_loc = (By.CLASS_NAME, 'recharge')

    # 进入充值页面
    def bgw_into_topup(self):
        myAccountButton(self.driver).bgw_into_view_account()
        self.find_element(*self.bgw_topup_button_loc).click()

    bgw_topup_amount_loc = (By.NAME,'rechargeAmount')
    bgw_topup_now_loc = (By.ID,'recharge_submit')
    # 银行定位
    bgw_topup_from_ICBC_loc = (By.XPATH,'/html/body/div[8]/div/div[3]/div[2]/div/div[1]/div/div[2]/img')
    bgw_topup_from_PSBC_loc = (By.XPATH,'/html/body/div[8]/div/div[3]/div[2]/div/div[2]/div/div[2]/img')
    bgw_topup_from_SPDB_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[3]/div/div[2]/img')
    bgw_topup_from_CGB_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[4]/div/div[2]/img')
    bgw_topup_from_CMBC_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[5]/div/div[2]/img')
    bgw_topup_from_ECITIC_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[6]/div/div[2]/img')
    bgw_topup_from_HXB_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[7]/div/div[2]/img')
    bgw_topup_from_PAB_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[8]/div/div[2]/img')
    bgw_topup_from_CEB_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[9]/div/div[2]/img')
    bgw_topup_from_CIB_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[10]/div/div[2]/img')
    bgw_topup_from_ABC_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[11]/div/div[2]/img')
    bgw_topup_from_BOC_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[12]/div/div[2]/img')
    bgw_topup_from_CCB_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[13]/div/div[2]/img')
    bgw_topup_from_BOCOM_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[14]/div/div[2]/img')
    bgw_topup_from_CMB_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[15]/div/div[2]/img')
    bgw_topup_from_BOB_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[16]/div/div[2]/img')
    bgw_topup_from_BOS_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[17]/div/div[2]/img')
    bgw_topup_from_BRCB_loc = (By.XPATH, '/html/body/div[8]/div/div[3]/div[2]/div/div[18]/div/div[2]/img')

    # 输入充值金额
    def bgw_topup_amount(self,amount):
        self.find_element(*self.bgw_topup_amount_loc).send_keys(amount)

    # 立即充值
    def bgw_topup_now(self):
        self.find_element(*self.bgw_topup_now_loc).click()

    # 定义统一充值入口
    def bgw_topup(self,amount):
        self.bgw_into_topup()
        self.bgw_topup_amount(amount)
        self.bgw_topup_now()
        sleep(1)

    # 网银支付
    # 中国工商银行
    def bwg_topup_bank_ICBC(self):
        self.find_element(*self.bgw_topup_from_ICBC_loc).click()
    # 中国邮政储蓄银行
    def bwg_topup_bank_PSBC(self):
        self.find_element(*self.bgw_topup_from_PSBC_loc).click()
    # 浦发银行
    def bwg_topup_bank_SPDB(self):
        self.find_element(*self.bgw_topup_from_SPDB_loc).click()
    # 广发银行
    def bwg_topup_bank_CGB(self):
        self.find_element(*self.bgw_topup_from_CGB_loc).click()
    # 中国民生银行
    def bwg_topup_bank_CMBC(self):
        self.find_element(*self.bgw_topup_from_CMBC_loc).click()
    # 中信银行
    def bwg_topup_bank_ECITIC(self):
        self.find_element(*self.bgw_topup_from_ECITIC_loc).click()
    # 华夏银行
    def bwg_topup_bank_HXB(self):
        self.find_element(*self.bgw_topup_from_HXB_loc).click()
    # 平安银行
    def bwg_topup_bank_PAB(self):
        self.find_element(*self.bgw_topup_from_PAB_loc).click()
    # 中国光大银行
    def bwg_topup_bank_CEB(self):
        self.find_element(*self.bgw_topup_from_CEB_loc).click()
    # 兴业银行
    def bwg_topup_bank_CIB(self):
        self.find_element(*self.bgw_topup_from_CIB_loc).click()
    # 中国农业银行
    def bwg_topup_bank_ABC(self):
        self.find_element(*self.bgw_topup_from_ABC_loc).click()
    # 中国银行
    def bwg_topup_bank_BOC(self):
        self.find_element(*self.bgw_topup_from_BOC_loc).click()
    # 中国建设银行
    def bwg_topup_bank_CCB(self):
        self.find_element(*self.bgw_topup_from_CCB_loc).click()
    # 交通银行
    def bwg_topup_bank_BOCOM(self):
        self.find_element(*self.bgw_topup_from_BOCOM_loc).click()
    # 招商银行
    def bwg_topup_bank_CMB(self):
        self.find_element(*self.bgw_topup_from_CMB_loc).click()
    # 北京银行
    def bwg_topup_bank_BOB(self):
        self.find_element(*self.bgw_topup_from_BOB_loc).click()
    # 上海银行
    def bwg_topup_bank_BOS(self):
        self.find_element(*self.bgw_topup_from_BOS_loc).click()
    # 北京农商银行
    def bwg_topup_bank_BRCB(self):
        self.find_element(*self.bgw_topup_from_BRCB_loc).click()

    topup_error_hint_loc = (By.CSS_SELECTOR,'#toast > span')

    # 输入金额错误提示
    def topup_error_hint(self):
        return self.find_element(*self.topup_error_hint_loc).text

    topup_final_loc = (By.ID,'sub_pay')

    # 充值
    def topup_pre(self):
        # js = 'window.scrollTo(0,document.body.scrollHeight);'
        js = 'window.scrollTo(0,400)'
        self.driver.execute_script(js)
        self.find_element(*self.topup_final_loc).click()
        sleep(1)

    topup_auth_loc = (By.ID,'mobileCode')
    topup_auth_button_loc = (By.ID,'code_sub')

    # 充值验证码输入
    def topup_auth_num(self,number):
        self.find_element(*self.topup_auth_loc).send_keys(number)

    def topup_auth_button(self):
        self.find_element(*self.topup_auth_button_loc).click()

    # 定义统一的充值验证码入口
    def topup_auth(self,number):
        self.topup_pre()
        sleep(2)
        self.topup_auth_num(number)
        sleep(4)
        self.topup_auth_button()
        sleep(1)

    # 充值成功页面
    topup_succ_loc = (By.CSS_SELECTOR,'body > div.trade_result > div.trade_result_content > p:nth-child(1)')

    def topup_succ(self):
        element = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.topup_succ_loc))
        return element.text

    # 充值金额超过单笔最大
    topup_over_once_loc = (By.CSS_SELECTOR,'#toast > span')

    def topup_over_once_hint(self):
        return self.find_element(*self.topup_over_once_loc).text