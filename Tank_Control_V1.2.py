"""
MCE 433 - Tank Control Project
Authors: Austin Clark & Matthew Morgan

This program encompasses a Fluid Tank Simulation
The GUI includes two states of control, inlet valve and dispense valve
Inlet valve control is given an Off (Default), On, and Automatic
Do note, that the Automatic Control is dependent on the Tank Height Setting

Notable flow rates of both states:
    Inlet Valve will intake at a rate of 2 cm/s
    Dispense Valve will output at a rate of 0.5 cm/s
    
Notable warning thresholds:
    Tank height exceeds 95cm - "Warning: High Tank Level"
    Tank height below 20cm - "Warning: Low Tank level"
    
In order to beign the program, the Start button must be selected

"""

### --- Libraries Used --- ###


import time
import tkinter as tk


### --- GUI Window Creation --- ###


window = tk.Tk()                                # initialize tkinter GUI
window.title("Tank Control GUI")                # Labels GUI Window
window.geometry('600x300')                      # Sets application window size
window.configure(background = 'light gray')     # Set background of window


### --- Variables --- ###

radio_values = {"Off"  : "1",
                "On"   : "2",
                "Auto" : "3"}                   # Radio Button Index
State1 = " "                                    # State 1 status - inlet operations
State2 = " "                                    # State 2 status - dispense operations
Next_State1 = "InletOff"                        # Next status for state 1
Next_State2 = "DispenseOff"                     # Next status for state 2
Start_Time1 = 0                                 # Store time for start of operation
Dispense_State = "Off"                          # Initial Dispense state is off
Control_Mode = "Off"                            # Initial Control Mode
Inlet_Op = 'Off'                                # Track inlet valve status from Radio Button
Dispense_On = False                             # Initial Dispense valve status
Inlet_State = tk.StringVar(window,"1")          # tkinter string to store radio button variable
flag = " "                                      # Warning message is blank on startup
height = tk.DoubleVar()                         # variable set by user as target by scale 
height.set(50.0)                                # Initial Slider Scale to 50.0
scale_height = 50.0                             # Initial Slider Label to 50.0
current_height = 50.0                           # Dynamically changes on inlet and outlet flow


### --- GUI Functions --- ###


# Close GUI Window
def Exitf():
    window.destroy()


# Hide widget in GUI
def forget(Widget):
    Widget.place_forget()


# Display widget in GUI
def retrieve(Widget, x, y):
    Widget.place(x = x, y = y)


### --- Auxilery Functions --- ###


# Get program run time
def Get_Time_Now():
    return(time.perf_counter())                                 


# Get the Slider Set tank height (For Auto Mode) 
def Get_Tank_Height():                                          
   if(Start == True):                                           
        scale_height = height.get()                             # Save scale value (height.get()) as scale_height for label
        print('Scale ht:' + str(scale_height))                  # Prints output
        Desired_Height1.config(text = scale_height)             # Configures label with updated value
        window.update()                                         # Updates window (optional?)
        return scale_height
   else:
       pass


# From GUI input, turn dispense on/off
def Dispense(Dispense_Button):
    global Dispense_On
    
    if (Dispense_Button == "On"):
        forget(Dispense_on); retrieve(Dispense_off, 300, 15)
        print('dispense on')
        Dispense_State = 'On'; 
        Dispense_On = True

    else:
        forget(Dispense_off); retrieve(Dispense_on, 200, 15)
        print('dispense off')
        Dispense_State = 'Off'; 
        Dispense_On = False

    Dispense_Mode1.config(text = Dispense_State)


# Set Control Mode based upon Radio Button selection
def Inlet_State_Status(Inlet_State):
    global Inlet_Op; Inlet_Op = 'Off'
    print('inlet state statues:  ' + str(Inlet_State))
    if Inlet_State == '1':
        Inlet_Op = 'Off'
    elif  Inlet_State == '2':
        Inlet_Op = 'On'
    elif Inlet_State == '3':
        Inlet_Op = 'Auto'
    print('inlet op: ' + Inlet_Op)
    Control_label1.config(text = Inlet_Op)
    return Inlet_Op


# Check tank height and display warning if over/under limits
def Warning_Status():
    if (current_height >= 95.0):                                #set warning labels (high)
        flag = "Warning: High Tank Level"
        print('tank level high')

    elif (current_height <= 20.0):                              #set warning labels (low)
        flag = "Warning: Low Tank Level"
        print('tank level low')

    else:
        flag = " "                                              #set warning labels (none)
        print("Warning: Tank Level nominal")
    Warnings.config(text = flag)


# --- State Logic --- #


# Start the program button
def Start():
    global Start; Start = True
    global Start_Time1; Start_Time1 = Get_Time_Now()
    Start_Button.place_forget()
    while (2>1):
        time.sleep(0.1)
        window.update()
        Control_Task()


# State control function
def Control_Task():
    global Start_Time1
    global Inlet_On
    global Dispense_On
    global Next_State
    global State1
    global State2
    global Delay_Over
    global Next_State1
    global Next_State2
    global current_height
    global height
    global scale_height
    
    scale_height = height.get()
    State1 = Next_State1
    State2 = Next_State2
    Get_Tank_Height()
    
    print(State1 + State2)
    print(Inlet_Op)
    print(scale_height)
     
    if (Get_Time_Now() - Start_Time1) >= 1:       
        Delay_Over = True
        Start_Time1 = Get_Time_Now()
        
        if State1 == "InletOff": 
            
            if ((Inlet_Op =='On') or (Inlet_Op == 'Auto' and (current_height <= scale_height - 0.5))):
                Next_State1 = 'InletOn'
                
        if State1 == 'InletOn':
            
            if Inlet_Op == 'Off' or current_height >= 100.0:
                Next_State1 = "InletOff"
            
            elif Delay_Over == True:    
                
            
                if (Inlet_Op == 'Auto' and current_height > scale_height - 0.5):   #should be > not >= (inlet valve open at scale_height -0.5cm)
                    Next_State1 = 'InletOff'        
                            
                else:
                    current_height += 2
                    
                    if(current_height > 100.0):              #sets upper bound to prevent tank from filling past 100.0cm
                        current_height = 100.0
    
            
        if State2 =="DispenseOff":
            
            if Dispense_On == True:
                
                Next_State2 = 'DispenseOn'
                print('THIS IS NOW ON YOO')
                
        if State2 == 'DispenseOn':
            
            if Dispense_On == False or current_height == 0: #Sets lower bound to prevent tank from emptying below 0.0cm
                Next_State2 = 'DispenseOff'
            
            elif Delay_Over == True:   
                #current_height -= 0.5             

                if (Inlet_Op == "Auto" and current_height <= scale_height - 0.5): #flag to make inlet op increment exactly at scale_height - 0.5
                    Next_State1 = "InletOn"
                else:
                    current_height -= 0.5
                    

    Warning_Status()
    Tank_Height1.config(text = current_height)
    print(current_height)


# --- GUI Buttons --- #


Exit_Button = tk.Button(text='Exit', command = Exitf)
Exit_Button.place(x = 20, y = 20)

Start_Button = tk.Button(text='Start', command = Start)
Start_Button.place(x = 20, y = 50)

Dispense_on = tk.Button(text='Dispense: On', command = lambda: Dispense("On"))
Dispense_on.place(x = 200, y = 15)

Dispense_off = tk.Button(text='Dispense: Off', command = lambda: Dispense("Off"))
Dispense_off.place(x = 300, y = 15)


# --- GUI Scale Button --- # --- #For Troubleshooting

#Scale_Button = tk.Button(text='Confirm Height', command = lambda: Get_Tank_Height())   #confirm height button to set scale value as target
#Scale_Button.place(x = 450, y = 260)

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

Control_label1 = tk.Label(text= Control_Mode, width = 5)
Control_label1.place(x = 350, y = 80)

Tank_Height1 = tk.Label(text= current_height, width = 5)
Tank_Height1.place(x = 350, y = 120)

Desired_Height1 = tk.Label(text= scale_height, width = 5)
Desired_Height1.place(x = 350, y = 160)

Dispense_Mode1 = tk.Label(text= Dispense_State, width = 5)
Dispense_Mode1.place(x = 350, y = 200)


#establish radio button layout
for (text, value) in radio_values.items():
    tk.Radiobutton(window, text = text, variable = Inlet_State,
    value = value, width = 10, command = lambda: Inlet_State_Status(Inlet_State.get()) ).place(x = 20, y = 120+int(value)*20)
    print('this is from radio button ' + str(Inlet_State.get()))


# Slider Widget to set height
Height_Scalar = tk.Scale(window, bg = 'light grey', variable = height, from_ = 100, to = 0, orient = 'vertical') #setup scale
Height_Scalar.place(x = 475, y = 140)                                                                            #place scale


#Begin Mainloop to generate window

window.after(10, forget(Dispense_off))              #Forget initial dispense_off widget button 
window.mainloop()