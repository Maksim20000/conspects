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

for i in range(5):
    for j in range(3):
        tk.Button(win, text=f'text {i} и {j}').grid(row=i, column=j)

# btn1 = tk.Button(win, text='Кнопка1')
# btn2 = tk.Button(win, text='Кнопка2')
# btn3 = tk.Button(win, text='Кнопка3')
# btn4 = tk.Button(win, text='Кнопка4 текст')
# btn5 = tk.Button(win, text='Кнопка5')
# btn6 = tk.Button(win, text='Кнопка6')
# btn7 = tk.Button(win, text='Кнопка7')
# btn8 = tk.Button(win, text='Кнопка8')
#
#
#
# btn1.grid(row=1, column=0)
# btn2.grid(row=1, column=1, sticky='ew')
# btn3.grid(row=2, column=0)
# btn4.grid(row=2, column=1)
# btn5.grid(row=3, column=0)
# btn6.grid(row=3, column=1, sticky='ew')
# btn7.grid(row=4, column=0, columnspan=2, sticky='ew')
# btn8.grid(row=1, column=3, rowspan=4, sticky='sn')

win.grid_columnconfigure(3, minsize=500)
win.mainloop()