import os
import pandas as pd
import csv
import pymysql.cursors
from zipfile import ZipFile


# read the user input
file_name = input('input the path of your filename')

# read file and do data processing
def read_file(file_name):

    #nest a conditional for connection

    if file_name.endswith('.zip') :
        with ZipFile(file_name, 'r') as zip:
            print(zip.extractall())
            #look for the file that ends with csv format

    elif file_name.endswith('.csv'):
        data = pd.read_csv(file_name)
        data_frame = pd.DataFrame(data)

    else:
        print('Sorry insert a zip file or a csv file')


def sql_insertion(processed_file):
    query1 = 'INSERT INTO .... where'
    query2 = 'INSERT INTO .... where'
    query3 = 'INSERT INTO ... where'
    #making sure
    check_query = 'select * from ... where ...'



"""
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='',
                             database='db',
                             cursorclass=pymysql.cursors.DictCursor,
                             autocommit=True)
"""








