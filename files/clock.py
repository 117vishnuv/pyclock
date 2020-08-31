from tkinter import *
from tkinter.ttk import *
import time



from time import strftime

root = Tk()
root.wm_attributes("-topmost", 1)
root.title('Time')


def time() :

    #t = time.strptime(timevalue_24hour, "%H:%M")
   # string= time.strftime( "%I:%M %p", t )

  
    string = strftime(' %A :: %I:%M:%S:: %p ')
    lbl.config(text = string)
    lbl.after(1000, time)


lbl = Label(root, font = ('calibri', 25, 'bold'),
            background ='purple',
            foreground = 'white' )
                                        
                                        
lbl.pack(anchor = 'center') 
time()

mainloop()


