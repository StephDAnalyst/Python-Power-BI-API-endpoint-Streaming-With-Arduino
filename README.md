# Streaming DHT Sensor Readings to the Power Bi Api Endpoint
This project streams DHT11 sensor data (Temperature & Humidity) in realtime from an Arduino microcontroller to Power BI using the Power BI Streaming API and Python

## 📌 **Steps to Set Up the Project**

### 1️⃣ **Upload Arduino Sketch**  

- Install the DHT sensor library in the Arduino IDE.  
- Connect the DHT11 sensor:  
  - **Vcc (first pin from the left)** → 5V on Arduino  
  - **Data (second pin)** → Pin 4 on Arduino (**with a 10kΩ pull-up resistor to Vcc**)  
  - **GND (fourth pin)** → GND on Arduino  
- Upload the Arduino Sketch (`arduino_dht.ino`).  




