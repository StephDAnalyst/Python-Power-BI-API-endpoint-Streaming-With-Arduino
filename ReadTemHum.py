import serial
import time
import requests
from datetime import datetime

ser = serial.Serial("COM4",9600,timeout=1)
time.sleep(3)

temperature = None
humidity = None
pbiurl = "https://api.powerbi.com/beta/12775d55-eb1f-4dcc-8ac2-62ac90ed0ec5/datasets/0dd4ff03-ac35-4708-b53d-6d53767bdeaf/rows?experience=power-bi&key=mdguQfkmBV5G9rIctALiTfIlRDDkzcfUYz0YokqjqExyZFS%2Bh9%2FvJ0zJIwCOL%2FGfwPeImT5JYe4GNyWCfZwyNQ%3D%3D"

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode("utf-8").strip()
            if line:
                #print(f"Data Received: {line}")
                if "Temperature" in line:
                    temperature = float(line.split(":")[1].strip().replace("C",""))
                if "Humidity" in line:
                    humidity = float(line.split(":")[1].strip().replace("%",""))

                if temperature is not None and humidity is not None:
                    data = [{"Temperature":temperature, "Humidity":humidity, "Time":datetime.utcnow().isoformat()+"Z"}]
                    response = requests.post(pbiurl,json = data, headers = {"Content-Type":"application/json"})

                    if response.status_code == 200:
                        temperature = None
                        humidity = None
                        print(f"{data} sent successfully")

                    else:
                        print(f"{response.status_code} because {response.text}")
            

except KeyboardInterrupt:
    print("\nExit")
finally:
    ser.close()