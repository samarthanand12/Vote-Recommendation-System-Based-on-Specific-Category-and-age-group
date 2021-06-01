import sys
import pandas as pd

class RangeDict(dict):
    def __getitem__(self, item):
        if type(item) != range:
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)

file = pd.read_csv('data.csv')

leader = RangeDict({range(1947, 1977): "Indian National Congress", range(1977, 1980): "Janata Dal",
                        range(1980, 1990): "Indian National Congress", range(1990, 1991): "Janata Dal",
                        range(1991, 1996): "Indian National Congress", range(1996, 1998): "Janata Dal",
                        range(1998, 2004): "Bharatiya Janata Party", range(2004, 2014): "Indian National Congress",
                        range(2014, 2024): "Bharatiya Janata Party"})

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def toplevel1(top):
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    font12 = "-family {Times New Roman} -size 24 -weight bold"
    font14 = "-family {Comic Sans MS} -size 14 -weight bold"
    font15 = "-family {Comic Sans MS} -size 18 -weight bold"
    font16 = "-family {Comic Sans MS} -size 17 -weight bold"
    font17 = "-family {Comic Sans MS} -size 14 -weight bold"
    font22 = "-family {Comic Sans MS} -size 12 -weight bold"
    style = ttk.Style()
    if sys.platform == "win32":
        style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font="TkDefaultFont")
    style.map('.',background=[('selected', _compcolor), ('active',_ana2color)])

    top.geometry("1201x814")
    top.minsize(148, 1)
    top.maxsize(1924, 1055)
    top.resizable(1, 1)
    top.title("Vote Recommendation System")
    top.configure(background="#bbbbff")
    top.configure(highlightcolor="#6464ff")
    top.protocol('WM_DELETE_WINDOW', sam)  # root is your root window


    global file,name,age,option,msg
    option = tk.StringVar()
    name = tk.StringVar()
    age = tk.StringVar()
    msg = tk.StringVar()

    Label6 = tk.Label(top)
    Label6.place(relx=0.25, rely=0.000, height=112, width=601)
    Label6.configure(background="#bbbbff")
    Label6.configure(disabledforeground="#a3a3a3")
    Label6.configure(font="-family {Times New Roman} -size 25 -weight bold")
    Label6.configure(foreground="#000000")
    Label6.configure(highlightbackground="#b7b7ff")
    Label6.configure(text='''Vote Recommendation System''')


    Label1 = tk.Label(top)
    Label1.place(relx=0.25, rely=0.091, height=90, width=601)
    Label1.configure(background="#bbbbff")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(font="-family {Times New Roman} -size 22 -weight bold")
    Label1.configure(foreground="#000000")
    Label1.configure(highlightbackground="#b7b7ff")
    Label1.configure(text='''Guess who is Best for Whom''')

    Label2 = tk.Label(top)
    Label2.place(relx=0.1, rely=0.207, height=75, width=362)
    Label2.configure(background="#bbbbff")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(font=font15)
    Label2.configure(foreground="#000000")
    Label2.configure(text='''Enter Your Name''')

    Entry1 = tk.Entry(top,textvariable=name)
    Entry1.place(relx=0.458, rely=0.207,height=74, relwidth=0.445)
    Entry1.configure(background="#ececec")
    Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(font=font16)
    Entry1.configure(foreground="#000000")
    Entry1.configure(insertbackground="black")

    Label3 = tk.Label(top)
    Label3.place(relx=0.1, rely=0.323, height=65, width=352)
    Label3.configure(background="#bbbbff")
    Label3.configure(cursor="watch")
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(font=font16)
    Label3.configure(foreground="#000000")
    Label3.configure(text='''Enter Your Age''')

    Entry2 = tk.Entry(top,textvariable=age)
    Entry2.place(relx=0.458, rely=0.323,height=71, relwidth=0.445)
    Entry2.configure(background="#ececec")
    Entry2.configure(disabledforeground="#a3a3a3")
    Entry2.configure(font="-family {Comic Sans MS} -size 17 -weight bold")
    Entry2.configure(foreground="#000000")
    Entry2.configure(highlightbackground="#d9d9d9")
    Entry2.configure(highlightcolor="black")
    Entry2.configure(insertbackground="black")
    Entry2.configure(selectbackground="#c4c4c4")
    Entry2.configure(selectforeground="black")

    Label4 = tk.Label(top)
    Label4.place(relx=0.075, rely=0.429, height=80, width=392)
    Label4.configure(background="#bbbbff")
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(font=font16)
    Label4.configure(foreground="#000000")
    Label4.configure(text='''Area of Interest''')

    TCombobox1 = ttk.Combobox(top, state='readonly',textvariable=option)
    value_list = file["Indicator_Name"].unique().tolist()
    TCombobox1.place(relx=0.458, rely=0.429, relheight=0.095, relwidth=0.448)
    TCombobox1.configure(font=font22)
    TCombobox1.configure(values=value_list)
    TCombobox1.configure(background="#ececec")
    option.set("Choose Category to Search")

    Label5 = tk.Label(top)
    Label5.place(relx=0.283, rely=0.541, height=71, width=504)
    Label5.configure(background="#bbbbff")
    Label5.configure(disabledforeground="#a3a3a3")
    Label5.configure(foreground="#000000")
    Label5.configure(font=font16)
    Label5.configure(text='''Your Result Display Here''')

    Entry3 = tk.Entry(top,textvariable=msg)
    Entry3.place(relx=0.092, rely=0.645,height=74, relwidth=0.828)
    Entry3.configure(background="#ececec")
    Entry3.configure(disabledforeground="#a3a3a3")
    Entry3.configure(font=font14)
    Entry3.configure(foreground="#000000")
    Entry3.configure(insertbackground="black")

    Button1 = tk.Button(top)
    Button1.place(relx=0.125, rely=0.888, height=73, width=306)
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#d9d9d9")
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(font=font17)
    Button1.configure(foreground="#000000")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(text='''Graphical Representation''')
    Button1.configure(pady="0")

    Button2 = tk.Button(top,command=clear)
    Button2.place(relx=0.25, rely=0.775, height=73, width=276)
    Button2.configure(activebackground="#ececec")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#d9d9d9")
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(font=font16)
    Button2.configure(foreground="#000000")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(text='''Clear''')

    Button3 = tk.Button(top,command=find)
    Button3.place(relx=0.591, rely=0.775, height=73, width=286)
    Button3.configure(activebackground="#ececec")
    Button3.configure(activeforeground="#000000")
    Button3.configure(background="#d9d9d9")
    Button3.configure(disabledforeground="#a3a3a3")
    Button3.configure(font=font16)
    Button3.configure(foreground="#000000")
    Button3.configure(highlightbackground="#d9d9d9")
    Button3.configure(highlightcolor="black")
    Button3.configure(pady="0")
    Button3.configure(text='''Find''')

    Button4 = tk.Button(top, command=sam)
    Button4.place(relx=0.716, rely=0.888, height=73, width=276)
    Button4.configure(activebackground="#ececec")
    Button4.configure(activeforeground="#000000")
    Button4.configure(background="#d9d9d9")
    Button4.configure(disabledforeground="#a3a3a3")
    Button4.configure(font=font16)
    Button4.configure(foreground="#000000")
    Button4.configure(highlightbackground="#d9d9d9")
    Button4.configure(highlightcolor="black")
    Button4.configure(pady="0")
    Button4.configure(text='''Exit''')


def sam():
    root.destroy()

def clear():
    name.set("")
    option.set("Choose Category to Search")
    msg.set("")
    age.set("")

def find():
    x=option.get()
    a = float(file[file.Indicator_Name == x]['Value'].max())
    pp=file[(file.Indicator_Name == x)&(file[file.Indicator_Name == x]["Value"]==a)]["Year"]
    pp=pp.max()

    text='Hey '+name.get()+'!, According to Your Search Result "'+leader[pp]+'" is the best Party to Vote.'
    msg.set(text)



if __name__ == '__main__':
    name,age,option,msg=None,None,None,None
    root = tk.Tk()
    # top = tk.Toplevel(root)
    toplevel1(root)
    root.mainloop()






