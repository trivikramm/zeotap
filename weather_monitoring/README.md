# Real-Time Data Processing System for Weather Monitoring

## Overview

This project is a real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates. The system retrieves weather data from the OpenWeatherMap API and processes it to generate daily summaries and alerts.

## Project Structure
weather_monitoring/
│
├── database/
│   └── schema.sql
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── weather_data.py
│   ├── rollups.py
│   ├── alerts.py
│   ├── visualizations.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_weather_monitoring.py
│
├── requirements.txt
└── README.md

### Prerequisites

- Python 3.x
- OpenWeatherMap API key

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/weather_monitoring.git
   cd weather_monitoring
   
2. Create and activate a virtual environment:
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Linux

3. Install dependencies:
   pip install -r requirements.txt

4. Initialize the database:
   cd database
   sqlite3 ../weather.db < schema.sql
   cd ..

5. Set your OpenWeatherMap API key in src/config.py:
   API_KEY = 'your_openweathermap_api_key'

### Running the Application
1. Run the main script:
   cd src
   python main.py

### Running Tests
1. Run the tests:
   python -m unittest discover -s tests

   
