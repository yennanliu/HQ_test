
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
	engine_ = create_engine('mysql+pymysql://root@localhost/bi_data')
	query_valid_offers='''
			 SELECT o.id AS offer_id,
       o.hotel_id,
       o.sellings_price,
       o.sellings_price AS original_price,
       lst_currency.code AS original_currency_code,
       o.breakfast_included_flag,
       o.offer_valid_from AS valid_from_date,
       o.offer_valid_to AS valid_to_date
FROM offer o
JOIN lst_currency ON o.currency_id=lst_currency.id 
		 '''
	print (query_valid_offers)
	df = pd.read_sql_query(query_valid_offers, engine)
	df.to_sql('valid_offers', engine_, if_exists = 'append') 
	return df 

def hotel_offers():
	engine = create_engine('mysql+pymysql://root@localhost/primary_data')
	engine_ = create_engine('mysql+pymysql://root@localhost/bi_data')
	query_hotel_offers='''
		 SELECT o.hotel_id AS hotel_id,
       DATE(o.offer_valid_from) AS date,
       hour(o.offer_valid_from) AS hour,
       o.breakfast_included_flag,
       o.valid_offer_flag
FROM offer o
WHERE TO_SECONDS(o.offer_valid_to) - TO_SECONDS(o.offer_valid_from) < 3600 
		 '''
	print (query_hotel_offers)
	df = pd.read_sql_query(query_hotel_offers, engine)
	df.to_sql('hotel_offers', engine_, if_exists = 'append') 
	return df 

