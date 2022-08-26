
"""
MIT License

Copyright (c) 2022 AircGroup Studio

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from glob import glob
import os
from pathlib import Path
import tkinter as tk
import shutil

def converter(B):
    """Return the given bytes as a human friendly KB, MB, GB, or TB string."""
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2) # 1,048,576
    GB = float(KB ** 3) # 1,073,741,824
    TB = float(KB ** 4) # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B / KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B / MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B / GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B / TB)

def folderSize(path):
    fsize = 0
    numfile = 0
    iteration = 0
    for file in Path(path).rglob('*'):
        if (os.path.isfile(file)):
            fsize += os.path.getsize(file)
            numfile +=1
        iteration+=1
    return (fsize, numfile, iteration)

def Scanning():
    log["text"] = log["text"] + "TEMPS" + "\n\n" #+tabbing
    log["text"] = log["text"] + "Windows Temps: " +converter(folderSize("C:\\\\Windows\\Temp")[0])+"\n" #+tabbing
    log["text"] = log["text"] + "Windows Downloads: " +converter(folderSize("C:\\\\Windows\\SoftwareDistribution\\Download")[0])+"\n" #+tabbing
    log["text"] = log["text"] + "User Cache: " +converter(folderSize("C:\\Users\\" + os.getlogin() + "\\AppData\\Local\\Temp")[0])+"\n" #+tabbing
    log["text"] = log["text"] + "All cahce: " + converter(folderSize("C:\\\\Windows\\Temp")[0]
                                              + folderSize("C:\\\\Windows\\SoftwareDistribution\\Download")[0]
                                              + folderSize("C:\\Users\\" + os.getlogin() + "\\AppData\\Local\\Temp")[0]) + "\n"
    log["text"] = log["text"] + tabbing
    scan["state"] = "disable"
    clear["state"] = "normal"

def Clearing():
    errors = 0
    log["text"] = log["text"] + "Remove Windows Temps: "
    for i in glob("C:\\Windows\\Temp\\*"):
        try:
            if os.path.isfile(i):
                os.remove(i)
            else:
                shutil.rmtree(i)
        except Exception as error:
            errors+=1
    log["text"] = log["text"] + "Success\n"

    log["text"] = log["text"] + "Remove Windows Downloads: "

    for i in glob("C:\\\\Windows\\SoftwareDistribution\\Download\\*"):
        try:
            if os.path.isfile(i):
                os.remove(i)
            else:
                shutil.rmtree(i)
        except Exception as error:
            errors+=1
    log["text"] = log["text"] + "Success\n"

    log["text"] = log["text"] + "Remove User Cache: "

    for i in glob("C:\\Users\\" + os.getlogin() + "\\AppData\\Local\\Temp\\*"):
        try:
            if os.path.isfile(i):
                os.remove(i)
            else:
                shutil.rmtree(i)
        except Exception as error:
            errors+=1
    log["text"] = log["text"] + "Success\n"

    if errors > 0:
        log["text"] = tabbing + "Cleared with" + errors +" errors\nPlease, check that noting active programs\n" + tabbing
    else:
        log["text"] = tabbing + "Cleared Success\n" + tabbing
    scan["state"] = "normal"
    clear["state"] = "disable"
    
    

# print(converter(folderSize("C:\\\\Windows\\Temp")[0]))
# print(converter(folderSize("C:\\\\Windows\\SoftwareDistribution\\Download")[0]))
# print(converter(folderSize(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp")[0]))

tabbing = "--------------------------------------------------------------------\n"

window = tk.Tk()
window.iconbitmap("Logo.ico")
window.geometry("1280x720+0+0")
window.resizable(False,False)

window.title("AirCleaner")
window["bg"] = "black"

hi = tk.Label(window, text="AirCleaner", font=("Arial", 30), bg="black", fg="white")
hi.place(x=0,y=0)

scan = tk.Button(window, text="   Scan   ",command=Scanning, bg="black",fg="white", font=("Arial", 30))
scan.place(x=0,y=0,rely=1.0,relx=0.0,anchor="sw")

clear = tk.Button(window,state="disable",command=Clearing, text="   Clear   ", bg="black",fg="white", font=("Arial", 30))
clear.place(x=0,y=0,rely=1.0,relx=1.0,anchor="se")

logFrame = tk.Frame(window)
logFrame.place(x=300,y=0, rely=0,relx=0)

log = tk.Label(logFrame, text="--------------------------------------------------------------------\nStart Program\n--------------------------------------------------------------------\n", bg="black",fg="white",font=("Arial", 20))
log.pack()
window.mainloop()
