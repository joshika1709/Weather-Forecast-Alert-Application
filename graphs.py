import pandas as pd
import matplotlib.pyplot as plt

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

# Convert date
df["time"] = pd.to_datetime(df["time"])

# Graph function
def show_graphs(city):

    city_data = df[
        df["city"].str.lower() == city.lower()
    ]

    if city_data.empty:

        print("❌ No Graph Data Found")
        return

    plt.figure(figsize=(12, 5))

    # Temperature
    plt.plot(
        city_data["time"],
        city_data["temperature"],
        label="Temperature"
    )

    # Humidity
    plt.plot(
        city_data["time"],
        city_data["humidity"],
        label="Humidity"
    )

    # Wind Speed
    plt.plot(
        city_data["time"],
        city_data["wind_speed"],
        label="Wind Speed"
    )

    plt.title(f"Weather Trends - {city}")

    plt.xlabel("Date")

    plt.ylabel("Values")

    plt.legend()

    plt.grid(True)

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()
