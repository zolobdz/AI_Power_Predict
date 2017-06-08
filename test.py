#coding='utf-8'
from xgboost import XGBRegressor
import pandas as pd

trainX = pd.read_csv('./')

#预测9月天气
xg = XGBRegressor()


