from data import path_clean_tree_data
import plotly.graph_objects as go
from dash import Dash, html, dcc
import pandas as pd


# Create the app
app = Dash(__name__)

# Import the data
data = pd.read_csv(path_clean_tree_data)

fig = go.Figure()

colors = ["#ea5545", "#f46a9b", "#ef9b20", "#edbf33", "#ede15b", "#bdcf32",
          "#87bc45", "#27aeef", "#b33dc6"]

# Add all trees to map
fig.add_trace(
    go.Scattergl(
        x=data['x'],
        y=data['y'],
        mode='markers',
        marker=dict(
            color='white',
            size=4,
        ),
        name=f'All trees ({len(data)})',
        visible='legendonly',
    )
)

freq = data['common_name'].value_counts()
for i, name in enumerate(freq.index):
    color = colors[i] if i < 9 else 'white'
    idata = data[data['common_name'] == name]

    # Generate the label
    label = f'{name.title()} ({len(idata)})'

    # Determine if visible
    visible = 'legendonly' if i > 2 else None

    # Make scatter plot
    scatter = go.Scattergl(
        x=idata['x'],
        y=idata['y'],
        mode='markers',
        marker=dict(
            color=color,
            size=4,
        ),
        name=label,
        visible=visible,
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
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            showgrid=False,
            showticklabels=False,
        ),
        yaxis=dict(
            showgrid=False,
            showticklabels=False,
        ),
        legend=dict(
            # test='test',
        )
    )
)

# Add to app
app.layout = html.Div(
    children=[
        html.H1(
            children='The trees of Vancouver, Canada',
        ),
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
    }
)

if __name__ == "__main__":
    app.run_server(debug=True)
