class DataInput:
    def __init__(self):
        self.cycle_data = {}

    def input_data(self):
        self.cycle_data['start_date'] = input("Enter the start date of your last menstrual period (YYYY-MM-DD): ")
        self.cycle_data['cycle_length'] = int(input("Enter your average cycle length (in days): "))
        self.cycle_data['period_length'] = int(input("Enter your average period length (in days): "))
        self.cycle_data['symptoms'] = input("Enter any symptoms experienced during the cycle (comma-separated): ").split(',')
        self.cycle_data['flow_intensity'] = input("Enter the intensity of menstrual flow (light, medium, heavy): ")
        self.cycle_data['ovulation_symptoms'] = input("Enter any ovulation symptoms (comma-separated): ").split(',')
        self.cycle_data['mood_changes'] = input("Enter any mood or emotional changes (comma-separated): ").split(',')
        self.cycle_data['basal_body_temperature'] = float(input("Enter your basal body temperature (in Celsius): "))
        self.cycle_data['weight'] = float(input("Enter your weight (in kg): "))
        self.cycle_data['lifestyle_factors'] = input("Enter any lifestyle factors (exercise, diet, sleep patterns) (comma-separated): ").split(',')
        self.cycle_data['medication'] = input("Enter any medication or supplements taken (comma-separated): ").split(',')
        self.cycle_data['sexual_activity'] = input("Enter information on sexual activity (if relevant for fertility tracking): ")
        self.cycle_data['notes'] = input("Enter any additional notes or observations: ")

    def get_data(self):
        return self.cycle_data