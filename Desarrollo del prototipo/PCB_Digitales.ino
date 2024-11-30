#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>
#include <Wire.h>
#include <DHT.h>

// Configuración del DHT11
#define DHTPIN 32       // Pin donde está conectado el DHT11
#define DHTTYPE DHT11  // Tipo de sensor
DHT dht(DHTPIN, DHTTYPE);

// Configuración de la pantalla OLED
#define SCREEN_WIDTH 128 // Ancho de la pantalla OLED
#define SCREEN_HEIGHT 64 // Altura de la pantalla OLED
#define OLED_RESET -1    // Pin de reset (usado en algunas pantallas, -1 si no se usa)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Configuración del LDR  
#define LDRPIN 15 // Pin analógico donde está conectado el LDR
int ldrValue;
const int darkThreshold = 300;    // Umbral para "oscuro"
const int mediumLightThreshold = 700; // Umbral para "luminosidad media"

void setup() {
  // Inicialización de la pantalla
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("No se pudo encontrar una pantalla OLED!"));
    //hile (true); // Detener el programa si no encuentra la pantalla
    for(;;);
  }

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("Inicializando...");
  display.display();
  delay(2000);

  // Inicialización del sensor DHT11
  dht.begin();

  // Inicialización del monitor serial
  Serial.begin(115200);
}

void loop() {
  // Leer temperatura y humedad del DHT11
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // Leer luminosidad del LDR
  ldrValue = analogRead(LDRPIN);

  // Verificar si las lecturas son válidas
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println(F("Error al leer del sensor DHT!"));
    display.clearDisplay();
    display.setCursor(0, 0);
    display.println("Error leyendo");
    display.println("sensor DHT");
    display.display();
    delay(2000);
    return;
  }

  // Determinar el estado de luminosidad
  String lightStatus;
  if (ldrValue < darkThreshold) {
    lightStatus = "Oscuro";
  } else if (ldrValue < mediumLightThreshold) {
    lightStatus = "Luz Media";
  } else {
    lightStatus = "Hay luz";
  }

  // Mostrar valores en el monitor serial
  Serial.print("Temperatura: ");
  Serial.print(temperature);
  Serial.println(" °C");
  Serial.print("Humedad: ");
  Serial.print(humidity);
  Serial.println(" %");
  Serial.print("Luminosidad: ");
  Serial.print(ldrValue);
  Serial.print(" - ");
  Serial.println(lightStatus);

  // Mostrar valores en la pantalla OLED
  display.clearDisplay();
  display.setCursor(0, 0);
  display.println("Sensor DHT11 & LDR");
  display.println("");
  display.print("Temp: ");
  display.print(temperature);
  display.println(" C");
  display.print("Humedad: ");
  display.print(humidity);
  display.println(" %");
  display.println("");
  display.print("Luz: ");
  display.print(lightStatus);
  display.display();

  delay(2000); // Actualizar cada 2 segundos
}