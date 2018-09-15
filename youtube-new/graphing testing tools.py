# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 11:32:30 2018

@author: DELL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy import optimize

"""
Change three integers representing the date uploaded to the no. of days the video has 
has been uploaded for
"""
def monthday_array():
    """
    helper function for days_uploaded
    """
    monthday = [31,0]
    for i in range(7,0,-1):
        if i % 2 == 1:
            monthday.insert(0,monthday[0] + 31)
        elif i == 2:
            monthday.insert(0,monthday[0] + 28)
        else:
            monthday.insert(0,monthday[0] + 30)
    for i in range(9,12):
        if i == 11:
            monthday.append(monthday[-1] - 31)
        else:
            monthday.append(monthday[-1] - 30)
    monthday.insert(0,0)
    return monthday

monthday = monthday_array()
print monthday

def days_uploaded(year, month, day):
    # assuming each year has 365 days
    days = (2018 - year) * 365
      
    days += monthday[month]
    
    days += 15 - day
    
    return days

print days_uploaded(2017, 1,13) , "expected: 610"
        
"""
x,y,z are three arrays of values for our x-var, y-var; x and y will be plotted
on their respective axis, while z-var will be represented by the size of the
dot on our scatterplot.
"""
# =============================================================================
# Graphing functions
# =============================================================================

def scattercompare2(x,y, labelx, labely):

    plt.scatter(x,y, c = 'red')
    axis_labeling(labelx, labely)
    plt.xlabel = (labelx)
    plt.ylabel = (labely)
    plt.show()

# =============================================================================
# Curve fitting and R square calculating Function for y vs x
# =============================================================================

def lin_func(x, a, b):
    return a*x + b

def inv_func(x, k, b):
    return k /x + b

def inv_2_func(x, k ,b):
    return k/(x**2) + b

def fit_curve(x_data, y_data, func):
    params, params_covariance = optimize.curve_fit(func, x_data, y_data)
    return params

def plot_curve(x_data, y_data, func):
    plt.figure(figsize=(6, 4))
    plt.scatter(x_data, y_data, label='Data')
    plt.plot(x_data, func(x_data, fit_curve(x_data, y_data, func)[0], 
                          fit_curve(x_data, y_data, func)[1]),)
    plt.legend(loc='best')
    plt.show()
    
# =============================================================================
# Create a multiple linear regression model from, hopefully, all independent 
# variables, y^ = ax1 + bx2 + cx3 + d, to predict Y, change in viewership
# =============================================================================

from sklearn import linear_model

def combine_var(lst1, lst2, lst3):
    lst = []
    lst.append(lst1).append(lst2).append(lst3)
    return lst

def mult_reg(lst1,lst2, lst3, y):
    lm = linear_model.LinearRegression()
    model = lm.fit(combine_var(lst1, lst2, lst3), y)
    return model

def create_prediction(model, )
    predictions = lm.predict(X)
    print(predictions)[0:5]
# =============================================================================
x_data = [1,2]
y_data = [2,3]
print scattercompare2(x_data, y_data, "fd","adf")

    