class MenstrualCyclePredictor:
    def __init__(self, cycle_data):
        self.cycle_data = cycle_data

    def predict_next_period(self):
        from datetime import datetime, timedelta

        start_date = datetime.strptime(self.cycle_data['start_date'], '%Y-%m-%d')
        cycle_length = self.cycle_data['cycle_length']
        next_period = start_date + timedelta(days=cycle_length)
        return next_period.strftime('%Y-%m-%d')

    def predict_ovulation(self):
        from datetime import datetime, timedelta

        start_date = datetime.strptime(self.cycle_data['start_date'], '%Y-%m-%d')
        cycle_length = self.cycle_data['cycle_length']
        ovulation_day = start_date + timedelta(days=(cycle_length - 14))
        return ovulation_day.strftime('%Y-%m-%d')

    def forecast_fertile_window(self):
        from datetime import datetime, timedelta

        ovulation_date = self.predict_ovulation()
        ovulation_date = datetime.strptime(ovulation_date, '%Y-%m-%d')
        fertile_start = ovulation_date - timedelta(days=5)
        fertile_end = ovulation_date + timedelta(days=1)
        return fertile_start.strftime('%Y-%m-%d'), fertile_end.strftime('%Y-%m-%d')