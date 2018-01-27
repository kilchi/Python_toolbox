# -*- coding: utf-8 -*-



"""


@author: Aki
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime



book = "/users/yp6ir/anaconda3/Kyoto_temp_plot2.xlsx"

sheet = "test_plot"  # 読み込むシートの名前
EXL = pd.ExcelFile(book)  # xlsxを開く
Data = EXL.parse(sheet) # データフレームとして読込

print(Data)
df = pd.DataFrame(EXL.parse(sheet))
print(df.mean())

print(df.max())

# X軸データ
x = [datetime.datetime(2017,1,1), datetime.datetime(2017,2,1),
     datetime.datetime(2017,3,1), datetime.datetime(2017,4,1),
     datetime.datetime(2017,5,1),datetime.datetime(2017,6,1), datetime.datetime(2017,7,1),
     datetime.datetime(2017,8,1), datetime.datetime(2017,9,1),
     datetime.datetime(2017,10,1), datetime.datetime(2017,11,1), datetime.datetime(2017,12,1)]




plt.plot(df)

plt.legend(['High','Low','Body_temp'])
plt.title("Temperature_Kyoto_2017 Also thank you next year!!")
plt.xlabel("Month")
plt.ylabel("Temp")
plt.show()


df.hist()
df.plot(kind='box')
