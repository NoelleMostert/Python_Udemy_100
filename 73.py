import pandas as pd
import numpy as np

data = pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = data * 2
data2.to_csv("sampledata2.txt", index = None)