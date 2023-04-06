import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

import plotly
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

from plotly.offline import plot, iplot, init_notebook_mode
init_notebook_mode(connected=True)
df = pd.read_csv('aapl/AAPL.csv')

df.head()
df.tail()
df.info()
df.columns
df['Date'] = pd.to_datetime(df['Date'])
type(df.loc[0,'Date'])

df.isna().sum()

df['Adj Close'].unique()
df.drop(columns='Adj Close', inplace=True)

df.set_index("Date", inplace=True)
df.head()

apple_df = df.drop(columns='Volume')
volume = df['Volume']

#VISUALIZATION

fig = make_subplots(rows=3, cols=1,subplot_titles=['Open', 'High', 'Low'])

fig.add_trace(go.Scatter(x=apple_df.index, y=apple_df['Open'], name='Open',
                        line=dict(color='darkblue')),row=1, col=1)

fig.add_trace(go.Scatter(x=apple_df.index, y=apple_df['High'], name='High',
                        line=dict(color='darkred')),row=2,col=1)

fig.add_trace(go.Scatter(x=apple_df.index, y=apple_df['Low'],
                         name='Low',line=dict(color='forestgreen')),row=3, col=1)

fig.update_layout(showlegend=False,title_text="OVERALL APPLE STOCKS", title_x=0.5,
                  height=1200, width=800,
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="black"
))
plot(fig)


#Analysis years between 1980 and 2000


years_1980_2000 = apple_df[apple_df.index.year < 2000]

fig = make_subplots(rows=3, cols=1,subplot_titles=['Open', 'High', 'Low'])

fig.add_trace(go.Scatter(x=years_1980_2000.index, y=years_1980_2000['Open'], mode='lines',
                         line=dict(color='deepskyblue')), row=1, col=1)

fig.add_trace(go.Scatter(x=years_1980_2000.index, y=years_1980_2000['High'], mode='lines',
                        line=dict(color='salmon')), row=2, col=1)

fig.add_trace(go.Scatter(x=years_1980_2000.index, y=years_1980_2000['Low'], mode='lines',
                        line=dict(color='lightgreen')), row=3, col=1)


fig.update_layout(showlegend=False,title_text="APPLE STOCKS IN YEARS 1980 - 1999 ", title_x=0.5,
                  height=1200, width=800,
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="black"
))
plot(fig)

#2000-2010 arası

years_2000_2010 =  apple_df[(apple_df.index.year <= 2010) & (apple_df.index.year >= 2000)]


fig = make_subplots(rows=3, cols=1,subplot_titles=['Open', 'High', 'Low'])

fig.add_trace(go.Scatter(x=years_2000_2010.index, y=years_2000_2010['Open'], mode='lines',
                         line=dict(color='lightyellow')), row=1, col=1)

fig.add_trace(go.Scatter(x=years_2000_2010.index, y=years_2000_2010['High'], mode='lines',
                        line=dict(color='mediumvioletred')), row=2, col=1)

fig.add_trace(go.Scatter(x=years_2000_2010.index, y=years_2000_2010['Low'], mode='lines',
                        line=dict(color='midnightblue')), row=3, col=1)


fig.update_layout(showlegend=False,title_text="APPLE STOCKS IN YEARS 2000-2010 ", title_x=0.5,
                  height=1200, width=800,
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="black"
))
plot(fig)

#2010 sonrası

years_after_2010 =  apple_df[apple_df.index.year > 2010]


fig = make_subplots(rows=3, cols=1,subplot_titles=['Open', 'High', 'Low'])

fig.add_trace(go.Scatter(x=years_after_2010.index, y=years_after_2010['Open'], mode='lines',
                         line=dict(color='darkslateblue')), row=1, col=1)

fig.add_trace(go.Scatter(x=years_after_2010.index, y=years_after_2010['High'], mode='lines',
                        line=dict(color='darkkhaki')), row=2, col=1)

fig.add_trace(go.Scatter(x=years_after_2010.index, y=years_after_2010['Low'], mode='lines',
                        line=dict(color='darkorange')), row=3, col=1)


fig.update_layout(showlegend=False,title_text="APPLE STOCKS IN YEARS 2011 - 2022 ", title_x=0.5,
                  height=1200, width=800,
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="black"
))
plot(fig)





#Hacim analizi
#hacim nedir? Basit bir ifadeyle, belirli bir süre içinde işlem gören bir menkul kıymetin hisse sayısıdır.


fig = go.Figure()

fig.add_trace(go.Scatter(x=volume.index, y=volume.values,
                         line=dict(color='plum')))

fig.update_layout(showlegend=False,title_text=" OVERALL VOLUME ", title_x=0.5,
                  height=800, width=600,
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="black"
))
plot(fig)
#1980-1999
volume_1980_1999 = volume[volume.index.year < 2000]

fig = go.Figure()
fig.add_trace(go.Scatter(x=volume_1980_1999.index, y=volume_1980_1999.values,
                        line = dict(color='darkblue')))

fig.update_layout(showlegend=False,title_text="VOLUME IN YEARS 1980-1999", title_x=0.5,
                  height=800, width=600,
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="black"
))
plot(fig)

#2000-2010
volume_2000_2010 = volume[(volume.index.year >= 2000) & (volume.index.year <= 2010)]

fig = go.Figure()
fig.add_trace(go.Scatter(x=volume_2000_2010.index, y=volume_1980_1999.values,
                        line = dict(color='mediumseagreen')))

fig.update_layout(showlegend=False,title_text="VOLUME IN YEARS 2000-2010", title_x=0.5,
                  height=800, width=600,
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="black"
))
plot(fig)



volume_2010_2022 = volume[volume.index.year > 2010]

fig = go.Figure()
fig.add_trace(go.Scatter(x=volume_2010_now.index, y=volume_2010_now.values,
                        line = dict(color='gray')))

fig.update_layout(showlegend=False,title_text="VOLUME IN YEARS 2010-2022", title_x=0.5,
                  height=800, width=600,
        font=dict(
            family="Courier New, monospace",
            size=14,
            color="black"
))
plot(fig)