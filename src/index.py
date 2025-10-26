"""
Main application entry point for the Air Passenger Satisfaction dashboard.
This module configures the navigation bar, routing, and page layout.
"""
import sys
sys.path.append("/home/kosala/git-repos/air-passenger-sat/")
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from src.app import server, app
from src.pages import classification, pie_chart
from src.config.constants import NAVBAR_CONFIG, APP_CONFIG


def create_navbar():
    """
    Create the navigation bar component.
    
    Returns:
        dbc.Navbar: Navigation bar component with dropdown menu
    """
    dropdown = dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("Categorical Visualization", href="/classification"),
            dbc.DropdownMenuItem("Ratings", href="/pie_chart")
        ],
        nav=True,
        in_navbar=True,
        label="Explore",
    )

    navbar = dbc.Navbar(
        dbc.Container([
            html.A(
                dbc.Row([
                    dbc.Col(html.Img(src=NAVBAR_CONFIG['logo_path'], height=NAVBAR_CONFIG['logo_height'])),
                    dbc.Col(dbc.NavbarBrand(NAVBAR_CONFIG['brand'], className="ml-2")),
                ], align="center"),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav([dropdown], className="ml-auto", navbar=True),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]),
        color=NAVBAR_CONFIG['color'],
        dark=True,
        className="mb-4 navBar",
    )
    
    return navbar


def toggle_navbar_collapse(n_clicks, is_open):
    """
    Toggle the navbar collapse state.
    
    Args:
        n_clicks: Number of times the navbar toggler has been clicked
        is_open: Current state of the navbar collapse
        
    Returns:
        bool: New state of the navbar collapse
    """
    if n_clicks:
        return not is_open
    return is_open


# Register navbar toggle callback
app.callback(
    Output("navbar-collapse2", "is_open"),
    [Input("navbar-toggler2", "n_clicks")],
    [State("navbar-collapse2", "is_open")],
)(toggle_navbar_collapse)

# Create the app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    create_navbar(),
    html.Div(id='page-content')
], style={"background": "#7991ab"})


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    """
    Route to the appropriate page based on the URL pathname.
    
    Args:
        pathname: URL pathname
        
    Returns:
        dash component: Layout of the selected page
    """
    if pathname == '/classification':
        return classification.layout
    elif pathname == '/pie_chart':
        return pie_chart.layout
    else:
        # Default to classification page
        return classification.layout


if __name__ == '__main__':
    app.run(host=APP_CONFIG['host'], debug=APP_CONFIG['debug'])
