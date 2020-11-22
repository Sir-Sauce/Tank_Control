#This is my first update!!
import time
import tkinter as tk

window = tk.Tk()                                #initialize tkinter GUI 
window.title("Tank Control GUI")           
window.geometry('600x300')                      #Sets application window size
window.configure(background='light gray')

#initial variables
mode = 'off'
dispense = 'off'
height = 0
current_height = 20

#radio button index
radio_values = {"off" : "1", 
                "on" : "2", 
                "Auto" : "3"} 

#establish functions
def Exitf():
    quit()

def Start():
    global Start; Start = True
    Start_Button.place_forget()
    time.sleep(0.1)

def forget(Widget):
    Widget.place_forget()

def retrieve(Widget, x, y):
    Widget.place(x = x, y = y)

def Dispense(dispense_mode):
    global dispense
    if (dispense_mode == "on"):
        dispense = True
        forget(Dispense_on); retrieve(Dispense_off, 300, 15)
    if(dispense_mode == "off"):
        dispense_mode = False
        forget(Dispense_off); retrieve(Dispense_on, 200, 15)
        

def Get_Height():  
    sel = "Tank Height = " #+ str(height.get()) 
    Scale.config(text = sel) 

#Buttons

Exit_Button = tk.Button(text='Exit', command = Exitf)
Exit_Button.place(x = 20, y = 20)

Start_Button = tk.Button(text='Start', command = Start)
Start_Button.place(x = 20, y = 50)

Dispense_on = tk.Button(text='Dispense: On', command = lambda: Dispense("on"))
Dispense_on.place(x = 200, y = 15)

Dispense_off = tk.Button(text='Dispense: Off', command = lambda: Dispense("off"))
Dispense_off.place(x = 300, y = 15)

# Labels indicating control parameters

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

Scale = tk.Label()
Scale.place(x = 300, y = 330)

#Output labels (for displaying continuously refreshed parameters) 

Control_label1 = tk.Label(text= mode, width = 5)
Control_label1.place(x = 350, y = 80)

Tank_Height1 = tk.Label(text= current_height, width = 5)
Tank_Height1.place(x = 350, y = 120)

Desired_Height1 = tk.Label(text= height, width = 5)
Desired_Height1.place(x = 350, y = 160)

Dispense_Mode1 = tk.Label(text= dispense, width = 5)
Dispense_Mode1.place(x = 350, y = 200)

# Slider Widget to set height

Height_Scalar = tk.Scale(window, bg = 'light grey', from_ = 100, to = 0, orient = 'vertical') 
Height_Scalar.place(x = 475, y = 140)

#establish radio button layout

for (text, value) in radio_values.items(): 
    tk.Radiobutton(window, text = text, variable = radio_values,
     value = value, width = 10).place(x = 20, y = 120+int(value)*20)

#Begin mainloop
while(Start == True):
    break

#Begin GUI mainloop    

window.mainloop()
