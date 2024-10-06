import pandas as pd
import plotly.graph_objs as go
from dash import Dash, dcc, html


app = Dash(__name__)
def candlesticks(df_):
    """Return a candlestick chart."""
    df = pd.read_csv(df_)
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'],
                increasing_line_color='green',
                decreasing_line_color= 'black'
            )
        ]
    )
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(
                      yaxis_title='Цена, USD',
                      xaxis_title='Дата',
                      font=dict(family="Times New Roman", size=20, color="Black")
                      )
    return fig


app.layout = html.Div(
        children=[
            html.H1('Объем торговли с течением времени'),
            dcc.Graph(
                figure=candlesticks('ohlc.csv'),
                style={"height": "85vh"}
                    )
        ]
    )

app.run_server(debug=True)
