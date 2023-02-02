import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("GUIn") 
window.geometry("300x200") 

def showImage():
  person=text.get("1.0","end")
  if person.lower().strip()=="mo":
    canvas.itemconfig(container,image=mo)
  elif person.lower().strip()=="gerald":
    canvas.itemconfig(container,image=gerald)
  elif person.lower().strip()=="katie":
    canvas.itemconfig(container,image=katie)
  elif person.lower().strip()=="charlotte":
    canvas.itemconfig(container,image=charlotte)
  else:
    hello["text"]="Oopsie! User not in here"
    button = tk.Button(text = "Add User")
    button.pack()
    canvas.itemconfig(container,image=person)



hello = tk.Label(text = "Guess Who") 
hello.pack() 
text=tk.Text(window, height=1,width=20)
text.pack()
button = tk.Button(text = "View",command=showImage)
button.pack()
canvas = tk.Canvas(window, width = 300, height=150) 
canvas.pack()

charlotte=ImageTk.PhotoImage(Image.open(".tutorial/Guess Who/charlotte.jpg"))
gerald=ImageTk.PhotoImage(Image.open(".tutorial/Guess Who/gerald.jpg"))
katie=ImageTk.PhotoImage(Image.open(".tutorial/Guess Who/katie.jpg"))
mo=ImageTk.PhotoImage(Image.open(".tutorial/Guess Who/mo.jpg"))
container=canvas.create_image(150,2,image=mo)

tk.mainloop()