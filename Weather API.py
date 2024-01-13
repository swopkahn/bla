import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests

def get_weekly_weather(city):
    API_key = "1b2f8c4cbcbd0ee0ce628c4130e28dc2"
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None

    weather_data = res.json()['list']
    
    # Extract relevant information for each day
    weekly_weather = []
    for entry in weather_data:
        date_time = entry['dt_txt']
        icon_id = entry['weather'][0]['icon']
        temperature = entry['main']['temp'] - 273.15  # Convert temperature to Celsius
        description = entry['weather'][0]['description']

        weekly_weather.append({
            'date_time': date_time,
            'icon_id': icon_id,
            'temperature': temperature,
            'description': description
        })

    return weekly_weather

def search():
    city = city_entry.get()
    weekly_weather = get_weekly_weather(city)

    if weekly_weather is None:
        return

    # Display weather information for each day on the GUI
    for i, day_weather in enumerate(weekly_weather):
        date_time = day_weather['date_time']
        icon_id = day_weather['icon_id']
        temperature = day_weather['temperature']
        description = day_weather['description']

        # Update GUI components for each day
        day_label = ttk.Label(root, text=f"Day {i + 1} - Date/Time: {date_time}, Icon ID: {icon_id}, Temperature: {temperature:.2f}°C, Description: {description}")
        day_label.pack()

root = tk.Tk()
root.title("Weather App")
root.geometry("450x450")

# Create an entry widget -> to enter the city name
city_entry = ttk.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

# Create a button widget -> to search for the weather information
search_button = ttk.Button(root, text="SEARCH", command=search)
search_button.pack(pady=10)

# Create a label widget -> to show the city/country name
location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

# Create a label widget -> to show the weather icon
icon_label = tk.Label(root)
icon_label.pack()

# Create a label widget -> to show the temperature
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

# Create a label widget -> to show the weather description
description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

root.mainloop()