import tkinter

FONT = ("Arial", 16, "bold")

window = window = tkinter.Tk()
window.title("Mile to Km Convertor")
window.minsize(width=500, height=300)

label01 = tkinter.Label(text="Miles", font=FONT)
label01.grid(column=2, row=0)

label02 = tkinter.Label(text="is equal to", font=FONT)
label02.grid(column=0, row=1)

label03 = tkinter.Label(text="Km", font=FONT)
label03.grid(column=2, row=1)


label04 = tkinter.Label(text="0", font=FONT)
label04.grid(column=1, row=1)

entry = tkinter.Entry(width=15, font=FONT, justify="center")
entry.grid(column=1, row=0)


def convert():
    mile = int(entry.get())
    km = mile * 1.609
    # print(km)
    label04.config(text=str(km))


button = tkinter.Button(text="Calculate", font=FONT, command=convert)
button.grid(column=1, row=2)

window.mainloop()
