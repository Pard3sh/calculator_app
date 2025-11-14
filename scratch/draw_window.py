import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("my first")

label = tk.Label(root, text="Hello World", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, font=("Arial", 16))
textbox.pack(padx=10)

button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)

button = tk.Button(root, text="Submit", font=("Arial", 16))
button.pack(padx=10, pady=10)

root.mainloop()
