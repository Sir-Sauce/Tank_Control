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

global Dispense_State; Dispense_State = "Off" 
radio_values = {"Off" : "1", "On" : "2", "Auto" : "3"}  #radio button index
flag = " "
global Inlet_State; Inlet_State = 1
height = 50.0
global current_height; current_height = 50.0
mode = "Off"

global Start_Time; Start_Time = time.time()
print(Start_Time)

global State_1_Interval; State_1_Interval = 2
global State_2_Interval; State_2_Interval = 0.5


# --- GUI Functions --- #

def Exitf():
    window.destroy()

def Start():
    global Start; Start = True
    Start_Button.place_forget()
    time.sleep(0.1)
    print('start button')

def forget(Widget):
    Widget.place_forget()
    
def retrieve(Widget, x, y):
    Widget.place(x = x, y = y)
         
# --- State Functions --- #

def Get_Tank_Height(): 
    height = Height_Scalar.get()
    print(height)

<<<<<<< HEAD
def Dispense_Open():
    
    global current_height
    
    if (time.time and (current_height > 0.0)):
def Dispense_Open(dispense_mode):
    global current_height
=======
def Dispense_Open(dispense_mode):
    global current_height
>>>>>>> parent of e231e99... Update Tank_Control_V1.py
    if ((dispense_mode == True) and (current_height > 0.0)):
        current_height -= 0.5
        print(current_height)
        #time.sleep(1000)
    else:
        pass

def Inlet_Open():
    global current_height
<<<<<<< HEAD
    
    
    ########## Change while loop to if(timer<starttime-interval) then increase ht. 
    if(time.time() > Start_Time + 1):
        current_height += 2
        print("current tank height: " + current_height)
        
    # while (current_height < 100.0): 
    #     current_height += 2
    #     print("current tank height: " + current_height)
    #     time.sleep(1000)
        
=======
    while (current_height < 100.0): 
        current_height += 2
        print(current_height)
        time.sleep(1000)
    #else:
    #    pass
>>>>>>> parent of e231e99... Update Tank_Control_V1.py

############ Timer tasks to update states

<<<<<<< HEAD
# def Timer():
#     if(time.time() > Start_Time + 1):
#         if(Dispense_State == 'On' and current_height > 0):
#             current_height -= 0.5
#             window.update()
#         else:
#             print('Cannot Dispense - Tank is Empty')
#         #if()




    while (current_height < 100.0): 
        current_height += 2
        print(current_height)
        time.sleep(1000)
    #else:
    #    pass


=======
>>>>>>> parent of e231e99... Update Tank_Control_V1.py
def Dispense(dispense_mode):
    if (Start == True):
        global Dispense_State
        if (dispense_mode == "on"):
            Dispense_Open(True)
            Dispense_State = "On"
            forget(Dispense_on); retrieve(Dispense_off, 300, 15)
            print('dispense on')
        else: 
            Dispense_State = "Off"
            forget(Dispense_off); retrieve(Dispense_on, 200, 15)  
            print('dispense off')
            #Dispense_Open(False)
        #print(dispense_txt) #troubleshoot
        Dispense_Mode1.config(text = Dispense_State) #must be moved to before the dispense function is called to prevent delay
    else:
        pass
    
def Warning_Status():
    if (height >= 95.0):                        #set warning labels (high)
        flag = "Warning: High Tank Level"
        print('tank level high')
    elif (height <= 20.0):                      #set warning labels (low)
        flag = "Warning: Low Tank Level"
        print('tank level low')
    else:
        flag = " "                              #set warning labels (none)
        print("Warning: Low Tank nominal")
    Warnings.config(text = flag)


# --- State Logic --- #

#Two seperate state logic functions for "two" concurrently active states

def Inlet_State_Logic(Inlet_State):             
    if(Start == True):
        print("executing state logic")
<<<<<<< HEAD
        print(Inlet_State)
        Get_Tank_Height()                           #get target tank height from scale      
        Warning_Status() 
        
        #Inlet status
=======
>>>>>>> parent of e231e99... Update Tank_Control_V1.py
        Get_Tank_Height()                           #get target tank height from scale
        print(radio_values)      

        #Inlet Status
        if(Inlet_State == 1):                       #inlet closed
            print("off-inlet closed")
            pass
        elif(Inlet_State == 2):                     #inlet open
            Inlet_Open()
            print("on-inlet open")
        elif(Inlet_State == 3):
            if(current_height <= (height - 0.5)):   #inlet auto mode
                Inlet_Open()
                print("auto-inlet open")
            else:
                Inlet_State = 1
                print("auto-inlet closed")
        else:
            pass
    else:
        pass
    Warning_Status()                                #Check tank status for Warnings

def Dispense_State_Logic(Dispense_State):
    if(Start == True):
        #Dispense Status
        if (Dispense_State == "On"):                #dispense on
            Dispense_Open()    
            Dispense("on")
        else:       
            Dispense("off")                         #dispense off   
            pass                       
    else:
        pass
    Warning_Status()                                #Check tank status for Warnings

#def Timer_Func():
#    Dispense_State_Logic(Dispense_State)
#    Inlet_State_Logic(Inlet_State)
#    window.after(1000, Timer_Func())

# --- GUI Buttons --- #
   
Exit_Button = tk.Button(text='Exit', command = Exitf)
Exit_Button.place(x = 20, y = 20)

Start_Button = tk.Button(text='Start', command = Start)
Start_Button.place(x = 20, y = 50)

Dispense_on = tk.Button(text='Dispense: On', command = lambda: Dispense_State_Logic("On"))
Dispense_on.place(x = 200, y = 15)

Dispense_off = tk.Button(text='Dispense: Off', command = lambda: Dispense_State_Logic("Off"))
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

Dispense_Mode1 = tk.Label(text= Dispense_State, width = 5)
Dispense_Mode1.place(x = 350, y = 200)

# Slider Widget to set height

Height_Scalar = tk.Scale(window, bg = 'light grey', variable = height, from_ = 100, to = 0, orient = 'vertical') 
Height_Scalar.place(x = 475, y = 140)
#Scale.config(text = "Tank Height")
Height_Scalar.set(50.0)

#establish radio button layout

for (text, value) in radio_values.items(): 
    tk.Radiobutton(window, text = text, variable = Inlet_State,
    value = value, width = 10, command = lambda: Inlet_State_Logic(Inlet_State)).place(x = 20, y = 120+int(value)*20)

# --- Begin GUI Mainloop --- #    

#window.after(1000, Timer_Func())
window.mainloop()