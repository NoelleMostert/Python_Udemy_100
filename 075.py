import pandas
import pylab as plt
 
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data.plot(x='x', y='y', kind='scatter')
plt.show()

#Using the Bokeh library a web based visualization can be achieved
#
# from bokeh.plotting import figure
# from bokeh.io import output_file, show
# import pandas
 
# output_file("bokeh_plot.html")
# data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
# f = figure()
# f.circle(x=data["x"], y=data["y"])
 
# show(f)