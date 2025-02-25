# Streaming DHT Sensor Readings to the Power Bi Api Endpoint
This project streams DHT11 sensor data (Temperature & Humidity) in realtime from an Arduino microcontroller to Power BI using the Power BI Streaming API and Python

## 📌 **Steps to Set Up the Project**

### 1️⃣ **Upload Arduino Sketch**  

- Install the **DHT sensor library** in the Arduino IDE.  
- Connect the **DHT11 sensor**:  
  - **Vcc pin (first pin from the left)** → **5V pin** on the Arduino.  
  - **Data pin (second pin)** → **Pin 4 on the Arduino** (*with a 10kΩ pull-up resistor to Vcc*).  
  - **GND pin (fourth pin)** → **GND on the Arduino**.  
- Upload the Arduino Sketch (`DHT11ArduinoSketch.ino`) to the Arduino (**Uno** in this case).  
- In the Arduino IDE:  
  - Ensure the correct **port** is selected under **Tools → Port** (*check in Device Manager*).  
  - Select the correct **Arduino board** under **Tools → Board**.  
- Open the **Serial Monitor** to verify that sensor data is displayed correctly.  
- If the data appears as expected, go to **Tools → Port** and disconnect the selected port to allow **Python** to access the serial communication without conflicts.  

### 2️⃣ Read Data from Serial Port in Python

Install PySerial:

`pip install pyserial`

Run the script (`PythonSerialRead.py`) to read Arduino data from COM4.

### 3️⃣ Set Up Power BI Streaming Dataset
Open Power BI Service → Go to Workspace → Search for Streaming Dataset.
Choose Streaming API and define the following fields:
 - **Temperature → Number**
 - **Humidity → Number**
 - **Time → Datetime**
(This field will store the timestamp for when the temperature and humidity readings were recorded.)
Click Create and copy the Push URL.

### 4️⃣ Modify Python Script to Send Data to Power BI

Install the requests library:

`pip install requests`

Edit the script (PythonPowerBiApi.py) and update it with your Power BI Push URL.

Run the script to start streaming data

### 5️⃣ Monitor in Power BI Dashboard

Add Streaming Line Charts,Cards to visualize Temperature & Humidity.

Download the Power BI Mobile App to monitor in real time.



