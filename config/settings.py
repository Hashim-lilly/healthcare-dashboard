# Configuration settings
DASHBOARD_CONFIG = {
    'port': 8050,
    'host': '0.0.0.0',
    'debug': True
}

DATABASE_CONFIG = {
    'data_start_date': '2023-01-01',
    'data_end_date': '2023-12-31'
}

STYLES = {
    'container': {
        'margin': '20px',
        'padding': '20px',
        'fontFamily': 'Arial, sans-serif'
    },
    'header': {
        'textAlign': 'center',
        'color': '#2c3e50',
        'marginBottom': '30px'
    },
    # ... other styles
}

# In config/settings.py, add these styles:

STYLES = {
    'container': {
        'margin': '20px',
        'padding': '20px',
        'fontFamily': 'Arial, sans-serif'
    },
    'header': {
        'textAlign': 'center',
        'color': '#2c3e50',
        'marginBottom': '30px'
    },
    'kpi-box': {
        'padding': '20px',
        'border': '1px solid #ddd',
        'borderRadius': '5px',
        'backgroundColor': '#f8f9fa',
        'textAlign': 'center',
        'width': '30%'
    }
}