# Programing_task
mymodule.py 
In this module was used next pkgs: 
1.statsmodels
https://www.statsmodels.org/stable/install.html
Autoregressive integrated moving average (ARIMA):
It explicitly creates a suite of standard structure in time series data and it provides a simple and powerful method for forecasting.
It combines both autoregressive and moving average models as well as a differencing pre-processing step of the sequence to make the sequence stationary. 

This method supports univariate time series with trend and without seasonal component. 

The statsmodel library provides the capability to fit ARIMA models.
from statsmodels.tsa.arima.model import ARIMA

2. Pandas: data processing toolbox in Python witch have 2-dimensional data structure. possible Various facilities for easily combining together Series or DataFrame 
with various kinds of set logic for the indexes and relational algebra functionality in the case of join/merge-type and search/compare operations

3. argparse — Parser for command-line options, arguments and sub-commands

4. To able run a monule please use command python mymodule.py -D SG.csv -M Consumption, where file with data  SG.csv and Consumption data sub-set, 
please be sure that console is linked to the right directory whre file with data is located
