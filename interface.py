from tkinter import *
from password_generator import *

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

        label_version = Label(root, text="Version number: ")
        self.entry_version = Entry(root)
        label_version.grid(row=3, column = 0)
        self.entry_version.grid(row=3, column = 1)

        label_passwrd_len = Label(root, text="Password length desired: ")
        self.entry_passwrd_len = Entry(root)
        label_passwrd_len.grid(row=4, column = 0)
        self.entry_passwrd_len.grid(row=4, column = 1)

        self.button_generate = Button(root,text="Generate",command=display_passowrd(self))
        self.button_generate.grid(row=5,column=0)

        self.psswrd_generated = Text(root, state=DISABLED)
        self.psswrd_generated.grid(row=5, column=1)
        
        self.root=root

    def set_text(self,text):
        self.psswrd_generated.config(state=NORMAL)
        self.psswrd_generated.delete(1.0,END)
        self.psswrd_generated.insert("end", text)
        self.psswrd_generated.config(state=DISABLED)
        self.psswrd_generated.update()
        
def display_passowrd(view):
    website=view.entry_website.get()
    user_name=view.entry_user.get()
    master_password=view.entry_master_pass.get()
    version=view.entry_version.get()
    
    length=view.entry_passwrd_len.get()
    if not (website and user_name and master_password and version and length):
        return
    length=int(length)
    password = generate_password(website, user_name, master_password, version,length)
    print(password)
    view.set_text(password)

   
root = Tk()
view = View(root)
root.mainloop()
