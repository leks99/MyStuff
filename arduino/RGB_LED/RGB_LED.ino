int r = 2;
int g = 3;
int b = 4;
int delayLed = 20;

void setup() {
pinMode(r, OUTPUT);
pinMode(g, OUTPUT);
pinMode(b, OUTPUT);
}

void loop() {
for(int i = 0; i < 256; i++)
{
  analogWrite(r, i);
  delay(delayLed);
  }
for(int i = 0; i < 256; i++)
{
  analogWrite(g, i);
  delay(delayLed);
  }
for(int i = 0; i < 256; i++)
{
  analogWrite(b, i);
  delay(delayLed);
  }
for(int i = 255; i == 0; i--)
{
  analogWrite(r, i);
  delay(delayLed);
  }
for(int i = 255; i == 0; i--)
{
  analogWrite(g, i);
  delay(delayLed);
  }
for(int i = 255; i == 0; i--)
{
  analogWrite(b, i);
  delay(delayLed);
  }
}
