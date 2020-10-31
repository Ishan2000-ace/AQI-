# AQI-PREDICTOR

## Overview of Project
Pollution is a major threat to world now a days and now people are now worried about this and world leaders are talking about this on many forums like UN and other summits. In 
every metting pollution and climate change is disussed now a days. Air pollution is one of the major threats of pollution and at what extent air of a particular area is polluted 
is measured by Air Quality Index(AQI). There are two parameters basically used, one is PM 2.5 and other is PM 10. I have used PM 2.5 as the parameter to predict the quality of air
in New Delhi(Palam area). Here we just have to give details of Maximum temprature,minimum temprature,pressure at sea level and other parameters I have mentioned them on my index 
of the web app. After entering all the details app will tell us the predicted AQI according to values enterd. I have created this project end to end from data collection to 
deployment.

## Data Collection
I have scrapped the data by using beautiful soup library in python. I scrapped the data from [climate Data](https://en.tutiempo.net/climate/03-2013/ws-421810.html). Here I have 
all the data from 2013-2018. The exctraction code is named as Extract.py. After that I combined all the extracted HTML Data of different years in different folders in csv format.
It is done by the code in the file AQI_Plot.py. 

## Machine Learning Algorithm
I have Performed EDA in seperate file to understand the relationship between various features. I used mainly Pandas, Matplotlib and Seaborn to perform the analysis
That file is named as EDA.ipynb. I used Linear Rigression but that dosen't gave me a 
very good accuracy. After that I tried several other models like SVC,Decision tree etc but best accuracy I got after using Random forest Regressor Algorithm. The whole code is 
available at RandomForest.ipynb. Random Forest fits a number of  decision tress of various sub sample of the datasets and average them to provide better accuracy and to avoid 
overfitting of the data. By defalut no. of trees that are combined are 100 but we can change them according to our needs. More details about the parameters and syntax can be viewed
at [Random Forest Regressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=A%20random%20forest%20regressor.%20A%20random%20forest%20is,to%20improve%20the%20predictive%20accuracy%20and%20control%20over-fitting.)
The link is of official website of the sci-kit learn.
![Algo representation](https%3a%2f%2fhardtasksin.files.wordpress.com%2f2019%2f06%2frandom-e1561729980815.png)


