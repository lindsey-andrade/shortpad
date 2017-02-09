from pyserial import serial
import struct

if __name__ == "__main__"
    ser = serial.Serial();
    ser.setPort('COM5')
    ser.baudrate = 9600
    ser.open()
    ser.flushInput()
    ser.flushOutput()

    ser.write(struct.pack('>B', 'Q'))

    print('Done')
