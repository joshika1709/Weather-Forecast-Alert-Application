from predictor import predict_weather
from graphs import show_graphs

print("\n🌦 WEATHER FORECAST APPLICATION")

city = input("\nEnter City Name: ")

date = input("Enter Date (YYYY-MM-DD): ")

result = predict_weather(city, date)

if result:

    print("\n📍 City:", result["city"])

    print("📅 Date:", result["date"])

    print("🌡 Temperature:", result["temperature"])

    print("💧 Humidity:", result["humidity"])

    print("💨 Wind Speed:", result["wind_speed"])

    print("☁ Condition:", result["condition"])

    print("\n⚠ Alerts:")

    for alert in result["alerts"]:
        print(alert)

    show_graphs(city)

else:

    print("\n❌ No Data Found")
