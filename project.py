from tkinter import *

ans_value = None

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 35, "bold")
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)


OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

total_expression = ""  
current_expression = "" 

def add_expression(value):
    global total_expression
    total_expression += str(value)
    update_total_label()

def operator(operators):
    global total_expression, current_expression
    if current_expression:
        total_expression += current_expression
        current_expression = ""
    
    total_expression += operators
    update_total_label()

def update_total_label():
    global total_expression
    display_label.config(text=total_expression[:11])

def update_label():
    global current_expression
    current_label.config(text=current_expression[:10])

def evaluate():
    global current_expression, total_expression, ans_value
    if not total_expression:
        return
    
##    answer=eval(total_expression)
####    total_expression += current_expression
##    current_expression = answer

    # Check for division by zero
    if '/' in total_expression:
        try:
            result = eval(total_expression)
            ans_value = result
            current_expression = str(result)
            total_expression = ""
        except (ZeroDivisionError, SyntaxError, NameError) as e:
            current_expression = "Error"
    else:
        try:
            result = eval(total_expression)
            ans_value = result
            current_expression = str(result)
            total_expression = ""
        except (SyntaxError, NameError) as e:
            current_expression = "Error"

    update_label()
    update_total_label()

        
# Add these function definitions
def divide_operator():
    operator("/")

def add_operator():
    operator("+")

def subtract_operator():
    operator("-")

def multiply_operator():
    operator("*")

def divide_operator():
    operator("/")
def add_7():
    add_expression(7)

def add_8():
    add_expression(8)

def add_9():
    add_expression(9)

def add_4():
    add_expression(4)

def add_5():
    add_expression(5)

def add_6():
    add_expression(6)

def add_1():
    add_expression(1)

def add_2():
    add_expression(2)

def add_3():
    add_expression(3)

def add_0():
    add_expression(0)

def add_decimal():
    add_expression('.')
def add_bracket():
    add_expression('(')

def add_brackets():
    add_expression(')')


def square():
    global current_expression, total_expression
    if total_expression:
        try:
            current_expression = str(float(total_expression) ** 2)
            update_label()
        except ValueError:
            current_expression = "Error"
            update_label()

def sqrt():
    global total_expression, current_expression
    if total_expression:
        try:
            current_expression = str(float(total_expression) ** 0.5)
            update_label()
        except ValueError:
            current_expression = "Error"
            update_label()

def clear():
    global current_expression, total_expression
    current_expression = ""
    total_expression = ""
    update_label()
    update_total_label()

def ans():
    global total_expression, ans_value
    if ans_value is not None:
        total_expression += str(ans_value)
        update_total_label()

def ac():
    global total_expression
    total_expression = total_expression[:-1]  # Remove the last character
    update_total_label()

root = Tk()
root.geometry("375x667")
root.title("Project_Calculator")
##root.minsize(375,667)
##root.maxsize(375,667)

label_frame = Frame(root, height=221, bg=OFF_WHITE)
label_frame.pack(expand=True, fill="both")
button_frame = Frame(root)
button_frame.pack(expand=True, fill="both")


display_label = Label(label_frame, text=total_expression, anchor=W, bg=LIGHT_GRAY, padx=24, font=SMALL_FONT_STYLE)
display_label.pack(expand=True, fill="both")
current_label = Label(label_frame, text=current_expression, anchor=E, bg=OFF_WHITE, padx=24, font=LARGE_FONT_STYLE)
current_label.pack(expand=True, fill="both")

for x in range(1, 5):
    button_frame.rowconfigure(x, weight=1)
    button_frame.columnconfigure(x, weight=1)

Button(button_frame, text="\u00F7", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
       borderwidth=0, command=divide_operator).grid(row=4, column=4, sticky=NSEW)

Button(button_frame, text="\u00D7", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
       borderwidth=0, command=multiply_operator).grid(row=1, column=4, sticky=NSEW)

Button(button_frame, text="-", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
       borderwidth=0, command=subtract_operator).grid(row=2, column=4, sticky=NSEW)

Button(button_frame, text="+", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
       borderwidth=0, command=add_operator).grid(row=3, column=4, sticky=NSEW)

Button(button_frame, text="7", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
       borderwidth=0, command=add_7).grid(row=1, column=1, sticky=NSEW)

Button(button_frame, text="8", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
       borderwidth=0, command=add_8).grid(row=1, column=2, sticky=NSEW)

Button(button_frame, text="9", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
       borderwidth=0, command=add_9).grid(row=1, column=3, sticky=NSEW)

Button(button_frame, text="4", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
       borderwidth=0, command=add_4).grid(row=2, column=1, sticky=NSEW)

Button(button_frame, text="5", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
       borderwidth=0, command=add_5).grid(row=2, column=2, sticky=NSEW)

Button(button_frame, text="6", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
       borderwidth=0, command=add_6).grid(row=2, column=3, sticky=NSEW)

Button(button_frame, text="1", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
       borderwidth=0, command=add_1).grid(row=3, column=1, sticky=NSEW)

Button(button_frame, text="2", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
       borderwidth=0, command=add_2).grid(row=3, column=2, sticky=NSEW)

Button(button_frame, text="3", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
       borderwidth=0, command=add_3).grid(row=3, column=3, sticky=NSEW)

Button(button_frame, text="0", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
       borderwidth=0, command=add_0).grid(row=4, column=2, sticky=NSEW)

Button(button_frame, text=".", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
       borderwidth=0, command=add_decimal).grid(row=4, column=1, sticky=NSEW)

Button(button_frame, text="(", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
       borderwidth=0, command=add_bracket).grid(row=5, column=1, sticky=NSEW)

Button(button_frame, text=")", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
       borderwidth=0, command=add_brackets).grid(row=5, column=2, sticky=NSEW)

btn_C = Button(button_frame, text="C", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=clear)
btn_C.grid(row=0, column=3, sticky=NSEW)

btn_equal = Button(button_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=evaluate)
btn_equal.grid(row=5, column=3, columnspan=2, sticky=NSEW)

btn_AC = Button(button_frame, text="AC", bg=LIGHT_BLUE, fg=LABEL_COLOR, borderwidth=0, font=DIGITS_FONT_STYLE, command=ac)
btn_AC.grid(row=0, column=4, sticky=NSEW)

btn_ans = Button(button_frame, text="ANS", bg=OFF_WHITE, fg=LABEL_COLOR, borderwidth=0, font=DIGITS_FONT_STYLE, command=ans)
btn_ans.grid(row=4, column=3, sticky=NSEW)

btn_sq = Button(button_frame, text="x\u00b2", bg=LIGHT_BLUE, fg=LABEL_COLOR, borderwidth=0, font=DIGITS_FONT_STYLE, command=square)
btn_sq.grid(row=0, column=1, sticky=NSEW)

btn_sqroot = Button(button_frame, text="\u221ax", bg=LIGHT_BLUE, fg=LABEL_COLOR, borderwidth=0, font=DIGITS_FONT_STYLE, command=sqrt)
btn_sqroot.grid(row=0, column=2, sticky=NSEW)

root.mainloop()
