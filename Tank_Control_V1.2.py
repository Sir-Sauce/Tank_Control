"""
MCE 433 - Tank Control Project
Authors: Austin Clark & Matthew Morgan

Items Left:
    1. State Logic Implementation 
    2. Slider Functionality (Confirm Passes Data Correctly - need tkinter variable?)            - Austin
    3. Warning/Error Messages on GUI 
    4. Compare to Requirements Document
    5. Organize Variables, Functions, and Code Flow

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
global Inlet_State; Inlet_State = tk.StringVar(window,"1") #tkinter string to store radio button variable
global current_height; current_height = 50.0               #dynamically changing based on inlet and outlet flow
global Start_Time1
global Start_Time2
global State1
global State2
global Next_State1
global Next_State2
global height

radio_values = {"Off"  : "1",
                "On"   : "2",
                "Auto" : "3"}  #radio button index

flag = " "

height = tk.DoubleVar()                         #variable set by user as target by scale 
height.set(50.0)                                #setting initial scale to 50.0
scale_height = 50.0                             #setting initial text to 50.0


Control_Mode = "Off"
State1 = " "
State2 = " "
Next_State1 = "InletOff"
Next_State2 = "DispenseOff"
Start_Time1 = 0
Start_Time2 = 0

Inlet_Op = 'Off'                                #radio button variable to track inlet valve
Dispense_On = False

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

def Get_Tank_Height():                                          #function called by confirm button
   if(Start == True):                                           #checks if start button has been pushed
        scale_height = height.get()                             #saves scale value (height.get()) as scale_height for label
        print('Scale ht:' + str(scale_height))                  #prints output
        Desired_Height1.config(text = scale_height)             #configures label with updated value
        window.update()                                         #updates window (optional?)
        return scale_height
   else:
       pass

def Dispense(Dispense_Button):
    global Dispense_On
    if (Start == True):

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
    
    else:
        pass



def Inlet_State_Status(Inlet_State):
    if(Start == True):
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
        print("Warning: Tank Level nominal")
    Warnings.config(text = flag)




# --- State Logic --- #


def Start():
    global Start; Start = True
    global Start_Time1; Start_Time1 = Get_Time_Now()
    global Start_Time2; Start_Time2 = Get_Time_Now()
    Start_Button.place_forget()
    while (2>1):
        time.sleep(0.1)
        window.update()
        Control_Task()

    print('start button')


### --- This is the new Control Function for State Org. --- ###
### --- This is still in progress
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
    
    print(State1 + State2)
    
    Get_Tank_Height()
    
    print(Inlet_Op)
    print(scale_height)
     
    if (Get_Time_Now() - Start_Time1) >= 1:
        Delay_Over = True
        Start_Time1 = Get_Time_Now()
        
        if State1 == "InletOff": 
            
            if ((Inlet_Op =='On') or (Inlet_Op == 'Auto' and (current_height <= scale_height - 0.5))):
                Next_State1 = 'InletOn'
                
            
        if State1 == 'InletOn':
            
            if Inlet_Op == 'Off':
                Next_State1 = "InletOff"
            
            elif Delay_Over == True:
                
                if (Inlet_Op == 'Auto' and current_height >= scale_height - 0.5):
                    Next_State1 = 'InletOff'
                    
                else:
                    current_height += 2
            
        if State2 =="DispenseOff":
            
            if Dispense_On == True:
                Next_State2 = 'DispenseOn'
                print('THIS IS NOW ON YOO')
                
        if State2 == 'DispenseOn':
            
            if Dispense_On == False:
                Next_State2 = 'DispenseOff'
            
            elif Delay_Over == True:
                current_height -= 0.5

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

# --- GUI Scale Button --- #

Scale_Button = tk.Button(text='Confirm Height', command = lambda: Get_Tank_Height())   #confirm height button to set scale value as target
Scale_Button.place(x = 450, y = 260)

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


window.after(10, forget(Dispense_off))              #Forget initial dispense_off widget button 
window.mainloop()

