import pandas as pd
import dash
from dash import dcc, html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import webbrowser
from threading import Timer

# Load data from the CSV file
file_name = "asset_costs_df.csv"
print(f"Loading data from {file_name}...")
asset_costs_df = pd.read_csv(file_name)

# Ensure the data types are correctly interpreted
asset_costs_df['Year'] = asset_costs_df['Year'].astype(int)
asset_costs_df['Median_Home_Value_USD'] = asset_costs_df['Median_Home_Value_USD'].astype(float)
asset_costs_df['Median_Income_USD'] = asset_costs_df['Median_Income_USD'].astype(float)
asset_costs_df['Bitcoin_Value_USD'] = asset_costs_df['Bitcoin_Value_USD'].astype(float)
asset_costs_df['Home_Price_in_Bitcoin'] = asset_costs_df['Home_Price_in_Bitcoin'].astype(float)

# Add year labels with Home_Price_in_Bitcoin for x-axis
asset_costs_df['Year_Label'] = asset_costs_df.apply(
    lambda row: f"{row['Year']} - {row['Home_Price_in_Bitcoin']:.2f}", axis=1
)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Bar Graph
bar_graph = dcc.Graph(
    id='bar-graph',
    figure={
        'data': [
            go.Bar(
                x=asset_costs_df['Year'],
                y=asset_costs_df['Median_Home_Value_USD'],
                name='Median Home Value',
                marker=dict(color='skyblue')
            ),
            go.Bar(
                x=asset_costs_df['Year'],
                y=asset_costs_df['Median_Income_USD'],
                name='Median Income',
                marker=dict(color='green')
            ),
            go.Bar(
                x=asset_costs_df['Year'],
                y=asset_costs_df['Bitcoin_Value_USD'],
                name='Bitcoin Value (USD)',
                marker=dict(color='gold')
            )
        ],
        'layout': {
            'title': 'Median Home Value, Median Income, and Bitcoin Value (2014-2024)',
            'xaxis': {'title': 'Year'},
            'yaxis': {'title': 'Value in USD'},
            'barmode': 'group'
        }
    }
)

# Line Graph
line_graph = dcc.Graph(
    id='line-graph',
    figure={
        'data': [
            go.Scatter(
                x=asset_costs_df['Year'],
                y=asset_costs_df['Median_Home_Value_USD'],
                mode='lines',
                name='Median Home Value',
                line=dict(color='skyblue', width=2)
            ),
            go.Scatter(
                x=asset_costs_df['Year'],
                y=asset_costs_df['Median_Income_USD'],
                mode='lines',
                name='Median Income',
                line=dict(color='green', width=2)
            ),
            go.Scatter(
                x=asset_costs_df['Year'],
                y=asset_costs_df['Bitcoin_Value_USD'],
                mode='lines',
                name='Bitcoin Value (USD)',
                line=dict(color='gold', width=2)
            ),
            go.Scatter(
                x=asset_costs_df['Year'],
                y=asset_costs_df['Home_Price_in_Bitcoin'],
                mode='lines',
                name='Home Price in Bitcoin',
                line=dict(color='purple', width=2, dash='dash'),
                yaxis='y2'
            )
        ],
        'layout': {
            'title': 'Asset Costs Comparison (2014-2024)',
            'xaxis': {'title': 'Year - BTC', 'tickvals': asset_costs_df['Year'], 'ticktext': asset_costs_df['Year_Label']},
            'yaxis': {'title': 'Value in USD', 'range': [0, 400000]},
            'yaxis2': {
                'title': 'Home Price in Bitcoin',
                'overlaying': 'y',
                'side': 'right',
                'range': [0, 700]
            }
        }
    }
)

# Time-Lapse Graph
time_lapse_graph = dcc.Graph(
    id='time-lapse-graph',
    figure={
        'data': [
            go.Scatter(
                x=[],
                y=[],
                mode='lines',
                name='Median Home Value',
                line=dict(color='skyblue', width=2)
            ),
            go.Scatter(
                x=[],
                y=[],
                mode='lines',
                name='Median Income',
                line=dict(color='green', width=2)
            ),
            go.Scatter(
                x=[],
                y=[],
                mode='lines',
                name='Bitcoin Value (USD)',
                line=dict(color='gold', width=2)
            ),
            go.Scatter(
                x=[],
                y=[],
                mode='lines',
                name='Home Price in Bitcoin',
                line=dict(color='purple', width=2, dash='dash'),
                yaxis='y2'
            )
        ],
        'layout': {
            'title': 'Time-Lapse of Asset Costs Comparison (2014-2024)',
            'xaxis': {'title': 'Year', 'tickvals': asset_costs_df['Year'], 'ticktext': asset_costs_df['Year']},
            'yaxis': {'title': 'Value in USD', 'range': [0, 400000]},
            'yaxis2': {
                'title': 'Home Price in Bitcoin',
                'overlaying': 'y',
                'side': 'right',
                'range': [0, 700]
            },
            'updatemenus': [{
                'type': 'buttons',
                'buttons': [
                    {
                        'label': 'Play',
                        'method': 'animate',
                        'args': [None, {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}]
                    },
                    {
                        'label': 'Pause',
                        'method': 'animate',
                        'args': [[None], {'mode': 'immediate', 'frame': {'duration': 0, 'redraw': False}}]
                    }
                ]
            }]
        },
        'frames': [
            {
                'name': str(frame),
                'data': [
                    go.Scatter(
                        x=asset_costs_df['Year'][:frame + 1],
                        y=asset_costs_df[column][:frame + 1],
                        mode='lines',
                        name=name,
                        line=dict(color=color, width=2),
                        yaxis='y2' if column == 'Home_Price_in_Bitcoin' else 'y'
                    ) for column, name, color in zip(
                        ['Median_Home_Value_USD', 'Median_Income_USD', 'Bitcoin_Value_USD', 'Home_Price_in_Bitcoin'],
                        ['Median Home Value', 'Median Income', 'Bitcoin Value (USD)', 'Home Price in Bitcoin'],
                        ['skyblue', 'green', 'gold', 'purple']
                    )
                ]
            }
            for frame in range(len(asset_costs_df))
        ]
    }
)

# Dashboard Layout
app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H1("Asset Costs Dashboard", className='text-center mb-4'))),
        dbc.Row(dbc.Col(bar_graph, width=12)),
        dbc.Row(dbc.Col(line_graph, width=12)),
        dbc.Row(dbc.Col(time_lapse_graph, width=12))
    ],
    fluid=True
)

# Automatically open the browser
def open_browser():
    webbrowser.open_new_tab("http://127.0.0.1:8050/")

# Run the app
if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run_server(debug=True)
