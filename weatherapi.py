from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
     try :
          city = textfield.get()

          geolocator = Nominatim(user_agent = "http://geonames.org/",timeout=200)
          location = geolocator.geocode(city)
          obj = TimezoneFinder()
          result = obj.timezone_at(lng = location.longitude,lat = location .latitude)
          
          home = pytz.timezone(result)
          local_time = datetime.now(home)
          current_time = local_time.strftime( "%I:%M %p")
          clock.config(text = current_time)
          name.config(text = "CURRENT WEATHER" )

          #weather
          api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=55834e088ad13f9b6eacc5a2ce3b3501"

          json_data = requests.get(api).json()
          condition = json_data['weather'][0]['main']
          description = json_data['weather'][0]['description']
          temp = int(json_data['main']['temp']-273.15)
          pressure = json_data['main']['pressure']
          humidity = json_data['main']['humidity']
          wind     = json_data['wind']['speed']
          

          t.config(text = (temp,"°C"))
          c.config(text = (condition,"|", "FEELS","LIKE",temp ,"°"))
          w.config(text = (wind,"m/s"))
          h.config(text = ( humidity,"%"))
          d.config(text = description)
          p.config(text = ( pressure,"hPa"))

     except Exception as e:
          messagebox.showerror("Weather App","INVALID ENTRY!!")
     

#icon

image_icon=ImageTk.PhotoImage(file = r"C:\Users\kaurj\OneDrive\Documents\logo-2.0.jpg") 
root.iconphoto(False,image_icon)

#search box
Search_image = ImageTk.PhotoImage(file = r"C:\Users\kaurj\Downloads\Copy of search.png")
myimage = Label(image = Search_image)
myimage.place(x=20,y=20)

textfield= tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=ImageTk.PhotoImage(file = r"C:\Users\kaurj\Downloads\Copy of search_icon.png")
myimage_icon = Button(image = Search_icon ,borderwidth =0,cursor="hand2",bg ="#404040",command = getWeather)
myimage_icon.place(x=400,y=32)

#logo
Logo_image = ImageTk.PhotoImage(file = r"C:\Users\kaurj\Downloads\Copy of logo.png")
logo = Label(image = Logo_image)
logo.place(x=150,y=100)

#bottom box
Frame_image =ImageTk.PhotoImage(file = r"C:\Users\kaurj\Downloads\Copy of box.png")
frame = Label(image = Frame_image)
frame.pack(padx =10, pady =10, side = BOTTOM)

#time
name = Label(root,font=("arial", 15,"bold "))
name.place(x=30,y=100)
clock = Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1 = Label(root,text = "WIND",font=("Helvetica",15,"italic","bold"),fg = "black",bg ="#1ab5ef")
label1.place(x=120,y=400)

label2 = Label(root,text = "HUMIDITY",font=("Helvetica",15,"italic","bold"),fg = "black",bg ="#1ab5ef")
label2.place(x=250,y=400)


label3 = Label(root,text = "DESCRIPTION",font=("Helvetica",15,"italic","bold"),fg = "black",bg ="#1ab5ef")
label3.place(x=420,y=400)

label4 = Label(root,text = "PRESSURE",font=("Helvetica",15,"italic","bold"),fg = "black",bg ="#1ab5ef")
label4.place(x=650,y=400)
