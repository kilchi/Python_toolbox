import os
import numpy as np
import pandas as pd
from pandas.io.parsers import read_csv

list_a = os.listdir(r"C:\Users\Aki\Anaconda3\A")
os.chdir(r"C:\Users\Aki\Anaconda3\A")

for i in range(0,len(list_a)+1):
    
    os.remove(r"C:\Users\Aki\Anaconda3\A\{0:01d}".format(i*3) + ".csv")
    
