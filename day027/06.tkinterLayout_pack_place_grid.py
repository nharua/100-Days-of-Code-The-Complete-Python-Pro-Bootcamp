import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=20)
# NOTE: PACK


# NOTE: PLACE

# NOTE: GRID

label = tkinter.Label(text="Old Label")
label.grid(column=0, row=0)

button01 = tkinter.Button(text="button01")
button01.grid(column=1, row=1)

button02 = tkinter.Button(text="button02")
button02.grid(column=1, row=0)

input = tkinter.Entry()
input.grid(column=2, row=2)


window.mainloop()
