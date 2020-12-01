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

# --- Variables --- #

global Dispense_State; Dispense_State = "Off" 

















############### HERE IS THE RADIO VARIABLE ##################

global Inlet_State; Inlet_State = '0'
# the way in which the variable is used may need changed for the radio loop
# Inlet_State = StrVar() 
radio_values = {"Off"  : "1",
                "On"   : "2",
                "Auto" : "3"}  #radio button index

############# END OF RELEVANT RADIO BUTTON STUFF ############



















global current_height; current_height = 50.0
global Start_Time1; 
global Start_Time2; 
global State_1_Interval; State_1_Interval = 2
global State_2_Interval; State_2_Interval = 0.5


flag = " "
height = 50.0
Control_Mode = "Off"

State = " "
Next_State = "InletOffDispenseOff"
Start_Time1 = 0
Start_Time2 = 0




# --- GUI Functions --- #

def Exitf():
    window.destroy()
    
def forget(Widget):
    Widget.place_forget()
    
def retrieve(Widget, x, y):
    Widget.place(x = x, y = y)
    
   
    
   
# --- Aux - State Functions --- # 
    
def Get_Time_Now():
    return(time.perf_counter())

def Get_Tank_Height(): 
    height = Height_Scalar.get()
    print('Scale ht.' + str(height))

<<<<<<< HEAD
########## Dispense and Inlet need to operate from timer functions
########## Must store a start time, store button on time, at each interval do something
########## Perform while loop, with embedded timer functions to do above
=======
def Dispense(Dispense_Button):
    if (Start == True):
        
        if (Dispense_Button == "On"):
            forget(Dispense_on); retrieve(Dispense_off, 300, 15)
            print('dispense on')
            Dispense_State = 'On'; return Dispense_State
            Dispense_On = True
        
        else: 
            forget(Dispense_off); retrieve(Dispense_on, 200, 15)  
            print('dispense off')
            Dispense_State = 'Off'; return Dispense_State
            Dispense_On = False
        return Dispense_On
        Dispense_Mode1.config(text = Dispense_State) 










>>>>>>> 8a6ae2a76bb04a98cbc840e128f0f748a79198c5














######## --- RADIO BUTTON FUNCTION --- ###########

def Inlet_State_Status(Inlet_State):
        global Inlet_Op; Inlet_Op = 'Off' 
        print('inlet state statues:  ' + str(Inlet_State))
        if Inlet_State == 0:
            Inlet_Op = 'Off'
        elif  Inlet_State == 1:
            Inlet_Op = 'On'
        elif Inlet_State == 2:
            Inlet_Op = 'Auto'
        print('inlet op: ' + str(Inlet_Op))
        return Inlet_Op   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def Warning_Status():
    
    if (height >= 95.0):                        #set warning labels (high)
        flag = "Warning: High Tank Level"
        print('tank level high')
    
    elif (height <= 20.0):                      #set warning labels (low)
        flag = "Warning: Low Tank Level"
        print('tank level low')
    
    else:
        flag = " "                              #set warning labels (none)
        print("Warning: Tank Level nominal")
    Warnings.config(text = flag)    





# --- State Logic --- #


def Start():
    global Start; Start = True
    global Start_Time1; Start_Time1 = Get_Time_Now()
    global Start_Time2; Start_Time2 = Get_Time_Now()
    Start_Button.place_forget()
    while (2>1):
        window.update()
        ####### THIS IS WHERE STATE FUNCTIONS WILL GO ###########
            ### Control_Task()
            ###
        
    
    print('start button')


### --- This is the new Control Function for State Org. --- ###
### --- This is still in progress
# def Control_Task():
#     State = Next_State
    
#     if (Get_Time_Now() - Start_Time1) >= 1:
        
#         if State == "InletOffDispenseOff":
            
            
            
            # if operation = on OR = auto & ht >= input ht. - 0.5
                #inlet on = true
            # else
                #inlet on = false
            
            # if dispense on = true & inlet on = true
                # Next State =  InletOnDispenseOn
            
            # elif inlet on = true
                # Next State = InletOnDispenseOff
            
            # elif dispense on = true
                # Next state = InletOffDispenseOn
                
            # if state = InletOnDispenseOff OR InletOnDispenseOn
                # if operation = off OR operation = Auto & ht < input ht - 0.5
                    # if state = InletOnDispenseOff
                        # Next State = InletOffDispenseOff
                    # else 
                        # Next State = InletOffDispenseOn
    
            
        

#### --- This will be replaced with Control Function --- ###
# def Inlet_State_Logic(Inlet_State):             
#     global Active_Inlet_State
#     if(Start == True):
#         #Pre-process 
#         print("executing state logic")
#         print(Inlet_State)
        
#         #Inlet status
#         if(Inlet_State == 1):                       #inlet closed
#             Active_Inlet_State = 1
#             Control_Mode = "Off"
#             print("off-inlet closed" + str(Active_Inlet_State))
                    
#         elif(Inlet_State == 2):                     #inlet open
#             Active_Inlet_State = 2
#             Control_Mode = "On"
#             print("on-inlet open" + str(Active_Inlet_State))
        
#         elif(Inlet_State == 3):
#             Control_Mode = "Auto"
#             print("Auto mode")
#             if(current_height <= (height - 0.5)):   #inlet auto mode
#                 Active_Inlet_State = 2
#                 print("auto-inlet open" + str(Active_Inlet_State))
#             else:
#                 Active_Inlet_State = 1
#                 print("auto-inlet closed" + str(Active_Inlet_State))
#         else:
#             pass
#         return Active_Inlet_State; return Control_Mode

#     else:
#         Active_Inlet_State = 0 
#         return Active_Inlet_State
#         print("Not Started")




# --- GUI Buttons --- #
   
Exit_Button = tk.Button(text='Exit', command = Exitf)
Exit_Button.place(x = 20, y = 20)

Start_Button = tk.Button(text='Start', command = Start)
Start_Button.place(x = 20, y = 50)

Dispense_on = tk.Button(text='Dispense: On', command = lambda: Dispense("On"))
Dispense_on.place(x = 200, y = 15)

Dispense_off = tk.Button(text='Dispense: Off', command = lambda: Dispense("Off"))
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

Control_label1 = tk.Label(text= Control_Mode, width = 5)
Control_label1.place(x = 350, y = 80)

Tank_Height1 = tk.Label(text= current_height, width = 5)
Tank_Height1.place(x = 350, y = 120)

Desired_Height1 = tk.Label(text= height, width = 5)
Desired_Height1.place(x = 350, y = 160)

Dispense_Mode1 = tk.Label(text= Dispense_State, width = 5)
Dispense_Mode1.place(x = 350, y = 200)




















########## --- RADIO BUTTON --- ##############

#establish radio button layout

for (text, value) in radio_values.items(): 
    tk.Radiobutton(window, text = text, variable = Inlet_State,            
    value = value, width = 10, command = lambda: Inlet_State_Status(Inlet_State)).place(x = 20, y = 120+int(value)*20)
    print('this is from radio button' + str(Inlet_State))


########## --- END OF RADIO BUTTON --- ##############























# Slider Widget to set height

Height_Scalar = tk.Scale(window, bg = 'light grey', variable = height, from_ = 100, to = 0, orient = 'vertical') 
Height_Scalar.place(x = 475, y = 140)
Height_Scalar.set(50.0)



<<<<<<< HEAD
    
############ Timer tasks to update states
while(2>1):
    window.update()
    print('it is on')
    print('curernt ht.: ' + str(current_height))
    print(Dispense_State)
    Radio_Button()
    
    Dispense(Dispense_State)
    Inlet_State_Logic(Inlet_State)
    
    if(time.time() > Start_Time + 1):
        
        if(Dispense_State == 'On' and current_height > 0):
            current_height -= 0.5
        else:
            print('Cannot Dispense - Tank is Empty')
    
    Inlet_State_Logic(Inlet_State)
    
    if(Active_Inlet_State == 1):
        current_height += 2
        print("current tank height: " + current_height)
    
    if(Dispense_State == 'On'):
        current_height -= 0.5
        print("current tank height: " + str(current_height))
        
    Start_Time = time.time()
    window.mainloop()
=======
window.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
>>>>>>> 8a6ae2a76bb04a98cbc840e128f0f748a79198c5
