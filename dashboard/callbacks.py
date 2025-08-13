from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

class DashboardCallbacks:
    def __init__(self, app, df):
        self.app = app
        self.df = df
        self.register_callbacks()

    def register_callbacks(self):
        self.register_kpi_callbacks()
        self.register_graph_callbacks()

    def register_kpi_callbacks(self):
        @self.app.callback(
            [Output('satisfaction-kpi', 'children'),
             Output('recovery-kpi', 'children'),
             Output('readmission-kpi', 'children')],
            [Input('date-range', 'start_date'),
             Input('date-range', 'end_date')]
        )
        def update_kpis(start_date, end_date):
            filtered_df = self._filter_data(start_date, end_date)
            return self._calculate_kpis(filtered_df)

    def register_graph_callbacks(self):
        @self.app.callback(
            [Output('trends-graph', 'figure'),
             Output('correlation-graph', 'figure')],
            [Input('date-range', 'start_date'),
             Input('date-range', 'end_date')]
        )
        def update_graphs(start_date, end_date):
            filtered_df = self._filter_data(start_date, end_date)
            return (
                self._create_trends_figure(filtered_df),
                self._create_correlation_figure(filtered_df)
            )

    def _filter_data(self, start_date, end_date):
        if start_date is not None and end_date is not None:
            mask = (self.df['date'] >= start_date) & (self.df['date'] <= end_date)
            return self.df.loc[mask]
        return self.df

    def _calculate_kpis(self, df):
        satisfaction = f"{df['patient_satisfaction'].mean():.1f}%"
        recovery = f"{df['recovery_time'].mean():.1f} days"
        readmission = f"{df['readmission_rate'].mean():.1f}%"
        return satisfaction, recovery, readmission
    
    def _create_trends_figure(self, df):
        return {
            'data': [
                go.Scatter(
                    x=df['date'],
                    y=df['patient_satisfaction'],
                    name='Patient Satisfaction',
                    mode='lines+markers',
                    hovertemplate='<b>Date</b>: %{x}<br>' +
                                '<b>Satisfaction</b>: %{y:.1f}%<br>',
                    line=dict(width=2)
                ),
                go.Scatter(
                    x=df['date'],
                    y=df['recovery_time'],
                    name='Recovery Time',
                    mode='lines+markers',
                    hovertemplate='<b>Date</b>: %{x}<br>' +
                                '<b>Recovery Time</b>: %{y:.1f} days<br>',
                    line=dict(width=2)
                ),
                go.Scatter(
                    x=df['date'],
                    y=df['readmission_rate'],
                    name='Readmission Rate',
                    mode='lines+markers',
                    hovertemplate='<b>Date</b>: %{x}<br>' +
                                '<b>Readmission Rate</b>: %{y:.1f}%<br>',
                    line=dict(width=2)
                )
            ],
            'layout': {
                'title': {
                    'text': 'Metrics Trends Over Time',
                    'font': {'size': 24}
                },
                'xaxis': {
                    'title': {
                        'text': 'Timeline (Date)',
                        'font': {'size': 16, 'color': '#333'}
                    },
                    'gridcolor': 'lightgray',
                    'showline': True,
                    'linewidth': 2,
                    'linecolor': 'black'
                },
                'yaxis': {
                    'title': {
                        'text': 'Metric Values (%)',
                        'font': {'size': 16, 'color': '#333'}
                    },
                    'gridcolor': 'lightgray',
                    'showline': True,
                    'linewidth': 2,
                    'linecolor': 'black'
                },
                'hovermode': 'closest',
                'showlegend': True,
                'legend': {
                    'x': 1.02,
                    'y': 1,
                    'bgcolor': 'rgba(255, 255, 255, 0.8)'
                },
                'margin': {'r': 100},
                'plot_bgcolor': 'white'
            }
        }

    def _create_correlation_figure(self, df):
        return {
            'data': [
                go.Scatter(
                    x=df['patient_satisfaction'],
                    y=df['treatment_success'],
                    mode='markers',
                    marker=dict(
                        size=10,
                        color=df['readmission_rate'],
                        colorscale='Viridis',
                        showscale=True,
                        colorbar=dict(
                            title='Readmission Rate (%)'
                        ),
                        opacity=0.7
                    ),
                    hovertemplate='<b>Patient Satisfaction</b>: %{x:.1f}%<br>' +
                                '<b>Treatment Success</b>: %{y:.1f}%<br>' +
                                '<b>Date</b>: %{text}<br>',
                    text=df['date'].dt.strftime('%Y-%m-%d')
                )
            ],
            'layout': {
                'title': {
                    'text': 'Patient Satisfaction vs Treatment Success',
                    'font': {'size': 24}
                },
                'xaxis': {
                    'title': {
                        'text': 'Patient Satisfaction Score (%)',
                        'font': {'size': 16, 'color': '#333'}
                    },
                    'gridcolor': 'lightgray',
                    'zeroline': False,
                    'showline': True,
                    'linewidth': 2,
                    'linecolor': 'black'
                },
                'yaxis': {
                    'title': {
                        'text': 'Treatment Success Rate (%)',
                        'font': {'size': 16, 'color': '#333'}
                    },
                    'gridcolor': 'lightgray',
                    'zeroline': False,
                    'showline': True,
                    'linewidth': 2,
                    'linecolor': 'black'
                },
                'hovermode': 'closest',
                'plot_bgcolor': 'white',
                'margin': {'r': 100, 'b': 50, 't': 50, 'l': 50}
            }
        }