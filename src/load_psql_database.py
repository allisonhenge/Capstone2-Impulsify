import psycopg2
import sys, os
import numpy as np
import pandas as pd
import db_credentials as creds
import pandas.io.sql as psql

#Set up a connection to the postgres server
conn_string = 'dbname='+ creds.PGDATABASE +' user='+ creds.PGUSER +' host='+ creds.PGHOST

conn=psycopg2.connect(conn_string)
print("Connected!")

#Create a cursor object
cursor = conn.cursor()

def load_pd_dataframe(table, schema='public'):
    sql_command = "SELECT * FROM {}.{};".format(str(schema), str(table))
    print(sql_command)
    
    #Load the data
    data = pd.read_sql(sql_command, conn)
    print(data.shape)
    return data


if __name__ == "__main__":
    # properties = load_pd_dataframe('properties')
    # print(properties)
    pass