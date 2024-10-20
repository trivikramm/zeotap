# src/config.py

API_KEY = 'b1fcdd11dabd1065e7fa2353536ee9ed'  # Replace with your actual OpenWeatherMap API key
METROS = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
INTERVAL = 300  # Interval for fetching weather data in seconds (5 minutes)
TEMP_UNIT = 'Celsius'  # Temperature unit, can be 'Celsius' or 'Fahrenheit'

# Alert thresholds
ALERT_THRESHOLDS = {
    'temp': 35,  # Temperature threshold in Celsius
    'consecutive_updates': 2  # Number of consecutive updates to trigger an alert
}

# Database configuration
DB_PATH = 'weather.db'
