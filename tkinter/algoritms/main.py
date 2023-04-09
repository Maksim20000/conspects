import tkinter as tk
def baseInterFace():
    thinterIcon = tk.PhotoImage(file='./img/tkinter-icon.png')
    win.iconphoto(False, thinterIcon)
    win.config(bg='#1539ed')
    w = 600
    h = 500
    win.geometry(f'{w}x{h}+700+100')
    win.title('Привет Мир')

win = tk.Tk()
baseInterFace()


win.mainloop()