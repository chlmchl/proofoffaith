import serial
import time

arduino = serial.Serial(port='/dev/cu.usbmodem1464301', baudrate=9600, timeout=1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
while True:
    num = input("Say something: ") # Taking input from user
    value = write_read(num)
    #print(value) # printing the value