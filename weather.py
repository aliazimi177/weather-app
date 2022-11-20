import requests
import tkinter as tk
from math import floor # or ceil # round is a built-in tool

window = tk.Tk()
window.geometry("300x404+200+200")
window.maxsize(500,600)
window.minsize(200,300)
#*********************************************************api*************************************************

#*********************************************************image***********************************************
img = tk.PhotoImage(file="./uuu.png")  # it's better to use os.path.join(os.directory(__file__), "uuu.png") but forget which I wrote
img_show = tk.Label(image = img)
#*********************************************************title***********************************************
window.title("weather")
#********************************************************defind***********************************************
def get_name():
    name = entry_1.get()
    city = entry_2.get()
    city = city.lower()
    print(f"name is {name} and city is {city}")
    window_2 = tk.TopLevel(window) # in this case user doesn't need to restart program to check another city
    window_2.geometry("200x200")
    window_2.maxsize(150,200)
    window_2.minsize(150,200)
    # readablity of f string is better than `+` operator
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=06c921750b9a82d8f5d1294e1586276f" 
    res = requests.get(api)
    data = res.json()
    condition = data['weather'][0]['main']
    """int in bigger than zero numbers makes the number smaller and in smaller than zero numbers make  the 
    number bigger, so that use floor (for make it smaller), ceil (for make it bigger), and round (to make 
    bigger or smaller depends on the decimal part) instead"""
    temp = floor(data['main']['temp'] - 273.15) # or ceil(data['main']['temp'] - 273.15) or round(data['main']['temp'] - 273.15)   
    final_info = f"{condition}\n{temp}°C"  # readablity of f string is better than `+` operator
    lable_3 = tk.Label(window_2,text=final_info)
    button_3 = tk.Button(window_2,text="exit",bg="khaki",fg="BLACK",command=exit,width=40,height=2) # you should change this
    button_3.pack()
    label_3.pack()
    
#*********************************************************frame***********************************************
frame_1 = tk.Frame(window)
frame_2 = tk.Frame(window)
#*********************************************************lable***********************************************
label_1 = tk.Label(frame_1,text="name :",bg="khaki",fg="BLACK",width=28,height=2)
label_2 = tk.Label(frame_2,text="city :",bg="khaki",fg="BLACK",width=28,height=2)
#*********************************************************entry***********************************************
entry_1 = tk.Entry(frame_1,bg="olive drab",fg="BLACK",font=('calibre',10,'normal'),width=25,show= "*")
entry_2 = tk.Entry(frame_2,bg="olive drab",fg="BLACK",font=('calibre',10,'normal'),width=25)
#*********************************************************button**********************************************
button = tk.Button(text="exit",bg="khaki",fg="BLACK",command=exit,width=25,height=2)
button_1 = tk.Button(text="get data",bg="khaki",fg="BLACK",command=get_name,width=25,height=2)

#**********************************************************pack*********************************************
img_show.pack()
frame_1.pack()
frame_2.pack()
label_1.pack()
entry_1.pack()
label_2.pack()
entry_2.pack()
button_1.pack()
button.pack()

if __name__ =="__main__":
    window.mainloop()
