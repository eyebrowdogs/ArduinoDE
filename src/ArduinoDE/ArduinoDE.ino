
int trigPin = 7;    // Trigger
int echoPin = 6;    // Echo
int buttonPin = 5; // Button
long duration, cm, inches;
int loopc = 0;
 
void setup() {
  //Serial Port begin
  Serial.begin (9600);
  //Define inputs and outputs
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buttonPin, INPUT);
  
}
 
void sender() {
 
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  pinMode(echoPin, INPUT);
  float duration = pulseIn(echoPin, HIGH);
 
 
  float cm = (duration/2.0) / 29.1; 
  


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


void loop(){
  while (digitalRead(buttonPin)==0)
  {
    
  }
  Serial.print("begin");
  while (digitalRead(buttonPin)==0)
  {
    sender();
  }
  Serial.print("end");



}
