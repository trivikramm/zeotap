import unittest
from src.weather_data import kelvin_to_celsius, get_weather_data
from src.rollups import calculate_daily_summary
from src.alerts import check_alerts

class TestWeatherMonitoring(unittest.TestCase):
    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0)
        self.assertAlmostEqual(kelvin_to_celsius(300), 26.85)

    def test_get_weather_data(self):
        weather_data = get_weather_data()
        self.assertTrue(len(weather_data) > 0)
        self.assertIn('city', weather_data[0])
        self.assertIn('temp', weather_data[0])

    def test_calculate_daily_summary(self):
        weather_data = [
            {'temp': 30, 'main': 'Clear', 'dt': 1609459200},
            {'temp': 32, 'main': 'Clear', 'dt': 1609459200},
            {'temp': 28, 'main': 'Rain', 'dt': 1609459200}
        ]
        summary = calculate_daily_summary(weather_data)
        self.assertEqual(summary['avg_temp'], 30)
        self.assertEqual(summary['max_temp'], 32)
        self.assertEqual(summary['min_temp'], 28)
        self.assertEqual(summary['dominant_condition'], 'Clear')

    def test_check_alerts(self):
        weather_data = [
            {'city': 'Delhi', 'temp': 36, 'main': 'Clear', 'dt': 1609459200},
            {'city': 'Mumbai', 'temp': 34, 'main': 'Clear', 'dt': 1609459200}
        ]
        thresholds = {'temp': 35}
        alerts = check_alerts(weather_data, thresholds)
        self.assertEqual(len(alerts), 1)
        self.assertIn('Delhi', alerts[0])

if __name__ == '__main__':
    unittest.main()
