import tkinter as tk
import shelve as sh

class Addgui(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
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
        name_ent.grid(row = 0, column = 1, columnspan = 3)
        # number entry
        number_lab = tk.Label(self, text="Number:")
        number_lab.grid(row=1, column=0)
        number_ent = tk.Entry(self, textvariable = self.str_number)
        number_ent.grid(row=1, column=1, columnspan = 3)
        # results tap
        result_ent = tk.Label(self)
        result_ent["textvariable"] = self.str_result
        result_ent["anchor"] = tk.CENTER
        result_ent.grid(row=2, column=0, columnspan = 4)
        # buttons for lookup, enter, remove and quit
        lookup_but = tk.Button(self, text = "Lookup")
        lookup_but["command"] = self.lookup_pb
        lookup_but.grid(row = 3, column = 0, padx=5)

        enter_but = tk.Button(self, text="Enter")
        enter_but["command"] = self.enter_pb
        enter_but.grid(row=3, column=1, sticky = tk.W, ipadx=5)

        remove_but = tk.Button(self, text="remove")
        remove_but["command"] = self.remove_pb
        remove_but.grid(row=3, column=2, padx=5)

        quit_but = tk.Button(self, text="quit")
        # quit_but["command"] = self.quit_pb
        quit_but.grid(row=3, column = 3, sticky = tk.E)

    def lookup_pb(self):
        phonebook = sh.open("phonebook")
        name = self.str_name.get()
        with phonebook as pb:
            if name in pb:
                results = ("the phonenumer of {} is {}").format(name, pb[name])
            else:
                results = ("The name {} is not in the phonebook").format(name)
        self.str_result.set(results)

    def enter_pb(self):
        phonebook = sh.open("phonebook")
        name = self.str_name.get()
        number = self.str_number.get()
        with phonebook as pb:
            if name not in phonebook:
                pb[name] = number
                result = "The name {} with number {} is added to the phonebook".format(name, number)
            else:
                result = "The name {} is already in the phonebook".format(name)
            self.str_result.set(result)

    def remove_pb(self):
        phonebook = sh.open("phonebook")
        name = self.str_name.get()
        with phonebook as pb:
            if name not in phonebook:
                result = ("The name {} is not in the phonebook").format(name)
            else:
                pb.pop(name)
                result = ("the name {} is removed from the phonebook").format(name)
            self.str_result.set(result)

    # def quit_pb(self):
    #     root = tk.TK()



phonebook = Addgui()
phonebook.mainloop()