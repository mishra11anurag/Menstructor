# Menstrual Cycle Tracker

## Overview
The Menstrual Cycle Tracker is a comprehensive application designed to help users track their menstrual cycles, predict periods and ovulation, forecast fertile windows, and provide educational resources and personalized advice. This application aims to empower users with knowledge about their menstrual health and assist them in managing their cycles effectively.

## Features
- **Cycle Tracking**: Input and store data related to menstrual cycles, including start dates, cycle lengths, symptoms, and lifestyle factors.
- **Predictions**: Predict upcoming periods, ovulation dates, and fertile windows based on user input.
- **Educational Resources**: Access articles, tips, and links to external resources related to menstrual health.
- **Personalized Advice**: Receive tailored advice based on input data, including symptom forecasting and lifestyle recommendations.
- **User-Friendly Interface**: Easy-to-use interface for data input and display.

## Project Structure
```
menstrual-cycle-tracker
├── src
│   ├── app.py                 # Flask application
│   ├── main.py                # Entry point of the application
│   ├── tracker                # Module for tracking menstrual cycle data
│   │   ├── __init__.py        # Tracker package initialization
│   │   ├── data_input.py      # User input handling
│   │   ├── data_display.py    # Data display functions
│   │   ├── prediction.py      # Prediction algorithms
│   │   ├── resources.py       # Educational resources
│   │   └── advice.py          # Personalized advice
│   ├── templates              # HTML templates for the frontend
│   │   ├── index.html         # Homepage template
│   │   ├── input.html         # Data input template
│   │   ├── display.html       # Data display template
│   │   ├── predict.html       # Predictions display template
│   │   ├── advice.html        # Advice display template
│   │   └── resources.html     # Resources display template
│   ├── utils                  # Utility functions
│   │   ├── __init__.py        # Utils package initialization
│   │   ├── date_utils.py      # Date-related utilities
│   │   └── calculation_utils.py # Calculation utilities
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd menstrual-cycle-tracker
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python src/app.py
```
Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.