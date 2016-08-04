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




def API_run(hotel_id,checkin_date,checkout_date):
	try:
		conn= pymysql.connect(user='root',db='primary_data')
		a=conn.cursor() 
		sql="select * from offer where hotel_id = '{hotel_id}' and checkin_date ='{checkin_date}' and checkout_date= '{checkout_date}'; "
		sql=sql.format(hotel_id=hotel_id,checkin_date=checkin_date,checkout_date=checkout_date)
		a.execute(sql)
		rows = a.fetchall()
		data={}
		for row in range(len(rows)):
			print ({'offerId':rows[row][1],'hotelId':rows[row][2],'checkinDate':rows[row][7],'checkoutDate':rows[row][8],'sellingPrice':rows[row][6],'currencyCode':rows[row][3]})
			data[row]={'offerId':rows[row][1],'hotelId':rows[row][2],'checkinDate':rows[row][7],'checkoutDate':rows[row][8],'sellingPrice':rows[row][6],'currencyCode':rows[row][3]}
		return data
	except:
		print ('MySQL connect failed')












