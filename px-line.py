import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html


app = Dash(__name__)

df = pd.read_csv('ohlc.csv')

fig = px.line(df, x='Date', y='Close', height=650)

fig.update_layout(
    yaxis_title='Цена закрытия',
    xaxis_title='Дата',
    font=dict(family="Times New Roman", size=20, color="Black"),
)
fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(
    buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(step="all")
        ])
    )
)


app.layout = html.Div(
        children=[
            html.H1('Динамика цены'),
            dcc.Graph(
                figure=fig
                    )
        ]
    )

app.run_server()
