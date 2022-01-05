int buttonState = 0;
int led = 2;
int button = 3;
int lastClick;
  int debounce = 20;
  int ledState;
  int lastButtonState;
  int brightnessPin = A0;
void setup() {
  pinMode(led, OUTPUT);
  pinMode(button, INPUT_PULLUP);
  pinMode(brightnessPin, INPUT);
}

void loop() {
  int buttonState = digitalRead(button);
  int brightness = analogRead(brightnessPin) / 4;
  if((millis() - lastClick) > debounce)
  {
    lastClick = millis();
    if(buttonState == 1 && lastButtonState == 0)
    {
      lastButtonState = 1;
      ledState =! ledState;
    }
    if(buttonState == 0 && lastButtonState == 1)
    {
      lastButtonState = 0;
    }
    analogWrite(led, brightness * ledState);
  }
}
