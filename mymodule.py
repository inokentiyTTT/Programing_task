import argparse
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore', 'statsmodels.tsa.arima_model.ARMA',
                        FutureWarning)
warnings.filterwarnings('ignore', 'statsmodels.tsa.arima_model.ARIMA',
                        FutureWarning)


# ____________________________load data________________
my_parser = argparse.ArgumentParser()
my_parser.add_argument('-D', action='store', type=str, required=True)
# my_parser.add_argument('-M', action='store', type=str, required=True)
# my_parser.add_argument("-S", default=False, action="store_true")
# args = my_parser.parse_args()
args = my_parser.parse_args()

# my_parser1 = argparse.ArgumentParser()
df = pd.read_csv(f'{args.D}',delimiter=';')
df.isnull().sum()
df=df.dropna(axis=0)
# print(df.head())
# my_parser1.add_argument('-D', action='store', type=str, required=True)
# args1 = my_parser1.parse_args()


# print(df[f'{args.M}'])

#
# class test():
#
#     def fit_to_model(self):
#         model = ARIMA(self, order=(0, 1, 2))
#         model_fit = model.fit(disp=0)
#         print(model_fit.summary())
#         model_fit.plot_predict()

# def fit_to_model(dts):
#     model = ARIMA((dts), order=(0,1,2))
#     model_fit = model.fit(disp=0)
#     print(model_fit.summary())
#     model_fit.plot_predict()
#     plt.show()


# df = pd.read_csv('SG.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
# df = pd.read_csv('SG.csv',delimiter=';')

def fit_to_model(data_set):
    print("Available list ")
    for col_name in data_set.columns:
        print(col_name)
#     data=input("Please select quantity: " + (data_set. columns))
    data=input("Please select quantity: " )
    dts= data_set[data]
    dts.isnull().sum()
    dfs=dts.dropna(axis=0)
    model = ARIMA((dfs), order=(0,1,2))
    model_fit = model.fit(disp=0)
    print(model_fit.summary())
#     model_fit.plot_predict()
    predicted =model_fit.predict(1, 1441, None,'levels',dynamic=False)
    result=pd.DataFrame(df.Time)
    result['Predicted'] = predicted
    result[data] = dfs
    result.plot('Time',figsize=(20, 4),  rot=15 )
    plt.grid('on')
    plt.show()
    return model_fit, dfs

if __name__ == "__main__":
    fit_to_model(df)
