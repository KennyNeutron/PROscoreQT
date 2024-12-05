import os; os.system('cls');

import serial
import threading
arduinoSerial = serial.Serial(port='COM8', baudrate=9600, timeout=0.1)

print("PROsoreQT v1.0")
print("System Begin...")

# msg_ToWrite = input("Enter a message: ");
# arduino.write(bytes(msg_ToWrite, 'utf-8')) 

# msg_ToRead = arduino.readline().decode('utf-8')
# print(f"Message Received: {msg_ToRead}")


def arduinoSerial_PrintMessage():
    while True:
        msg_ToRead = arduinoSerial.readline().decode('utf-8')
        if(len(msg_ToRead)!=0):
            print(f"Message Received: {msg_ToRead}")

thread = threading.Thread(target=arduinoSerial_PrintMessage)