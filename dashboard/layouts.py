from dash import html, dcc
import plotly.graph_objects as go
from config.settings import STYLES

def create_main_layout(df):
    return html.Div([
        create_header(),
        create_date_picker(df),
        create_kpi_section(),
        create_graphs_section()
    ], style=STYLES['container'])

def create_header():
    return html.H1("Patient Outcomes Dashboard", style=STYLES['header'])

def create_date_picker(df):
    return html.Div([
        dcc.DatePickerRange(
            id='date-range',
            start_date=df['date'].min(),
            end_date=df['date'].max(),
            display_format='YYYY-MM-DD'
        )
    ], style={'margin': '20px'})

def create_kpi_section():
    return html.Div([
        html.Div([
            html.H3("Patient Satisfaction"),
            html.Div(id='satisfaction-kpi')
        ], className='kpi-box'),
        
        html.Div([
            html.H3("Recovery Time"),
            html.Div(id='recovery-kpi')
        ], className='kpi-box'),
        
        html.Div([
            html.H3("Readmission Rate"),
            html.Div(id='readmission-kpi')
        ], className='kpi-box')
    ], style={'display': 'flex', 'justifyContent': 'space-around', 'margin': '20px'})

def create_graphs_section():
    return html.Div([
        html.Div([
            html.H3("Trends Over Time"),
            dcc.Graph(id='trends-graph')
        ], style={'width': '100%', 'marginBottom': '20px'}),
        
        html.Div([
            html.H3("Correlation Analysis"),
            dcc.Graph(id='correlation-graph')
        ], style={'width': '100%'})
    ])

def create_trend_graph(df):
    return {
        'data': [
            go.Scatter(
                x=df['date'],
                y=df['patient_satisfaction'],
                name='Patient Satisfaction',
                mode='lines+markers'
            ),
            go.Scatter(
                x=df['date'],
                y=df['recovery_time'],
                name='Recovery Time',
                mode='lines+markers'
            ),
            go.Scatter(
                x=df['date'],
                y=df['readmission_rate'],
                name='Readmission Rate',
                mode='lines+markers'
            )
        ],
        'layout': go.Layout(
            title='Metrics Trends Over Time',
            xaxis={'title': 'Date'},
            yaxis={'title': 'Value'},
            hovermode='closest'
        )
    }

def create_correlation_graph(df):
    return {
        'data': [
            go.Scatter(
                x=df['patient_satisfaction'],
                y=df['treatment_success'],
                mode='markers',
                marker=dict(
                    size=10,
                    color='rgb(51, 204, 153)',
                    opacity=0.6
                ),
                text=df['date']
            )
        ],
        'layout': go.Layout(
            title='Patient Satisfaction vs Treatment Success',
            xaxis={'title': 'Patient Satisfaction'},
            yaxis={'title': 'Treatment Success'},
            hovermode='closest'
        )
    }