import plotly.figure_factory as ff
import csv
import pandas as pd

f = pd.read_csv('mobiledata.csv')

plot  = ff.create_distplot([f ['Avg Rating'].tolist()],['Mobile Brand'], show_hist = False)
plot.show()
