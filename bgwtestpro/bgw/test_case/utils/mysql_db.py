#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time   : 2018/8/15 10:36
# @Author : jamus
# @File   : mysql_db.py.py
import pymysql
from .conf import  read_conf as rc

class DB:
    def __init__(self):
        self.host = rc().get('DATABASE','host')
        self.port = int(rc().get('DATABASE','port'))
        self.db = rc().get('DATABASE','db_name')
        self.user = rc().get('DATABASE','user')
        self.password = rc().get('DATABASE','password')
        try:
            self.con = pymysql.connect(host = self.host,
                                       port = self.port,
                                       db = self.db,
                                       user = self.user,
                                       password = self.password
                                       )
            self.c = self.con.cursor()
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def query(self,statement):
        self.c.execute(statement)
        rows = self.c.fetchall()
        return rows


if __name__ == '__main__':
    db = DB()
    statement = 'select * from bs_auth where mobile = 13362185609'
    print(db.query(statement))
    print(db.query(statement)[0][3])