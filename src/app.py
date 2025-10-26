"""
Application initialization module for the Air Passenger Satisfaction dashboard.
This module creates and configures the Dash application instance.
"""
import dash
import dash_bootstrap_components as dbc

# Bootstrap theme configuration
# Using LUX theme for a modern, professional appearance
# Documentation: https://bootswatch.com/lux/
EXTERNAL_STYLESHEETS = [dbc.themes.LUX]

# Viewport meta tags for responsive design
META_TAGS = [{
    'name': 'viewport',
    'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5'
}]

# Create Dash application instance
app = dash.Dash(
    __name__,
    meta_tags=META_TAGS,
    assets_external_path='assets/',
    external_stylesheets=EXTERNAL_STYLESHEETS,
)

# Expose the Flask server for deployment (e.g., Heroku, Gunicorn)
server = app.server

# Allow callbacks to be defined across multiple files without initial validation
app.config.suppress_callback_exceptions = True


