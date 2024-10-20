# Real-Time Data Processing System for Weather Monitoring

## Overview

This project is a real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates. The system retrieves weather data from the OpenWeatherMap API and processes it to generate daily summaries and alerts.

## Features

- **Real-time Data Retrieval**: Continuously fetches weather data for specified metro cities in India.
- **Temperature Conversion**: Converts temperature values from Kelvin to Celsius or Fahrenheit based on user preference.
- **Daily Weather Summary**: Calculates daily aggregates such as average, maximum, and minimum temperatures, and dominant weather condition.
- **Alerting System**: Triggers alerts based on user-configurable thresholds for temperature or specific weather conditions.
- **Visualization**: Displays daily weather summaries and historical trends using matplotlib.

## Setup Instructions

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

### Project Structure
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

### File Descriptions
database/schema.sql: SQL script to create the database schema.
src/config.py: Configuration file containing API key, metro cities, interval, temperature unit, alert thresholds, and database path.
src/weather_data.py: Functions to retrieve weather data from the OpenWeatherMap API and convert temperature values.
src/rollups.py: Functions to calculate daily weather summaries and store them in the database.
src/alerts.py: Functions to check for alert conditions based on user-configurable thresholds.
src/visualizations.py: Functions to generate visualizations of daily weather summaries and historical trends.
src/main.py: Main script to run the application.
tests/test_weather_monitoring.py: Unit tests for the weather monitoring system.
requirements.txt: List of dependencies required for the project.
README.md: Project documentation.

### Design Choices
SQLite: Chosen for simplicity and ease of setup.
Matplotlib: Used for visualizations.
Threading: Used to fetch weather data periodically without blocking the main thread.

### Dependencies
requests: For making API calls to OpenWeatherMap.
matplotlib: For generating visualizations.
sqlite3: For storing daily weather summaries.

### Example Usage
## Fetching Weather Data
The fetch_weather_data_periodically function in src/weather_data.py fetches weather data for the specified metro cities at a configurable interval.

## Calculating Daily Summaries
The calculate_daily_summary function in src/rollups.py calculates daily aggregates such as average, maximum, and minimum temperatures, and dominant weather condition.

## Checking Alerts
The check_alerts function in src/alerts.py checks for alert conditions based on user-configurable thresholds and triggers alerts if thresholds are breached.

## Visualizing Data
The plot_daily_summaries function in src/visualizations.py generates visualizations of daily weather summaries and historical trends using matplotlib.

### Running the Application
To run the application, execute the main.py script in the src directory. This will start fetching weather data periodically, calculate daily summaries, check for alerts, and generate visualizations.

cd src
python main.py

### Running Tests
To run the unit tests, execute the following command from the project root directory:

python -m unittest discover -s tests

This will run all the test cases in the tests directory and display the results.

### Conclusion
This project provides a real-time data processing system for monitoring weather conditions and generating summarized insights using rollups and aggregates. It includes features for data retrieval, temperature conversion, daily summaries, alerting, and visualization. The system is designed to be extensible and can be enhanced with additional features in the future.

   
