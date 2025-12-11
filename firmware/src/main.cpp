#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include <TFT_eSPI.h> // Hardware-specific library

// WiFi Credentials
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

// API Endpoint
const char* api_url = "http://YOUR_SERVER_IP:8000/api/v1/data/latest";

TFT_eSPI tft = TFT_eSPI(); 

void setup() {
  Serial.begin(115200);
  
  // Display Init
  tft.init();
  tft.setRotation(1);
  tft.fillScreen(TFT_BLACK);
  tft.setTextColor(TFT_WHITE, TFT_BLACK);
  tft.setTextSize(2);
  tft.setCursor(0, 0);
  tft.println("Connecting to WiFi...");

  // WiFi Connection
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting...");
  }
  
  tft.fillScreen(TFT_BLACK);
  tft.println("Connected!");
  delay(1000);
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(api_url);
    int httpResponseCode = http.GET();

    if (httpResponseCode > 0) {
      String payload = http.getString();
      Serial.println(payload);

      // Parse JSON
      DynamicJsonDocument doc(1024);
      deserializeJson(doc, payload);

      float ph = doc["ph"];
      float temp = doc["temperature"];
      float tds = doc["tds"];

      // Update Display
      tft.fillScreen(TFT_BLACK);
      tft.setCursor(0, 0);
      tft.setTextSize(3);
      tft.println("Water Monitor");
      tft.setTextSize(2);
      tft.println("");
      
      tft.print("pH: "); tft.println(ph);
      tft.print("Temp: "); tft.print(temp); tft.println(" C");
      tft.print("TDS: "); tft.println(tds);

    } else {
      Serial.print("Error code: ");
      Serial.println(httpResponseCode);
      tft.println("API Error");
    }
    http.end();
  }

  // Update every 60 seconds
  delay(60000);
}
