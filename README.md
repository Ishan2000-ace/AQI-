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
![pandas](https://pythonawesome.com/content/images/2018/05/pandas-logo.png) ![beautifulsoup](https://python-scripts.com/wp-content/uploads/2019/10/beautifulsoup-html-parsing-example.png)

## Machine Learning Algorithm
I have Performed EDA in seperate file to understand the relationship between various features. I used mainly Pandas, Matplotlib and Seaborn to perform the analysis
That file is named as EDA.ipynb. I used Linear Rigression but that dosen't gave me a 
very good accuracy. After that I tried several other models like SVC,Decision tree etc but best accuracy I got after using Random forest Regressor Algorithm. The whole code is 
available at RandomForest.ipynb. Random Forest fits a number of  decision tress of various sub sample of the datasets and average them to provide better accuracy and to avoid 
overfitting of the data. By defalut no. of trees that are combined are 100 but we can change them according to our needs. More details about the parameters and syntax can be viewed
at [Random Forest Regressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#:~:text=A%20random%20forest%20regressor.%20A%20random%20forest%20is,to%20improve%20the%20predictive%20accuracy%20and%20control%20over-fitting.)
The link is of official website of the sci-kit learn.
![Random Forest](https://hardtasksin.files.wordpress.com/2019/06/random-e1561729980815.png?w=522&h=347)
![sklearn](https://machine-earning.net/wp-content/uploads/2018/02/eye_sklearn.png)

## Deployment of the Model
This model is deployed by using flask framework of python that is used for backend development of web. HTML and CSS has been used for the frontend UI. This app is being hosted on 
Heroku cloud which is considerd as platform as a service. This app can be viewed,used and tested directly by clicking at:
[AQI APP](https://aqipredictordelhi.herokuapp.com/)
![Heroku](https://a.slack-edge.com/bfaba/img/api/hosting_heroku.png)
![Flask](https://avatars1.githubusercontent.com/u/18305767)

## Installation Details
Steps for Installation:
1. First we have to download Anaconda we can visit the page directly by clicking at [Anaconda Download](https://www.anaconda.com/products/individual)
Here we have scroll to the bottom and we can see installers for various opearating systems. We have to choose according to our system requirements.
This step can be skipped if anaconda is already installed.

2. In anaconda prompt create a new environment by the following command:
```conda create --name myenv```

3. After creating a new environment it is activated by following command: ```conda activate myenv'''

4. Now we have to navigate to directory where we have downloaded this repository and we have to it via anaconda prompt using command: ```cd path of the directory``` 

5. After navigating to the directory we have to install the dependencies of this project by using a file that is called requirements.txt that I have already provided in 
my repository and the dependencies can be installed by using command ```pip install requirements.txt```
but this command must be executed after executing step 4 otherwise it will won't work.

6. To run this app in the local machine we have to use the command:```python app.py```
After execution it will give a local address just copy that and paste that in the address bar of the browser and the web app is ready to use.

## Credits
Credits of this project goes to krish Naik sir's YouToube channel. Lead data scientist at Ineuron. His videos were a great help
[Link of the channel](https://www.youtube.com/user/krishnaik06)




