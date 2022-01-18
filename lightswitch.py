import tkinter as tk
from os.path import exists

window = tk.Tk()

button = tk.Button(text='Light is off', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
light = "off"
window.configure(bg="black")
filename = "actions.log"
doesExist = exists(filename)

if not doesExist:
    with open(filename, "x") as file:
        file.write("Actions: \n")

def changeLight(event):
    global light
    global button
    light = "off" if light == "on" else "on"
    printToFile("Light is turned off") if light == "off" else printToFile("Light is turned on")
    button.configure(text='Light is off') if light == "off" else button.configure(text='Light is on')
    window.configure(bg="black") if light == "off" else window.configure(bg='yellow')

def printToFile(text):
    with open(filename, "a") as file:
        file.write(text + "\n")

button.bind('<Button>', changeLight)

window.mainloop()