#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <FirebaseArduino.h>


// Set these to run example.
#define FIREBASE_HOST "example.firebaseio.com"
#define FIREBASE_AUTH "token_or_secret"
/* Set these to your desired credentials. */
const char *ssid = "DIGISOL"; //Enter your WIFI ssid
const char *password = "skumar102"; //Enter your WIFI password
String path = "/";
void setup() {
  Serial.begin(9600);
  pinMode(D4, OUTPUT);
  digitalWrite(D4,LOW);
  // put your setup code here, to run once:
  // connect to wifi.
  WiFi.begin(ssid, password);
  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());
  //firebase initialization
  Firebase.begin("iotfundamentals.firebaseio.com", "MR4zsp9rOfWZjZXMGvb52h2jYXeIjtR5z7fTePQS");
  
  
  

}


void loop() {
  // put your main code here, to run repeatedly:
  int id = Firebase.getInt("/regid/mask_status");
  String Name = Firebase.getString("/regid/ID");
  Serial.println(id);
  Serial.println(Name);
  if(id==1){
    digitalWrite(D4,HIGH);
  }
  else{
    digitalWrite(D4,LOW);
  }

}
