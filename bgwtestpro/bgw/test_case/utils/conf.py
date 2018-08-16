#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/8/15 13:08
# @Author : jamus
# @File   : conf.py.py
import configparser as cparser
import os

def read_conf():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/bgw/test_case')[0]
    file_path = base + '/data/config' + '/db_config.ini'

    cf = cparser.ConfigParser()
    cf.read(file_path)
    return cf


if __name__ == '__main__':
    cr = read_conf()
    host = cr.get("DATABASE", "host")
    print(host)


