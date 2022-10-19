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
            size=4,
        ),
        name=name.title(),
    )

    # Add to figure
    fig.add_trace(scatter)

# Format

# Scale axes equally
fig.update_yaxes(
    scaleanchor='x',
    scaleratio=1,
)

# Make transparent
fig.update_layout(
    dict(
        xaxis=dict(
            showgrid=False,
            showticklabels=False,
        ),
        yaxis=dict(
            showgrid=False,
            showticklabels=False,
        )
    )
)

# Add to app
app.layout = html.Div(
    children=[
        html.H1(children='The trees of Vancouver, Canada'),
        dcc.Graph(
            id='my scatter',
            figure=fig,
            style={
                'height': '100%',
            },

        ),

        ],
    style={
        'height': '90vh',
        'background-color': 'black',
}
)

if __name__ == "__main__":
    app.run_server(debug=True)
