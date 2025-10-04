class MenstrualCycleTracker:
    def __init__(self):
        self.cycle_data = {}

    def input_data(self):
        from datetime import datetime

        while True:
            try:
                self.cycle_data['start_date'] = input("Enter the start date of your last menstrual period (YYYY-MM-DD): ")
                datetime.strptime(self.cycle_data['start_date'], '%Y-%m-%d')
                break
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

        while True:
            try:
                self.cycle_data['cycle_length'] = int(input("Enter your average cycle length (in days): "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer value.")

        while True:
            try:
                self.cycle_data['period_length'] = int(input("Enter your average period length (in days): "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer value.")

        self.cycle_data['symptoms'] = input("Enter any symptoms experienced during the cycle (comma-separated): ").split(',')
        self.cycle_data['flow_intensity'] = input("Enter the intensity of menstrual flow (light, medium, heavy): ")
        self.cycle_data['ovulation_symptoms'] = input("Enter any ovulation symptoms (comma-separated): ").split(',')
        self.cycle_data['mood_changes'] = input("Enter any mood or emotional changes (comma-separated): ").split(',')

        while True:
            try:
                self.cycle_data['basal_body_temperature'] = float(input("Enter your basal body temperature (in Celsius): "))
                break
            except ValueError:
                print("Invalid input. Please enter a float value.")

        while True:
            try:
                self.cycle_data['weight'] = float(input("Enter your weight (in kg): "))
                break
            except ValueError:
                print("Invalid input. Please enter a float value.")

        self.cycle_data['lifestyle_factors'] = input("Enter any lifestyle factors (exercise, diet, sleep patterns) (comma-separated): ").split(',')
        self.cycle_data['medication'] = input("Enter any medication or supplements taken (comma-separated): ").split(',')
        self.cycle_data['sexual_activity'] = input("Enter information on sexual activity (if relevant for fertility tracking): ")
        self.cycle_data['notes'] = input("Enter any additional notes or observations: ")

    def display_data(self):
        print("\nMenstrual Cycle Data:")
        for key, value in self.cycle_data.items():
            print(f"{key.replace('_', ' ').title()}: {value}")

if __name__ == "__main__":
    tracker = MenstrualCycleTracker()
    tracker.input_data()
    tracker.display_data()