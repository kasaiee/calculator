# Import the tkinter module
import tkinter

# Creating the GUI window.
window = tkinter.Tk()
window.title("Welcome to geeksforgeeks")
window.geometry("800x200")

# Creating our text widget.
sample_text = tkinter.Entry(window)
sample_text.pack()

# Creating the function to set the text 
# with the help of button
def set_text_1():
	sample_text.insert("end", "1")

def set_text_2():
	sample_text.insert("end", "2")

def set_text_3():
	sample_text.insert("end", "3")

def set_text_plus():
	sample_text.insert("end", "+")

def reset():
	sample_text.delete(0, "end")

def delete():
    text = sample_text.get()
    sample_text.delete(0, "end")
    sample_text.insert(0, text[:-1])

def result():
    res = eval(sample_text.get())
    sample_text.delete(0, "end")
    sample_text.insert(0, res)


btn1 = tkinter.Button(window, height=1, width=10, text="1", command=set_text_1)
btn1.pack()

btn2 = tkinter.Button(window, height=1, width=10, text="2", command=set_text_2)
btn2.pack()

btn3 = tkinter.Button(window, height=1, width=10, text="3", command=set_text_3)
btn3.pack()

plus = tkinter.Button(window, height=1, width=10, text="+", command=set_text_plus)
plus.pack()

result = tkinter.Button(window, height=1, width=10, text="=", command=result)
result.pack()

reset = tkinter.Button(window, height=1, width=10, text="reset", command=reset)
reset.pack()

delete = tkinter.Button(window, height=1, width=10, text="delete", command=delete)
delete.pack()

window.mainloop()