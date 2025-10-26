"""
Ratings visualization page module for the Air Passenger Satisfaction application.
Displays pie charts for various service rating categories.
"""
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px

from src.app import app
from src.utils.data_utils import get_processed_airline_data, aggregate_ratings_by_category
from src.config.constants import RATING_COLUMNS, CHART_TITLES, PLOTLY_THEME


# Load and preprocess data once at module level
processed_data, _ = get_processed_airline_data()

# Pre-aggregate ratings data for all categories
ratings_data = {
    column: aggregate_ratings_by_category(processed_data, column)
    for column in RATING_COLUMNS
}


# Layout configuration
layout = html.Div([
    dbc.Container([
        # Main title
        dbc.Row([
            dbc.Col(
                html.H1(children='Airline Passenger Satisfaction Prediction'),
                className="mb-2"
            )
        ], className="main-topic"),
        
        # Subtitle
        dbc.Row([
            dbc.Col(
                html.H6(children='Analysis & Passenger Satisfaction Prediction on US Airline'),
                className="mb-2"
            )
        ], className="main-topic"),

        # Section header
        dbc.Row([
            dbc.Col(
                dbc.Card([
                    html.H4(children="Ratings (1 - 5)", className="text-center text-nav")
                ], body=True, className="card-col-main-row"),
                className="mt-2 mb-1"
            )
        ], className="main-row"),

        # First row of charts
        dbc.Row([
            dbc.Col(dcc.Graph(id='my-graph-sat-Seat-comfort-pie'), width=4),
            dbc.Col(dcc.Graph(id='my-graph-sat-Inflight'), width=4),
            dbc.Col(dcc.Graph(id='my-graph-sat-Inflight-entertainment'), width=4)
        ], className="f-card mb-4 mt-4"),

        # Second row of charts
        dbc.Row([
            dbc.Col(dcc.Graph(id='my-graph-sat-Online-support'), width=4),
            dbc.Col(dcc.Graph(id='my-graph-sat-Ease-of-Online-booking'), width=4),
            dbc.Col(dcc.Graph(id='my-graph-sat-Online-boarding'), width=4)
        ], className="f-card md-4"),

        # Third row of charts
        dbc.Row([
            dbc.Col(dcc.Graph(id='my-graph-sat-Leg-room-service'), width=4),
            dbc.Col(dcc.Graph(id='my-graph-sat-Cleanliness'), width=4),
            dbc.Col(dcc.Graph(id='my-graph-sat-Food-and-drink'), width=4)
        ], className="f-card mt-4")
    ], className="container-out")
])


def create_pie_chart(data, category):
    """
    Create a pie chart for a specific rating category.
    
    Args:
        data: Aggregated data for the category
        category: Name of the rating category
        
    Returns:
        plotly.graph_objs.Figure: Pie chart figure
    """
    fig = px.pie(
        data_frame=data,
        values='Online boarding',
        names=category,
        labels={'Online boarding': 'Percentage'},
        title=CHART_TITLES.get(category, f"{category} Rate")
    )
    fig.layout.template = PLOTLY_THEME
    return fig


@app.callback([
    Output('my-graph-sat-Seat-comfort-pie', 'figure'),
    Output('my-graph-sat-Inflight', 'figure'),
    Output('my-graph-sat-Inflight-entertainment', 'figure'),
    Output('my-graph-sat-Online-support', 'figure'),
    Output('my-graph-sat-Ease-of-Online-booking', 'figure'),
    Output('my-graph-sat-Online-boarding', 'figure'),
    Output('my-graph-sat-Leg-room-service', 'figure'),
    Output('my-graph-sat-Cleanliness', 'figure'),
    Output('my-graph-sat-Food-and-drink', 'figure')],
    [Input('my-graph-sat-Seat-comfort-pie', 'hover-data')]
)
def update_rating_charts(_):
    """
    Update all rating pie charts.
    
    This callback is triggered on page load and generates all rating charts.
    The input is unused but required for the callback to trigger.
    
    Returns:
        tuple: Nine plotly figures for different rating categories
    """
    return tuple(create_pie_chart(ratings_data[column], column) for column in RATING_COLUMNS)

