from tkinter import *


class Calculadora:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculadora")
        self.root.geometry("255x220")
        self.result_button = Button(self.root, text="=", width=2,
                                    command=self.calc)
        self.result = Label(self.root, fg='Blue', font=16)
        self.input = Entry(self.root, width=29)
        self.delete_button = Button(self.root, text="⌫", width=2,
                                    command=lambda:
                                    self.input.delete(len(self.input.get()) - 1, END))
        self.addition_button = Button(self.root, text="+", width=2,
                                      command=lambda: self.input.insert(END, "+"))
        self.subtraction_button = Button(self.root, text="-", width=2,
                                         command=lambda: self.input.insert(END, "-"))
        self.multiplication_button = Button(self.root, text="x", width=2,
                                            command=lambda: self.input.insert(END, "*"))
        self.division_button = Button(self.root, text="÷", width=2,
                                      command=lambda: self.input.insert(END, "/"))
        self.percent = Button(self.root, text="%", width=2,
                              command=lambda: self.input.insert(END, '%'))
        self.comma = Button(self.root, text=",", width=2,
                            command=lambda: self.input.insert(END, '.'))
        self.number_0 = Button(self.root, text="0", width=2,
                               command=lambda: self.input.insert(END, '0'))
        self.number_3 = Button(self.root, text="3", width=2,
                               command=lambda: self.input.insert(END, '3'))
        self.number_2 = Button(self.root, text="2", width=2,
                               command=lambda: self.input.insert(END, '2'))
        self.number_1 = Button(self.root, text="1", width=2,
                               command=lambda: self.input.insert(END, '1'))
        self.number_6 = Button(self.root, text="6", width=2,
                               command=lambda: self.input.insert(END, '6'))
        self.number_5 = Button(self.root, text="5", width=2,
                               command=lambda: self.input.insert(END, '5'))
        self.number_4 = Button(self.root, text="4", width=2,
                               command=lambda: self.input.insert(END, '4'))
        self.number_7 = Button(self.root, text="7", width=2,
                               command=lambda: self.input.insert(END, '7'))
        self.number_8 = Button(self.root, text="8", width=2,
                               command=lambda: self.input.insert(END, '8'))
        self.number_9 = Button(self.root, text="9", width=2,
                               command=lambda: self.input.insert(END, '9'))
        self.number_7.place(x=5, y=70)
        self.number_8.place(x=55, y=70)
        self.number_9.place(x=105, y=70)
        self.number_4.place(x=5, y=105)
        self.number_5.place(x=55, y=105)
        self.number_6.place(x=105, y=105)
        self.number_1.place(x=5, y=140)
        self.number_2.place(x=55, y=140)
        self.number_3.place(x=105, y=140)
        self.number_0.place(x=5, y=175)
        self.comma.place(x=55, y=175)
        self.percent.place(x=105, y=175)
        self.input.place(x=7, y=40)
        self.division_button.place(x=155, y=70)
        self.multiplication_button.place(x=155, y=105)
        self.subtraction_button.place(x=155, y=140)
        self.addition_button.place(x=155, y=175)
        self.delete_button.place(x=205, y=70)
        self.result.place(x=10, y=10)
        self.result_button.place(x=205, y=105)
        self.root.mainloop()

    def calc(self):
        self.result['text'] = f'{self.input.get()} = {eval(self.input.get())}'
        self.input.delete(0, END)


calculadora = Calculadora()
