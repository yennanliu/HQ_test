

import pandas as pd, numpy as np 
%matplotlib inline
%pylab inline
import seaborn  as sns 
import pymysql
from pymysql import * 
from sqlalchemy import create_engine
import datetime as dt   
import time
import csv
import pprint


offer=pd.read_csv('offer.csv')

offer.columns = ['id',
			'hotel_id',
			'currency_id',
			'source_system_code', 
			'available_cnt', 
			'sellings_price',
			'checkin_date',
			'checkout_date',
			'valid_offer_flag', 
			'offer_valid_from',
			'offer_valid_to', 
			'breakfast_included_flag', 
			'insert_datetime' ]

offer.describe()

# check how many NaN in columns in dataframe


offer.isnull().sum()

'''

possible columns need to be cleaned : 
csv offer: offer['sellings_price'] , df['offer_valid_to'], 

'''



def offer_cleaning():
	engine = create_engine('mysql+pymysql://root@localhost/primary_data')
	query_offer_clean='''
			 SELECT 
			 *
			FROM offer o
			where year(o.offer_valid_to) - year(o.offer_valid_from) < 100 
			and available_cnt >= 0
			and sellings_price >= 0 
			and valid_offer_flag >= 0 
			and breakfast_included_flag >= 0 
			limit 1000

		 '''
	print (query_offer_clean)
	df = pd.read_sql_query(query_offer_clean, engine)
	return df 









