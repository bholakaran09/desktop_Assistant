from tkinter import  *
import tkinter as tk
from tkinter import messagebox

main = tk.Tk()
main.geometry("300x100")
main.resizable(0,0)
main.configure(background="sky blue")


main.title("My Assistant")

def fun():
  messagebox.showinfo(message="Great! The assistant is now ready.", title="Ready!")
  main.destroy()
  import Desktop_Assistant

startbutton= Button(main, text="Yes", bg="Green",command=fun)
startbutton.place(x=50,y=50)

exitbutton= Button(main, text="No", command=main.destroy, bg="Red")
exitbutton.place(x=180,y=50)

label=tk.Label(main,text="Do you want to start using the assistant?", bg="sky blue",font=("Times New Roman",13))
label.place(x=10,y=10)

main.mainloop()