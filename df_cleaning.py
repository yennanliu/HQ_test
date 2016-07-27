

import pandas as pd, numpy as np 
%matplotlib inline
%pylab inline
import seaborn  as sns 


df=pd.read_csv('offer.csv')

df.columns = ['id',
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

df.describe()

# check how many NaN in columns in dataframe


df.isnull().sum()

'''

possible columns need to be cleaned : 
csv offer: df['sellings_price'] , df['offer_valid_to'], 
csv fx_rate: currency_rate,
'''














