#This is my first update!!
import time
import tkinter as tk

window = tk.Tk()                                #initialize tkinter GUI 
window.title("Tank Control GUI")           
window.geometry('400x200')                      #Sets application window size
window.configure(background='light gray')

def Exitf():
    time.sleep(0.1)
    quit()

def MattTest():
    time.sleep(1)

ExitButton = tk.Button(text='Exit', command = Exitf)
ExitButton.place(x = 20, y = 160)

window.mainloop()
