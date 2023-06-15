def forecast(*args):
    sunny_locations = []
    cloudy_locations = []
    rainy_locations = []

    for arg in args:
        location, weather = arg
        if weather == "Sunny":
            sunny_locations.append(location)
        elif weather == "Cloudy":
            cloudy_locations.append(location)
        elif weather == "Rainy":
            rainy_locations.append(location)

    sunny_locations.sort()
    cloudy_locations.sort()
    rainy_locations.sort()

    sorted_locations = sunny_locations + cloudy_locations + rainy_locations

    forecast_info = []
    for location in sorted_locations:
        weather = "Sunny" if location in sunny_locations else "Cloudy" if location in cloudy_locations else "Rainy"
        forecast_info.append(f"{location} - {weather}")

    return "\n".join(forecast_info)

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
