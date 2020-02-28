import numpy as np
import pandas as pd
import pandas.io.sql as psql
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib
import matplotlib.pyplot as plt

flag_groupings = pd.read_excel(flag_groupings_filepath)

class Hotel:
    def __init__(self, flag_groupings, input_brand, input_flag, input_rooms, input_type, specialty_service, input_occupancy_rate, input_revenue, revenue_period, input_profit, profit_type):
        self.brand = get_brand(input_brand)
        self.flag = input_flag
        self.num_rooms = input_rooms
        self.room_range = get_room_range(input_rooms)
        self.size_subset = get_size_subset(input_rooms)
        self.hotel_type = get_type(input_type)
        self.hotel_group = get_group(flag_groupings, input_brand, input_flag)
        self.specialty_service = is_specialty(specialty_service)
        self.occupancy_rate = get_occupancy_rate(input_occupancy_rate)
        self.revenue = get_monthly_revenue(input_revenue, revenue_period)
        self.profit_margin = get_profit_margin(input_profit, profit_type)

    def get_brand(input_brand):
        if input_brand == 'Apartment' | 'Retail':
            brand == 'Not Hotel'
        elif input_brand == 'Hilton':
            brand =='Hilto'
        elif input_brand == 'IHG - International Hotel Group':
            brand =='IHG'
        else:
            brand='Other'
        return brand
    
    def get_room_range(num_rooms):
        rooms_plus_ten = int(input_rooms + input_rooms*0.1)
        rooms_minus_ten = int(input_rooms - input_rooms*0.1)
        return room_range = range(size_minus_ten, size_plus_ten)

    def get_size_subset(num_rooms):
        if num_rooms <= 0:
            size_subset = 0 
        elif 0 < num_rooms < 80:
            size_subset = 1
        elif 80 <= num_rooms < 100:
            size_subset = 2
        elif 100 <= num_rooms < 150:
            size_subset = 3
        elif 150 <= num_rooms < 200:
            size_subset = 4
        else:
            size_subset = 5
        return size_subset 
    
    def hotel_type(flag_groupings, input_brand, input_flag):
       brand_mask = flag_groupings['Brand'] == input_brand
        flag_mask = flag_groupings['Flag'] == input_flag
        if input_brand isin ['Other', 'Retail', 'Apartment']:
            hotel_type = 'Not Hotel'
        else:
            group_df = flag_groupings[flag_mask]
            hotel_type = hotel_df['Type']
        return hotel_type
    
    def get_group(flag_groupings, input_brand, input_flag):
        brand_mask = flag_groupings['Brand'] == input_brand
        flag_mask = flag_groupings['Flag'] == input_flag
        if input_brand isin ['Other', 'Retail', 'Apartment']:
            hotel_group = 'Not Hotel'
        else:
            group_df = flag_groupings[flag_mask]
            hotel_group = hotel_df['Group']
        return hotel_group
        
    def is_specialty(input_specialty_service):
        if input_specialty_service == 'None':
            specialty_service = 'None'
        else:
            specialty_service = input_specialty_service
        return specialty_service

    def get_occupancy_rate(input_occupancy_rate):
        if input_occupancy_rate == 'Unsure'
            occupancy_rate = 0.68
        else:
            occupancy_rate = input_occupancy_rate
        return occupancy_rate

    def get_monthly_revenue(input_revenue, revenue_period):
        if input_revenue == 0:
            revenue = 'No Current Retail Revenue'
        elif revenue_period == 'Yearly':
            revenue = input_revenue/12
        elif revenue_period == 'Quarterly':
            revenue = input_revenue/4
        else:
            revenue = input_revenue
        return revenue

    # def get_profit_margin(input_profit, profit_type, input_revenue, revenue_period):
    #     if input_profit == 0 | input_revenue == 0:
    #         profit_margin = 'Not Currently Profitable'
    #     elif profit_type == 'Current Profit' & revenue_period == 'Yearly':
    #         profit_margin = (input_profit)
    #         elif revenue_period == 'Quarterly':
    #             revenue = input_revenue/4
    #         else:
    #             revenue = input_revenue 

if __name__ == "__main__":
    # brand = 'Hilto'
    # flag = 'Hilton
    # #rooms = 150
    # target_market = business_hotel
    # pass

 
