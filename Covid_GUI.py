# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 02:05:38 2020

@author: vamsi
"""


import tkinter as tk
import tkinter.filedialog as filedialog

master = tk.Tk()
master.update_idletasks()
width = master.winfo_width()
height = master.winfo_height()
x = (master.winfo_screenwidth() // 2) - (width // 2)
y = (master.winfo_screenheight() // 2) - (height // 2)
master.geometry('{}x{}+{}+{}'.format(width+150, height+50, x, y))

def input():
    input_path = tk.filedialog.askopenfilename()
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'

def test():
    #print(input_entry.get())
    from test_covid_images import test_covid
    test_covid(input_entry.get())
    master.destroy()

top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

input_path = tk.Label(top_frame, text="Please Select Xray Image Path")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input)



begin_button = tk.Button(bottom_frame, text='Begin Testing!',command=test)

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)


begin_button.pack(pady=20, fill=tk.X)


master.mainloop()