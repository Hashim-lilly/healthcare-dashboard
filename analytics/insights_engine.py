import pandas as pd
import numpy as np
from scipy import stats

class InsightsEngine:
    def __init__(self, data):
        self.data = data

    def generate_insights(self):
        return {
            'trend_analysis': self._analyze_trends(),
            'correlations': self._analyze_correlations(),
            'anomalies': self._detect_anomalies(),
            'improvement_areas': self._identify_improvement_areas()
        }

    def _analyze_trends(self):
        # Implement trend analysis using time series decomposition
        trends = {}
        for column in ['patient_satisfaction', 'recovery_time', 'readmission_rate']:
            trend = self.data[column].rolling(window=7).mean()
            trends[column] = {
                'direction': 'up' if trend.iloc[-1] > trend.iloc[0] else 'down',
                'magnitude': abs(trend.iloc[-1] - trend.iloc[0])
            }
        return trends

    def _analyze_correlations(self):
        metrics = ['patient_satisfaction', 'recovery_time', 'readmission_rate', 'treatment_success']
        return self.data[metrics].corr().to_dict()

    def _detect_anomalies(self):
        # Implement anomaly detection using z-score
        anomalies = {}
        for column in ['patient_satisfaction', 'recovery_time', 'readmission_rate']:
            z_scores = stats.zscore(self.data[column])
            anomalies[column] = self.data[abs(z_scores) > 2]
        return anomalies

    def _identify_improvement_areas(self):
        return {
            'high_priority': self._get_high_priority_areas(),
            'opportunities': self._get_improvement_opportunities()
        }

    def _get_high_priority_areas(self):
        # Identify areas that need immediate attention
        high_priority = []
        
        # Check patient satisfaction
        avg_satisfaction = self.data['patient_satisfaction'].mean()
        if avg_satisfaction < 80:
            high_priority.append({
                'area': 'Patient Satisfaction',
                'current_value': avg_satisfaction,
                'target': 80,
                'impact': 'High'
            })

        # Check readmission rate
        avg_readmission = self.data['readmission_rate'].mean()
        if avg_readmission > 10:
            high_priority.append({
                'area': 'Readmission Rate',
                'current_value': avg_readmission,
                'target': 10,
                'impact': 'High'
            })

        # Check recovery time
        avg_recovery = self.data['recovery_time'].mean()
        if avg_recovery > 15:
            high_priority.append({
                'area': 'Recovery Time',
                'current_value': avg_recovery,
                'target': 15,
                'impact': 'Medium'
            })

        return high_priority

    def _get_improvement_opportunities(self):
        # Identify areas with potential for improvement
        opportunities = []

        # Analyze treatment success variability
        success_std = self.data['treatment_success'].std()
        if success_std > 5:
            opportunities.append({
                'area': 'Treatment Consistency',
                'metric': 'Standard Deviation',
                'current_value': success_std,
                'potential_impact': 'Medium'
            })

        # Analyze satisfaction trends
        satisfaction_trend = self.data['patient_satisfaction'].diff().mean()
        if satisfaction_trend < 0:
            opportunities.append({
                'area': 'Patient Experience',
                'metric': 'Satisfaction Trend',
                'current_value': satisfaction_trend,
                'potential_impact': 'High'
            })

        # Analyze correlation between satisfaction and recovery
        corr = self.data['patient_satisfaction'].corr(self.data['recovery_time'])
        if abs(corr) < 0.5:
            opportunities.append({
                'area': 'Recovery Process',
                'metric': 'Satisfaction-Recovery Correlation',
                'current_value': corr,
                'potential_impact': 'Medium'
            })

        return opportunities

# import pandas as pd
# import numpy as np
# from scipy import stats

# class InsightsEngine:
#     def __init__(self, data):
#         self.data = data

#     def generate_insights(self):
#         return {
#             'trend_analysis': self._analyze_trends(),
#             'correlations': self._analyze_correlations(),
#             'anomalies': self._detect_anomalies(),
#             'improvement_areas': self._identify_improvement_areas()
#         }

#     def _analyze_trends(self):
#         # Implement trend analysis using time series decomposition
#         trends = {}
#         for column in ['patient_satisfaction', 'recovery_time', 'readmission_rate']:
#             trend = self.data[column].rolling(window=7).mean()
#             trends[column] = {
#                 'direction': 'up' if trend.iloc[-1] > trend.iloc[0] else 'down',
#                 'magnitude': abs(trend.iloc[-1] - trend.iloc[0])
#             }
#         return trends

#     def _analyze_correlations(self):
#         metrics = ['patient_satisfaction', 'recovery_time', 'readmission_rate', 'treatment_success']
#         return self.data[metrics].corr().to_dict()

#     def _detect_anomalies(self):
#         # Implement anomaly detection using z-score
#         anomalies = {}
#         for column in ['patient_satisfaction', 'recovery_time', 'readmission_rate']:
#             z_scores = stats.zscore(self.data[column])
#             anomalies[column] = self.data[abs(z_scores) > 2]
#         return anomalies

#     def _identify_improvement_areas(self):
#         return {
#             'high_priority': self._get_high_priority_areas(),
#             'opportunities': self._get_improvement_opportunities()
#         }