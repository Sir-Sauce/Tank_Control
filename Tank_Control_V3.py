"""
MCE 433 - Final Project - Extension of Tank Control
Authors: Austin Clark & Matthew Morgan

This program encompasses a Fluid Tank Simulation
The GUI includes two states of control, inlet valve and dispense valve
Inlet valve control is given an Off (Default), On, and Automatic
Do note, that the Automatic Control is dependent on the Tank Height Setting
    
Notable warning thresholds:
    Tank height exceeds 95cm - "Warning: High Tank Level"
    Tank height below 20cm - "Warning: Low Tank level"
    
In order to beign the program, the Start button must be selected

"""

### --- Libraries Used --- ###


import time
import tkinter as tk
import serial           #imports serial library
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk   #Needed for Task 8
from matplotlib.figure import Figure



### --- GUI Window Creation --- ###

window = tk.Tk()                                # initialize tkinter GUI
window.title("Tank Control GUI")                # Labels GUI Window
window.geometry('600x750')                      # Sets application window size
window.configure(background = 'light gray')     # Set background of window

### --- Establish Serial Communication --- ###
                                                                    #opens port for serial device, sets baudrate
serArduino = serial.Serial('/dev/cu.usbmodem1431101',38400)         #Austin's default port
#serArduino = serial.Serial('/dev/cu.usbmodem1451301',38400)        #Matt's default port
time.sleep(2)                                                       
print(serArduino.name) 




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
buzzerOp = False                                # Used to set off buzzer (one time) in auto mode

Fill_Rate = 2.0                                 #initiate varying fillrate variable (TASK 7)
update_Fill_Rate = 0

input_array = []; output_array = []             #initiate input and output lists for plot (TASK 8)
current_time = 0
counter = 0


### --- GUI Functions --- ###


# Close GUI Window
def Exitf():
    serArduino.close()  
    time.sleep(0.1)
    window.destroy()


# Hide widget in GUI
def forget(Widget):
    Widget.place_forget()


# Display widget in GUI
def retrieve(Widget, x, y):
    Widget.place(x = x, y = y)











### --- Serial Write Functions --- ###
### --- Will be integrated into all other logic --- ###

'''
def Function_Select(usr_input):         # Function to determine serial data to send to arduino
    window.update()
    print(usr_input, "Serial Byte")                    # Troubleshoot 
    if(usr_input == '0'):               #Warning High
        serArduino.write(b'0')
        print('Sent Serial Byte')
        #print(')         # Troubleshoot 
        time.sleep(0.1)
    elif(usr_input == '1'):             #Warning Low
        serArduino.write(b'1')
        #print('')       # Troubleshoot 
        time.sleep(0.1)
    elif(usr_input == '2'):             #Warning Off
        serArduino.write(b'2')
        #print('')         # Troubleshoot 
        time.sleep(0.1)
    elif(usr_input == '3'):             #Height Indicator LEDS Off (0%)
        serArduino.write(b'3')
        #print('')         # Troubleshoot 
        time.sleep(0.1)
    elif(usr_input == '4'):             #Height Indicator LEDS <20%
        serArduino.write(b'4')
        #print('')         # Troubleshoot 
        time.sleep(0.1)
    elif(usr_input == '5'):             #Height Indicator LEDS <40%
        serArduino.write(b'5')
        #print('')         # Troubleshoot 
        time.sleep(0.1)
    elif(usr_input == '6'):             #Height Indicator LEDS <60%
        serArduino.write(b'6')
        #print('')         # Troubleshoot 
        time.sleep(0.1)
    elif(usr_input == '7'):             #Height Indicator LEDS <80%
        serArduino.write(b'7')
        #print('')         # Troubleshoot 
        time.sleep(0.1)
    elif(usr_input == '8'):             #Height Indicator LEDS >80%
        serArduino.write(b'8')
        #print('')         # Troubleshoot 
        time.sleep(0.1)
    elif(usr_input == '9'):             #Sets Dispense_On  RUE in arduino sketch
        serArduino.write(b'9')
        time.sleep(0.1)
    elif(usr_input == '10'):            #Sets Dispense_On FALSE in arduino sketch
        serArduino.write(b'10')
        time.sleep(0.1)
    else:
        pass
'''


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
    serArduino.write(b'2')                                          #Triggers Task 4 (uses serial write lines below)
    
    if (Dispense_Button == "On"):
        serArduino.write(b'1')                                      #Dispense on setting to arduino
        forget(Dispense_on); retrieve(Dispense_off, 300, 15)
        print('dispense on')
        Dispense_State = 'On'; 
        Dispense_On = True
        

    else:
        serArduino.write(b'0')                                     #Dispense off setting to arduino
        forget(Dispense_off); retrieve(Dispense_on, 200, 15)
        print('dispense off')
        Dispense_State = 'Off'; 
        Dispense_On = False

    Dispense_Mode1.config(text = Dispense_State)












def Get_Fill_Rate():                    #NEW FUNCTION TO SET FILL RATE BASED OFF OF POTENTIOMETER OUTPUT
    global Fill_Rate
    global update_Fill_Rate

    n = serArduino.inWaiting()          #Checks if serial is available
    print(n)
    if (n>0):
        i = serArduino.read(1)          #Reads first serial byte in register
        print(i)
        if (i == b'\x01' and update_Fill_Rate != 1):
            Fill_Rate = 1.0
            update_Fill_Rate = 1

        elif (i == b'\x02' and update_Fill_Rate != 2):
            Fill_Rate = 2.0
            update_Fill_Rate = 2

        elif (i == b'\x03' and update_Fill_Rate != 3):
            Fill_Rate = 3.0
            update_Fill_Rate = 3

        elif (i == b'\x04' and update_Fill_Rate != 4):
            Fill_Rate = 4.0
            update_Fill_Rate = 4

        else:
            pass
    
    else:
        pass
    #print(Fill_Rate)
    serArduino.flushInput()                         # Flushes extra serial Bytes
    Fill_Rate_Label1.config(text = Fill_Rate)       # Reconfigures Text


















# Set Control Mode based upon Radio Button selection
def Inlet_State_Status(Inlet_State):
    global Inlet_Op; Inlet_Op = 'Off'
    print('inlet state statues:  ' + str(Inlet_State))
    if Inlet_State == '1':
        Inlet_Op = 'Off'
    elif  Inlet_State == '2':
        Inlet_Op = 'On'
        serArduino.write(b'4')                                  #Triggers Task 6 in arduino sketch
    elif Inlet_State == '3':
        Inlet_Op = 'Auto'
        buzzerOp = False
    print('inlet op: ' + Inlet_Op)
    Control_label1.config(text = Inlet_Op)
    return Inlet_Op


# Check tank height and display warning if over/under limits
def Warning_Status():
    if (current_height >= 95.0):                                #set warning labels (high)
        flag = "Warning: High Tank Level"    
        serArduino.write(b'0')                                  #writes serial byte to arduino
        print('tank level high')

    elif (current_height <= 20.0):                              #set warning labels (low)
        flag = "Warning: Low Tank Level"
        serArduino.write(b'1')                                  #writes serial byte to arduino
        print('tank level low')

    else:
        flag = " "                                              #set warning labels (none)
        serArduino.write(b'2')                                  #writes serial byte to arduino
        print("Warning: Tank Level nominal")

    Warnings.config(text = flag)    

# --- Height indicator LED logic --- could be merged with warning status????? --- #

def Height_Indicator():                                         
    if (current_height == 0.0):                                 #0%      
        print("Clear Indicator")       
        serArduino.write(b'0')                

    elif (current_height > 0.0 and current_height <= 20.0):     #1-20%                            
        print("Level 1 Indicator")  
        serArduino.write(b'1')                                  

    elif (current_height > 20.0 and current_height <= 40.0):    #21-40%                                    
        print("Level 2 Indicator") 
        serArduino.write(b'2')                                   

    elif (current_height > 40.0 and current_height <= 60.0):    #41-60%                                     
        print("Level 3 Indicator")
        serArduino.write(b'3')                                    

    elif (current_height > 60.0 and current_height <= 80.0):    #61-80%                              
        print("Level 4 Indicator")   
        serArduino.write(b'4')                                 

    else:                                                       #81-100%
        print("Level 5 Indicator")  
        serArduino.write(b'5')                                  

# --- State Logic --- #

# Start the program button

def Start():
    global Start; Start = True
    global Start_Time1; Start_Time1 = Get_Time_Now()
    Start_Button.place_forget()
    while (2>1):
        time.sleep(0.2)
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
    global buzzerOp

    global current_time
    global input_array
    global output_array
    global counter
    
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

        Get_Fill_Rate()             ##### CALLS FILL RATE SET FUNCTION
        
        if State1 == "InletOff": 
            
            if ((Inlet_Op =='On') or (Inlet_Op == 'Auto' and (current_height <= scale_height - 0.5))):
                Next_State1 = 'InletOn'
                
        if State1 == 'InletOn':
            
            if Inlet_Op == 'Off' or current_height >= 100.0:
                Next_State1 = "InletOff"
            
            elif Delay_Over == True:    
                
            
                if (Inlet_Op == 'Auto' and current_height > scale_height - 0.5):   #should be > not >= (inlet valve open at scale_height -0.5cm)

                    if (buzzerOp == False):                   #NOTE THIS PROGRAM WILL NOW NOT ACTIVATE BUZZER
                        #serArduino.write(b'3')               #Task 5 serial write buzzer high for 3 sec
                        buzzerOp == True

                    Next_State1 = 'InletOff'        
                            
                else:
                    current_height += Fill_Rate              #NOTE FILL RATE NOW SET BY POTENTIOMETER
                    
                    if(current_height > 100.0):              #sets upper bound to prevent tank from filling past 100.0cm
                        current_height = 100.0
    
            
        if State2 =="DispenseOff":
            #Function_Select('10')   #Dispense off setting to arduino
            
            if Dispense_On == True:
                
                Next_State2 = 'DispenseOn'
                #print('THIS IS NOW ON YOO')
                
        if State2 == 'DispenseOn':
            #Function_Select('9')    #Dispense on setting to arduino

            if Dispense_On == False or current_height == 0: #Sets lower bound to prevent tank from emptying below 0.0cm
                Next_State2 = 'DispenseOff'
            
            elif Delay_Over == True:   
                #current_height -= 0.5             

                if (Inlet_Op == "Auto" and current_height <= scale_height - 0.5): #flag to make inlet op increment exactly at scale_height - 0.5
                    Next_State1 = "InletOn"
                else:
                    
                    current_height -= 0.5     #Now the Dispense Rate Variable 
                    
    #NOTE THIS PROGRAM WILL NOW NOT SET WARNING OR HEIGHT INDICATOR LEDS - SEE BELOW

    #serArduino.write(b'0'); Warning_Status()     #Sets warning flag and indicator LEDs
    #serArduino.write(b'1'); Height_Indicator()     #Sets indicator LEDs based off tank height              

    Tank_Height1.config(text = current_height)
    print(current_height)
    

    #Appends plot for task 8 once per second
    #print(Get_Time_Now())
    if ((Get_Time_Now() - current_time) >= 1): 

        output_array.append(current_height); print(output_array)
        input_array.append(counter); print(input_array)

        counter += 1
        current_time = Get_Time_Now()
        
        # Data to graph 
        plot_x = input_array 
        plot_y = output_array

        # plotting the graph 
        plot1.plot(plot_x,plot_y)
        if (counter == 1 or counter == 2):
            plot1.set_xlim([0,2])
        elif (counter < 60):
            plot1.set_xlim([input_array[0],input_array[len(input_array)-1]])
        else:
            plot1.set_xlim([input_array[0],input_array[59]])
        canvas.draw()

        if(len(output_array) == 60):
            del output_array[0]
            del input_array[0]
     
    else:
        pass

    











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

Fill_Rate_Label = tk.Label(text= "Fill Rate", width = 15)         #NOTE THIS IS NEW LABEL FOR FILL RATE
Fill_Rate_Label.place(x = 200, y = 290)

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

Fill_Rate_Label1 = tk.Label(text= Fill_Rate, width = 5)            #NOTE THIS IS NEW LABEL FOR FILL RATE (DYNAMIC)
Fill_Rate_Label1.place(x = 350, y = 290)










# --- FIGURE LAYOUT --- #

# set figure size
fig = Figure(figsize = (3, 3), dpi = 100) 

# adding the subplot 
plot1 = fig.add_subplot(111) 

#label plot axis
plot1.set_title('Tank Height Activity')
plot1.set_xlabel('Time (seconds)')
plot1.set_ylabel('Tank Height (cm)')
plot1.grid()


#create canvas
canvas = FigureCanvasTkAgg(fig,master = window)   
canvas.draw() 

# place canvas on window 
canvas.get_tk_widget().place(x=75,y=325, width = 450, height = 400)

















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