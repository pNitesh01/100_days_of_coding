from tkinter import *

FONT = ("Arial", 18)

def button_clicked():
    mile_val = float(miles_input.get())
    km_val = round(mile_val * 1.609344, 2)
    result_label.config(text=km_val)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Labels
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="is equal to", font=FONT)
is_equal_to_label.grid(row=1, column=0)

km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

result_label = Label(text="0", font=FONT)
result_label.grid(row=1, column=1)

# Entry
miles_input = Entry(width=7)
miles_input.focus()
miles_input.grid(row=0, column=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

window.mainloop()
