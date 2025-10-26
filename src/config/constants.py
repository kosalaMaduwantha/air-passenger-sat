"""
Constants and configuration values for the Air Passenger Satisfaction application.
This module centralizes all magic numbers, paths, and configuration values.
"""
import os

# Get the base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# File paths
DATA_FILE_PATH = os.path.join(BASE_DIR, 'models', 'Invistico_Airline_initial.sav')
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

# Class mappings
CLASS_MAPPINGS = {
    1: 'business',
    2: 'eco',
    3: 'eco_plus'
}

# Satisfaction mappings
SATISFACTION_MAPPINGS = {
    0: 'dissatisfied',
    1: 'satisfied'
}

# Gender mappings
GENDER_MAPPINGS = {
    1: 'male',
    2: 'female'
}

# Customer type mappings
CUSTOMER_TYPE_MAPPINGS = {
    0: 'loyal customer',
    1: 'disloyal customer'
}

# Travel type mappings
TRAVEL_TYPE_MAPPINGS = {
    1: 'business travel',
    2: 'personal travel'
}

# Column indices for data preprocessing
COL_SATISFACTION = 0
COL_GENDER = 1
COL_CUSTOMER_TYPE = 2
COL_TRAVEL_TYPE = 4
COL_CLASS = 5

# Dropdown options
CLASS_DROPDOWN_OPTIONS = [
    {'label': 'Business', 'value': 1},
    {'label': 'Eco', 'value': 2},
    {'label': 'Eco Plus', 'value': 3}
]

# Plotly theme
PLOTLY_THEME = 'plotly_dark'

# Column names for ratings analysis
RATING_COLUMNS = [
    'Seat comfort',
    'Inflight wifi service',
    'Inflight entertainment',
    'Online support',
    'Ease of Online booking',
    'Online boarding',
    'Leg room service',
    'Cleanliness',
    'Food and drink'
]

# Chart titles
CHART_TITLES = {
    'Seat comfort': 'Seat Comfort Rate',
    'Inflight wifi service': 'Inflight Wifi Service Rate',
    'Inflight entertainment': 'Inflight Entertainment Rate',
    'Online support': 'Online Support Rate',
    'Ease of Online booking': 'Ease of Online Booking Rate',
    'Online boarding': 'Online Boarding Rate',
    'Leg room service': 'Leg Room Service Rate',
    'Cleanliness': 'Cleanliness Rate',
    'Food and drink': 'Food and Drink Rate'
}

# Label mappings for charts
CHART_LABELS = {
    'Class': 'Class',
    'Online boarding': 'Number of Passengers',
    'Customer Type': 'Customer Type',
    'Gender': 'Gender',
    'Type of Travel': 'Type of Travel',
    'Percentage': 'Percentage'
}

# Navbar configuration
NAVBAR_CONFIG = {
    'color': '#17252A',
    'brand': 'AIR U.S.',
    'logo_height': '80px',
    'logo_path': '/assets/icon.png'
}

# App configuration
APP_CONFIG = {
    'host': '127.0.0.2',
    'debug': True
}
