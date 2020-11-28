"""
MCE 433 - Tank Control Project
Authors: Austin Clark & Matthew Morgan
"""
# --- Libraries Used --- #

import time
import tkinter as tk

# --- GUI Window Creation --- #

window = tk.Tk()                                #initialize tkinter GUI 
window.title("Tank Control GUI")           
window.geometry('600x300')                      #Sets application window size
window.configure(background = 'light gray')

# --- Initial Variables --- #
dispense_txt = "Off"
dispense_var = tk.StringVar()
mode = 'Off'
radio_values = {"Off" : "1", "On" : "2", "Auto" : "3"} #radio button index
flag = " "

# --- Chaning Variables --- #

height = 50.0
current_height = 50.0

# --- GUI Functions --- #

def Exitf():
    window.destroy()

def Start():
    global Start; Start = True
    Start_Button.place_forget()
    time.sleep(0.1)

def forget(Widget):
    Widget.place_forget()
def retrieve(Widget, x, y):
    Widget.place(x = x, y = y)
         
# --- State Functions --- #

def Dispense_Open(dispense_mode):
    if (dispense_mode == True):
        global current_height
        current_height -= 0.5
        print(current_height)
        time.sleep(1)
    else:
        pass

def Inlet_Open():
    global current_height
    current_height += 2
    print(current_height)
    time.sleep(1)


def Dispense(dispense_mode):
    if (Start == True):
        global dispense_txt
        if (dispense_mode == "on"):
            Dispense_Open(True)
            dispense_txt = "On"
            forget(Dispense_on); retrieve(Dispense_off, 300, 15)
        else: 
            dispense_txt = "Off"
            forget(Dispense_off); retrieve(Dispense_on, 200, 15)   
            #Dispense_Open(False)
        #print(dispense_txt) #troubleshoot
        Dispense_Mode1.config(text = dispense_txt) #must be moved to before the dispense function is called to prevent delay
    else:
        pass

# --- GUI Buttons --- #
   
Exit_Button = tk.Button(text='Exit', command = Exitf)
Exit_Button.place(x = 20, y = 20)

Start_Button = tk.Button(text='Start', command = Start)
Start_Button.place(x = 20, y = 50)

Dispense_on = tk.Button(text='Dispense: On', command = lambda: Dispense("on"))
Dispense_on.place(x = 200, y = 15)

Dispense_off = tk.Button(text='Dispense: Off', command = lambda: Dispense("off"))
Dispense_off.place(x = 300, y = 15)

# --- GUI Control Labels --- #

Control_label = tk.Label(text= "Control Mode", width = 15)
Control_label.place(x = 200, y = 80)

Tank_Height = tk.Label(text= "Current Tank Height", width = 15)
Tank_Height.place(x = 200, y = 120)

Desired_Height = tk.Label(text= "Target Tank Height", width = 15)
Desired_Height.place(x = 200, y = 160)

Dispense_Mode = tk.Label(text= "Dispense Mode", width = 15)
Dispense_Mode.place(x = 200, y = 200)

Control_Set = tk.Label(text= "Control Mode Setting", width = 15)
Control_Set.place(x = 20, y = 100)

Height_Set = tk.Label(text= "Tank Height Setting", width = 15)
Height_Set.place(x = 440, y = 100)

Warnings = tk.Label(text = flag, bg = "yellow", width = 25)
Warnings.place(x = 185, y = 250)

Scale = tk.Label()
Scale.place(x = 300, y = 330)

# --- GUI Output Labels --- #
#for displaying continuously refreshed parameters

Control_label1 = tk.Label(text= mode, width = 5)
Control_label1.place(x = 350, y = 80)

Tank_Height1 = tk.Label(text= current_height, width = 5)
Tank_Height1.place(x = 350, y = 120)

Desired_Height1 = tk.Label(text= height, width = 5)
Desired_Height1.place(x = 350, y = 160)

Dispense_Mode1 = tk.Label(text= dispense_txt, width = 5)
Dispense_Mode1.place(x = 350, y = 200)

# Slider Widget to set height

Height_Scalar = tk.Scale(window, bg = 'light grey', variable = height, from_ = 100, to = 0, orient = 'vertical') 
Height_Scalar.place(x = 475, y = 140)
#Scale.config(text = "Tank Height")
Height_Scalar.set(50.0)

#establish radio button layout

for (text, value) in radio_values.items(): 
    tk.Radiobutton(window, text = text, variable = radio_values,
     value = value, width = 10).place(x = 20, y = 120+int(value)*20)

# --- State Logic --- #

if(Start == True):
    if(radio_values == 1):                      #inlet closed
        pass
    elif(radio_values == 2):                    #inlet open
        Inlet_Open()
    else:
        if(current_height <= (height - 0.5)):   #inlet auto mode
            Inlet_Open()
        else:
            pass
    if (dispense_txt == "On"):                  #dispense on
        Dispense("on")
    else:                                       #dispense off   
        pass
    if (height >= 95.0):                        #set warning labels (high)
        flag = "Warning: High Tank Level"
    elif (height <= 20.0):                      #set warning labels (low)
        flag = "Warning: Low Tank Level"
    else:
        flag = " "                              #set warning labels (none)
    Warnings.config(text = flag)
else:
    pass

# --- Begin GUI Mainloop --- #    

window.mainloop()