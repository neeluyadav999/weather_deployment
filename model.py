
#from app import Temperature
import re
import pandas as pd
import numpy as np
import os
import pickle

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def temp_prediction(ApparentTemperature,Pressure,Humidity,WindBearing,WindSpeed,LoudCover,Visibility):
    data = pd.read_csv("C:/Users/Arvind/weather/weatherHistory.csv")
    data_num=data[list (data.dtypes [data.dtypes!='object'].index)]
    print(data_num.head())
    data_num=data_num.rename(columns={'Temperature (C)':'Temperature','Apparent Temperature (C)':'ApparentTemperature','Wind Speed (km/h)':'WindSpeed','Wind Bearing (degrees)':'WindBearing','Visibility (km)':'Visibility','Loud Cover':'LoudCover','Pressure (millibars)':'Pressure'})
    data_num
    weather_y = data_num.pop('Temperature')
    weather_X = data_num
    train_X,test_X, train_y,test_y = train_test_split(weather_X, weather_y, test_size = 0.2, random_state=4)
    train_X.head()
    train_y.head()
    from sklearn.tree import DecisionTreeRegressor
    model = DecisionTreeRegressor(random_state=0)
    model.fit(train_X, train_y)
    
    final=[[ApparentTemperature,Humidity,WindSpeed,WindBearing,Visibility,LoudCover,Pressure]]
    
    test_X=np.array(final)
    #test_X=test_X.reshape(1,-1)
    return model.predict(test_X)




