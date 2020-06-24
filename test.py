import APLIKASINAIVEBAYES as ab
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

UI = ab.New_Toplevel()
UII = UI.config(1)