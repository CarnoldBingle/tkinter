#Carson
#Mr. Beradino
#Compute Science
#10/4/2023

from tkinter import *

master = Tk()
var1 = IntVar()
Checkbutton(master, text='Boy', variable=var1).pack()
var2 = IntVar()
Checkbutton(master, text='Girl', variable=var2).pack()
var3 = IntVar()
Checkbutton(master, text='Student', variable=var3).pack()
var4 = IntVar()
Checkbutton(master, text='Coding Genius', variable=var4).pack()


Label(master, text='Give me your first name ').pack()
Label(master, text='Give me your last name ').pack()
e1 = Entry(master)
e2 = Entry(master)
e1.pack()
e2.pack()


w = Label(master, text='1) Label')
w.pack()
w2 = Label(master, text='2) Label')
w2.pack()
w3 = Label(master, text='3) Label')
w3.pack()
w4 = Label(master, text='4) Label')
w4.pack()



#r = tk.Tk()
#Button number 1
master.title('Buttons')
button = Button(master, text='Press for super powers', width=30, command=master.destroy)
button.pack()
#Button number 2
button2 = Button(master, text='Press for insane luck', width=30, command=master.destroy)
button2.pack()
#Button number 3
button3 = Button(master, text='Press for dreams to come true', width=30, command=master.destroy)
button3.pack()
#Button number 4
button4 = Button(master, text='Press for money', width=30, command=master.destroy)
button4.pack()

mb = Menubutton ( master, text = "Menu Page!")
mb.pack()
mb.menu = Menu ( mb, tearoff = 0 )
mb["menu"] = mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton ( label ='Contact info', variable = cVar )
mb.menu.add_checkbutton ( label = 'About us', variable = aVar )
mb.pack()


ourMessage ='Message us'
messageVar = Message(master, text = ourMessage)
messageVar.config(bg='Black')
messageVar.pack( )

w = Scale(master, from_=0, to=100000000000000)
w.pack()
w = Scale(master, from_=0, to=2, orient=HORIZONTAL)
w.pack()
mainloop()



v = IntVar()
#Need help asking a question before this
Radiobutton(master, text='Science', variable=v, value=1).pack(anchor=W)
Radiobutton(master, text='Math', variable=v, value=2).pack(anchor=W)
Radiobutton(master, text='Lang & Lit', variable=v, value=3).pack(anchor=W)
Radiobutton(master, text='Computer Science', variable=v, value=4).pack(anchor=W)
Radiobutton(master, text='ECON', variable=v, value=5).pack(anchor=W)



w = Spinbox(master, from_ = 0, to = 100)
w.pack()
mainloop()


