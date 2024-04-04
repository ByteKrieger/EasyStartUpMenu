1  # ! /usr/bin/env python3
2  # -*- coding: utf-8 -*-
3  #
4  # GUI module generated by PAGE version 8.0
5  # in conjunction with Tcl version 8.6
6  # Apr 03, 2024 11:50:19 PM CEST  platform: Windows NT
7
8
import sys

9
import tkinter as tk

10
import tkinter.ttk as ttk

11
from tkinter.constants import *

12
import os.path

13
14
_location = os.path.dirname(__file__)
15
16
import autosave_support

17
18
_bgcolor = 'SystemButtonFace'
19
_fgcolor = 'SystemWindowText'
20
_tabfg1 = 'black'
21
_tabfg2 = 'white'
22
_bgmode = 'light'
23
_tabbg1 = '#d9d9d9'
24
_tabbg2 = 'gray40'
25
26


class Toplevel1:
    27

    def __init__(self, top=None):

        28
    '''This class configures and populates the toplevel window.
29            top is the toplevel containing window.'''


30
31
top.geometry("405x305+468+138")
32
top.minsize(120, 1)
33
top.maxsize(5124, 1345)
34
top.resizable(1, 1)
35
top.title("Toplevel 0")
36
top.configure(highlightcolor="SystemWindowText")
37
38
self.top = top
39
40
self.Button1_1_1 = tk.Button(self.top)
41
self.Button1_1_1.place(relx=0.0, rely=0.295, height=36, width=407)
42
self.Button1_1_1.configure(activebackground="#d9d9d9")
43
self.Button1_1_1.configure(activeforeground="black")
44
self.Button1_1_1.configure(background="#000000")
45
self.Button1_1_1.configure(disabledforeground="#b4b4b4")
46
self.Button1_1_1.configure(font="-family {Tondu Beta} -size 24 -weight bold")
47
self.Button1_1_1.configure(foreground="#fbdde0")
48
self.Button1_1_1.configure(highlightcolor="SystemWindowText")
49
self.Button1_1_1.configure(relief="flat")
50
self.Button1_1_1.configure(text='''Herunterfahren in x Sec''')
51
52
self.Button1 = tk.Button(self.top)
53
self.Button1.place(relx=0.0, rely=0.033, height=36, width=407)
54
self.Button1.configure(activebackground="#d9d9d9")
55
self.Button1.configure(activeforeground="black")
56
self.Button1.configure(background="#000000")
57
self.Button1.configure(disabledforeground="#b4b4b4")
58
self.Button1.configure(font="-family {Tondu Beta} -size 24 -weight bold")
59
self.Button1.configure(foreground="#fbdde0")
60
self.Button1.configure(highlightcolor="SystemWindowText")
61
self.Button1.configure(relief="flat")
62
self.Button1.configure(text='''Restart in Sec''')
63
64
self.Button1_1 = tk.Button(self.top)
65
self.Button1_1.place(relx=0.0, rely=0.164, height=36, width=407)
66
self.Button1_1.configure(activebackground="#d9d9d9")
67
self.Button1_1.configure(activeforeground="black")
68
self.Button1_1.configure(background="#000000")
69
self.Button1_1.configure(command=autosave_support.command1)
70
self.Button1_1.configure(disabledforeground="#b4b4b4")
71
self.Button1_1.configure(font="-family {Tondu Beta} -size 24 -weight bold")
72
self.Button1_1.configure(foreground="#fbdde0")
73
self.Button1_1.configure(highlightcolor="SystemWindowText")
74
self.Button1_1.configure(relief="flat")
75
self.Button1_1.configure(text='''Abbrechen''')
76
77
self.menubar = tk.Menu(top, font="TkMenuFont", bg='SystemButtonFace'
78, fg = _fgcolor)
79
top.configure(menu=self.menubar)
80
81
self.Button1_1_1_1 = tk.Button(self.top)
82
self.Button1_1_1_1.place(relx=0.0, rely=0.426, height=36, width=407)
83
self.Button1_1_1_1.configure(activebackground="#d9d9d9")
84
self.Button1_1_1_1.configure(activeforeground="black")
85
self.Button1_1_1_1.configure(background="#000000")
86
self.Button1_1_1_1.configure(disabledforeground="#b4b4b4")
87
self.Button1_1_1_1.configure(font="-family {Tondu Beta} -size 24 -weight bold")
88
self.Button1_1_1_1.configure(foreground="#fbdde0")
89
self.Button1_1_1_1.configure(highlightcolor="SystemWindowText")
90
self.Button1_1_1_1.configure(relief="flat")
91
self.Button1_1_1_1.configure(text='''Restart in BIOS''')
92
93


def start_up():
    94
    autosave_support.main()


95
96
if __name__ == '__main__':
    97
    autosave_support.main()
98
