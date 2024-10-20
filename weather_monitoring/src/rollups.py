import sqlite3
from datetime import datetime

def calculate_daily_summary(weather_data):
    date = datetime.utcfromtimestamp(weather_data[0]['dt']).strftime('%Y-%m-%d')
    temps = [data['temp'] for data in weather_data]
    avg_temp = sum(temps) / len(temps)
    max_temp = max(temps)
    min_temp = min(temps)
    conditions = [data['main'] for data in weather_data]
    dominant_condition = max(set(conditions), key=conditions.count)
    
    return {
        'date': date,
        'avg_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_condition': dominant_condition
    }

def store_daily_summary(summary):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO daily_weather_summary (date, avg_temp, max_temp, min_temp, dominant_condition)
                      VALUES (?, ?, ?, ?, ?)''', 
                   (summary['date'], summary['avg_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition']))
    conn.commit()
    conn.close()
