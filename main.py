from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
import pandas as pd

class Frame():

    def __init__(self):
        self.window = Tk()
        self.label1_str = StringVar()
        self.label2_str = StringVar()
        self.label3_str = StringVar()
        self.label4_str = StringVar()

    def open_excel(self):
            file = filedialog.askopenfile(title='Cargar Excel', 
                                        initialdir=os.path.expanduser('~/Documents'), 
                                        filetypes=(('Excel Files', '*.xlsx'),
                                                    ('All files', '*.*')))
            self.label1_str.set(file.name)
            self.excel_file = pd.read_excel(self.label1_str.get())
            self.label3_str.set(self.get_cols(df=self.excel_file))

    def open_csv(self):
            file = filedialog.askopenfile(title='Cargar CSV', 
                                        initialdir=os.path.expanduser('~/Documents'), 
                                        filetypes=(('CSV Files', '*.csv'),
                                                    ('All files', '*.*')))
            self.label2_str.set(file.name)
            self.csv_file = pd.read_csv(self.label2_str.get(), encoding='utf-8-sig')
            self.label4_str.set(self.get_cols(df=self.csv_file))

    def export_to_csv(self):    
        df = pd.DataFrame(self.excel_file, columns=self.csv_file.columns)
        file_path = filedialog.asksaveasfilename(defaultextension='.csv')
        df.to_csv(file_path, index=None, encoding='utf-8-sig')
        messagebox.showinfo('Info', '¡CSV generado!')
        
    def init_components(self):
        self.boton1 = Button(self.window, text='Cargar Excel', command=self.open_excel)
        self.boton2 = Button(self.window, text='Cargar plantilla', command=self.open_csv)
        self.label1 = Label(self.window, textvariable=self.label1_str, relief=RAISED)
        self.label2 = Label(self.window, textvariable=self.label2_str, relief=RAISED)
        self.label3 = Label(self.window, textvariable=self.label3_str, relief=RAISED)
        self.label4 = Label(self.window, textvariable=self.label4_str, relief=RAISED)
        self.label5 = Label(self.window, text='Columas: ')
        self.boton3 = Button(self.window, text='Exportar a csv', command=self.export_to_csv)


    def run(self):
        self.window.geometry('1000x300')
        self.window.title('Exportar a CSV')
        self.boton1.grid(row=1, column=0, sticky='W')
        self.label1.grid(row=1, column=1)
        self.label5.grid(row=1, column=2)
        self.label3.grid(row=1, column=3)
        self.boton2.grid(row=2, column=0, sticky='W')
        self.label2.grid(row=2, column=1)
        self.label5.grid(row=2, column=2)
        self.label4.grid(row=2, column=3)
        self.boton3.grid(row=3, column=0, sticky='W')
        self.window.mainloop()

    def get_cols(self, df: pd.DataFrame):
        cols = []
        for col in df.columns:
            cols.append('{},'.format(col))
        return cols

if __name__ == '__main__':
    frame = Frame()
    frame.init_components()
    frame.run()

# autor: Bernardo Javier Miranda Tarelo