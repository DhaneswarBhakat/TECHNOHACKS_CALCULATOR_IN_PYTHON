import tkinter as tk
from tkinter import messagebox

# Setting the initial values of some variables
var = ""
A = 0
operator = ""

# Defining the function for Button 1
def button_1_is_clicked():
    global var
    var = var + "1"
    the_data.set(var)

# Defining the function for Button 2
def button_2_is_clicked():
    global var
    var = var + "2"
    the_data.set(var)

# Defining the function for Button 3
def button_3_is_clicked():
    global var
    var = var + "3"
    the_data.set(var)

# Defining the function for Button 4
def button_4_is_clicked():
    global var
    var = var + "4"
    the_data.set(var)

# Defining the function for Button 5
def button_5_is_clicked():
    global var
    var = var + "5"
    the_data.set(var)

# Defining the function for Button 6
def button_6_is_clicked():
    global var
    var = var + "6"
    the_data.set(var)

# Defining the function for Button 7
def button_7_is_clicked():
    global var
    var = var + "7"
    the_data.set(var)

# Defining the function for Button 8
def button_8_is_clicked():
    global var
    var = var + "8"
    the_data.set(var)

# Defining the function for Button 9
def button_9_is_clicked():
    global var
    var = var + "9"
    the_data.set(var)

# Defining the function for Button 0
def button_0_is_clicked():
    global var
    var = var + "0"
    the_data.set(var)

# Defining the function for Button +
def button_add_is_clicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "+"
    var = var + "+"
    the_data.set(var)

# Defining the function for Button -
def button_sub_is_clicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "-"
    var = var + "-"
    the_data.set(var)

# Defining the function for Button *
def button_mul_is_clicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "*"
    var = var + "*"
    the_data.set(var)

# Defining the function for Button /
def button_div_is_clicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "/"
    var = var + "/"
    the_data.set(var)

# Defining the function for Button =
def button_equal_is_clicked():
    global A
    global var
    global operator
    A = float(var)
    operator = "="
    var = var + "="
    the_data.set(var)

# Defining the function for Button C
def button_c_is_clicked():
    global A
    global var
    global operator
    var = ""
    A = 0
    operator = ""
    the_data.set(var)

# Defining the function to display result
def res():
    global A
    global operator
    global var
    var2 = var
    if operator == "+":
        a = float((var2.split("+")[1]))
        x = A + a
        the_data.set(x)
        var = str(x)
    elif operator == "-":
        a = float((var2.split("-")[1]))
        x = A - a
        the_data.set(x)
        var = str(x)
    elif operator == "*":
        a = float((var2.split("*")[1]))
        x = A * a
        the_data.set(x)
        var = str(x)
    elif operator == "/":
        a = float((var2.split("/")[1]))
        if a == 0:
            messagebox.showerror("Division by 0 Not Allowed.")
            A == ""
            var = ""
            the_data.set(var)
        else:
            x = float(A / a)
            the_data.set(x)
            var = str(x)

# Creating an object of the Tk() class
gui_window = tk.Tk()

# Setting the size of the window
gui_window.geometry("320x500+400+400")

# Disabling the resize option for better UI
gui_window.resizable(0, 0)

# Setting the title of the Calculator window
gui_window.title("Calculator")

# Creating the label for the window
the_data = tk.StringVar()
gui_label = tk.Label(
    gui_window,
    text="Label",
    anchor=tk.SE,
    font=("Cambria Math", 20),
    textvariable=the_data,
    background="#ffffff",
    fg="#000000"
)
gui_label.pack(expand=True, fill="both")

# Creating the frames for the buttons
# First frame
frame_one = tk.Frame(gui_window, bg="#000000")
frame_one.pack(expand=True, fill="both")

# Second frame
frame_two = tk.Frame(gui_window, bg="#000000")
frame_two.pack(expand=True, fill="both")

# Third frame
frame_three = tk.Frame(gui_window, bg="#000000")
frame_three.pack(expand=True, fill="both")

# Fourth frame
frame_four = tk.Frame(gui_window, bg="#000000")
frame_four.pack(expand=True, fill="both")

# Creating buttons for each frame
# Buttons for the first frame
# Button 1
button_one = tk.Button(
    frame_one,
    text="1",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=button_1_is_clicked,
    bg="#4CAF50",
    fg="#ffffff"
)
button_one.pack(side=tk.LEFT, expand=True, fill="both")

# Button 2
button_two = tk.Button(
    frame_one,
    text="2",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=button_2_is_clicked,
    bg="#4CAF50",
    fg="#ffffff"
)
button_two.pack(side=tk.LEFT, expand=True, fill="both")

# Button 3
button_three = tk.Button(
    frame_one,
    text="3",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=button_3_is_clicked,
    bg="#4CAF50",
    fg="#ffffff"
)
button_three.pack(side=tk.LEFT, expand=True, fill="both")

# Button C
button_c = tk.Button(
    frame_one,
    text="C",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=button_c_is_clicked,
    bg="#f44336",
    fg="#ffffff"
)
button_c.pack(side=tk.LEFT, expand=True, fill="both")

# Buttons for the second frame
# Button 4
button_four = tk.Button(
    frame_two,
    text="4",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=button_4_is_clicked,
    bg="#4CAF50",
    fg="#ffffff"
)
button_four.pack(side=tk.LEFT, expand=True, fill="both")

# Button 5
button_five = tk.Button(
    frame_two,
    text="5",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=button_5_is_clicked,
    bg="#4CAF50",
    fg="#ffffff"
)
button_five.pack(side=tk.LEFT, expand=True, fill="both")

# Button 6
button_six = tk.Button(
    frame_two,
    text="6",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=button_6_is_clicked,
    bg="#4CAF50",
    fg="#ffffff"
)
button_six.pack(side=tk.LEFT, expand=True, fill="both")

# Button +
button_add = tk.Button(
    frame_two,
    text="+",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=button_add_is_clicked,
    bg="#FF9800",
    fg="#ffffff"
)
button_add.pack(side=tk.LEFT, expand=True, fill="both")

# Buttons for the third frame
# Button 7
button_seven = tk.Button(
    frame_three,
    text="7",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=button_7_is_clicked,
    bg="#4CAF50",
    fg="#ffffff"
)
button_seven.pack(side=tk.LEFT, expand=True, fill="both")

# Button 8
button_eight = tk.Button(
    frame_three,
    text="8",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=button_8_is_clicked,
    bg="#4CAF50",
    fg="#ffffff"
)
button_eight.pack(side=tk.LEFT, expand=True, fill="both")

# Button 9
button_nine = tk.Button(
    frame_three,
    text="9",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=button_9_is_clicked,
    bg="#4CAF50",
    fg="#ffffff"
)
button_nine.pack(side=tk.LEFT, expand=True, fill="both")

# Button -
button_sub = tk.Button(
    frame_three,
    text="-",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=button_sub_is_clicked,
    bg="#FF9800",
    fg="#ffffff"
)
button_sub.pack(side=tk.LEFT, expand=True, fill="both")

# Buttons for the fourth frame
# Button 0
button_zero = tk.Button(
    frame_four,
    text="0",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=button_0_is_clicked,
    bg="#4CAF50",
    fg="#ffffff"
)
button_zero.pack(side=tk.LEFT, expand=True, fill="both")

# Button *
button_mul = tk.Button(
    frame_four,
    text="*",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=button_mul_is_clicked,
    bg="#FF9800",
    fg="#ffffff"
)
button_mul.pack(side=tk.LEFT, expand=True, fill="both")

# Button /
button_div = tk.Button(
    frame_four,
    text="/",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=button_div_is_clicked,
    bg="#FF9800",
    fg="#ffffff"
)
button_div.pack(side=tk.LEFT, expand=True, fill="both")

# Button =
button_equal = tk.Button(
    frame_four,
    text="=",
    font=("Cambria", 22),
    relief=tk.GROOVE,
    border=0,
    command=res,
    bg="#2196F3",
    fg="#ffffff"
)
button_equal.pack(side=tk.LEFT, expand=True, fill="both")

# Running the GUI
gui_window.mainloop()
