from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city =city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=dde141605ecab2c286ee1bba4860784c").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=int(data["main"]["temp"]-273.15))
    pre_label1.config(text=data["main"]["pressure"])

win=Tk()
win.title("VNR VJIET")
win.config(bg="blue")
win.geometry("500x570")

name_label=Label(win,text="VNR Weather App",font=("times new roman",25,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name=StringVar()
list_name=["Mumbai","Delhi","Bangalore","Hyderabad","Ahmedabad","Chennai","Kolkata","Surat","Pune","Jaipur","Lucknow","Kanpur","Nagpur","Visakhapatnam","Indore","Thane","Bhopal","Patna","Vadodara","Ghaziabad"]
com=ttk.Combobox(win,text="VNR Weather App",values=list_name,font=("times new roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

w_label=Label(win,text="Weather Climate",font=("times new roman",18))
w_label.place(x=25,y=260,height=50,width=210)
w_label1=Label(win,text="",font=("times new roman",18))
w_label1.place(x=250,y=260,height=50,width=210)

wb_label=Label(win,text="Weather Description",font=("times new roman",14))
wb_label.place(x=25,y=330,height=50,width=210)
wb_label1=Label(win,text="",font=("times new roman",15))
wb_label1.place(x=250,y=330,height=50,width=210)

temp_label=Label(win,text="Temperature",font=("times new roman",20))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1=Label(win,text="",font=("times new roman",20))
temp_label1.place(x=250,y=400,height=50,width=210)

pre_label=Label(win,text="Pressure",font=("times new roman",20))
pre_label.place(x=25,y=470,height=50,width=210)
pre_label1=Label(win,text="",font=("times new roman",20))
pre_label1.place(x=250,y=470,height=50,width=210)

done_button=Button(win,text="Done",font=("times new roman",20,"bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)

win.mainloop()