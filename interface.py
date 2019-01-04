from tkinter import *

class View:

    def __init__(self, root):
        label_website = Label(root, text="Domain name: ")
        self.entry_website = Entry(root)
        label_website.grid(row=0, column = 0)
        self.entry_website.grid(row=0, column = 1)

        label_user = Label(root, text="Username: ")
        self.entry_user = Entry(root)
        label_user.grid(row=1, column = 0)
        self.entry_user.grid(row=1, column = 1)

        label_master_pass = Label(root, text="Master password: ")
        self.entry_master_pass = Entry(root)
        label_master_pass.grid(row=2, column = 0)
        self.entry_master_pass.grid(row=2, column = 1)

        label_version_num = Label(root, text="Version number: ")
        self.entry_version_num = Entry(root)
        label_version_num.grid(row=3, column = 0)
        self.entry_version_num.grid(row=3, column = 1)

        label_passwrd_len = Label(root, text="Password length desired: ")
        self.entry_passwrd_len = Entry(root)
        label_passwrd_len.grid(row=4, column = 0)
        self.entry_passwrd_len.grid(row=4, column = 1)

        self.button_generate = Button(root,text="Generate")
        self.button_generate.grid(row=5,column=0)

        self.psswrd_generated = Text(root, state=DISABLED)
        self.psswrd_generated.grid(row=5, column=1)


    def set_text(self,text):
        pass
        
##put this in controller        
root = Tk()
view = View(root)
view.set_text("lkjhlkjhlkj")
root.mainloop()
