#include <NewPing.h>
#include <ESP8266WiFi.h>
#include <WebSocketServer.h>
//#include <String.h>

#define sonar_range 200

WiFiServer server(80);
WebSocketServer webSocketServer;
 
const char* ssid = "Parth";
const char* password =  "parth1234";

NewPing sonarF (D1,D2,sonar_range);
NewPing sonarL (D3,D4,sonar_range);
NewPing sonarR (D5,D6,sonar_range);

int distanceLeft = 0, distanceFront = 0, distanceRight = 0;
String data;

void setup() {
  Serial.begin(115200);
 
  WiFi.begin(ssid, password); 
  NewPing sonar();
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
 
  Serial.println("Connected to the WiFi network");
  Serial.println(WiFi.localIP());
 
  server.begin();
  delay(100);
  
}
 
void loop() {
 
  WiFiClient client = server.available();
// 
    if (client.connected() && webSocketServer.handshake(client)) {

    while (client.connected()) {
         distanceFront = sonarF.ping_cm();
         distanceRight = sonarR.ping_cm();
         QdistanceLeft = sonarL.ping_cm();
         data = String(String(distanceLeft) + String(' ') + String(distanceFront) + String(' ') + String(distanceRight));
         Serial.println(data);
//         Serial.print(distanceLeft);
//         Serial.print(' ');
//         Serial.print(distanceFront);
//         Serial.print(' ');
//         Serial.println(distanceRight);
         webSocketServer.sendData(data);
         delay(1000); // Delay needed for receiving the data correctly
    }
   Serial.println("The client disconnected");
   delay(100);
  }
 
  delay(100);
}
