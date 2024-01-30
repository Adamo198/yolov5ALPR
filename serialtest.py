import serial, time, keyboard

arduino = serial.Serial("COM3", 115200)

    #if (keyboard.is_pressed('o')):
time.sleep(2)
arduino.write("1".encode('utf-8'))
time.sleep(0.05)
arduino_data = arduino.readline().decode('utf-8')
print(arduino_data)
arduino.close()