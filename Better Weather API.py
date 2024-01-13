from tkinter import *
import tkinter as tk
from timezonefinder import TimezoneFinder
from datetime import *
import requests
from opencage.geocoder import OpenCageGeocode
from PIL import Image, ImageTk
import pytz

root = Tk()
root.title("Weather App")
root.geometry("1000x450+300+200")
root.configure(bg="#FAEBD3")
root.resizable(False, False)

def getWeather():
    city = textfield.get()

    # Geocoding using OpenCage
    api_key_opencage = "2c32d6fbabcc46cdadba7a2f9e9fe9be"
    geocoder_opencage = OpenCageGeocode(api_key_opencage)

    try:
        location = geocoder_opencage.geocode(city)[0]
        # ... (rest of the geocoding code)
    except Exception as e:
        print(f"Error during geocoding: {e}")
        return  # Exit the function if geocoding fails

    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location['geometry']['lng'], lat=location['geometry']['lat'])

    timezone.config(text=result)
    long_lat.config(text=f"{round(location['geometry']['lat'], 4)}°N,{round(location['geometry']['lng'], 4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    # Weather
    api = "https://api.openweathermap.org/data/2.5/onecall?lat=" + str(location['geometry']['lat']) + "&lon=" + str(
        location['geometry']['lng']) + "&units=metric&exclude=hourly&appid=cca950f476162f279e0aa3cb7b9df039"
    json_data = requests.get(api).json()

    try:
        # Check if 'daily' key exists in the JSON response
        if 'daily' in json_data:
            # Extract information for the first day
            firstdayimage = json_data['daily'][0]['weather'][0]['icon']
            tempday1 = json_data['daily'][0]['temp']['day']
            tempnight1 = json_data['daily'][0]['temp']['night']
        
        else:
            print("Error: 'daily' key not found in API response")

    except Exception as e:
        print(f"Error processing weather data: {e}")
        
    try:
        # Extract weather information
        temp = json_data['current']['temp']
        humidity = json_data['current']['humidity']
        pressure = json_data['current']['pressure']
        wind = json_data['current']['wind_speed']
        description = json_data['current']['weather'][0]['description']

    except Exception as e:
        print(f"Error extracting weather information: {e}")
    # Optionally, you can set default values or handle the error in another way
    temp = "N/A"
    humidity = "N/A"
    pressure = "N/A"
    wind = "N/A"
    description = "N/A"
    
    #Current
    if 'current' in json_data:
        # Extract weather information
        temp = json_data['current']['temp']
        humidity = json_data['current']['humidity']
        pressure = json_data['current']['pressure']
        wind = json_data['current']['wind_speed']
        description = json_data['current']['weather'][0]['description']
    
    else:
        print("Error: 'current' key not found in API response")
    
    t.config(text=(temp, "°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=description)

    #First Cell
    firstdayimage= json_data['daily'][0]['weather'][0]['icon']

    photo1 = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
    firstimage.config(image = photo1)
    firstimage.image = photo1

    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']

    day1temp.config(text=f"Day:{tempday1} | Night:{tempnight1}")


    #Second Cell
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']

    img=(Image.open(f"icon/{seconddayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image = photo2

    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']

    day2temp.config(text=f"Day:{tempday2}\n Night:{tempnight2}")

    #Third Cell
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']

    img=(Image.open(f"icon/{thirddayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3

    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3 = json_data['daily'][2]['temp']['night']

    day3temp.config(text=f"Day:{tempday3}\n Night:{tempnight3}")

    #Fourth Cell
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']

    img=(Image.open(f"icon/{fourthdayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4

    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4 = json_data['daily'][3]['temp']['night']

    day4temp.config(text=f"Day:{tempday4}\n Night:{tempnight4}")

    #Fifth Cell
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']

    img=(Image.open(f"icon/{fifthdayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5

    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']

    day5temp.config(text=f"Day:{tempday5}\n Night:{tempnight5}")

    #Sixth Cell
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']

    img=(Image.open(f"icon/{sixthdayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6

    tempday6= json_data['daily'][5]['temp']['day']
    tempnight6= json_data['daily'][5]['temp']['night']

    day6temp.config(text=f"Day:{tempday6}\n Night:{tempnight6}")

    #Seventh Cell
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']

    img=(Image.open(f"icon/{seventhdayimage}@2x.png"))
    resized_image = img.resize((50,50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image = photo7

    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7 = json_data['daily'][6]['temp']['night']

    day7temp.config(text=f"Day:{tempday7}\n Night:{tempnight7}")

    #Days

    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))


##Icon
image_icon = tk.PhotoImage(file="Images\logo.png")
root.iconphoto(False,image_icon)

##Top

#Clock
clock=Label(root,font=("Helvetica",35,'bold'),fg="#321E17",bg="#FAEBD3")
clock.place(x=30,y=20)

#Timezone
timezone=Label(root,font=("Helvetica",20),fg="#321E17",bg="#FAEBD3")
timezone.place(x=30,y=70)

long_lat=Label(root,font=("Helvetica",10),fg="#321E17",bg="#FAEBD3")
long_lat.place(x=30,y=105)

#Search Box
searchframe=Frame(root,width=500,height=60,bg="#321E17")
searchframe.place(x=450,y=20)

weat_image=PhotoImage(file="Images\Layer 7.png")
weatherimage=Label(root,image=weat_image,bg="#321E17")
weatherimage.place(x=470,y=27)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#321E17",border=0,fg="white")
textfield.place(x=560,y=30)
textfield.focus()

search_icon_image = Image.open("Images\Layer 6.png")
resized_search_icon = ImageTk.PhotoImage(search_icon_image.resize((50, 50), resample=Image.NEAREST))

def on_search_icon_click():
    getWeather()  # Call the getWeather function when the button is clicked

search_icon_button = tk.Button(root, image=resized_search_icon, bg="#321E17", borderwidth=0, command=on_search_icon_click)
search_icon_button.pack()
search_icon_button.place(x=880, y=25)

##Label
labelframe=Frame(root,width=250,height=115,bg="#321E17")
labelframe.place(x=700,y=115)

label1=Label(root,text="Temperature",font=('Helvetica',11),fg="white",bg="#321E17")
label1.place(x=710,y=120)

label2=Label(root,text="Humidity",font=('Helvetica',11),fg="white",bg="#321E17")
label2.place(x=710,y=140)

label3=Label(root,text="Pressure",font=('Helvetica',11),fg="white",bg="#321E17")
label3.place(x=710,y=160)

label4=Label(root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="#321E17")
label4.place(x=710,y=180)

label5=Label(root,text="Description",font=('Helvetica',11),fg="white",bg="#321E17")
label5.place(x=710,y=200)

#thpwd (temperature, humidity, pressure, wind speed, description)
t=Label(root,font=("Helvetica",11),fg="white",bg="#321E17")
t.place(x=820,y=120)
h=Label(root,font=("Helvetica",11),fg="white",bg="#321E17")
h.place(x=820,y=140)
p=Label(root,font=("Helvetica",11),fg="white",bg="#321E17")
p.place(x=820,y=160)
w=Label(root,font=("Helvetica",11),fg="white",bg="#321E17")
w.place(x=820,y=180)
d=Label(root,font=("Helvetica",11),fg="white",bg="#321E17")
d.place(x=820,y=200)

##Bottom
frame=Frame(root,width=1000,height=180,bg="#321E17")
frame.pack(side=BOTTOM)

#Bottom Boxes
first_box = Image.open("Images\Rounded Rectangle 2.png")
resized_first_box = ImageTk.PhotoImage(first_box.resize((325, 137), resample=Image.NEAREST))

first_box_label = tk.Label(root, image=resized_first_box, bg="#321E17")
first_box_label.pack()

first_box_label.place(x=30, y=290)

secondbox=PhotoImage(file="Images\Rounded Rectangle 2 copy.png")

Label(frame,image=secondbox,bg="#321E17").place(x=400,y=30)
Label(frame,image=secondbox,bg="#321E17").place(x=500,y=30)
Label(frame,image=secondbox,bg="#321E17").place(x=600,y=30)
Label(frame,image=secondbox,bg="#321E17").place(x=700,y=30)
Label(frame,image=secondbox,bg="#321E17").place(x=800,y=30)
Label(frame,image=secondbox,bg="#321E17").place(x=900,y=30)

#First Cell
firstframe = Frame(root,width=320,height=132,bg="#321E17")
firstframe.place(x=35,y=295)

day1 = Label(firstframe,font="arial 20",bg="#321E17",fg="#fff")
day1.place(x=100,y=5)

firstimage = Label(firstframe,bg="#321E17")
firstimage.place(x=1,y=15)

day1temp = Label(firstframe,bg="#321E17",fg="#fff",font="arial 15 bold")
day1temp.place(x=100,y=50)

#Second Cell
secondframe = Frame(root,width=70,height=115,bg="#321E17")
secondframe.place(x=405,y=305)

day2 = Label(secondframe,bg="#321E17",fg="#fff")
day2.place(x=10,y=5)

secondimage = Label(secondframe,bg="#321E17")
secondimage.place(x=7,y=23)

day2temp = Label(secondframe,bg="#321E17",fg="#fff")
day2temp.place(x=2,y=70)

#Third Cell
thirdframe = Frame(root,width=70,height=115,bg="#321E17")
thirdframe.place(x=505,y=305)

day3 = Label(thirdframe,bg="#321E17",fg="#fff")
day3.place(x=10,y=5)

thirdimage = Label(thirdframe,bg="#321E17")
thirdimage.place(x=7,y=23)

day3temp = Label(thirdframe,bg="#321E17",fg="#fff")
day3temp.place(x=2,y=70)

#Fourth Cell
fourthframe = Frame(root,width=70,height=115,bg="#321E17")
fourthframe.place(x=605,y=305)

day4 = Label(fourthframe,bg="#321E17",fg="#fff")
day4.place(x=10,y=5)

fourthimage = Label(fourthframe,bg="#321E17")
fourthimage.place(x=7,y=23)

day4temp = Label(fourthframe,bg="#321E17",fg="#fff")
day4temp.place(x=2,y=70)

#Fifth Cell
fifthframe = Frame(root,width=70,height=115,bg="#321E17")
fifthframe.place(x=705,y=305)

day5 = Label(fifthframe,bg="#321E17",fg="#fff")
day5.place(x=10,y=5)

fifthimage = Label(fifthframe,bg="#321E17")
fifthimage.place(x=7,y=23)

day5temp = Label(fifthframe,bg="#321E17",fg="#fff")
day5temp.place(x=2,y=70)

#Sixth Cell
sixthframe = Frame(root,width=70,height=115,bg="#321E17")
sixthframe.place(x=805,y=305)

day6 = Label(sixthframe,bg="#321E17",fg="#fff")
day6.place(x=10,y=5)

sixthimage = Label(sixthframe,bg="#321E17")
sixthimage.place(x=7,y=23)

day6temp = Label(sixthframe,bg="#321E17",fg="#fff")
day6temp.place(x=2,y=70)

#Seventh Cell
seventhframe = Frame(root,width=70,height=115,bg="#321E17")
seventhframe.place(x=905,y=305)

day7 = Label(seventhframe,bg="#321E17",fg="#fff")
day7.place(x=10,y=5)

seventhimage = Label(seventhframe,bg="#321E17")
seventhimage.place(x=7,y=23)

day7temp = Label(seventhframe,bg="#321E17",fg="#fff")
day7temp.place(x=2,y=70)


root.mainloop()