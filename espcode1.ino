#include <ESP8266WiFi.h>
#include <WiFiClient.h> 
#include <ESP8266WebServer.h>

/* Set these to your desired credentials. */
const char *ssid = "GET_PARKING_2G";
const char *pass = "playtmbiz";

int status = WL_IDLE_STATUS; /* temporary status assigned when WiFi.begin() is called */
boolean alreadyConnected = false; // whether or not the client was connected previously
byte ip[] = {192,168,0,14};
WiFiClient client;

void setup() 
{
   delay(1000);
   Serial.begin(115200);  /*Start server*/
   Serial.println();
   Serial.print("Configuring access point...");
   /* You can remove the password parameter if you want the AP to be open. */
   WiFi.begin(ssid,pass); /*Initializes the WiFi library's network settings and provides current status*/
    delay(10000);
   IPAddress myIP = WiFi.softAPIP();/* get IP address*/
   Serial.print("AP IP address: ");
   Serial.println(myIP);

   if(client.connect(ip,8080)) /* to connect to specific IP address and port 1 for success , 0 for failure */
   {
    Serial.println("Connected");
   }
   else {
    Serial.println("Connection Failed");
   }
}

void loop() 
{
   
   while (client.connected()) /* checks whether client is connected to server*/
 
   {
    
   if(client.available())
   {
    Serial.println("Output : ");
    client.write('m');
    Serial.println("Packet sent");
    Serial.println("Still Connected.");
    delay(5000);
   }
   }
   delay(1000);
} 
