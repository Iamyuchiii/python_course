import tkinter as tk

class AddGUI(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title('quadratic solver')
        self.define_widgets()
        self.grid()

    def define_widgets(self):
        # for using a
        a_lab = tk.Label(self, text = "A")
        a_lab.grid(row = 0, column = 0)
        a_txt = tk.Entry(self)
        a_txt.grid(row = 0, column = 1)
        # a_but = tk.Button(self, text = "add")
        # a_but.grid(row=0, column = 2)
        # for using b
        b_lab = tk.Label(self, text="B")
        b_lab.grid(row=1, column=0)
        b_txt = tk.Entry(self)
        b_txt.grid(row=1, column=1)
        # b_but = tk.Button(self, text="add")
        # b_but.grid(row=1, column=2)
        # for using C
        c_lab = tk.Label(self, text="C")
        c_lab.grid(row=2, column=0)
        c_txt = tk.Entry(self)
        c_txt.grid(row=2, column=1)
        # c_but = tk.Button(self, text="add")
        # c_but.grid(row=2, column=2)
        # solve button for answers
        ans_but = tk.Button(self, text = "Solve")
        ans_but.grid(row = 3, column = 1)



solver = AddGUI()
solver.mainloop()