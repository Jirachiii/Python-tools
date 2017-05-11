#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *

def change1():#保留缩进
	res=addSlash(1)
	t2.insert(INSERT, res)

def change2():#不保留缩进
	res=addSlash(2)
	t2.insert(INSERT, res)

def addSlash(type):
    t2.delete('0.0', END)
    data=t1.get('1.0', 'end-1c')
    content='str = '
    for index,line in enumerate(data.splitlines()):
        if (line and line!='\n'):
            line=line.replace('\"','\\\"').replace('\'','\\\"')
            if index ==  0:
                if (type == 1):
                    content+="\""+line.rstrip()+'\" +\n'
                elif (type == 2):
                    content+="\""+line.strip()+'\" +\n'
                continue
            if index == len(data.splitlines()) - 1:
                if (type == 1):
                    content+="      \""+line.rstrip()+'\" ;\n'
                elif (type == 2):
                    content+="      \""+line.strip()+'\" ;\n'
                continue
            if (type == 1):
            	content+="      \""+line.rstrip()+'\" +\n'
            elif (type == 2):
            	content+="      \""+line.strip()+'\" +\n'
    return content
root = Tk()
root.title('HTML TO JS')
root.geometry('1300x600')
# 输入输出框
Label(root, text="转换前").grid(row=0,column=1)
t1=Text(root)
t1.grid(row=0,column=2)
Label(root, text="转换后").grid(row=0,column=3)
t2=Text(root)
t2.grid(row=0,column=4)
btn1 = Button(root, text='无缩进转换(no indent)',command=change2)
btn1.grid(row=2, column=2)
btn1 = Button(root, text='保留缩进转换(keep indent)',command=change1)
btn1.grid(row=3, column=2)
root.mainloop()