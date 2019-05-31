# import pandas
# import pylab as plt
 
# data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
# data.plot(x='x', y='y', kind='scatter')
# plt.show()

#Using the Bokeh library a web based visualization can be achieved

from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas
 
output_file("bokeh_plot.html")
data = pandas.read_csv("batch.csv")
f = figure(x_axis_type='datetime')
f.line(x=data["Date"], y=data["Batch 1"])
 
show(f)