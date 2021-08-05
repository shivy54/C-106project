import pandas as pd
import plotly.express as pe
import csv
import  numpy as np


  

def getDataSource(path,x,y):
    IcecreamSales = []
    Temperature = []
    print(IcecreamSales)
    print(Temperature)
    with open(path)as f:
        df = csv.DictReader(f)
        for rows in df:
            IcecreamSales.append(float(rows[x]))
            Temperature.append(float(rows[y]))
    return{'x':Temperature,'y': IcecreamSales}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource ['x'],dataSource ['y'])
    print(correlation[0,1])

def setup():
    print("What data's correlation do you wan to find? ")
    print("1: Cups of Coffee and Sleep time")
    print("2:Attendance and marks data")
    ans = input("Ans: ")
    path = ''
    x = ''
    y = ''
    if ans == "2":
        path = 'coffee.csv'
        x = 'Coffee'
        y = 'sleep'
    elif ans == "1":
        path = 'School.csv'
        x = 'Marks In Percentage'
        y = 'Days Present'
    else:
        print("Enter a valid number")
        exit()
    dataSource = getDataSource(path,x,y)
    findCorrelation(dataSource)
    
setup()