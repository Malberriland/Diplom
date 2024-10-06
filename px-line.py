import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html


app = Dash(__name__)

def linegraph(df_):
    """Return a line graph."""
    df = pd.read_csv(df_)
    fig = px.line(df, x='Date', y='Close', height=650)
    fig.update_layout(
        yaxis_title='Цена, USD',
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
    return fig


app.layout = html.Div(
        children=[
            html.H1('Динамика цены'),
            dcc.Graph(
                figure=linegraph('ohlc.csv')
                    )
        ]
    )

app.run_server(debug=True)
