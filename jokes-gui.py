from tkinter import *
import pyjokes

root = Tk()
root.geometry("600x300")

root.title("Jokes GUI Application")

try:
    icon = PhotoImage(file='jerry.png')
    root.iconphoto(True, icon)
except Exception as e:
    print(f"Error loading icon: {e}")


root.configure(bg='#2c3e50')

def new_joke():
    scvalue.set(pyjokes.get_joke())


def clear_text():
    scvalue.set("")


frame = Frame(root, bg='#34495e')
frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

scvalue = StringVar()

joke_label = Label(frame, textvariable=scvalue, font=('Comic Sans MS', 14), bg='#ecf0f1',
                   fg='#2c3e50', wraplength=500, justify=LEFT, anchor="w", padx=20, pady=20)
joke_label.pack(fill=BOTH, expand=True)


b1 = Button(frame, text='New Joke', command=new_joke, font=('Helvetica', 12, 'bold'),
            bg='#1abc9c', fg='white', padx=10, pady=5, relief=RAISED, bd=3)
b1.pack(side=LEFT, padx=20, pady=10)

b2 = Button(frame, text='Clear', command=clear_text, font=('Helvetica', 12, 'bold'),
            bg='#e74c3c', fg='white', padx=10, pady=5, relief=RAISED, bd=3)
b2.pack(side=LEFT, padx=20, pady=10)

b3 = Button(frame, text='Exit', command=root.destroy, font=('Helvetica', 12, 'bold'),
            bg='#95a5a6', fg='white', padx=10, pady=5, relief=RAISED, bd=3)
b3.pack(side=LEFT, padx=20, pady=10)

root.mainloop()
