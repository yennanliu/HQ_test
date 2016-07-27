
import pymysql
from pymysql import * 
from sqlalchemy import create_engine
import datetime as dt   
import time
import csv
import pandas as pd, numpy as np
import pprint



def valid_offers():
	engine = create_engine('mysql+pymysql://root@localhost/primary_data')
	query_valid_offers='''
			 SELECT 
			 o.id as offer_id,
			 o.hotel_id,
			 o.sellings_price, 
			 o.sellings_price as original_price,
			 lst_currency.code as original_currency_code,
			 o.breakfast_included_flag,
			 o.offer_valid_from as valid_from_date,
			 o.offer_valid_to as valid_to_date
			 from offer o
			 join lst_currency on o.currency_id=lst_currency.id
			 limit 10 
		 '''
	print (query_valid_offers)
	df = pd.read_sql_query(query_valid_offers, engine)
	return df 

def hotel_offers():
	engine = create_engine('mysql+pymysql://root@localhost/primary_data')
	query_hotel_offers='''
		
			 
		 '''
	print (query_hotel_offers)
	df = pd.read_sql_query(query_hotel_offers, engine)
	return df 





