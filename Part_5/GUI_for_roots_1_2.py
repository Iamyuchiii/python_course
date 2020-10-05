import tkinter as tk
import math

class AddGUI(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.var_a_value = tk.IntVar()
        self.var_b_value = tk.IntVar()
        self.var_c_value = tk.IntVar()
        self.results = tk.StringVar()
        self.master.title('quadratic solver')
        self.define_widgets()
        self.grid()

    def define_widgets(self):
        # for using a
        a_lab = tk.Label(self, text = "A")
        a_lab.grid(row = 0, column = 0)
        a_txt = tk.Entry(self, textvariable = self.var_a_value)
        a_txt.grid(row = 0, column = 1)
        # a_but = tk.Button(self, text = "add")
        # a_but.grid(row=0, column = 2)
        # for using b
        b_lab = tk.Label(self, text="B")
        b_lab.grid(row=1, column=0)
        b_txt = tk.Entry(self, textvariable = self.var_b_value)
        b_txt.grid(row=1, column=1)
        # b_but = tk.Button(self, text="add")
        # b_but.grid(row=1, column=2)
        # for using C
        c_lab = tk.Label(self, text="C")
        c_lab.grid(row=2, column=0)
        c_txt = tk.Entry(self, textvariable = self.var_c_value)
        c_txt.grid(row=2, column=1)
        # c_but = tk.Button(self, text="add")
        # c_but.grid(row=2, column=2)
        # solve button for answers
        ans_show = tk.Entry(self, textvariable = self.results)
        ans_show.grid(row = 3, column = 1)
        ans_but = tk.Button(self, text = "Solve", command = self.function)
        ans_but.grid(row = 4, column = 1)


    def function(self):
        a = float(self.var_a_value.get())
        b = float(self.var_b_value.get())
        c = float(self.var_c_value.get())
        n_list = []
        discr = b**2 - 4 * a * c
        if discr > 0:
            x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
            x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
            # return "discr is " + str(discr), "x1 is " + str(x1), "x2 is " + str(x2)
            return self.results.set ("x1 = " + str(x1) + " x2 = " + str(x2))
        else:
            return self.results.set("sorry :( doesn't work")


solver = AddGUI()
solver.mainloop()