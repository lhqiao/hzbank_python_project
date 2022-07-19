import tkinter
from tkinter import *
from tkinter import ttk

def admmit_button (txt1,label_tishi):
        txt = txt1.get()
        print(txt)
        if(txt == "1"):
                label_tishi.set("huanying")
def hello():
                print('hello')
def main_page():

        #frame.grid_forget()
        #win.quit()
        win.destroy()
        #win.grid_forget()

        win2 = tkinter.Tk()  # 定义一个窗体
        menubar = Menu(win2)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='打开', command=hello)
        filemenu.add_command(label='保存')
        filemenu.add_separator()
        filemenu.add_command(label='退出', command=quit)
        menubar.add_cascade(label='文件', menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        win2.config(menu=menubar)
        win2.geometry('200x200')

        win2.mainloop()
def register():
        register_win = tkinter.Tk()
        L1 = Label(register_win, text="zhuce", font='Helvetica -36 bold')
        L2 = Label(register_win, text="学号：", font='song -20')
        L3 = Label(register_win, text="姓名：", font='song -20')
        L4 = Label(register_win, text="密码：", font='song -20')

        L1.grid(row=0, column=1)
        L2.grid(row=1)
        L3.grid(row=2)
        L4.grid(row=3)

        txt1 = StringVar()
        txt2 = StringVar()
        txt3 = StringVar()
        e1 = Entry(register_win, textvariable=txt2, width=20, font='song -20')
        e2 = Entry(register_win, textvariable=txt2, width=20, font='song -20')
        e3 = Entry(register_win, textvariable=txt3, width=20, font='song -20')
        button1 = Button(register_win, text='提交')


        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)
        e3.grid(row=3, column=1)
        button1.grid(row=4)


        register_win.mainloop()


def sign_in_page():

        win.title('学生信息')

        L1 = Label(frame, text="学生信息", font='Helvetica -36 bold')
        L2 = Label(frame, text="学号：", font='song -20')
        L3 = Label(frame, text="姓名：", font='song -20')
        L4 = Label(frame, text="密码：", font='song -20')

        L1.grid(row=0, column=1)
        L2.grid(row=1)
        L3.grid(row=2)
        L4.grid(row=3)

        photo = PhotoImage(file='QQ截图20220714130733.png')
        L_Phot = Label(frame,image=photo)
        L_Phot.image = photo
        L_Phot.grid(row=0, column=2 , columnspan=2, rowspan=4)

        # 输入框
        txt1 = StringVar()
        txt2 = StringVar()
        txt3 = StringVar()
        label_tishi = StringVar()
        label_tishi.set("fdasfa")

        numberChosen = ttk.Combobox(frame, width=12, state='readonly')
        numberChosen['values'] = (1, 2, 3, 4)  # 设置下拉列表的值
        numberChosen.grid(column=1, row=1)
        numberChosen.current(0)  # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值


        e2 = Entry(frame, textvariable=txt2, width=20, font='song -20')
        e3 = Entry(frame, textvariable=txt3, width=20, font='song -20')
        button_ad = Button(frame, text='提交', command=main_page)
        button_re = Button(frame, text='注册', command=register)
        label_tishi = Label(frame, textvariable=label_tishi, relief='ridge', width=30)

        # e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)
        e3.grid(row=3, column=1)
        button_ad.grid(row=4)
        button_re.grid(row=4,column =2)
        label_tishi.grid(row=5, column=2)

        win.mainloop()


if __name__=="__main__":
        win = tkinter.Tk()  # 定义一个窗体
        frame = ttk.LabelFrame(win, text=" denglu")
        frame.grid(column=0, row=0, padx=10, pady=10)
        sign_in_page()