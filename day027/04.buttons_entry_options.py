import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label component
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side="left")
my_label["text"] = "New Text"  # change label text
my_label.config(text="this is new text")  # option 2 to change label text


# Button component
def button_clicked():
    print("I got clicked")


my_button = tkinter.Button(text="Click Me", command=button_clicked)
my_button.pack()


# challenge: Show "Button Got Clicked" on my_label when the butoon get's clicked
def show_challenge():
    my_label.config(text="Button Got Clicked")


my_challenge = tkinter.Button(text="Challenge", command=show_challenge)
my_challenge.pack(side="right")


# Entry component
input = tkinter.Entry(width=10)
input.pack(side="bottom")
my_input = input.get()


# challenge: get content of input and show in label when i click the buttun
def change_challenge():
    new_text = input.get()
    my_label.config(text=new_text)


my_challenge02 = tkinter.Button(text="challenge02", command=change_challenge)
my_challenge02.pack()

window.mainloop()
