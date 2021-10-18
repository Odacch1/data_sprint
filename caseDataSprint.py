import pandas as pd
import datetime

taxi_data_2009 = pd.read_json('data-sample_data-nyctaxi-trips-2009-json_corrigido.json',lines=True)
taxi_data_2010 = pd.read_json('data-sample_data-nyctaxi-trips-2010-json_corrigido.json',lines=True)
taxi_data_2011 = pd.read_json('data-sample_data-nyctaxi-trips-2011-json_corrigido.json',lines=True)
taxi_data_2012 = pd.read_json('data-sample_data-nyctaxi-trips-2012-json_corrigido.json',lines=True)

max_passenger_2_2009 = taxi_data_2009[taxi_data_2009['passenger_count'] <= 2]
max_passenger_2_2010 = taxi_data_2010[taxi_data_2010['passenger_count'] <= 2]
max_passenger_2_2011 = taxi_data_2011[taxi_data_2011['passenger_count'] <= 2]
max_passenger_2_2012 = taxi_data_2012[taxi_data_2012['passenger_count'] <= 2]

mean_2009 = (max_passenger_2_2009['trip_distance'].mean())
mean_2010 = (max_passenger_2_2010['trip_distance'].mean())
mean_2011 = (max_passenger_2_2011['trip_distance'].mean())
mean_2012 = (max_passenger_2_2012['trip_distance'].mean())

mean_all = (mean_2009 + mean_2010 + mean_2011 + mean_2012)/4

print(mean_all)

taxi_data_2009['pickup_datetime'] = pd.to_datetime(taxi_data_2009['pickup_datetime'])
taxi_data_2010['pickup_datetime'] = pd.to_datetime(taxi_data_2010['pickup_datetime'])
taxi_data_2011['pickup_datetime'] = pd.to_datetime(taxi_data_2011['pickup_datetime'])
taxi_data_2012['pickup_datetime'] = pd.to_datetime(taxi_data_2012['pickup_datetime'])

taxi_data_2009['pickup_month'] = taxi_data_2009['pickup_datetime'].dt.month
taxi_data_2010['pickup_month'] = taxi_data_2010['pickup_datetime'].dt.month
taxi_data_2011['pickup_month'] = taxi_data_2011['pickup_datetime'].dt.month
taxi_data_2012['pickup_month'] = taxi_data_2012['pickup_datetime'].dt.month

taxi_data_2009['pickup_day'] = taxi_data_2009['pickup_datetime'].dt.date
taxi_data_2010['pickup_day'] = taxi_data_2010['pickup_datetime'].dt.date
taxi_data_2011['pickup_day'] = taxi_data_2011['pickup_datetime'].dt.date
taxi_data_2012['pickup_day'] = taxi_data_2012['pickup_datetime'].dt.date

sum_2009 = taxi_data_2009.groupby('vendor_id')
sum_2009 = sum_2009.sum()
sum_2009['total_amount'].plot()

sum_2010 = taxi_data_2010.groupby('vendor_id')
sum_2010 = sum_2010.sum()
sum_2010['total_amount'].plot()

sum_2011 = taxi_data_2011.groupby('vendor_id')
sum_2011 = sum_2011.sum()
sum_2011['total_amount'].plot()

sum_2012 = taxi_data_2012.groupby('vendor_id')
sum_2012 = sum_2012.sum()
sum_2012['total_amount'].plot()

trips_cash_2009 = taxi_data_2009[taxi_data_2009['payment_type'].str.lower().isin(['cash', 'cas', 'csh'])]
trips_cash_2009.hist('pickup_month')
trips_cash_2010 = taxi_data_2010[taxi_data_2010['payment_type'].str.lower().isin(['cash', 'cas', 'csh'])]
trips_cash_2010.hist('pickup_month')
trips_cash_2011 = taxi_data_2011[taxi_data_2011['payment_type'].str.lower().isin(['cash', 'cas', 'csh'])]
trips_cash_2011.hist('pickup_month')
trips_cash_2012 = taxi_data_2012[taxi_data_2012['payment_type'].str.lower().isin(['cash', 'cas', 'csh'])]
trips_cash_2012.hist('pickup_month')

tips_2012 = taxi_data_2012[taxi_data_2012['tip_amount'] > 0]
tips_2012 = tips_2012[tips_2012['pickup_month'] >= 10]
tips_2012 = tips_2012.groupby('pickup_day')
tips_2012 = tips_2012['pickup_day'].count()

tips_2012.plot()
