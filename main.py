print("Do not Close the console")
print("To stop packetspam press :CTRL + C")


#Packet Spammer With a simple GUI
from tkinter import*
from tkinter import ttk
from ttkthemes import themed_tk as tk
root = tk.ThemedTk()
root.get_themes()                 
root.set_theme("radiance")
root.title("Packet Spammer")
root.geometry("340x300")
root.iconbitmap(r"imgres\error.ico")
from random import randint,choices          
running = False

def choicez(array):
    if isinstance(array,list):
        return choices(array,k=1)[0]
    else:
        raise TypeError("Item must be an array")

def execute(input):
    global FINALE
    print(str(scl.get() * 100))
    FINALE = int(scl.get() *100)

scl = Scale(root,from_=0,to=100,orient=HORIZONTAL,command=execute)
scl.grid(row=2,column=3)

class Info:
    def __init__(self):
        global e,e_2,e_3,e_0,a
        e_0 = ttk.Label(root,text="If you dont need something set it equal to <none>")
        a = ttk.Entry(root)
        a.insert(0,"Request URL")
        a.grid(row=3,column=3)
        e = ttk.Entry(root)
        e.insert(0,"Username",)
        e_2 = ttk.Entry(root)
        e_2.insert(0,"Password")
        e_3 = ttk.Entry(root)
        e_3.insert(0,"Email")
        e.grid(row=4,column=3)
        e_0.grid(row=1,column=3)
        e_2.grid(row=5,column=3)
        e_3.grid(row=6,column=3)

def IsList(*args):
    if isinstance(args,list):
        return True
    else:
        raise TypeError("Item must be an array")


information = Info()
try:
    from names import lmao
    IsList(lmao)
    print("Sucessfully imported nameslist")
except TypeError:
    pass

class spam:
    def __init__(self):
        pass        
    def begin(self):
        self.url = a.get()
        self.password = e_2.get()
        self.email = e_3.get()
        self.username = e.get()
        statusbar = ttk.Label(root,text="Packet spam started",relief=SUNKEN)
        statusbar.grid(row=15,column=3,pady=44,ipadx=65)
        check_t = True
        ran_chars = ["a","b","c","d","e","f","g","h",'i',"j","k","l","m","n","o",'p',"q","r","s","t","u","v","w","x",'y',"z"]
        import requests
        import json
        from random import randint,choices
        running = True
        for item in lmao:
            if lmao[FINALE] == item:
                print("Reached the specified amount of " + str(FINALE))
                break;
            else:
                pass_gen = str(randint(100,999)) + str(choicez(ran_chars)) + str(choicez(ran_chars)) + str(choicez(ran_chars)) + str(choicez(ran_chars)) + str(choicez(ran_chars).upper())+str(randint(1000,9999))
                username = item + str(randint(1000,9999))
                web = ["@gmail.com","@hotmail.com","@outlook.com",]
                gmail = str(item) + str(randint(69,420)) +"{}".format(choicez(web))
                password = str(pass_gen) + ran_chars[randint(1,25)].upper()
                if self.email == "" or self.email.lower() == "none":
                    status = 1
                    data_dict = {
                        str(self.username): username,
                        str(self.password): gmail,
                    }
                elif self.username == "" or self.username.lower() == "none" or self.username.lower() == "<none>":
                    status = 2
                    data_dict = {
                        str(self.email): email,
                        str(self.password): gmail,
                    }
                elif self.password == "" or self.password.lower() == "none" or self.password.lower() == "<none>":
                    status = 3
                    data_dict = {
                        str(self.email): email,
                        str(self.username): username,
                    }              
                requests.post(self.url, allow_redirects=False, data=data_dict)
                if status == 1:
                    print("Sending username " + str(username) + " and password " + str(password))
                elif status ==2:
                    print("Sending password " + str(password) + " and email " + str(gmail))
                elif status ==3:
                    print("Sending username " + str(username) + " and email " + str(gmail))
                print("Request URL is {}".format(str(self.url)))
                print("Progressing...")

spammer = spam()


#Exit and Begin Buttons
class StartButs:
    def __init__(self):
        global exit_bt
        global photo
        str_bt = ttk.Button(root,text="Begin Packetspam",command=spammer.begin)
        str_bt.grid(row=7,column=3)
        photo = PhotoImage(file=r"imgres\close.png")
        exit_bt = ttk.Button(root,image = photo,command=root.quit)
        exit_bt.grid(row=8,column=3)

menubar = Menu(root)
root.config(menu =menubar)

menou = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=menou)
menou.add_command(label="Exit",command=root.quit)  

def Get_Help():
    from os import startfile
    file = r"help\index.html"
    startfile(file)

menou = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=menou)
menou.add_command(label="Open Help Pastebin",command=Get_Help)
statusbar = Label(root,text="Packet spam has not begun yet",relief=SUNKEN)
statusbar.grid(row=15,column=3,pady=44,ipadx=65)


bgn = StartButs()
        
mainloop()