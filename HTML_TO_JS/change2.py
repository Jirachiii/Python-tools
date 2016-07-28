#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.filedialog import askopenfilename
root = Tk()
text = Text(root)
fname = askopenfilename(filetypes=(("HTML files", "*.html;*.htm;*.js;*.txt"),("All files", "*.*")))
with open(fname, 'r',encoding='utf8') as f:
    content='';
    for line in f.readlines():
    	if ( line!='\n'):
	        line=line.replace('\"','\\\"').replace('\'','\\\"');#TODO正则匹配引号
	        content+="str+=\""+line.rstrip()+'\";\n';#不需要前面缩进就strip()
root = Tk()
text = Text(root)
text.insert(INSERT, content)
text.pack()
root.mainloop()
