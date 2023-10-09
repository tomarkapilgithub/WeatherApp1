from tkinter import *

import requests
import json


window = Tk()
window.title("Welcome to DUCAT")
l1 = Label(window, text="Weather APP", bg="yellow", fg="blue", width=40)
# l1.pack()
#l1.grid(rows=1500, columns=250)
l1.place(x=550, y=400)

img = PhotoImage(file="logo1.png")
l2 = Label(window, image=img)
l2.pack()

v = StringVar()

def action():
    city = v.get()
# API - application programming interface
    # url = "http://api.weatherapi.com/v1/current.json?key=bd962ac5e2c045b590b82104231306&q=Jaipur"
    url = "http://api.weatherapi.com/v1/current.json?key=e4e954117008449da6581103231306&q="+city
    df = requests.get(url)
    data = json.loads(df.content)
    l8.config(text="" +
              str(data['current']['temp_c']), bg="pink", fg="blue")
    l9.config(text="" +
              str(data['current']['temp_f']), bg="pink", fg="blue")
    l10.config(text="" +
               str(data['current']['wind_mph']), bg="pink", fg="blue")
    l11.config(text="" +
               str(data['current']['wind_kph']), bg="pink", fg="blue")

    #print(f"Temperature of {data['location']['name']} is {data['current']['temp_c']}")

    # print(df.content)


e1 = Entry(window, width=20, font=("Calibri", 20), textvariable=v)
e1.place(x=600, y=445)
b1 = Button(window, text="Submit", bg="green", fg="yellow", command=action)
b1.place(x=650, y=500)
l3 = Label(window, text="Weather Forecasting",
           bg="yellow", fg="blue", width=40)
l3.place(x=550, y=550)
l4 = Label(window, text="Enter your city name : ->",
           bg="white", fg="black", width=40)
l4.place(x=300, y=450)
window.minsize(width=100, height=200)
window.maxsize(width=500, height=800)

l5 = Label(window, text="Temperature in Celsius: -> ",                  
           bg="white", fg="black", width=40)
l5.place(x=300, y=600)
l6 = Label(window, text="Temperature in Ferenheit: -> ",
           bg="white", fg="black", width=40)
l6.place(x=300, y=640)
l7 = Label(window, text="Wind Speed in Mph: -> ",
           bg="white", fg="black", width=40)
l7.place(x=300, y=680)
l12 = Label(window, text="Wind Speed in kph: -> ",
            bg="white", fg="black", width=40)
l12.place(x=300, y=720)
l8 = Label(window, text="",
           bg="white", fg="black", width=40)
l8.place(x=600, y=595)
l9 = Label(window, text="",
           bg="white", fg="black", width=40)
l9.place(x=600, y=635)
l10 = Label(window, text="",
            bg="white", fg="black", width=40)
l10.place(x=600, y=675)
l11 = Label(window, text="",
            bg="white", fg="black", width=40)
l11.place(x=600, y=705)
window.mainloop()


import tkinter as tk
import requests
import time


def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + \
        city+"&appid=8ebac43c75dad9960600bd53f39a35c7"
    json_data = requests.get(api).json()
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    condition = json_data['weather'][0]['main']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(
        json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(
        json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Pressure: " + str(
        pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


 canvas = tk.Tk()
 canvas.geometry("600x500")
 canvas.title("Weather App")
 f = ("poppins", 15, "bold")
 t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()

label1 = tk.label(canvas, font=t)
label1.pack()

label2 = tk.label(canvas, font=f)
label2.pack()

canvas.mainloop()




