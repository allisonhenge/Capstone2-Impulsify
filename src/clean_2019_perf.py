import numpy as np
import pandas as pd
import pandas.io.sql as psql
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib
import matplotlib.pyplot as plt
import openpyxl

'''
WAS THINKING THIS COULD BE USED ACROSS MULTIPLE DATASETS BUT IT SEEMS AS IF IT WOULD BE HEAVILY 
DEPENDANT ON FEATURE NAMES.... NEED TO EXTRACT COLUMN NAMES FROM ANY INPUT DATA TO THEN SORT BY
BUT ALSO NEED TO BE ABLE TO IDENTIFY WHICH ARE MEANINGFUL. IF IT WAS ONLY USED IN APPLICATION BY 
IMPULSIFY AND EVERY YEAR NONE OF THE METRICS CHANGED AND THE EXCEL FILE HAD THE SAME COLUMN DATA 
IT COULD WORK. WOULD NEED TO MAKE SURE THE MANUAL ENTRY OPTIONS ARE GONE AND THERE IS A DROP DOWN 
MENU FOR BRAND AND TYPE.
'''

#import raw excel file
performance_raw = pd.read_excel(filepath)

#drop all rows without a property code (this could be done with another feature maybe?)
dropping_nans = performance_raw.dropna(subset=['Property Code'])

#replace duplicates
#THIS IS VERY SPECIFIC TO THE ONE DATASET RIGHT NOW... NEED TO 
#CODE FOR APPLICATION TO ANY DATASET IN THE FUTURE 
dropping_nans.replace(to_replace='Tru B', value='Tru b', inplace=True)
dropping_nans.replace(to_replace='TRU B', value='Tru b', inplace=True)
dropping_nans.replace(to_replace='TRU b', value='Tru b', inplace=True)

#change month of reporting to an integer for plotting
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
value = 1
for month in months:
    dropping_nans.replace(to_replace=month, value=value, inplace=True)
    value+=1

#create sorted revenue and profit dataframe
revenue_and_profit_columns = ['Property Name', 'Property Code', 'Brand', '#Rooms', 'Revenue', 'Profit Margin', 'Month of Reporting']
rev_and_prof_df = dropping_nans[revenue_and_profit_columns].sort_values(['Brand', 'Property Code', 'Month of Reporting', '#Rooms'])


if __name__ == "__main__":
    filepath = '../data/2019_sales_by_month.xlsx'

    pass