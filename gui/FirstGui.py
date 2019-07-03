#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as hello
import tkinter.messagebox #这个是消息框，对话框的关键


def but():
    tkinter.messagebox.showinfo('提示', '人生苦短,及时python')
    root=tkinter.Tk()
    root.title('GUI')#标题
    root.geometry('800x600')#窗体大小
    root.resizable(False, False)#固定窗体
    tkinter.Button(root, text='hello button',command=but).pack()
    root.mainloop()

class APP:
    def __init__(self, master):
        frame = hello.Frame(master)
        frame.pack(side=hello.LEFT, padx=100, pady=100)

        self.hi_there = hello.Button(frame, text="打招呼", bg="black", fg="white", command=self.say_hi)
        self.hi_there.pack()

    def say_hi(self):
        but()


if __name__ == "__main__":
    root = hello.Tk()
    app = APP(root)

    root.mainloop()

