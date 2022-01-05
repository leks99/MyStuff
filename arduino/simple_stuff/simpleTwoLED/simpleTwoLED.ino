int led1 = 2;
int led2 = 3;

void setup() {
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
  
}

void loop() {
  digitalWrite(led1,HIGH);
  digitalWrite(led2,LOW);
  delay(600);
  digitalWrite(led1,LOW);
  digitalWrite(led2,HIGH);
  delay(600);
}
