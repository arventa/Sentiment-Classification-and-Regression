# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:56:37 2018

@author: user
"""

import csv
with open ('dataset.csv','r') as csvfile:
    reader=csv.reader(csvfile)
    next(reader)
#    to_db=[(x[0],x[1],x[2],x[3] for x in reader ]

import MySQLdb
con=MySQLdb.connect(host='127.0.0.1', port=3306, user='root', db='csv_db', charset='utf8')
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS dataset (id_str varchar(18), time_laps date, text varchar(153), sentiment(8));")
cur.executemany("INSERT INTO dataset VALUES(%s %s %s %s)", reader)