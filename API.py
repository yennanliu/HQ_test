#ref : http://www.anthonydebarros.com/2012/03/11/generate-json-from-sql-using-python/

#ref : https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html

#ref : http://bottlepy.org/docs/dev/tutorial_app.html

#ref : https://strendly.wordpress.com/2015/10/28/how-to-build-an-api-with-python-and-flask/

#ref :http://flask.pocoo.org/docs/0.11/quickstart/#url-building

#ref : http://flask.pocoo.org/docs/0.10/api/#flask.json.jsonify


import pymysql
from pymysql import * 
from sqlalchemy import create_engine
import datetime as dt   
import time
import pandas as pd, numpy as np
import pprint








def API_test():
	try:
		conn= pymysql.connect(user='root',db='primary_data')
		a=conn.cursor()
		sql='select * from offer limit 10 ; '
		a.execute(sql)
		rows = a.fetchall()
		for row in range(len(rows)):
			print ({'offerId':rows[row][1],'hotelId':rows[row][2],'checkinDate':rows[row][7],'checkoutDate':rows[row][8],'sellingPrice':rows[row][6],'currencyCode':rows[row][3]})
		
	except:
		print ('MySQL connect failed')




def API_run(offerId):
	try:
		conn= pymysql.connect(user='root',db='primary_data')
		a=conn.cursor()
		sql="select * from offer where id = '{offerId}' limit 10 ; "
		sql=sql.format(offerId=offerId)
		a.execute(sql)
		rows = a.fetchall()
		for row in range(len(rows)):
			print ({'offerId':rows[row][1],'hotelId':rows[row][2],'checkinDate':rows[row][7],'checkoutDate':rows[row][8],'sellingPrice':rows[row][6],'currencyCode':rows[row][3]})
		
	except:
		print ('MySQL connect failed')








