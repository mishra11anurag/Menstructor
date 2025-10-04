class DataDisplay:
    def __init__(self, cycle_data):
        self.cycle_data = cycle_data

    def display_data(self):
        print("\nMenstrual Cycle Data:")
        for key, value in self.cycle_data.items():
            print(f"{key.replace('_', ' ').title()}: {value}")

    def display_prediction(self, predictions):
        print("\nPredicted Dates:")
        for key, value in predictions.items():
            print(f"{key.replace('_', ' ').title()}: {value}")

    def display_resources(self, resources):
        print("\nEducational Resources:")
        for resource in resources:
            print(f"- {resource}")

    def display_advice(self, advice):
        print("\nPersonalized Advice:")
        print(advice)