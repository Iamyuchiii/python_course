import tkinter as tk
# class AddGUI (tk.Frame):
#     def __init__(self):
#         tk.Frame.__init__(self)
#         self.master.title('adding one')
#         self.define_widget()
#         self.grid() # self.grid()
#
#     def define_widget(self):
#         lbl_num = tk.Label(self, text= "Number")
#         lbl_num.grid(row = 0, column =0)
#         # can also do it like this, its more readable
#         """
#         lbl_num = tk.Label(self) # changed
#         lbl_num["text"] = "Number" # new
#         """
#         txt_num = tk.Entry(self)
#         txt_num.grid(row=0, column =1)
#         """
#         btn_add = tk.Button(self) # changed
#         btn_add['text'] = 'Add one' # new
#         """
#         btn_num = tk.Button(self, text ="Add one")
#         btn_num.grid(row=0, column =2)
#         """
#         lbl_result = tk.Label(self) # changed
#         lbl_result['anchor'] = tk.CENTER # new
#         """
#
# my_gui = AddGUI()
# my_gui.mainloop()

class CalcGUI (tk.Frame):
    def __init__ (self):
        tk.Frame.__init__(self)
        self.master.title('calculator')
        self.define_widgets()
        self.grid()
    def define_widgets (self):
        lbl_left = tk.Label(self, text='Left operand')
        lbl_left.grid(row=0, column=0)
        txt_left = tk.Entry(self)
        txt_left.grid(row=1, column=0)
        rb_left_str = tk.Radiobutton(self, text='string')
        rb_left_str.grid(row=2, column=0, sticky = tk.W)
        rb_left_int = tk.Radiobutton(self, text='int')
        rb_left_int.grid(row=3, column=0, sticky = tk.W)
        rb_left_flt = tk.Radiobutton(self, text='float')
        rb_left_flt.grid(row=4, column=0, sticky = tk.W)
        chb_left = tk.Checkbutton(self, text='valid')
        chb_left.grid(row=5, column=0, sticky = tk.W)
        btn_add = tk.Button(self, text='+')
        btn_add.grid(row=1, column=1, sticky=tk.W+tk.E)
        btn_sub = tk.Button(self, text='-')
        btn_sub.grid(row=2, column=1)
        btn_mul = tk.Button(self, text='*')
        btn_mul.grid(row=3, column=1)
        btn_div = tk.Button(self, text='/')
        btn_div.grid(row=4, column=1)
        btn_intdiv = tk.Button(self, text='//')
        btn_intdiv.grid(row=5, column=1)
        btn_mod = tk.Button(self, text='%')
        btn_mod.grid(row=6, column=1)
        lbl_right = tk.Label(self, text='Right operand')
        lbl_right.grid(row=0, column=2)
        txt_right = tk.Entry(self)
        txt_right.grid(row=1, column=2)
        rb_right_str = tk.Radiobutton(self, text='string')
        rb_right_str.grid(row=2, column=2)
        rb_right_int = tk.Radiobutton(self, text='int')
        rb_right_int.grid(row=3, column=2)
        rb_right_flt = tk.Radiobutton(self, text='float')
        rb_right_flt.grid(row=4, column=2)
        chb_right = tk.Checkbutton(self, text='valid')
        chb_right.grid(row=5, column=2)
        msg_error = tk.Message(self, width=280)
        msg_error.grid(row=7, column=0, columnspan=3)
        lbl_result = tk.Label(self, text='Result')
        lbl_result.grid(row=0, column=3)
        txt_result = tk.Entry(self)
        txt_result.grid(row=1, column=3)
        lbl_history = tk.Label(self, text='History')
        lbl_history.grid(row=2, column=3)
        txt_history = tk.Text(self, height=7, width=30)
        txt_history.grid(
        row=3, rowspan=5,
        column=3, columnspan=2)
my_gui = CalcGUI()
my_gui.mainloop()