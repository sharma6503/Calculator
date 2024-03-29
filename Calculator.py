from tkinter import *

window = Tk()
window.title('Calculator')
window.geometry('700x700')


def equals():
    global equation_txt
    try:
        total = str(eval(equation_txt))

        equation_label.set(total)
        equation_txt = total

    except SyntaxError:
        equation_label.set('Syntax Error')

    except ZeroDivisionError:

        equation_label.set('Math Error')
        equation_txt = ''


def clear():
    global equation_txt

    equation_label.set(' ')

    equation_txt = ' '


def button_press(num):
    global equation_txt
    equation_txt = equation_txt + str(num)
    equation_label.set(equation_txt)


label = Label(window, text='Simple Calculator', font=('Arial Bold', 30), fg='red', bd=10)
label.pack()

equation_txt = ''

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('Arial', 25), background='#FAFAFA', height=2, width=24,
              fg='red')
label.pack(pady=20)
frm = Frame(window)
frm.pack()

button1 = Button(frm, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frm, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)
button3 = Button(frm, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)
button4 = Button(frm, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)
button5 = Button(frm, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)
button6 = Button(frm, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)
button7 = Button(frm, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frm, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frm, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frm, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3, column=0)

button_dot = Button(frm, text='.', height=4, width=9, font=35,
                    command=lambda: button_press('.'))
button_dot.grid(row=3, column=1)

button_equal = Button(frm, text='=', height=4, width=9, font=35,
                      command=lambda: equals())
button_equal.grid(row=3, column=2)

button_add = Button(frm, text='+', height=4, width=9, font=35,
                    command=lambda: button_press('+'))
button_add.grid(row=0, column=3)

button_sub = Button(frm, text='-', height=4, width=9, font=35,
                    command=lambda: button_press('-'))
button_sub.grid(row=1, column=3)

button_mul = Button(frm, text='*', height=4, width=9, font=35,
                    command=lambda: button_press('*'))
button_mul.grid(row=2, column=3)

button_div = Button(frm, text='/', height=4, width=9, font=35,
                    command=lambda: button_press('/'))
button_div.grid(row=3, column=3)

button_clear = Button(window, text='Clear', height=4, width=38, font=35,
                      command=lambda: clear())
button_clear.pack(pady=22)

window.mainloop()
