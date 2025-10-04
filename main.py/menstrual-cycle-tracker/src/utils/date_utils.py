from datetime import datetime, timedelta

def parse_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d")

def format_date(date):
    return date.strftime("%Y-%m-%d")

def calculate_next_period(start_date, cycle_length):
    start = parse_date(start_date)
    next_period = start + timedelta(days=cycle_length)
    return format_date(next_period)

def calculate_ovulation_date(start_date, cycle_length):
    start = parse_date(start_date)
    ovulation_date = start + timedelta(days=(cycle_length - 14))
    return format_date(ovulation_date)

def calculate_fertile_window(start_date, cycle_length):
    ovulation_date = calculate_ovulation_date(start_date, cycle_length)
    ovulation = parse_date(ovulation_date)
    fertile_start = format_date(ovulation - timedelta(days=5))
    fertile_end = format_date(ovulation + timedelta(days=1))
    return fertile_start, fertile_end