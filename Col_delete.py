import os
import pandas as pd




list_a = os.listdir(r"C:\Users\Aki\file1")
lst = [i for i in range(100)]
a = lst[1::2]  #奇数表現
os.chdir(r"C:\Users\Aki\save_file")
for i in range(1, len(list_a)):
     df = pd.read_csv(r"C:\users\Aki\data\{0:01d}".format(i) + ".csv" ,  header = None)   #ヘッダがない場合　:「header = None」
     A = df.drop(a)
     A = A.drop(a, axis=1)
     A.to_csv("{0:01d}".format(i) + ".csv" , header = None, index = None)
          
