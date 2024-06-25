import tkinter

# Creating a new windows and configuration

window = tkinter.Tk()
# NOTE: TITLE
window.title("Widget Samples")
window.minsize(width=500, height=500)

# NOTE: LABEL
label = tkinter.Label(text="this is old text")
# label.config(text="This is new text")
label.pack()


# NOTE: BUTTON
def button_action():
    print("I got the clicked!!")


button = tkinter.Button(text="Click Me!", command=button_action)
button.pack()

# NOTE: ENTRY
entry = tkinter.Entry(width=30)
# Add something with entry
entry.insert(0, string="Some text to begin with.")
# Get text in entry
print(entry.get())
entry.pack()

# NOTE: TEXT - Multiline text box
text = tkinter.Text(height=5, width=35)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert("end", "Example of multi-line text intry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", "end"))
text.pack()


# NOTE: SPINBOX
def spinbox_used():
    # Get the current value in spinbox
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# NOTE: SCALE
def scale_use(value):  # Called the current scale value.
    print(value)


scale = tkinter.Scale(from_=0, to=10, command=scale_use)
scale.pack()


# NOTE: CHECKBUTTON
def checkbutton_used():
    # print 1 = ON, 0 = OFF
    print(check_state.get())


check_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(
    text="Is ON?", variable=check_state, command=checkbutton_used
)
check_state.get()
checkbutton.pack()


# NOTE: RADIOBUTTON
def radio_used():
    print(radio_state.get())


radio_state = tkinter.IntVar()
radio_button01 = tkinter.Radiobutton(
    text="Option 1", value=1, variable=radio_state, command=radio_used
)
radio_button02 = tkinter.Radiobutton(
    text="Option 2", value=2, variable=radio_state, command=radio_used
)
radio_button01.pack()
radio_button02.pack()


# NOTE: LISTBOX
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
