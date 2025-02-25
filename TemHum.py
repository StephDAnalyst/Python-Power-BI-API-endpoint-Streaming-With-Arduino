import serial
import time

arduino_port = "COM4"
baud_rate = 9600  # Updated baud rate

try:
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)
    print(f"Connected to {arduino_port} at {baud_rate} baud.")
    time.sleep(3)  # Allow Arduino to initialize
except Exception as e:
    print(f"Failed to connect: {e}")
    exit()

print("Reading data from Arduino... Press Ctrl+C to stop.")

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode("utf-8").strip()
            if line:
                print(f"Received: {line}")
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    ser.close()
