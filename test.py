#coding='utf-8'
from xgboost import XGBRegressor
import pandas as pd

oldData = pd.read_csv('./helper_data/temp/user_one.csv')
needPredictData = pd.read_csv('./helper_data/temp/future.csv')

# print(oldData)

#组建数据
#
power_features = ['date_offset','week_day','holiday_type','avg_temp']
power_labels = ['cost_el']

#,'user_id'
tempFeatures = ['date_offset','week_day','holiday_type']
labels = ['avg_temp']


x_train = oldData[tempFeatures]
y_train = oldData[labels]

x_test = needPredictData[tempFeatures]



from sklearn.ensemble import RandomForestRegressor
#预测9月天气
# xg = XGBRegressor()
# xg.fit(x_train,y_train)
# y_predict = xg.predict(x_test)
#
#
# tempPredict = []
# for i in y_predict:
#     temp = float('%.2f' % i)
#     tempPredict.append(temp)
#
# xg_submission = pd.DataFrame({'date_offset':needPredictData['date_offset'],'week_day':needPredictData['week_day'],
#                               'holiday_type':needPredictData['holiday_type'],'user_id':needPredictData['user_id']
#                                  ,'avg_temp':tempPredict})
# xg_submission.to_csv('./helper_data/predict/needPredict.csv',index=False)
# print(tempPredict)


#读取预测9月天气来训练用电量
powerPredictData = pd.read_csv('./helper_data/predict/needPredict.csv')

power_x_train = oldData[power_features]
power_y_train = oldData[power_labels]

power_x_test = powerPredictData[power_features]


xg = RandomForestRegressor()
xg.fit(power_x_train,power_y_train)
y_predict = xg.predict(power_x_test)
print(y_predict)