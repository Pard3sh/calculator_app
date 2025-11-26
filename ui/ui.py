import tkinter as tk
from tkinter import ttk

NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
OPERATORS = ["+", "-", "x", "/"]
ADVANCED_OPERATORS = ...  # to be implemented
GRID_DIMENSION = 3

"""
populate:
    Each parent element will populate itself of its immediate child element
"""


class CalculatorWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("calculator")
        self.geometry("500x500")
        self.main_frame = MainFrame(self)
        self.main_frame.populate()


class MainFrame(tk.Frame):
    def __init__(self, root):
        self.root = root
        super().__init__(root)

    def populate(self):
        button_frame = ButtonFrame(self)
        button_frame.grid(column=0, row=0, sticky="nsew")
        button_frame.populate()


class DisplayFrame(tk.Frame):
    def __init__(self, root):
        self.root = root
        super().__init__(root)
        self.display_string = tk.StringVar()
        self.entry_string = tk.StringVar()

    def populate(self):
        display_label = CalculatorLabel(self.root, self.display_string)
        entry_label = CalculatorLabel(self.main_frame, self.entry_string)
        display_label.pack(padx=20, pady=20)
        entry_label.pack(padx=20, pady=20)


class TemplateButton(tk.Button):
    def __init__(self, root, number):
        super().__init__(root, text=number, font=("Arial", 16))


class ButtonFrame(tk.Frame):
    """Frame that holds all numerical and operation buttons
    Attributes:
        root: The widget that it is a child to.
    Methods:
        populate: Creates and grids each button that it will contain.
    """
    def __init__(self, root):
        super().__init__(root)
    
    def populate(self):
        for idx, number in enumerate(NUMBERS):
            button = TemplateButton(self, number)
            button.grid(
                row=idx // GRID_DIMENSION, column=idx % GRID_DIMENSION, padx=5, pady=5
            )
        for idx, operator in enumerate(OPERATORS):
            button = TemplateButton(self, operator)
            button.grid(
                row=(idx // GRID_DIMENSION) + GRID_DIMENSION,
                column=(idx % GRID_DIMENSION),
                padx=5,
                pady=5,
            )

        enter_button = TemplateButton(self, "ENTER")
        enter_button.grid(row=4, column=1, columnspan=5)


class CalculatorLabel(tk.Label):
    def __init__(self, root, var):
        super().__init__(root, textvariable=var)
