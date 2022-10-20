from data import path_clean_tree_data
import plotly.graph_objects as go
from dash import Dash, html, dcc
import pandas as pd
import numpy as np
import datetime

# Create the app
app = Dash(__name__)

# Import the data
data = pd.read_csv(path_clean_tree_data)

fig = go.Figure()


colors = ["#ea5545", "#f46a9b", "#ef9b20", "#edbf33", "#ede15b", "#bdcf32",
          "#87bc45", "#27aeef", "#b33dc6"]

# Generate a new column for the labels
data['label'] = data['common_name'].apply(lambda x: f'<a href="https://www.google.com/search?tbm=isch&q={x.title()}">{x.title()}</a><br />')
data['label'] += 'Sci. name: <i>'
data['label'] += data['genus_name'].apply(lambda x: x.title() + ' ')
data['label'] += data['species_name'].apply(lambda x: x.lower())
data['label'] += '</i><br />'
data['label'] += f'Diameter: '
data['label'] += data['diameter'].astype(str)
data['label'] += ' in <br />Date planted: '
data['label'] += data['date_planted'].apply(
    lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').strftime('%b %d, %Y')
    if isinstance(x, str) else 'unknown'
)

freq = data['common_name'].value_counts()
top_trees = freq.index[:10]
for i, name in enumerate(top_trees):
    color = colors[i] if i < 9 else 'white'
    idata = data[data['common_name'] == name]

    # Generate the label
    label = f'{name.title()} ({len(idata)})'

    # Make scatter plot
    scatter = go.Scattermapbox(
        lat=idata['lat'],
        lon=idata['lon'],
        customdata=np.array(idata['label'])[:, None],
        mode='markers',
        marker=dict(
            color=color,
            size=5,
        ),
        name=label,
        hoverinfo='skip',
        hovertemplate='%{customdata[0]}<extra></extra>'
    )

    # Add to figure
    fig.add_trace(scatter)

# Plot all the other trees as one group
other_trees = data[~data['common_name'].isin(top_trees)]
scatter = go.Scattermapbox(
    lat=other_trees['lat'],
    lon=other_trees['lon'],
    customdata=np.array(other_trees['label'])[:, None],
    mode='markers',
    marker=dict(
        color='white',
        size=5,
        opacity=0.5,
    ),
    name=f'All other trees ({len(other_trees)})',
    visible='legendonly',
    hoverinfo='skip',
    hovertemplate='%{customdata[0]}<extra></extra>'
)
fig.add_trace(scatter)

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
            font=dict(
                color='white',
            ),
            title='Species (click to view)',
            xanchor='right',
            yanchor='top',
            x=0.99,
            y=0.99,
            bgcolor='#151515',

        ),
        hoverlabel=dict(
            bgcolor='white',
        ),
        mapbox=dict(
            accesstoken="pk.eyJ1IjoiZnJhc2VycGFybGFuZSIsImEiOiJjbDlnODRiZm8wOXA5M3dwdWZvenhsdDl3In0.2fXTi1aTpM_86QcvFbLROA",
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=49.2518,
                lon=-123.1289
            ),
            zoom=12,
            pitch=0,
            style='dark',
        ),
        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0,
        )
    )
)

# Add to app
app.layout = html.Div(
    children=[
        html.H1(
            children='The Trees of Vancouver, Canada',
        ),
        html.Span(
            children=[
                html.A(
                    href='https://github.com/FraserParlane/trees',
                    children='About this data.',
                    target='_blank',
                ),
                ' Made by ',
                html.A(
                    href='https://www.parlane.ca',
                    children='Fraser Parlane',
                    target='_blank',
                ),
            ]
        ),

        dcc.Graph(
            id='my scatter',
            figure=fig,
            style={
                'height': '100%',
            },
            config={
                'displayModeBar': False,
            }
        ),
    ],
    style={
        'height': '90vh',
    }
)

if __name__ == "__main__":
    app.run_server(debug=True)
