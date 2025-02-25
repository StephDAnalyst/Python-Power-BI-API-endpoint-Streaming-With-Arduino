#include <DHT.h>

#define DHTPIN 4        // Pin where the sensor is connected
#define DHTTYPE DHT11   // DHT 11 Sensor

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);   // Set baud rate to 9600
  dht.begin();
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  
  // Print output in the specified format
  Serial.println();  // New Line
  Serial.print("Humidity (%): ");
  Serial.print(humidity, 2);  // Print humidity with 2 decimal places
  Serial.println();

  Serial.print("Temperature (C): ");
  Serial.print(temperature, 2);  // Print temperature with 2 decimal places
  Serial.println();

  delay(1000);
}
