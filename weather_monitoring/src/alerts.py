def check_alerts(weather_data, thresholds):
    alerts = []
    for data in weather_data:
        if data['temp'] > thresholds['temp']:
            alerts.append(f"Alert: Temperature in {data['city']} exceeded {thresholds['temp']}°C")
    return alerts
