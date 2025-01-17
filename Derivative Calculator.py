from tkinter import *


#date January 4th 2024


root = Tk()
root.title("Simple Calculator")
e = Entry(root, borderwidth=50)
e.grid(row= 0, column=0, columnspan= 4, padx=10, pady=10)

 #making 2 global varaibles that will be used in the clear,add,subtract,x and = method
fnum = None
operation = None #not sure why this is set to none but the tutorial guy said that they need to be predefined so lets assumethat

def buttonclick(number):
    current = e.get()
    e.delete(0, END)  # Clears the current entry
    e.insert(0, current + str(number))

def clear_entry():
    e.delete(0, END)

def buttonaddmethod():
    global fnum, operation
    firstnumber= e.get()
    fnum = int(firstnumber)
    operation = "+"
    e.delete(0, END)

def buttonsubstractmethod():
    global fnum, operation
    firstnumber =e.get()
    fnum = int(firstnumber)
    operation= "-"
    e.delete(0, END)

def buttonmultiplymethod():
    global fnum, operation
    firstnumber= e.get()
    fnum = int(firstnumber)
    operation = "x"
    e.delete(0, END)

def buttondividemethod():
    global fnum, operation
    firstnumber= e.get()
    fnum = int(firstnumber)
    operation ="/"
    e.delete(0, END)

def buttonequal():
    secondnumber= e.get()
    e.delete(0, END)
    if operation=="+":
        e.insert(0, fnum + int(secondnumber))
    elif operation == "-":
        e.insert(0, fnum - int(secondnumber))
    elif operation== "x":
        e.insert(0, fnum * int(secondnumber))
    elif operation =="/":
        e.insert(0, fnum / int(secondnumber))

#following saunders advice and not hardcoding the buttons although I cannot use loops for the subtract, divide etc buttons because they are not numbers and do not have sequential ascii numbers
number_buttons =[]
for i in range(10):
    button = Button(root, text=str(i), padx =40, pady=20, command=lambda i =i: buttonclick(i))#i=i is needed so i will update after each loop and be stored in each button instead of the last value of 9 only being saved and being used for every button
    number_buttons.append(button)

#now I am going to code the buttons for this, I will not be coding the derivative button here as it must be placed after or else it wont be able to be called by the deriviative function below
button_add =Button(root,text="+", padx=40, pady=20, command =buttonaddmethod)
button_equal= Button(root,text="=", padx=40, pady=20, command=buttonequal)
button_clear = Button(root,text ="CLEAR", padx=40, pady=20, command= clear_entry)
button_subtract =Button(root,text="-", padx= 40, pady= 20, command= buttonsubstractmethod)
button_multiply = Button(root,text="x", padx=40, pady=20, command=buttonmultiplymethod)
button_divide= Button(root,text="/", padx =40, pady =20, command= buttondividemethod)

number_buttons[1].grid(row =1, column =0)
number_buttons[2].grid(row =1, column=1)
number_buttons[3].grid(row =1, column= 2)
number_buttons[4].grid(row =2, column=0)
number_buttons[5].grid(row=2, column=1)
number_buttons[6].grid(row=2, column =2)
number_buttons[7].grid(row=3, column=0)
number_buttons[8].grid(row=3, column= 1)
number_buttons[9].grid(row= 3, column=2)
number_buttons[0].grid(row=4, column=0)
#placing the buttons on the grid system in tkinter
button_add.grid(row= 4, column= 1)
button_equal.grid(row=4, column =2)
button_clear.grid(row= 4, column =3)
button_subtract.grid(row=1, column=3)
button_multiply.grid(row=3, column= 3)
button_divide.grid(row=2, column=3)

#now we shall begin the derivative button processs :)
def open_derivative_window(): #defining derivative window that will be holding my derivative calc
    def calculate_derivative():# now I shall code the function that will calculate the deriviative
        a = float(entry_a.get() or 0) #casting values to float
        b = float(entry_b.get() or 0)
        c = float(entry_c.get() or 0)
        d = float(entry_d.get() or 0)

        if d: #once a polynomial button is selected then I will input a number in the vairables and if the inputs have a d value for ex, then ik its cubic
            derivative = f"{3 * a}x^2 + {2 * b}x + {c}"
        elif c:
            derivative = f"{2 * a}x + {b}" #I learned how to use f strings and I sourced them on my google doc
        elif b:
            derivative = f"{a}"
        else:
            derivative = f"0" # If only 'a' is provided, its derivative is 0.

        result_label.config(text=f"Derivative: {derivative}") #config method allows for my label to be constantly updating

    def show_linear(): #these will be called once the linear button is clicked as the button will call this function
        hide_all_entries()
        entry_a.grid(row =1, column=1)
        label_a.grid(row=1, column =0)
    def show_quadratic():#same again here is that these will be called once the quad button is clicked as the button will call this function
        hide_all_entries()
        entry_a.grid(row =1, column=1)
        label_a.grid(row =1, column=0)
        entry_b.grid(row= 2, column=1)
        label_b.grid(row=2, column=0)
        entry_c.grid(row =3, column=1)
        label_c.grid(row=3, column=0)

    def show_cubic():
        hide_all_entries()
        entry_a.grid(row=1, column =1)
        label_a.grid(row=1, column=0)
        entry_b.grid(row =2, column=1)
        label_b.grid(row=2, column= 0)
        entry_c.grid(row =3, column=1)
        label_c.grid(row=3, column=0)
        entry_d.grid(row=4, column=1)
        label_d.grid(row =4, column=0)
    def hide_all_entries():
        entry_a.grid_remove()
        label_a.grid_remove()
        entry_b.grid_remove()
        label_b.grid_remove()
        entry_c.grid_remove()
        label_c.grid_remove()
        entry_d.grid_remove()
        label_d.grid_remove()



#now that all of the methods and functions are done I shall move to the actual GUI part so I can have my calc deriv showing
    derivative_window = Toplevel(root) #making the derivative window pop up on my screen
    derivative_window.title("Derivative Calculator")

    Button(derivative_window, text="Linear", command=show_linear).grid(row=0, column=0)
    Button(derivative_window, text="Quadratic", command=show_quadratic).grid(row=0, column=1)
    Button(derivative_window, text="Cubic", command=show_cubic).grid(row=0, column=2)

    label_a = Label(derivative_window, text="a:")
    entry_a= Entry(derivative_window)

    label_b = Label(derivative_window, text="b:")
    entry_b= Entry(derivative_window)

    label_c =Label(derivative_window, text="c:")
    entry_c = Entry(derivative_window)

    label_d =Label(derivative_window, text="d:")
    entry_d = Entry(derivative_window)

    calculate_button = Button(derivative_window, text="Calculate Derivative", command=calculate_derivative)
    calculate_button.grid(row=5, column=0, columnspan=2)

    result_label = Label(derivative_window, text="")
    result_label.grid(row=6, column=0, columnspan=2)

# Adding Derivative button to the main calculator
button_derivative = Button(root, text="Derivative", padx=20, pady=20, command=open_derivative_window)
button_derivative.grid(row=4, column=4)

root.mainloop()

