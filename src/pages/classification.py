"""
Classification page module for the Air Passenger Satisfaction application.
Displays categorical visualizations including satisfaction analysis by class, customer type, gender, and travel type.
"""
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px

from src.app import app
from src.utils.data_utils import (
    get_processed_airline_data,
    aggregate_satisfaction_by_class,
    aggregate_satisfaction_by_customer_type,
    aggregate_satisfaction_by_gender,
    aggregate_satisfaction_by_travel_type
)
from src.config.constants import (
    CLASS_DROPDOWN_OPTIONS,
    PLOTLY_THEME,
    CHART_LABELS
)

# Load and preprocess data once at module level for efficiency
processed_data, raw_data = get_processed_airline_data()

# Pre-aggregate data for visualizations
satisfaction_by_class = aggregate_satisfaction_by_class(processed_data)
satisfaction_by_customer_type = aggregate_satisfaction_by_customer_type(processed_data)
satisfaction_by_gender = aggregate_satisfaction_by_gender(processed_data)
satisfaction_by_travel_type = aggregate_satisfaction_by_travel_type(processed_data)

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

        # Section: Satisfaction count by age
        dbc.Row([
            dbc.Col(
                dbc.Card([
                    html.H4(
                        children="Satisfaction count of each class by Age",
                        className="text-center text-nav"
                    )
                ], body=True, className="card-col-main-row"),
                className="mt-2 mb-1"
            )
        ], className="main-row"),

        # Dropdown for class selection
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='genre-choice',
                    options=CLASS_DROPDOWN_OPTIONS,
                    value=1  # Default to Business class
                ),
                className="drop-down"
            )
        ], className="main-row"),

        # Age distribution graph
        dbc.Row([
            dbc.Col(dcc.Graph(id='my-graph'))
        ], className="f-card"),

        # Section: Satisfaction count by class
        dbc.Row([
            dbc.Col(
                dbc.Card([
                    html.H4(
                        children="Satisfied/Dissatisfied Count of each class",
                        className="text-center text-nav"
                    )
                ], body=True, className="card-col-main-row"),
                className="mt-2 mb-1"
            )
        ], className="main-row"),
                
        dbc.Row([
            dbc.Col(dcc.Graph(id='my-graph-sat'))
        ], className="f-card"),

        # Section: Satisfaction by customer type
        dbc.Row([
            dbc.Col(
                dbc.Card([
                    html.H4(
                        children="Satisfied/Dissatisfied Count of each class by their passenger type",
                        className="text-center text-nav"
                    )
                ], body=True, className="card-col-main-row"),
                className="mt-2 mb-1"
            )
        ], className="main-row"),

        dbc.Row([
            dbc.Col(dcc.Graph(id='my-graph-sat-custype'))
        ], className="f-card"),
        
        # Section: Satisfaction by gender
        dbc.Row([
            dbc.Col(
                dbc.Card([
                    html.H4(
                        children="Satisfied/Dissatisfied Count of each class by their gender",
                        className="text-center text-nav"
                    )
                ], body=True, className="card-col-main-row"),
                className="mt-2 mb-1"
            )
        ], className="main-row"),

        dbc.Row([
            dbc.Col(dcc.Graph(id='my-graph-sat-gender'))
        ], className="f-card"),

        # Section: Satisfaction by travel type
        dbc.Row([
            dbc.Col(
                dbc.Card([
                    html.H4(
                        children="Satisfied/Dissatisfied Count of each class by their type of travel",
                        className="text-center text-nav"
                    )
                ], body=True, className="card-col-main-row"),
                className="mt-2 mb-1"
            )
        ], className="main-row"),

        dbc.Row([
            dbc.Col(dcc.Graph(id='my-graph-sat-tot'))
        ], className="f-card")
    ], className="container-out")
])



@app.callback([
    Output('my-graph', 'figure'),
    Output('my-graph-sat', 'figure'),
    Output('my-graph-sat-custype', 'figure'),
    Output('my-graph-sat-gender', 'figure'),
    Output('my-graph-sat-tot', 'figure')],
    [Input('genre-choice', 'value')]
)
def update_classification_graphs(class_value):
    """
    Update all classification graphs based on selected class.
    
    Args:
        class_value: Selected class value from dropdown
        
    Returns:
        tuple: Five plotly figures for different classification views
    """
    # Age distribution histogram for selected class
    fig_age = px.histogram(
        data_frame=raw_data[raw_data.Class == class_value],
        x='Age',
        y="satisfaction",
        color="Age"
    )
    fig_age.layout.template = PLOTLY_THEME

    # Satisfaction count by class
    fig_class = px.bar(
        data_frame=satisfaction_by_class,
        x="Class",
        y="Online boarding",
        color="Class",
        facet_col="satisfaction",
        labels=CHART_LABELS
    )
    fig_class.layout.template = PLOTLY_THEME

    # Satisfaction by customer type
    fig_customer_type = px.bar(
        data_frame=satisfaction_by_customer_type,
        x="Customer Type",
        y="Online boarding",
        color="satisfaction",
        barmode="group",
        facet_col="Class",
        labels=CHART_LABELS
    )
    fig_customer_type.layout.template = PLOTLY_THEME

    # Satisfaction by gender
    fig_gender = px.bar(
        data_frame=satisfaction_by_gender,
        x="Gender",
        y="Online boarding",
        color="satisfaction",
        barmode="group",
        facet_col="Class",
        labels=CHART_LABELS
    )
    fig_gender.layout.template = PLOTLY_THEME

    # Satisfaction by travel type
    fig_travel = px.bar(
        data_frame=satisfaction_by_travel_type,
        x="Type of Travel",
        y="Online boarding",
        color="satisfaction",
        barmode="group",
        facet_col="Class",
        labels=CHART_LABELS
    )
    fig_travel.layout.template = PLOTLY_THEME

    return fig_age, fig_class, fig_customer_type, fig_gender, fig_travel




