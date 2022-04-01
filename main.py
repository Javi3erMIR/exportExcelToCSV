from cProfile import run
from tkinter import *
from tkinter import filedialog
import os
import pandas as pd

window = Tk()
label1_str = StringVar()
label2_str = StringVar()

def open_excel():
        file = filedialog.askopenfile(title='Cargar Excel', 
                                    initialdir=os.path.expanduser('~/Documents'), 
                                    filetypes=(('Excel Files', '*.xlsx'),
                                                ('All files', '*.*')))
        label1_str.set(file.name)


def open_csv():
        file = filedialog.askopenfile(title='Cargar CSV', 
                                    initialdir=os.path.expanduser('~/Documents'), 
                                    filetypes=(('CSV Files', '*.csv'),
                                                ('All files', '*.*')))
        label2_str.set(file.name)

def export_to_csv():
    excel_file = pd.read_excel(label1_str.get())
    csv_file = pd.read_csv(label2_str.get())
    df = pd.DataFrame(excel_file, columns=csv_file.columns)
    file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv(file_path, index=None)
    
boton1 = Button(window, text='Cargar Excel', command=open_excel)
boton2 = Button(window, text='Cargar plantilla', command=open_csv)
label1 = Label(window, textvariable=label1_str, relief=RAISED)
label2 = Label(window, textvariable=label2_str, relief=RAISED)
boton3 = Button(window, text='Exportar a csv', command=export_to_csv)


def run():
    window.geometry('800x300')
    boton1.grid(row=1, column=0, sticky='W')
    label1.grid(row=1, column=1)
    boton2.grid(row=2, column=0, sticky='W')
    label2.grid(row=2, column=1)
    boton3.grid(row=3, column=0, sticky='W')
    window.mainloop()

    

if __name__ == '__main__':
    run()