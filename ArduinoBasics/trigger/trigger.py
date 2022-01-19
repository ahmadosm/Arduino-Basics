#Ahmad Osman
#2022-01-18
#Programs used to run code: Arduino 1.8.19, Python GUI (IDLE) 2.7.12
#Packages & toolkits may differ depending on python version 3.4+
#Refer @ https://www.python.org/downloads/ to ensure correct version is installed
"""
The following code allows the user to control an LED light connected to an adruino board using a 
systematic button. When the button is clicked the LED will turn on/off. Each time the button is clicked
on the circuit board, a message will be relayed to the gui mentioning the button has been pressed.
"""
#-----------------------------------------------------------------------------------------------------
"""
The following code implements all utilities and toolkits needed for the code.
The program under 'try' check if the toolkits are installed and if so continues.
Otherwise in 'except', the toolkits will be installed and the process will continue
"""
try:
    import pyfirmata, time
    from pyfirmata import Arduino, util
except:
    import pip
    pip.main(['install','pyfirmata'])
    import pyfirmata, time
    from pyfirmata import Arduino, util

import Tkinter
import tkMessageBox

#-----------------------------------------------------------------------------------------------------
"""
The code below is a simple setup to access the arduino board. This consists of connecting the board
to the respective port which is set up on the desktop hardware.
"""
root = Tkinter.Tk() # sets Tkinter package to root variable
root.withdraw() #open root variable packages

board = pyfirmata.Arduino('COM7')

it = pyfirmata.util.Iterator(board)
it.start()

digital_input = board.get_pin('d:10:i')
led = board.get_pin('d:13:o')

#-----------------------------------------------------------------------------------------------------

while True: #starts loop
    sw = digital_input.read() #read digital input from arduino
    if sw is True: #if digital input is acquired begin conditional loop
        led.write(1)
        tkMessageBox.showinfo("Notification", "Button was pressed") #if LED button input is applied display message
        root.update() #update package output
        led.write(0) #turn off LED
        time.sleep(0.1)
