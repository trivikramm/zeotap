import threading
from .weather_data import fetch_weather_data_periodically, get_weather_data
from .config import INTERVAL
from .rollups import calculate_daily_summary, store_daily_summary
from .alerts import check_alerts
from .visualizations import plot_daily_summaries

def main():
    # Start fetching weather data periodically
    weather_thread = threading.Thread(target=fetch_weather_data_periodically, args=(INTERVAL,))
    weather_thread.start()

    # Example usage of rollups and alerts
    weather_data = get_weather_data()
    daily_summary = calculate_daily_summary(weather_data)
    store_daily_summary(daily_summary)
    
    thresholds = {'temp': 35}
    alerts = check_alerts(weather_data, thresholds)
    for alert in alerts:
        print(alert)
    
    # Plot daily summaries
    plot_daily_summaries()

if __name__ == '__main__':
    main()
