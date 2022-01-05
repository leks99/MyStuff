int m1 = 2;
int m2 = 3;
int m3 = 4;
int m4 = 5;

void setup() {
pinMode(m1, OUTPUT);
pinMode(m2, OUTPUT);
pinMode(m3, OUTPUT);
pinMode(m4, OUTPUT);

}

void loop() {
digitalWrite(m1, HIGH);
delay(2);
digitalWrite(m1, LOW);
digitalWrite(m2, HIGH);
delay(2);
digitalWrite(m2, LOW);
digitalWrite(m3, HIGH);
delay(2);
digitalWrite(m3, LOW);
digitalWrite(m4, HIGH);
delay(2);
digitalWrite(m4, LOW);

}
