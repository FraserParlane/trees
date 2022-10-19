from data import path_clean_tree_data
import plotly.graph_objects as go
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
# Create the app
app = Dash(__name__)

# Import the data
data = pd.read_csv(path_clean_tree_data)

fig = go.Figure()

colors = [
    "#ea5545",
    "#f46a9b",
    "#ef9b20",
    "#edbf33",
    "#ede15b",
    "#bdcf32",
    "#87bc45",
    "#27aeef",
    "#b33dc6",
]

freq = data['common_name'].value_counts()
for i, color in enumerate(colors):
    name = freq.index[i]
    idata = data[data['common_name'] == name]

    # Make scatter plot
    scatter = go.Scatter(
        x=idata['lon'],
        y=idata['lat'],
        mode='markers',
        marker=dict(
            color=color,
        )
    )

    # Add to figure
    fig.add_trace(scatter)

# scat = go.Scatter(
#         x=df['lon'],
#         y=df['lat'],
#         mode='markers',
#         marker=dict(color='grey'),
# )
# fig.add_trace(
#     scat
# )



app.layout = html.Div(children=[
    html.H1(children='My first plot'),
    html.Div(children=[
        'Some text in a div.'
    ]),
    dcc.Graph(
        id='my scatter',
        figure=fig,
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
