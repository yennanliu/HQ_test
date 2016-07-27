

import pymysql
from pymysql import * 
from sqlalchemy import create_engine
import datetime as dt   
import time
import csv
import pandas as pd, numpy as np
import pprint




def insert_data_df_local_mysql(csvname):
	try:
		# db = HQ_test, table = csvname 
		engine = create_engine('mysql+pymysql://root@localhost/HQ_test')
		df=pd.read_csv('%s.csv'%csvname)
		df.to_sql(csvname, engine, if_exists = 'append')
		print ('insert df OK')
	except:
		print ('insert df failed')














