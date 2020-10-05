import tkinter as tk

class Addgui(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.phonebook = {}
        self.str_name = tk.StringVar()
        self.str_number = tk.StringVar()
        self.str_result = tk.StringVar()
        self.master.title("Phonebook")
        self.define_widgets()
        self.grid()

    def define_widgets(self):
        # name entry
        name_lab = tk.Label(self, text = "Name:")
        name_lab.grid(row = 0, column = 0)
        name_ent = tk.Entry(self, textvariable = self.str_name)
        name_ent.grid(row = 0, column = 1)
        # number entry
        number_lab = tk.Label(self, text="Number:")
        number_lab.grid(row=1, column=0)
        number_ent = tk.Entry(self, textvariable = self.str_number)
        number_ent.grid(row=1, column=1)
        # results tap
        result_ent = tk.Entry(self, textvariable = self.str_result)
        result_ent.grid(row=2, column=1)
        # buttons for lookup, enter, remove and quit
        lookup_but = tk.Button(self, text = "Lookup", command = self.enter_pb)
        lookup_but.grid(row = 3, column = 0)
        enter_but = tk.Button(self, text="Enter")
        enter_but.grid(row=3, column=1, sticky = tk.W)
        remove_but = tk.Button(self, text="remove")
        remove_but.grid(row=3, column=1)
        quit_but = tk.Button(self, text="quit")
        quit_but.grid(row=3, column = 1, sticky = tk.E)

    # def lookup_pb(self):
    #     if name in dic_phonebook:
    #         print("the phonenumer of", name, "is:", dic_phonebook[name])
    #     else:
    #         print(">name is not in the phonebook")

    def enter_pb(self):
        if self.str_name not in self.phonebook.keys():
            self.phonebook[self.str_name] = self.str_number
            return self.phonebook
        else:
            print(">name is already in the phonebook")
    #
    # def remove_pb(self):
    #     dic_phonebook.pop(name)
    #
    # def check_name(self):
    #     check = False
    #     if name in dic_phonebook:
    #         check = True
    #     return check
    #
    # def quit_pb(self):
    #     print("program terminated")


phonebook = Addgui()
phonebook.mainloop()