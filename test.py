from tkinter import *

def main():
    global entry1
    root = Tk()
    label1 = Label(text='entry your name here')
    label1.pack()
    label1.place(x=200, y=180)

    entry1 = Entry(bd=2)
    entry1.pack()
    entry1.place(x=180, y=220)

    button1 = Button(text='click', command=hello)
    button1.pack()
    button1.place(x=250, y=260)

    root.mainloop()

def hello():
    label2 = Label(text=('Hello!! '+ entry1.get()))
    label2.pack()

if __name__ == '__main__':
    main()
