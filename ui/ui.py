import tkinter as tk
from tkinter import ttk
from tkinter.constants import N, W, E, S

class CalculatorWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("calculator")
        self.geometry('500x500')

class MainFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        
        
