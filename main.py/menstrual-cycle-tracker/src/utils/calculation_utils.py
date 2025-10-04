# datetime has been used for date conversion
# #timedelta has been used for date calculation
#timedelta is a class that represents a duration, the difference between two dates or times.
def calculate_next_period(start_date, cycle_length):
    from datetime import datetime, timedelta
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    next_period = start_date + timedelta(days=cycle_length)
    return next_period.strftime("%Y-%m-%d")

def calculate_ovulation_date(start_date, cycle_length):
    from datetime import datetime, timedelta
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    ovulation_date = start_date + timedelta(days=cycle_length - 14)
    return ovulation_date.strftime("%Y-%m-%d")

def calculate_fertile_window(ovulation_date):
    from datetime import datetime, timedelta
    ovulation_date = datetime.strptime(ovulation_date, "%Y-%m-%d")
    fertile_start = ovulation_date - timedelta(days=5)
    fertile_end = ovulation_date + timedelta(days=1)
    return fertile_start.strftime("%Y-%m-%d"), fertile_end.strftime("%Y-%m-%d")

def forecast_symptoms(symptoms, cycle_length):
    symptom_forecast = {}
    for symptom in symptoms:
        symptom_forecast[symptom] = "Expected around ovulation" if "ovulation" in symptom else "Expected during period"
    return symptom_forecast