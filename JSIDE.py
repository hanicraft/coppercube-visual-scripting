
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from tkinter.filedialog import asksaveasfilename
import tkinter.font
import tkinter.messagebox
import customtkinter
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")



class Widget1():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#414141')
            self.w1.geometry('520x420')
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg = '#414141')
            self.w1.place(x = 0, y = 0, width = 520, height = 420)
        self.text1 = Text(self.w1, font = tkinter.font.Font(family = "Calibri", size = 8), cursor = "arrow", state = "normal")
        self.text1.place(x = 10, y = 40, width = 500, height = 360)
        self.button1 = customtkinter.CTkButton(self.w1, text = "Open", text_font = "Calibri", cursor = "arrow", state = "normal", command = self.openfile)
        self.button1.place(x = 10, y = 10, width = 90, height = 22)
        self.button2 = customtkinter.CTkButton(self.w1, text = "Save", text_font = "Calibri", cursor = "arrow", state = "normal", command = self.savefile)
        self.button2.place(x = 100, y = 10, width = 90, height = 22)
        self.label1 = customtkinter.CTkLabel(self.w1, text = "JS IDE v0.1", text_color = "#ffffff", text_font = "Calibri", cursor = "arrow", state = "normal")
        self.label1.place(x = 400, y = 10, width = 110, height = 22)
        self.label2 = customtkinter.CTkLabel(self.w1, text = "CopyRight HaniCraft", text_color = "#ffffff", text_font = "Calibri", cursor = "arrow", state = "normal")
        self.label2.place(x = 370, y = 400, width = 150, height = 22)

    def openfile(self):
        fname = askopenfilename(filetypes=(("JavaScript Files", "*.js"),
                                           ("HTML files", "*.html;*.htm")))
        with open(fname, "r") as fname2:
            text = fname2.read()
            self.text1.insert('1.0',text)

    def savefile(self):
        fnametext = self.text1.get("1.0", "end-1c")
        fnamesave = asksaveasfilename(defaultextension="js", filetypes=(("JavaScript Files", "*.js"),
                                           ("HTML files", "*.html")))
        with open(fnamesave, "w") as fname3:
            fname3.write(fnametext)

if __name__ == '__main__':
    a = Widget1(0)
    a.w1.mainloop()