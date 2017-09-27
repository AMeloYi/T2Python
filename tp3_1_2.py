from tkinter import *
import math

fenetre = Tk()
fenetre.title('Calculator')
frm = Frame(fenetre)
frm.pack(expand = YES,fill = BOTH)

menubar = Menu(fenetre)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=None)
filemenu.add_command(label="Save", command=None)
filemenu.add_command(label="Exit", command=fenetre.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=None)
editmenu.add_command(label="Copy", command=None)
editmenu.add_command(label="Paste", command=None)
menubar.add_cascade(label="Edit", menu=editmenu)

fenetre.config(menu=menubar)

display=StringVar()
ent = Entry(frm, textvariable=display)
ent.grid(row=0, column=0, sticky=N+E+S+W, columnspan=5, rowspan=2)

Button(frm, text='sin', width=4, bg='yellow', command=lambda:display.set(math.sin(float(display.get())))).grid(row=2, column=0, sticky=W)
Button(frm, text='cos', width=4, bg='yellow', command=lambda:display.set(math.cos(float(display.get())))).grid(row=2, column=1)
Button(frm, text='tan', width=4, bg='yellow', command=lambda:display.set(math.tan(float(display.get())))).grid(row=2, column=2)
Button(frm, text='(', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'(')).grid(row=2, column=3)
Button(frm, text=')', width=4, bg='yellow', command=lambda:ent.insert(INSERT,')')).grid(row=2, column=4)
Button(frm, text='1', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'1')).grid(row=3, column=0, sticky=W)
Button(frm, text='2', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'2')).grid(row=3, column=1)
Button(frm, text='3', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'3')).grid(row=3, column=2)
Button(frm, text='AC', width=4, bg='yellow', command=lambda:display.set('')).grid(row=3, column=3)
Button(frm, text='C', width=4, bg='yellow', command=lambda:display.set(display.get()[0:len(display.get())-1])).grid(row=3, column=4)
Button(frm, text='4', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'4')).grid(row=4, column=0, sticky=W)
Button(frm, text='5', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'5')).grid(row=4, column=1)
Button(frm, text='6', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'6')).grid(row=4, column=2)
Button(frm, text='+', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'+')).grid(row=4, column=3)
Button(frm, text='-', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'-')).grid(row=4, column=4)
Button(frm, text='7', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'7')).grid(row=5, column=0, sticky=W)
Button(frm, text='8', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'8')).grid(row=5, column=1)
Button(frm, text='9', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'9')).grid(row=5, column=2)
Button(frm, text='*', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'*')).grid(row=5, column=3)
Button(frm, text='/', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'/')).grid(row=5, column=4)
Button(frm, text='-', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'-')).grid(row=6, column=0, sticky=W)
Button(frm, text='0', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'0')).grid(row=6, column=1)
Button(frm, text='.', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'.')).grid(row=6, column=2)
Button(frm, text='^', width=4, bg='yellow', command=lambda:ent.insert(INSERT,'**')).grid(row=6, column=3)
Button(frm, text='=', width=4, bg='yellow', command=lambda:display.set(eval(display.get()))).grid(row=6, column=4)

fenetre.mainloop()
