# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:14:26 2020

@author: Ishan Nilotpal
"""

import pandas as pd
import matplotlib.pyplot as plt

def avg_data_2013():
    temp_i = 0
    average = []
    for rows in pd.read_csv('AQI/aqi2013.csv',chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='Invalid':
                    temp = float(i)
                    add_var = add_var+temp
        avg = add_var/24
        temp_i = temp_i+1
        
        average.append(avg)
    return average
    
def avg_data_2014():
    temp_i = 0
    average = []
    for rows in pd.read_csv('AQI/aqi2014.csv',chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='Invalid':
                    temp = float(i)
                    add_var = add_var+temp
        avg = add_var/24
        temp_i = temp_i+1
        
        average.append(avg)
    return average



def avg_data_2015():
    temp_i = 0
    average = []
    for rows in pd.read_csv('AQI/aqi2015.csv',chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='InVld' and i!='---':
                    temp = float(i)
                    add_var = add_var+temp
        avg = add_var/24
        temp_i = temp_i+1
        
        average.append(avg)
    return average

def avg_data_2016():
    temp_i = 0
    average = []
    for rows in pd.read_csv('AQI/aqi2016.csv',chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='Invalid':
                    temp = float(i)
                    add_var = add_var+temp
        avg = add_var/24
        temp_i = temp_i+1
        
        average.append(avg)
    return average    
    
def avg_data_2017():
    temp_i = 0
    average = []
    for rows in pd.read_csv('AQI/aqi2017.csv',chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='Invalid':
                    temp = float(i)
                    add_var = add_var+temp
        avg = add_var/24
        temp_i = temp_i+1
        
        average.append(avg)
    return average  

def avg_data_2018():
    temp_i = 0
    average = []
    for rows in pd.read_csv('AQI/aqi2018.csv',chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='Invalid':
                    temp = float(i)
                    add_var = add_var+temp
        avg = add_var/24
        temp_i = temp_i+1
        
        average.append(avg)
    return average

if __name__=="__main__":
    ist2013 = avg_data_2013()
    ist2014 = avg_data_2014()
    ist2015 = avg_data_2015()
    ist2016 = avg_data_2016()
    ist2017 = avg_data_2017()
    ist2018 = avg_data_2018()
    plt.plot(range(0,365),ist2013,label="2013 Data")
    plt.plot(range(0,364),ist2014,label="2014 Data")
    plt.plot(range(0,364),ist2018,label="2018 Data")
    
    