from tkinter import *

# window
root = Tk()
root.title(f'Converter')
# root.minsize(height=400, width=800)

# content
content_f = Frame(root, padx=20, pady=20)
content_f.grid()

### widgets

# Row 1
entry = Entry(master=content_f, width=5)
label_input = Label(master=content_f, text="Miles", font=('Arial', 15, 'normal'), anchor='w')

entry.grid(row=0, column=1, sticky='nesw')
label_input.grid(row=0, column=2, sticky='w')

# Row 2

label_text = Label(master=content_f, text="equal to", font=('Arial', 15, 'normal'), anchor='w')
output = Label(master=content_f, text=' ')
label_output = Label(master=content_f, text="Kilometers", font=('Arial', 15, 'normal'), anchor='w')

label_text.grid(row=1, column=0)
output.grid(row=1, column=1)
label_output.grid(row=1, column=2, sticky='w')


# row 3

def calculate():
    output.config(text=round(1.609 * int(entry.get()), 3))


button = Button(master=content_f, text='calculate', command=calculate)

button.grid(row=3, column=1)

# Tidy up

for widget in content_f.winfo_children():
    widget.grid(padx = 5, pady = 5)

root.mainloop()
