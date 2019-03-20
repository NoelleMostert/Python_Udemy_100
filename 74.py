# import pandas as pd

# a = pd.read_csv("http://www.pythonhow.com/data/sampledata.txt")
# b = pd.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")
# merged = a.merge(b, on="x")
# merged.to_csv("sampledata_ab.txt", index = None)

# Answer 1 with pandas and concat

# import pandas
 
# data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
# data2 = pandas.read_csv("sampledata_x_2.txt")
# data12 = pandas.concat([data1, data2])
# data12.to_csv("sampledata12.txt", index=None)

#Answer 2 with stronger library requests used instead of internal urllib:

import io
import pandas
import requests
 
r = requests.get("http://www.pythonhow.com/data/sampledata.txt")
c = r.content
data1 = pandas.read_csv(io.StringIO(c.decode('utf-8')))
data2 = pandas.read_csv("sampledata_x_2.txt")
data12 = pandas.concat([data1, data2])
data12.to_csv("sampledata12.txt", index=None