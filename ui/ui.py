import tkinter as tk
from tkinter import ttk
from tkinter.constants import N, W, E, S

NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
OPERATORS = ["+", "-", "x", "/"]
ADVANCED_OPERATORS = ... # to be implemented
GRID_DIMENSION = 3


class CalculatorWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("calculator")
        self.geometry("500x500")
        self.main_frame = MainFrame(self)
        self.main_frame.grid(column=0, row=0, sticky="nsew")
        self.populate()

    def populate(self):
        for idx, number in enumerate(NUMBERS):
            button = TemplateButton(self.main_frame, number)
            button.grid(row=idx // GRID_DIMENSION, column=idx % GRID_DIMENSION, padx=5, pady=5)
        for idx, operator in enumerate(OPERATORS):
            button = TemplateButton(self.main_frame, operator)
            button.grid(row=(idx // GRID_DIMENSION) + GRID_DIMENSION, column=(idx % GRID_DIMENSION), padx=5, pady=5)
        
        button = TemplateButton(self.main_frame, "ENTER")
        button.grid(row=4, column=1, columnspan=5)
        
        
        


class MainFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)


class TemplateButton(tk.Button):
    def __init__(self, root, number):
        super().__init__(root, text=number, font=("Arial", 16))
