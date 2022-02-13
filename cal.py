

from tkinter import *

win = Tk()  # It is used to create a basic window
win.geometry("312x324")  # It is used for the size of the window
win.resizable(0, 0)  # This is to prevent from resizing the window
win.title("Simple Calculator")


###################Starting with functions ####################
# 'button_click' function :
# This Function continuously updates the
# input field whenever you enter a number

def button_click(numb):
    global expression
    expression = expression + str(numb)
    input_value.set(expression)


# 'button_clear' function :This is used to clear
# the input field

def button_clear():
    global expression
    expression = ""
    input_value.set("")


# 'button_equal':This method calculates the expression
# present in input field

def button_equal():
    global expression
    result = str(eval(expression))  # 'eval':This function is used to evaluates the string expression directly
    input_value.set(result)
    expression = ""


expression = ""

# 'StringVar()' :It is used to get the instance of input field

input_value = StringVar()

# Used for creating a frame for the input field

input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="grey",
                    highlightthickness=1.5)

input_frame.pack(side=TOP)

# Used to create input field inside the 'Frame'

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_value, width=50, bg="#eee", bd=0,
                    justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the height of input field

# Let us creating another 'Frame' for the button below the 'input_frame'

#btns_frame = Frame(win, width=312, height=272.5, bg="blue")

#btns_frame.pack()

# first row

clear = Button(win, text="C", fg="black", width=32, height=3, bd=0, bg="#eee",
               command=lambda: button_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide = Button(win, text="/", fg="black", width=10, height=3, bd=0, bg="#eee",
                command=lambda: button_click("/")).grid(row=0, column=3, padx=1, pady=1)

# second row

button7 = Button(win, text="7", fg="black", width=10, height=3, bd=0, bg="#fff",
               command=lambda: button_click(7)).grid(row=1, column=0, padx=1, pady=1)

button8 = Button(win, text="8", fg="black", width=10, height=3, bd=0, bg="#fff",
               command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1)

button9 = Button(win, text="9", fg="black", width=10, height=3, bd=0, bg="#fff",
              command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)

multiply = Button(win, text="*", fg="black", width=10, height=3, bd=0, bg="#eee",
                  command=lambda: button_click("*")).grid(row=1, column=3, padx=1, pady=1)

# third row

button4 = Button(win, text="4", fg="black", width=10, height=3, bd=0, bg="#fff",
              command=lambda: button_click(4)).grid(row=2, column=0, padx=1, pady=1)

button5 = Button(win, text="5", fg="black", width=10, height=3, bd=0, bg="#fff",
              command=lambda: button_click(5)).grid(row=2, column=1, padx=1, pady=1)

button6 = Button(win, text="6", fg="black", width=10, height=3, bd=0, bg="#fff",
             command=lambda: button_click(6)).grid(row=2, column=2, padx=1, pady=1)

minus = Button(win, text="-", fg="black", width=10, height=3, bd=0, bg="#eee",
               command=lambda: button_click("-")).grid(row=2, column=3, padx=1, pady=1)

# fourth row

button1 = Button(win, text="1", fg="black", width=10, height=3, bd=0, bg="#fff",
             command=lambda: button_click(1)).grid(row=3, column=0, padx=1, pady=1)

button2 = Button(win, text="2", fg="black", width=10, height=3, bd=0, bg="#fff",
             command=lambda: button_click(2)).grid(row=3, column=1, padx=1, pady=1)

button3 = Button(win, text="3", fg="black", width=10, height=3, bd=0, bg="#fff",
               command=lambda: button_click(3)).grid(row=3, column=2, padx=1, pady=1)

plus = Button(win, text="+", fg="black", width=10, height=3, bd=0, bg="#eee",
              command=lambda: button_click("+")).grid(row=3, column=3, padx=1, pady=1)

# fourth row

button0 = Button(win, text="0", fg="black", width=21, height=3, bd=0, bg="#fff",
              command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = Button(win, text=".", fg="black", width=10, height=3, bd=0, bg="#eee",
               command=lambda: button_click(".")).grid(row=4, column=2, padx=1, pady=1)

equals = Button(win, text="=", fg="black", width=10, height=3, bd=0, bg="#eee",
                command=lambda: button_equal()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
