from machine import Pin
import utime

m1 = Pin(22, Pin.OUT)
m2 = Pin(23, Pin.OUT)

while True:
    m1.value(1)
    m2.value(0)
    utime.sleep(2)
    m1.value(0)
    m2.value(0)
    utime.sleep(1)
    m1.value(0)
    m2.value(1)
    utime.sleep(2)
    m1.value(0)
    m2.value(0)
    utime.sleep(1)


##################
######HTML########
##################

include <WiFi.h>
include <WebServer.h>

#Configuración de WiFi
const char* ssid = "FamiliaMarta";
const char* password = "51752291";

#Pines del motor
uint8_t MotorP1pin = 22;  // Dirección 1
uint8_t MotorP2pin = 23;  // Dirección 2
bool MotorP1Estado = LOW;
bool MotorP2Estado = LOW;

#Servidor web
WebServer server(80);

#Función para generar la página web
String SendHTML(bool MotorP1Estado, bool MotorP2Estado) {
  String ptr = "<!DOCTYPE html><html>";
  ptr += "<head><title>Control de Motor DC</title>";
  ptr += "<style>";
  ptr += "body {font-family: 'Arial', sans-serif; background-color: #f4f4f9; margin: 0; padding: 0; text-align: center;}";
  ptr += "h1 {color: #2c3e50; margin-top: 30px; font-size: 36px;}";
  ptr += "h3 {color: #34495e; font-size: 24px; margin-bottom: 30px;}";
  ptr += "button {background-color: #3498db; color: white; padding: 15px 30px; font-size: 18px; border: none; border-radius: 5px; margin: 10px; cursor: pointer; transition: background-color 0.3s;}";
  ptr += "button:hover {background-color: #2980b9;}";
  ptr += "button:active {background-color: #1c6c9b;}";
  ptr += ".status {font-size: 20px; color: #2c3e50; margin: 20px 0;}";
  ptr += ".status-on {color: #27ae60;}";
  ptr += ".status-off {color: #e74c3c;}";
  ptr += "</style>";
  ptr += "</head><body>";
  ptr += "<h1>Control de Motor DC</h1>";
  ptr += "<h3>Controla el Motor con el ESP32</h3>";
  ptr += "<div class='status'>Motor P1: <span class='" + String(MotorP1Estado ? "status-on" : "status-off") + "'>" + String(MotorP1Estado ? "ON" : "OFF") + "</span></div>";
  ptr += "<a href=\"/MotorP1on\"><button>Encender Motor P1</button></a>";
  ptr += "<a href=\"/MotorP1off\"><button>Apagar Motor P1</button></a>";
  ptr += "<div class='status'>Motor P2: <span class='" + String(MotorP2Estado ? "status-on" : "status-off") + "'>" + String(MotorP2Estado ? "ON" : "OFF") + "</span></div>";
  ptr += "<a href=\"/MotorP2on\"><button>Encender Motor P2</button></a>";
  ptr += "<a href=\"/MotorP2off\"><button>Apagar Motor P2</button></a>";
  ptr += "</body></html>";
  return ptr;
}

#Funciones de manejo de rutas
void handle_OnConnect() {
  server.send(200, "text/html", SendHTML(MotorP1Estado, MotorP2Estado));
}

void handle_MotorP1on() {
  MotorP1Estado = HIGH;
  MotorP2Estado = LOW; // Evita conflicto de dirección
  server.send(200, "text/html", SendHTML(MotorP1Estado, MotorP2Estado));
}

void handle_MotorP1off() {
  MotorP1Estado = LOW;
  server.send(200, "text/html", SendHTML(MotorP1Estado, MotorP2Estado));
}

void handle_MotorP2on() {
  MotorP2Estado = HIGH;
  MotorP1Estado = LOW; // Evita conflicto de dirección
  server.send(200, "text/html", SendHTML(MotorP1Estado, MotorP2Estado));
}

void handle_MotorP2off() {
  MotorP2Estado = LOW;
  server.send(200, "text/html", SendHTML(MotorP1Estado, MotorP2Estado));
}

void handle_NotFound() {
  server.send(404, "text/plain", "Página no encontrada");
}

void setup() {
  #Configuración serial y de pines
  Serial.begin(115200);
  pinMode(MotorP1pin, OUTPUT);
  pinMode(MotorP2pin, OUTPUT);

  #Conexión WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nConectado a WiFi");
  Serial.print("Dirección IP: ");
  Serial.println(WiFi.localIP());

  #Configuración de rutas del servidor
  server.on("/", handle_OnConnect);
  server.on("/MotorP1on", handle_MotorP1on);
  server.on("/MotorP1off", handle_MotorP1off);
  server.on("/MotorP2on", handle_MotorP2on);
  server.on("/MotorP2off", handle_MotorP2off);
  server.onNotFound(handle_NotFound);
  server.begin();
  Serial.println("Servidor HTTP iniciado");
}

void loop() {
  server.handleClient();

  #Control del motor basado en el estado
  digitalWrite(MotorP1pin, MotorP1Estado);
  digitalWrite(MotorP2pin, MotorP2Estado);
}
