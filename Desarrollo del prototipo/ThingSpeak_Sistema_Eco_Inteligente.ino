#include <WiFi.h>
#include <HTTPClient.h>
#include <Adafruit_SSD1306.h>
#include <DHT.h>

#define PIN_DHT 32
#define TIPO_DHT DHT11
DHT dht(PIN_DHT, TIPO_DHT);

#define ANCHO_PANTALLA 128
#define ALTO_PANTALLA 64
Adafruit_SSD1306 pantalla(ANCHO_PANTALLA, ALTO_PANTALLA, &Wire, -1);

#define PIN_ANALOGICO 15

const char* ssid = "Tatiana";
const char* contrasena = "12345678";

const char* servidor = "http://api.thingspeak.com/update";
const char* claveApi = "8K20X6OF251TR04C";

void setup() {
  Serial.begin(115200);
  dht.begin();
  if (!pantalla.begin(0x3C)) {
    for (;;);
  }
  pantalla.clearDisplay();
  pantalla.display();
  WiFi.begin(ssid, contrasena);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }
}

void loop() {
  float temperatura = dht.readTemperature();
  float humedad = dht.readHumidity();
  int valorAnalogico = analogRead(PIN_ANALOGICO);
  float luz = (valorAnalogico / 4095.0) * 100.0;

  pantalla.clearDisplay();
  pantalla.setTextSize(1);
  pantalla.setTextColor(SSD1306_WHITE);
  pantalla.setCursor(0, 0);
  pantalla.print("Temp: ");
  pantalla.print(temperatura);
  pantalla.println(" C");
  pantalla.print("Hum: ");
  pantalla.print(humedad);
  pantalla.println(" %");
  pantalla.print("Luz: ");
  pantalla.print(luz, 1);
  pantalla.println(" %");
  pantalla.display();

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    String url = String(servidor) + "?api_key=" + claveApi +
                 "&field1=" + String(temperatura) +
                 "&field2=" + String(humedad) +
                 "&field3=" + String(luz, 1);
    http.begin(url);
    http.GET();
    http.end();
  }

  delay(15000);
}