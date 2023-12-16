# -*- coding: utf-8 -*-
import tkinter as tk
from code.string_calculator import add


def call_add():
    textwidget.delete(1.0, tk.END)
    if text_input.get():
        text_response = text_input.get()
        response = add(text_response)
        textwidget.insert(index=tk.END, chars=response)
        
    else:
        text_response = "Inserire i numeri da sommare"


app = tk.Tk()
button = tk.Button(text="Inserire i numeri da sommare", command=call_add)
button.grid(row=2, column=0, sticky="WE", pady=10, padx=10)
text_input = tk.Entry()
text_input.grid(row=1, column=0, sticky="WE", padx=10)
textwidget = tk.Text()
textwidget.grid(row=3, column=0, sticky="WE", padx=10, pady=10)

if __name__ == "__main__":
    app.mainloop()