def aggregate_weather_data(records):
    # Initialize dictionaries to store temperature, humidity, and count of valid records for each city
    city_data = {}

    for record in records:
        city = record.get('city')

        if city not in city_data:
            city_data[city] = {'total_temp': 0, 'total_humidity': 0, 'count_temp': 0, 'count_humidity': 0}

        # Handle missing temperature data
        temp = record.get('temperature')
        if temp is not None:
            city_data[city]['total_temp'] += temp
            city_data[city]['count_temp'] += 1

        # Handle missing humidity data
        humidity = record.get('humidity')
        if humidity is not None:
            city_data[city]['total_humidity'] += humidity
            city_data[city]['count_humidity'] += 1

    # Calculate average for each city
    avg_data = {}
    for city, data in city_data.items():
        avg_temp = data['total_temp'] / data['count_temp'] if data['count_temp'] > 0 else None
        avg_humidity = data['total_humidity'] / data['count_humidity'] if data['count_humidity'] > 0 else None
        avg_data[city] = {'avg_temp': avg_temp, 'avg_humidity': avg_humidity}

    return avg_data

# Example usage:
weather_records = [
    {'city': 'CityA', 'temperature': 25, 'humidity': 60},
    {'city': 'CityB', 'temperature': 22},
    {'city': 'CityA', 'temperature': 27, 'humidity': 65},
    {'city': 'CityB', 'humidity': 55}
]

print(aggregate_weather_data(weather_records))
