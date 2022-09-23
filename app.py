# from tkinter import *
# from configparser import ConfigParser
# from tkinter import messagebox
import requests
#
# api_url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}"
#
# api_file = "weather.key"
#
# file_a = ConfigParser()
# file_a.read(api_file)
# api_key = file_a["api_key"]["key"]
#
#
# def weather_get(city):
#     final = requests.get(api_url.format(city, api_key))
#     if final:
#         json_file = final.json()
#         city = json_file["name"]
#         country = json_file["sys"]["country"]
#         k_temperature = json_file["main"]["temp"]
#         c_temperature = k_temperature - 273.15
#         f_temperature = (k_temperature - 273.15) * 9 / 5 + 32
#         weather_condition = json_file["weather"][0]["main"]
#         result = (city, country, c_temperature, f_temperature, weather_condition)
#
#         return result
#     else:
#         return None
#
# #
# # def print_weather():
# #     city = city_text.get()
# #     weather =weather
#
#
# root = Tk()
# root.title("Weather App")
# root.configure(background="black")
# root.geometry("700x400")
#
# searchbar = StringVar()
# enter_city = Entry(root, textvariable=searchbar, fg="grey", font="Arial 20")
# enter_city.insert(0, "enter your city here")
#
#
# def callback(event):
#     enter_city.delete(0, "end")
#     enter_city['foreground'] = 'black'
#     enter_city['font'] = 'Arial 20 bold'
#     enter_city.unbind("<FocusIn>")
#
#     return None
#
#
# enter_city.bind("<FocusIn>", callback)
# enter_city.grid(row=0, column=0, ipady=5, padx=200, pady=50)
#
# search_button = Button(root, text="Search", width=20, fg="white", bg="blue", borderwidth=5)
# search_button.grid(row=1, column=0, rowspan=1, ipady=5, padx=200)
#
# city_location = Label(root, text="", fg="white", bg="blue")
# city_location.grid(row=3, column=0, ipady=5, padx=200, pady=1)
#
# city_temperature = Label(root, text="", fg="white", bg="blue")
# city_temperature.grid(row=4, column=0, ipady=5, padx=200, pady=1)
#
# city_weather = Label(root, text="", fg="white", bg="blue")
# city_weather.grid(row=5, column=0, ipady=5, padx=200, pady=1)
#
# root.mainloop()

api_key = 'f1886475398d75b0103e58ab291ac519'

user_input = input("enter your city: ")

data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

if data.json()["cod"] == "404":
    print("No city found")
else:
    weather = data.json()["weather"][0]["main"]
    f_temperature = data.json()["main"]["temp"]
    temperature = round(((f_temperature + 32) * 5 / 9), 2)

    print(f"The weather condition in {user_input} is: {weather}")
    print(f"The temperature is {temperature}°C")

