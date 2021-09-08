# -*- coding: utf-8 -*-
"""
@author: anitecki
"""

import pandas as pd
import pandas.api.types as types
from sqlalchemy import create_engine
from sqlalchemy.types import DateTime
from sqlalchemy.dialects.postgresql import *


inputfilepath = r'C:\\Users\\aniteck\\Downloads\\FoodaPython\\'

def tester(inputfilepath):

    
    df = pd.read_csv(inputfilepath + 'event_finance_customer_order_line_items.csv', sep =',', index_col=False, encoding = 'utf-8')
    print('csv file read')

#unit testing for missing values
    assert df['id'].isna().sum()<1 
    assert df['customer_order_id'].isna().sum()<1 
    assert df['event_id'].isna().sum()<1 
    assert df['event_type'].isna().sum()<1 
    assert df['created_at'].isna().sum()<1 
    assert df['updated_at'].isna().sum()<1 
    
#duplicate testing in id values
    assert len(df['id'].unique())==df.shape[0]
    
#Unit Testing data types brought in(these will likely be changed later on)
    assert types.is_int64_dtype(df['id'])
    assert types.is_object_dtype(df['customer_order_id'])
    assert types.is_int64_dtype(df['event_id'])
    assert types.is_object_dtype(df['event_type'])
    assert types.is_object_dtype(df['line_item_id'])
    assert types.is_float_dtype(df['deleted_at'])
    assert types.is_object_dtype(df['created_at'])
    assert types.is_object_dtype(df['updated_at'])
    print('testing complete')

def main(inputfilepath):
    try:
        
        df = pd.read_csv(inputfilepath + 'event_finance_customer_order_line_items.csv', sep =',', index_col=False, encoding = 'utf-8')
        print('csv file read')

        engine = create_engine('postgresql://anitecki:NpFDWDCWXUfMmDqNgmj2Q9fqv6M7Gjfj@dsa-candidate-challenge-anitecki.cxoih28cgprt.us-west-2.rds.amazonaws.com:5432/customer_transactions')
        df.to_sql('event_finance_customer_order_line_items', engine, index=False, dtype={'customer_order_id': VARCHAR(length=128),
        'line_item_id': VARCHAR(length=128),
        'deleted_at': DateTime(),
        'created_at': DateTime(),
        'updated_at': DateTime()})
        print('connection and data inserted')

    except Exception as e:
            print(e)
            
if __name__ == '__main__':
    tester(inputfilepath)
    main(inputfilepath)