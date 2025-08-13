import pandas as pd
import numpy as np
from config.settings import DATABASE_CONFIG

class PatientDatabase:
    def __init__(self):
        self.connection = None
        self.data = None

    def connect(self):
        self.connection = True
        return self

    def get_patient_data(self):
        dates = pd.date_range(
            start=DATABASE_CONFIG['data_start_date'], 
            end=DATABASE_CONFIG['data_end_date'], 
            freq='D'
        )
        
        data = self._generate_sample_data(dates)
        self.data = pd.DataFrame(data)
        return self.data

    def _generate_sample_data(self, dates):
        np.random.seed(42)
        return {
            'date': dates,
            'patient_satisfaction': np.random.normal(85, 5, len(dates)),
            'recovery_time': np.random.normal(14, 2, len(dates)),
            'readmission_rate': np.random.normal(5, 1, len(dates)),
            'treatment_success': np.random.normal(90, 3, len(dates))
        }