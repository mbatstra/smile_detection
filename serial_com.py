import serial

arduino = serial.Serial('/dev/ttyACM0', 115200)
while True:
    n = input('input: ')
    arduino.write(n.encode())
