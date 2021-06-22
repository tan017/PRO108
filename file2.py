import pandas as pd
import plotly.figure_factory as ff
import csv
df=pd.read_csv("huh.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["Avg rating"],show_hist=False)
fig.show()