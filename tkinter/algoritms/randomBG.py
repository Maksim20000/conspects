import random
import tkinter as tk

def baseInterFace():
    thinterIcon = tk.PhotoImage(file='./img/tkinter-icon.png')
    win.iconphoto(False, thinterIcon)
    win.config(bg='#1539ed')
    w = 600
    h = 500
    win.geometry(f'{w}x{h}+700+100')
    win.title('Привет Мир')


colors = ['red', 'white', 'blue', 'black', 'green']

def randomColorDef():
    global colors
    randomColorResult = random.choice(colors)
    win.config(bg=randomColorResult)

win = tk.Tk()
baseInterFace()
btn = tk.Button(win, command=randomColorDef, text='Поменять цвет фона')
btn.pack()
win.mainloop()