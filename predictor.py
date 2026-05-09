import pandas as pd

# Load dataset
df = pd.read_csv("weather_data.csv")

# Rename columns
df.columns = [
    "index",
    "temperature",
    "humidity",
    "dew_point",
    "precipitation",
    "rain",
    "pressure",
    "cloud_cover",
    "cloud_density",
    "wind_speed",
    "wind_direction",
    "time",
    "city",
    "rain_tomorrow"
]

# Convert time
df["time"] = pd.to_datetime(df["time"])

# Create month-day
df["month_day"] = df["time"].dt.strftime("%m-%d")

# Prediction function
def predict_weather(city, future_date):

    future_date = pd.to_datetime(future_date)

    month_day = future_date.strftime("%m-%d")

    data = df[
        (df["city"].str.lower() == city.lower()) &
        (df["month_day"] == month_day)
    ]

    if data.empty:

        return None

    temperature = round(data["temperature"].mean(), 2)

    humidity = round(data["humidity"].mean(), 2)

    wind_speed = round(data["wind_speed"].mean(), 2)

    rain = data["rain_tomorrow"].mode()[0]

    if rain == 1:
        condition = "Rain Expected"
    else:
        condition = "Normal Weather"

    alerts = []

    if temperature > 35:
        alerts.append("⚠ High Temperature Alert")

    if humidity > 85:
        alerts.append("⚠ High Humidity Alert")

    if rain == 1:
        alerts.append("⚠ Rain Alert")

    return {

        "city": city,
        "date": str(future_date.date()),
        "temperature": f"{temperature} °C",
        "humidity": f"{humidity}%",
        "wind_speed": f"{wind_speed} km/h",
        "condition": condition,
        "alerts": alerts
    }
