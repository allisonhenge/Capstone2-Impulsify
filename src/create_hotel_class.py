import numpy as np
import pandas as pd
import pandas.io.sql as psql
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib
import matplotlib.pyplot as plt
import openpyxl

class Hotel:
    def __init__(self, data, brand, size):
        self.cleaned_data = data
        self.brand = brand
        pass

    def get_brand_subset(self.data, brand):
        brand_subset = cleaned_data.loc['Brand'== brand]
        pass

    def size(self.data, brand, size):
        ### these sizes probably need adjustment
        boutique_hotel = brand_subset.loc[['#Rooms'] <= 100]
        small_hotel = brand_subset[(brand_subset['#Rooms'] >100) & (brand_subset['#Rooms'] <= 200)]
        medium_hotel = brand_subset[(brand_subset['#Rooms'] >200) & (brand_subset['#Rooms'] <= 400)]
        large_hotel = brand_subset[(brand_subset['#Rooms'] >400) & (brand_subset['#Rooms'] <= 600)]
        xlarge_hotel = brand_subset[(brand_subset['#Rooms'] >600) & (brand_subset['#Rooms'] <= 1000)]
        xxlarge_hotel = brand_subset.loc[brand_subset['#Rooms'] > 1000]
        pass

    def target_market(self.data, brand, target_market):
        #these are my best guesses for target_market categories - from "setupmyhotel.com"
        business_hotel
        airport_hotel
        suite_hotel
        extended_stay_hotel
        serviced_apartments
        resort_hotels
        b_and_b_type
        timeshare_vacation_rental
        casino_hotels
        conference_convention_centers
        pass 

    def level_of_service():
        #maybe more classes?? I think these are different in impulsify's data == type?
        world_class_service
        mid_range_service
        budget_limited_service
        pass

if __name__ == "__main__":
    filepath = '../data/2019_sales_by_month.xlsx'
    # data = clean_2019_perf(filepath)
    # brand = 'Hilto'
    # size = 150
    # target_market = business_hotel
    # pass


