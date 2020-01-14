
#include <NewPing.h>
#include <ESP8266WiFi.h>
#include <WebSocketServer.h>
// -#include "io.h"
//#include <String.h>

#define sonar_range 200

WiFiServer server(80);
WebSocketServer webSocketServer;

#define in1Right D6
#define in2Right D7

const char* ssid = "Parth";
const char* password =  "parth1234";

NewPing sonarF (D0, D1, sonar_range);
NewPing sonarL (D0, D2, sonar_range);
NewPing sonarR (D0, D3, sonar_range);

#define in1Left D4
#define in2Left D5

int distanceLeft = 0, distanceFront = 0, distanceRight = 0;
String data;

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  NewPing sonar();

  pinMode(in1Right, OUTPUT);
  pinMode(in2Right, OUTPUT);

  pinMode(in1Left, OUTPUT);
  pinMode(in2Left, OUTPUT);

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
      distanceLeft = sonarL.ping_cm();
      data = String(String(distanceLeft) + String(' ') + String(distanceFront) + String(' ') + String(distanceRight));
      Serial.println(data);
      //         Serial.print(distanceLeft);
      //         Serial.print(' ');
      //         Serial.print(distanceFront);
      //         Serial.print(' ');
      //         Serial.println(distanceRight);
      webSocketServer.sendData(data);
      String command =  webSocketServer.getData();
      Serial.println("command :" + command);
      if (command == "W") {
        //forward
        digitalWrite(in1Right, HIGH);
        digitalWrite(in2Right, LOW);
        
        digitalWrite(in1Left, HIGH);  
        digitalWrite(in2Left, LOW);
      }
      else if (command =="S") {
        //backwards
        digitalWrite(in1Left, LOW);
        digitalWrite(in2Left, HIGH);

        digitalWrite(in1Right, LOW);
        digitalWrite(in2Right, HIGH);
      } else if (command == "A") {
        //left
        digitalWrite(in1Left, HIGH);
        digitalWrite(in2Left, LOW);

        digitalWrite(in1Right, LOW);
        digitalWrite(in2Right, HIGH);
      } else if (command == "D") {
        //right
        digitalWrite(in1Right, LOW);
        digitalWrite(in2Right, HIGH);
        
        digitalWrite(in1Left, LOW);
        digitalWrite(in2Left, HIGH);
        
        
      } else {
        digitalWrite(in1Left, LOW);
        digitalWrite(in2Left, LOW);

        digitalWrite(in1Right, LOW);
        digitalWrite(in2Right, LOW);
      }
      delay(500); // Delay needed for receiving the data correctly
    }
    Serial.println("The client disconnected");
    delay(100);
  }

  delay(100);
}
