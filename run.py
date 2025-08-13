import dash
from data.database import PatientDatabase
from dashboard.layouts import create_main_layout
from dashboard.callbacks import DashboardCallbacks
from analytics.insights_engine import InsightsEngine
from config.settings import DASHBOARD_CONFIG

def app():
    # Initialize database and get data
    db = PatientDatabase()
    df = db.connect().get_patient_data()

    # Initialize analytics
    insights_engine = InsightsEngine(df)
    insights = insights_engine.generate_insights()

    # Initialize dashboard
    app = dash.Dash(__name__)
    app.layout = create_main_layout(df)
    callbacks = DashboardCallbacks(app, df)

    # Run server
    app.run(
        host=DASHBOARD_CONFIG['host'],
        port=DASHBOARD_CONFIG['port'],
        debug=DASHBOARD_CONFIG['debug']
    )

if __name__ == '__main__':
    app()