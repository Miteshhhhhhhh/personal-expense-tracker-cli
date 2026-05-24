import requests
import os
import csv
from datetime import datetime
from config import API_KEY

def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        return response.json()
    except:
        return {"cod": 404}

def save_to_csv(city, temp, humidity, condition):
    file_exists = os.path.isfile("weather_log.csv")

    with open("weather_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "City", "Temp_C", "Humidity", "Condition"])
        writer.writerow([datetime.now(), city, temp, humidity, condition])

def show_history():
    print("\n--- Last 5 Searches ---")
    try:
        with open("weather_log.csv", "r") as f:
            lines = f.readlines()

            if len(lines) == 0:
                print("No History Yet")
            else:
                if lines[0].startswith("Timestamp"):
                    data_lines = lines[1:]
                else:
                    data_lines = lines

                if len(data_lines) == 0:
                    print("No History Yet")
                else:
                    for line in data_lines[-5:]:
                        parts = line.strip().split(",")
                        print(f"{parts[1]}: {parts[2]}°C, {parts[4]}")

    except FileNotFoundError:
        print("No History Yet")
    print("-----------------------\n")

while True:
    print("\n1. Check weather")
    print("2. View History")
    print("3. Exit")
    choice = input("Enter choice:")

    if choice == "1":
        city = input("Enter city: ")
        data = get_weather(city)

        if data["cod"]!= 200:
            print("Error: city not found")
        else:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["main"]

            print(f"\nWeather in {city}: ")
            print(f"Temp: {temp}C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {condition}")

            save_to_csv(city, temp, humidity, condition)
            print("Saved to weather_log.csv")
    elif choice == "2":
        show_history()
    elif choice == "3":
        print("bye!!!")
        break
    else:
        print("Invalid Choice")
