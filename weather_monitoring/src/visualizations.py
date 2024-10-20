import matplotlib.pyplot as plt
import sqlite3

def plot_daily_summaries():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('SELECT date, avg_temp, max_temp, min_temp FROM daily_weather_summary')
    rows = cursor.fetchall()
    conn.close()

    dates = [row[0] for row in rows]
    avg_temps = [row[1] for row in rows]
    max_temps = [row[2] for row in rows]
    min_temps = [row[3] for row in rows]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, avg_temps, label='Average Temperature')
    plt.plot(dates, max_temps, label='Maximum Temperature')
    plt.plot(dates, min_temps, label='Minimum Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Daily Weather Summaries')
    plt.legend()
    plt.show()
