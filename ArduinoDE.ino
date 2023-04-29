
int trigPin = 7;    // Trigger
int echoPin = 6;    // Echo
long duration, cm, inches;
int loopc = 0;
 
void setup() {
  //Serial Port begin
  Serial.begin (9600);
  //Define inputs and outputs
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
}
 
void loop() {
  // The sensor is triggered by a HIGH pulse of 10 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  // Read the signal from the sensor: a HIGH pulse whose
  // duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(echoPin, INPUT);
  float duration = pulseIn(echoPin, HIGH);
 
  // Convert the time into a distance
  float cm = (duration/2.0) / 29.1;     // Divide by 29.1 or multiply by 0.0343
  //float inches = (duration/2.0) / 74;   // Divide by 74 or multiply by 0.0135


  if (cm>= 50.0){
    Serial.print(loopc);
    Serial.print("  ");
    Serial.println("NA");

  }
  else{
      Serial.print(loopc);
      Serial.print("  ");
      Serial.print(cm);
      Serial.print("cm");
      Serial.println();
  }
  
  loopc = loopc + 1;

  delay(0);
}