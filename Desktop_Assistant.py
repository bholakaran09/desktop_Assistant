 #-------------------------------------------MODULES REQUIRED------------------------------------------------------------

import wikipedia
from tkinter import *
import speech_recognition as sr
import pyjokes
import pyaudio
import os
import pyttsx3
import datetime
import time
from datetime import date

#-----------------------------------------Creating Tkinter Window-----------------------------------------------------

win=Tk()
win.title("Desktop Assistant")
win.geometry('500x530')
win.resizable(0,0)
win.config(bg='sky blue')

#-----------------------------------------------Functions Used-----------------------------------------------------

text="" 
answer="" 
num=0
mun=0

a=0
def modechange(b):                               #For changing background of Textbox
    global a
    a=a+b
    if(a%2==0):
        response.configure(background="White")
        userlabel.configure(background="White")
    else:
        response.configure(background="Black")
        userlabel.configure(background="Black")


def update_clock():                              #for update clock
    now=time.strftime("%H:%M:%S")
    timelabel.configure(text=now)
    win.after(1000,update_clock)


def update_date():                               #for updating date
    curr_date=date.today()
    datelabel.configure(text=curr_date)
    win.after(90000,update_date)


def sendtext():                                  #for taking command from entry
    global t2
    global text
    global num
    t2=entry.get()
    num=num+1
    userlabel.insert(END,num)
    userlabel.insert(END,".) ")
    userlabel.insert(END,t2)
    userlabel.insert(END,'\n')
    text=t2
    entry.delete(0, END)
    check()

   
def speak():                                      #for converting voice input into text
    global text
    global num
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        num=num+1
        userlabel.insert(END,num)
        userlabel.insert(END,".) ")
        userlabel.insert(END,text)
        userlabel.insert(END,'\n')
        check()   


def check():                                      #for searching answer
    global text
    global answer
    global mun
    try:
        if (text== "what is your name" or text=="what's your name" ):
            answer=  "My name is Corona \n"
        elif (text== "who made you" or text=="who developed you" ):
            answer=  "Karan Bhola created me \n"
        elif (text== "what can you do for me" or "what can you do"):
            answer=  "Anything you like \n"
        elif (text== "how old are you"):
            answer=  ("I was launched this month, so I'm still fairly young. But I've learned so much! I hope I'm wise beyond my years. \n")     
        elif (text =="tell me a joke" or text=="can you tell me a joke"):
            answer=  (pyjokes.get_joke())   
        elif (text== "do you ever get tired"):
            answer=  "It would be impossible to tired of our conversation \n"   
        elif (text =="what are you wearing"):
            answer=  "I am just wearing the skin of your PC \n" 
        elif (text== "where do you live"):
            answer=  "I live in your pc to provide you best service \n"
        elif (text =="when is your birthday" or text=="what is your birth date"):
            answer=  "I was launched on 30th july \n"    
        elif (text =="how we can kill you" or text=="can we kill you"):
            answer=  "haa,haa,haa, no one can kill my program except my developers,you can just stop me \n"
        elif (text =="do you like maths" or text=="do you like science"):
            answer=  "Yeah i like it \n"
        elif (text=="do you like animals"):
            answer=  "I don't know,I never deal with them!!! \n" 
        elif (text=="how are you"):
            answer=  "Well, I'm fine ,what about you? \n" 
        elif (text=="I am good" or text=="I am fine"):
            answer=  "That's great!!! \n"            
        elif (text =="which is your favorite sport" or text=="which sport do you like"):
            answer= "I like every sport but Cricket is my favorite \n"
        elif(text=="who is your favorite cricketer" or text=="which is best cricketer"):
            answer= "Obviously MS Dhoni \n"
        elif(text=='what is my current working directory'):
            answer= os.getcwd()
        elif (text =="shut down pc" or text =="shutdown"):
            answer="Shutting down PC"
            os.system("shutdown /s /t 1")
        elif (text =="restart pc" or text =="restart"):
            answer="Restarting PC"
            os.system("shutdown /r /t 1")
        elif (text =="open Chrome" or text =="I want to search something"):
            answer="Opening Chrome..."
            os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        elif (text =="open Word" or text=="open world"):
            answer="Opening Word..."
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Word.lnk')
        elif (text=="I want to take notes"):
            answer="OneNote or Notepad?"
        elif (text=="notepad"):
            answer="Opening Notepad..."
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Notepad.lnk')
        elif (text== "one note"):
            answer="Opening One note..."
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OneNote 2016.lnk')
        elif (text =="open Excel"):
            answer="Opening Excel..."
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Excel.lnk')
        elif (text=="do you believe in God" or text=="does god exist"):
            answer=  "Yes,actually my developers believe in God, and that is what they taught me \n"
        elif (text=="play a song"):
            answer="Which song you want to listen?\nPerfect\nShape of you"
        elif (text=="Perfect" or text=="perfect" or text=="play perfect"):
            os.system("perfect.mp3") 
        elif (text=="shape of you" or text=="play shape of you"):
            os.system('shapeofyou.mp3')   
        else:
            response.insert("I don't understand. Trying Wikipedia....\n")
    except :
        answer=wikipedia.summary(text)
        response.insert(END,'Answer from Wikipedia...\n')
    mun=mun+1    
    response.insert(END,mun) 
    response.insert(END,'.) ')    
    response.insert(END,answer,'\n')  
    outputaudio()

def outputaudio():                                #for giving audio output
    global answer
    engine = pyttsx3.init()
    engine.say(answer)
    engine.runAndWait()

#----------------------------------------------Tkinter widgets--------------------------------------------------------

canvas=Canvas(win,bd=5,bg='sky blue',height=422,width=460)
canvas.place(x=10,y=30)                                                                                                                                                                                                                                                                                                         

modebtn=Button(win,text="Change\nMode",fg='black',width=6,font=('Arial',12),bg='sky blue',activebackground='pink',command=lambda:modechange(1))
modebtn.place(x=10,y=470)

photo=PhotoImage(file="voiceimage.png")
speakbtn=Button(win,image=photo,height=45,width=35,activebackground="pink",command=lambda:speak())
speakbtn.place(x=80,y=470)

t1=StringVar()
entry=Entry(win,width=45,bd=10,textvariable=t1)
entry.place(x=130,y=475)

sendbtn=Button(win,text="Send",fg='black',font=('Arial',12),bg='sky blue',activebackground='pink',command=lambda:sendtext())
sendbtn.place(x=434,y=477)

response=Text(canvas,font=('Arial, 12'),bg='white',fg='green',wrap=WORD,width=24,height=23)
response.place (x=10,y=10)

userlabel=Text(canvas,font=('Arial',12),wrap=WORD,bg='white',fg='red',width=24,height=23)
userlabel.place(x=242,y=10)

timelabel=Label(text="",fg='black',bg='sky blue',width=15,font=('Times New Roman',15))
timelabel.pack(anchor='nw')
update_clock()

datelabel=Label(text="",fg='black',bg='sky blue',width=15,font=('Times New Roman',15))
datelabel.place(x=320)
update_date()

win.mainloop()