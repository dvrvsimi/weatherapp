from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests

api_url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}"

api_file = "weather.key"

file_a = ConfigParser()
file_a.read(api_file)
api_key = file_a["api_key"]["key"]


def weather_get(city):
    final = requests.get(api_url.format(city, api_key))
    # print(api_key)
    if final:
        json_file = final.json()
        city = json_file["name"]
        country = json_file["sys"]["country"]
        c_temperature = json_file["main"]["temp"]
        k_temperature = 273.15 - c_temperature
        f_temperature = c_temperature * (9 / 5) + 32
        weather_condition = json_file["weather"][0]["main"]
        result = (city, country, c_temperature, f_temperature, k_temperature, weather_condition)

        return result
    else:
        return None


def print_weather():
    city = searchbar.get()
    # print(city)
    weather = weather_get(city)
    if weather:
        city_country["text"] = "{}, {}".format(weather[0], weather[1])
        city_temperature["text"] = "{:.2f}°C, {:.2f}°F, {:.2f}K".format(weather[2], weather[3], weather[4])
        city_weather["text"] = weather[5]
    else:
        messagebox.showerror(f"Error", f"Cannot find that city. Please enter a valid city name")


root = Tk()
root.title("Weather App")
root.configure(background="black")
root.geometry("700x400")

searchbar = StringVar()
enter_city = Entry(root, textvariable=searchbar, fg="grey", font="Hack 20")
enter_city.insert(0, "enter your city here")


def callback(event):
    enter_city.delete(0, "end")
    enter_city['foreground'] = 'black'
    enter_city['font'] = 'Hack 20 bold'
    enter_city.unbind("<FocusIn>")

    return None


enter_city.bind("<FocusIn>", callback)
enter_city.grid(row=0, column=0, ipady=5, padx=200, pady=50)

search_button = Button(root, text="Search", width=20, fg="white", bg="blue", activeforeground="white", activebackground="black", font="Hack, 15", command=print_weather)
search_button.grid(row=1, column=0, rowspan=1, ipady=5, padx=200)

city_country = Label(root, text="", fg="white", font="Hack 15", bg="black")
city_country.grid(row=4, column=0, ipady=5, padx=200, pady=5)

city_temperature = Label(root, text="", fg="white", font="Hack 15", bg="black")
city_temperature.grid(row=5, column=0, ipady=5, padx=200, pady=1)

city_weather = Label(root, text="", fg="white", font="Hack 15", bg="black")
city_weather.grid(row=6, column=0, ipady=5, padx=200, pady=1)

root.mainloop()

# api_key = 'f1886475398d75b0103e58ab291ac519'
#
# user_input = input("enter your city: ")
#
# data = requests.get(
#     f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")
#
# if data.json()["cod"] == "404":
#     print("No city found")
# else:
#     weather = data.json()["weather"][0]["main"]
#     f_temperature = data.json()["main"]["temp"]
#     temperature = round(((f_temperature + 32) * 5 / 9), 2)
#
#     print(f"The weather condition in {user_input} is: {weather}")
#     print(f"The temperature is {temperature}°C")
