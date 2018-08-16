from tkinter import Tk, Label, mainloop
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

def notify(message):
    master = Tk()
    notification = Label(master, text=message)
    notification.pack()
    master.after(5000, lambda: master.destroy())
    mainloop()

ftypes = [('GCODE File', '*.gcode')]

Tk().withdraw()
gcode = askopenfilename(filetypes=ftypes,title='Please select the gcode you want to print')
if gcode != None and gcode != '':
    dstPath = askdirectory(title='Please select the location of the microSD card')
    
    inFile = open(gcode, 'r')
    
    outFileOne = open(dstPath+"\\SAMPLE01.gcode", 'w')
    outFileTwo = open(dstPath+"\\SAMPLE02.gcode", "w")
    outFileThree = open(dstPath+"\\SAMPLE03.gcode", "w")
    
    for line in inFile.read():
        outFileOne.write(line)
        outFileTwo.write(line)
        outFileThree.write(line)
        
    inFile.close()
    outFileOne.close()
    outFileTwo.close()
    outFileThree.close()
    
    notify("Transfer was a success!")
else:
    notify("The action was canceled by the user and files were not transfered")