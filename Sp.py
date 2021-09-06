import pandas as pd
import plotly.express as px

dp =  pd.read_csv("Copy+of+data+-+data.csv")
fig = px.scatter(dp,x='date',y='cases',color='country')

fig.show()