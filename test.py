#coding='utf-8'
# from xgboost import
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

oldData = pd.read_csv('./helper_data/temp/all.csv')#所有数据
# oneData = pd.read_csv('./helper_data/temp/user_one.csv')#用户1的数据用来预测天气
# needPredictData = pd.read_csv('./helper_data/temp/future1.csv')#预测天气数据



# #组建天气预测数据
# temperture_features = ['date_offset','week_day','holiday_type']
# temperture_labels = ['avg_temp']
#
#
# x_train = oneData[temperture_features]
# y_train = oneData[temperture_labels]
#
# x_test = needPredictData[temperture_features]




# #预测9月天气
# xg = RandomForestRegressor()
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
#                               'holiday_type':needPredictData['holiday_type']
#                                  ,'avg_temp':tempPredict})
# xg_submission.to_csv('./helper_data/predict/temperaturePredict.csv',index=False)
# print(tempPredict)


# 读取预测9月天气来训练用电量
predictedTempertrueData = pd.read_csv('./helper_data/predict/temperaturePredict9.csv') #预测后的天气数据 16/10/1-16/10/31
userIDs = oldData['user_id']
userIDs = set(userIDs)
# print(userIDs)

power_features = ['high_temp','low_temp','date_offset','week_day','holiday_type']
# power_labels = ['cost_el']

from collections import defaultdict
from datetime import datetime, timedelta
from xgboost import XGBRegressor


el_dict = defaultdict(int)
base_date = datetime(year=2016, month=9, day=1)

# xg = XGBRegressor(learning_rate=0.1,subsample=0.85,
#                         colsample_bytree=0.7,
#                         colsample_bylevel=1,
#                         reg_alpha=0,
#                         reg_lambda=1,
#                         scale_pos_weight=1)

xg = RandomForestRegressor()

# x_all = oldData[power_features]
# y_all = oldData['cost_el']
# xg.fit(x_all,y_all)

for i in userIDs:
    # print(i)
    currentData = oldData[oldData.user_id == i]
    x_train = currentData[power_features]
    y_train = currentData['cost_el']
    x_test  = predictedTempertrueData[power_features]
    xg.fit(x_train,y_train)
        
    y_predict = xg.predict(x_test)
    # print(y_predict)
    # if int(y_predict[0]) < 2:
    #     print(y_predict)
    #     print(i)
    #     print(x_test)
    #     break
    for delta, day_el in enumerate(y_predict):
        el_dict[(base_date+timedelta(days=delta)).strftime('%Y%m%d')] += float(day_el)
        print(el_dict.items())
        break


with open('Tianchi_power_predict_table9.csv', 'w') as new_file:
    lines = ['predict_date,predict_power_consumption\n']
    data_lines = ['{0},{1}\n'.format(time_key, int(total_el)) for time_key, total_el in sorted(el_dict.items())]
    new_file.writelines(lines+data_lines)

# print(oldData[oldData.user_id == 1])



