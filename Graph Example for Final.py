# Matthew Morgan - MCE 433 - Project Assignment 1 - Part 2
#Import tkinter, math, and matplotlib libraries
import tkinter as tk                
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

#initiate window
window = tk.Tk()                                 
window.title("Matthew Morgan Project 1 Part 2") 
window.geometry('500x500')          

# Create labels
instructions = tk.Label(text="Please input the Initial and Final Angles",font=14)                
instructions.place(x=120, y =10) 

input_start_angle = tk.Label(text="Initial Angle(Degrees)",font=14)                
input_start_angle.place(x=50, y =40)   

input_end_angle = tk.Label(text="Final Angle(Degrees)",font=14)                
input_end_angle.place(x=270, y =40)  

calc_comp = tk.Label(text="",font=14,fg='red')                
calc_comp.place(x=165, y =180) 

error_message = tk.Label(text="",font=14,fg='red')                
error_message.place(x=20, y =105) 

output_max_value = tk.Label(text="Maximum Value",font=14)                
output_max_value.place(x=190, y =220)   

output_min_value = tk.Label(text="Minimum Value",font=14)                
output_min_value.place(x=190, y =300)   

output_avg_value = tk.Label(text="Average value",font=14)                
output_avg_value.place(x=195, y =380)   

#Create input boxes
input_box_start = tk.Entry(fg="black", bg="yellow", width=15,font=16) 
input_box_start.place(x= 60, y =75)   

input_box_end = tk.Entry(fg="black", bg="yellow", width=15,font=16) 
input_box_end.place(x= 290, y =75)  

input_array = []; output_array = [] #initiate input and output lists

#Function to calc. min,max,avg - return values - plot sine wave
def Start():  

    # If one of the inputs is empty then fail
    if not input_box_start.get() or not input_box_end.get():
        error_message["text"] = 'One of your inputs is empty, please correct and try again.'
        calc_comp["text"] = ""
    
    # If input #1 > input #2 then fail
    elif int(input_box_end.get()) < int(input_box_start.get()):
        error_message["text"] = 'Start point is greater than end point, please correct and try again.'
        calc_comp["text"] = ""
        
    #Passes all tests
    else: 
        error_message["text"] = ''
        start_point = int(input_box_start.get())
        end_point = int(input_box_end.get())
    
        print(start_point); print(end_point) #print inputs to console
        
        output_array.clear(); input_array.clear() #clear lists
        
        #Loop to create inputs and calc outputs
        for i in [float(j)/10 for j in range(start_point*10,1+end_point*10,1)]:
            y = round(math.sin(math.radians(i)),2)
            output_array.append(y); input_array.append(i)
        
        #print lists to console
        print("this is the input array"); print(input_array) 
        print("this is the output array"); print(output_array)
        print("this is how long:"); print(len(output_array))

        #calc min, max, avg values
        max_value = round(max(output_array),2)
        min_value = round(min(output_array),2)
        avg_value = 0 if len(output_array) == 0 else round(sum(output_array)/len(output_array),2)
    
        #print calc. values to console
        print("Max Value:"); print(max_value)
        print("Min Value:"); print(min_value)
        print("Avg Value:"); print(avg_value)
        
        # Display Calcualted values
        
        # Min. Value Calc
        min_label = tk.Label(window, text = min_value, bg='white', font=16, width = 10)
        min_label.place(x=200, y=330)
        
        # Avg. Value Calc
        avg_label = tk.Label(window, text = avg_value, bg='white', font=16, width = 10)
        avg_label.place(x=200, y=410)
        
        # Max. Value Calc
        max_label = tk.Label(window, text = max_value, bg='white', font=16, width = 10)
        max_label.place(x=200, y=250)
        
        ## Create Sin Wave Graph
        
        # set figure size
        fig = Figure(figsize = (3, 3), dpi = 100) 
        
        # Data to graph 
        plot_x = input_array 
        plot_y = output_array
        
        # adding the subplot 
        plot1 = fig.add_subplot(111) 
        
        # plotting the graph 
        plot1.plot(plot_x,plot_y) 
        
        #label plot axis
        plot1.set_title('Sine Wave of Given Range')
        plot1.set_xlabel('x')
        plot1.set_ylabel('y = sin(x)')
        
        #create canvas
        canvas = FigureCanvasTkAgg(fig,master = window)   
        canvas.draw() 
        
        # place canvas on window 
        canvas.get_tk_widget().place(x=25,y=475, width = 450, height = 325)
        window.geometry("500x825")
        
        calc_comp["text"] = "Calculation Completed"  #Complete calc message

#Function to close the window   
def close_window(): 

    window.destroy()

#Function to clear and reset GUI inputs and outputs
def Reset():
    
    calc_comp["text"] = ""
    
    max_label = tk.Label(window, text = "", bg='white', font=16, width = 10)
    max_label.place(x=200, y=250)
    
    min_label = tk.Label(window, text = "", bg='white', font=16, width = 10)
    min_label.place(x=200, y=330)
    
    avg_label = tk.Label(window, text = "", bg='white', font=16, width = 10)
    avg_label.place(x=200, y=410)
    
    error_message["text"] = 'Cleared'

#Creating a command button    
StartButton = tk.Button(text="Calculate Minimum, Maximum, and Average Values",command = Start,font=14)   #Define Start button and associated function
StartButton.place(x= 60, y =140)                         #Set the position of the Start button in the GUI 

#Creating a command button
ExitButton = tk.Button(text="Exit",command = close_window, width = 10, height = 2) #Define Exit button and associated function
ExitButton.place(x= 350, y =430)                         #Set the position of the Exit button in the GUI 

#Creating a command button
ClearButton = tk.Button(text="Reset",command = Reset, width = 10, height = 2)     #Define Exit button and associated function
ClearButton.place(x= 60, y =430)                         #Set the position of the Exit button in the GUI 

window.mainloop() #//start the event loop














































