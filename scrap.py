import plotly.graph_objects as go
from dash import Dash, html, dcc

# Create the app
app = Dash(__name__)

trace = go.Scattermapbox(
    lat=['49.1913'],
    lon=['-122.801094'],
    mode='markers',
)

point = go.Scattermapbox(
    lat=['49.3'],
    lon=['-123'],
    mode='markers',
)

fig = go.Figure()
fig.add_trace(trace)
fig.add_trace(point)

fig.update_layout(
    mapbox=dict(
        accesstoken="pk.eyJ1IjoiZnJhc2VycGFybGFuZSIsImEiOiJjbDlnODRiZm8wOXA5M3dwdWZvenhsdDl3In0.2fXTi1aTpM_86QcvFbLROA",
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=49,
            lon=-122
        ),
        zoom=8,
        pitch=0
    )
)

# Add to app
app.layout = html.Div(
    children=[
        dcc.Graph(
            id='my scatter',
            figure=fig,
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)