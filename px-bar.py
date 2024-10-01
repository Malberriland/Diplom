import pandas as pd
import plotly.graph_objs as go
from dash import Dash, dcc, html


app = Dash(__name__)
df = pd.read_csv('budget_data.csv')
df.head()
fig = go.Figure(
    data=[
        go.Bar(x=df['Date'], y=df['Profit/Losses'], marker_color='lightskyblue')
    ], layout=dict(height=650)
)

fig.update_layout(
                  yaxis_title='Прибыль / Убытки, тыс.',
                  xaxis_title='',
                  font=dict(family="Times New Roman", size=20, color="Black")
)

app.layout = html.Div(
        children=[
            html.H1('Объем торговли с течением времени'),
            dcc.Graph(
                figure=fig
                    )
        ]
    )

app.run_server(debug=True)

