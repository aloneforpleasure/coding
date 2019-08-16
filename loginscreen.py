from tkinter import *
import shelve
db = shelve.open('database')


class LoginWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Login")
        self.user_txt = Label(self.root, text="User")
        self.user_input = Entry(self.root)
        self.pass_txt = Label(self.root, text="Password")
        self.pass_input = Entry(self.root, show="*")
        self.login_button = Button(self.root, text="Login", command=self.login)
        self.register_button = Button(self.root, text="Register", command=self.new_account)
        self.sit_txt = Label(self.root, text="Sign in")
        self.packs = [self.user_txt, self.user_input, self.pass_txt, self.pass_input,
                      self.sit_txt]
        for self.pack in self.packs:
            self.pack.pack()
        self.login_button.pack(side=LEFT)
        self.register_button.pack(side=RIGHT)
        self.root.mainloop()

    def new_account(self):
        self.user_input.delete(0, END)
        self.pass_input.delete(0, END)
        self.user_txt['text'] = "New User"
        self.pass_txt['text'] = "New Password"
        self.pass_txt['fg'] = 'green'
        self.user_txt['fg'] = 'green'
        self.login_button['command'] = self.home_screen
        self.register_button['command'] = self.register

    def home_screen(self):
        self.user_input.delete(0, END)
        self.pass_input.delete(0, END)
        self.user_txt['text'] = "User"
        self.pass_txt['text'] = "Password"
        self.pass_txt['fg'] = 'black'
        self.user_txt['fg'] = 'black'
        self.sit_txt['text'] = ''
        self.login_button['command'] = self.login
        self.register_button['command'] = self.new_account

    def login(self):
        if self.user_input.get() == db['user']:
            if self.pass_input.get() == db['password']:
                self.sit_txt['text'] = "Logged Successfully!"
                self.sit_txt['fg'] = "green"
            else:
                self.sit_txt["text"] = "Wrong Password!"
                self.sit_txt["fg"] = 'red'
        else:
            self.sit_txt['text'] = "Invalid User!"
            self.sit_txt['fg'] = 'red'

    def register(self):
        if len(self.user_input.get()) >= 5:
            if len(self.pass_input.get()) >= 5:
                self.sit_txt['text'] = "Registered Successfully!"
                self.sit_txt['fg'] = 'green'
                db['user'] = self.user_input.get()
                db['password'] = self.pass_input.get()
            else:
                self.sit_txt['text'] = "Invalid Password!"
                self.sit_txt['fg'] = "red"
                self.pass_input.delete(0, END)
        else:
            self.sit_txt['text'] = "Invalid User!"
            self.sit_txt['fg'] = "red"
            self.user_input.delete(0, END)


screen = LoginWindow()
db.close()
