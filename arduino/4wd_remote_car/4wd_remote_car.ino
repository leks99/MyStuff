int m1A = 22;
int m1B = 23;
int m1C = 24;
int m1D = 25;
int m2A = 26;
int m2B = 27;
int m2C = 28;
int m2D = 29;
int m3A = 30;
int m3B = 31;
int m3C = 32;
int m3D = 33;
int m4A = 34;
int m4B = 35;
int m4C = 36;
int m4D = 37;
int remoteR = 2;
int pilotOne = 12495;
int pilotTwo = 16718055;
int pilotThree = 31365;
int pilotFor = 16716015;
int pilotFive = 14535;
int pilotSix = 16734885;
int pilotSeven = 17085;
int pilotEight = 16730805;
int pilotNine = 21165;
int pilotNull = 26775;
int pilot100Plus = -26521;
int pilot200Plus = -20401;
int pilotEQ = -28561;
int pilotPlus = -22441;
int pilotMinus = -8161;
int pilotPause = -15811;
int pilotNext = 765;
int pilotPreviou = 8925;
int pilotChPlus = -7651;
int pilotCh = 25245;
int pilotChMinus = -23971;
int mDelay = 2;
int moveMode = 0;
int long cTime = 0;
#include <IRremote.h>
IRrecv irrecv(remoteR);
decode_results results;

void forward()
{
  digitalWrite(m1A, HIGH);
  digitalWrite(m2A, HIGH);
  digitalWrite(m3A, HIGH);
  digitalWrite(m4A, HIGH);
  delay(mDelay);
  digitalWrite(m1A, LOW);
  digitalWrite(m2A, LOW);
  digitalWrite(m3A, LOW);
  digitalWrite(m4A, LOW);
  digitalWrite(m1B, HIGH);
  digitalWrite(m2B, HIGH);
  digitalWrite(m3B, HIGH);
  digitalWrite(m4B, HIGH);
  delay(mDelay);
  digitalWrite(m1B, LOW);
  digitalWrite(m2B, LOW);
  digitalWrite(m3B, LOW);
  digitalWrite(m4B, LOW);
  digitalWrite(m1C, HIGH);
  digitalWrite(m2C, HIGH);
  digitalWrite(m3C, HIGH);
  digitalWrite(m4C, HIGH);
  delay(mDelay);
  digitalWrite(m1C, LOW);
  digitalWrite(m2C, LOW);
  digitalWrite(m3C, LOW);
  digitalWrite(m4C, LOW);
  digitalWrite(m1D, HIGH);
  digitalWrite(m2D, HIGH);
  digitalWrite(m3D, HIGH);
  digitalWrite(m4D, HIGH);
  delay(mDelay);
  digitalWrite(m1D, LOW);
  digitalWrite(m2D, LOW);
  digitalWrite(m3D, LOW);
  digitalWrite(m4D, LOW);
  }
void backward()
{
  digitalWrite(m1D, HIGH);
  digitalWrite(m2D, HIGH);
  digitalWrite(m3D, HIGH);
  digitalWrite(m4D, HIGH);
  delay(mDelay);
  digitalWrite(m1D, LOW);
  digitalWrite(m2D, LOW);
  digitalWrite(m3D, LOW);
  digitalWrite(m4D, LOW);
  digitalWrite(m1C, HIGH);
  digitalWrite(m2C, HIGH);
  digitalWrite(m3C, HIGH);
  digitalWrite(m4C, HIGH);
  delay(mDelay);
  digitalWrite(m1C, LOW);
  digitalWrite(m2C, LOW);
  digitalWrite(m3C, LOW);
  digitalWrite(m4C, LOW);
  digitalWrite(m1B, HIGH);
  digitalWrite(m2B, HIGH);
  digitalWrite(m3B, HIGH);
  digitalWrite(m4B, HIGH);
  delay(mDelay);
  digitalWrite(m1B, LOW);
  digitalWrite(m2B, LOW);
  digitalWrite(m3B, LOW);
  digitalWrite(m4B, LOW);
  digitalWrite(m1A, HIGH);
  digitalWrite(m2A, HIGH);
  digitalWrite(m3A, HIGH);
  digitalWrite(m4A, HIGH);
  delay(mDelay);
  digitalWrite(m1A, LOW);
  digitalWrite(m2A, LOW);
  digitalWrite(m3A, LOW);
  digitalWrite(m4A, LOW);
  }
void left()
{
  digitalWrite(m1D, HIGH);
  digitalWrite(m2A, HIGH);
  digitalWrite(m3D, HIGH);
  digitalWrite(m4A, HIGH);
  delay(mDelay);
  digitalWrite(m1D, LOW);
  digitalWrite(m2A, LOW);
  digitalWrite(m3D, LOW);
  digitalWrite(m4A, LOW);
  digitalWrite(m1C, HIGH);
  digitalWrite(m2B, HIGH);
  digitalWrite(m3C, HIGH);
  digitalWrite(m4B, HIGH);
  delay(mDelay);
  digitalWrite(m1C, LOW);
  digitalWrite(m2B, LOW);
  digitalWrite(m3C, LOW);
  digitalWrite(m4B, LOW);
  digitalWrite(m1B, HIGH);
  digitalWrite(m2C, HIGH);
  digitalWrite(m3B, HIGH);
  digitalWrite(m4C, HIGH);
  delay(mDelay);
  digitalWrite(m1B, LOW);
  digitalWrite(m2C, LOW);
  digitalWrite(m3B, LOW);
  digitalWrite(m4C, LOW);
  digitalWrite(m1A, HIGH);
  digitalWrite(m2D, HIGH);
  digitalWrite(m3A, HIGH);
  digitalWrite(m4D, HIGH);
  delay(mDelay);
  digitalWrite(m1A, LOW);
  digitalWrite(m2D, LOW);
  digitalWrite(m3A, LOW);
  digitalWrite(m4D, LOW);
  }
  void right()
{
  digitalWrite(m1A, HIGH);
  digitalWrite(m2D, HIGH);
  digitalWrite(m3A, HIGH);
  digitalWrite(m4D, HIGH);
  delay(mDelay);
  digitalWrite(m1A, LOW);
  digitalWrite(m2D, LOW);
  digitalWrite(m3A, LOW);
  digitalWrite(m4D, LOW);
  digitalWrite(m1B, HIGH);
  digitalWrite(m2C, HIGH);
  digitalWrite(m3B, HIGH);
  digitalWrite(m4C, HIGH);
  delay(mDelay);
  digitalWrite(m1B, LOW);
  digitalWrite(m2C, LOW);
  digitalWrite(m3B, LOW);
  digitalWrite(m4C, LOW);
  digitalWrite(m1C, HIGH);
  digitalWrite(m2B, HIGH);
  digitalWrite(m3C, HIGH);
  digitalWrite(m4B, HIGH);
  delay(mDelay);
  digitalWrite(m1C, LOW);
  digitalWrite(m2B, LOW);
  digitalWrite(m3C, LOW);
  digitalWrite(m4B, LOW);
  digitalWrite(m1D, HIGH);
  digitalWrite(m2A, HIGH);
  digitalWrite(m3D, HIGH);
  digitalWrite(m4A, HIGH);
  delay(mDelay);
  digitalWrite(m1D, LOW);
  digitalWrite(m2A, LOW);
  digitalWrite(m3D, LOW);
  digitalWrite(m4A, LOW);
  }
  
void setup() {
  Serial.begin(9600);
  irrecv.enableIRIn();
  pinMode(m1A, OUTPUT);
  pinMode(m1B, OUTPUT);
  pinMode(m1C, OUTPUT);
  pinMode(m1D, OUTPUT);
  pinMode(m2A, OUTPUT);
  pinMode(m2B, OUTPUT);
  pinMode(m2C, OUTPUT);
  pinMode(m2D, OUTPUT);
  pinMode(m3A, OUTPUT);
  pinMode(m3B, OUTPUT);
  pinMode(m3C, OUTPUT);
  pinMode(m3D, OUTPUT);
  pinMode(m4A, OUTPUT);
  pinMode(m4B, OUTPUT);
  pinMode(m4C, OUTPUT);
  pinMode(m4D, OUTPUT);
  
}

void loop(){
  if(irrecv.decode(&results))
  {
    Serial.print(results.value);
    Serial.println(" ");
    if(results.value == 16718055)
    {
      moveMode = 1;
      }
    if(results.value == 16730805)
    {
      moveMode = 2;
      }
    if(results.value == 16716015)
    {
      moveMode = 3;
      }
    if(results.value == 16734885)
    {
      moveMode = 4;
      }
    if(results.value == 4294967295)
    {
      cTime = millis();
      }
    
    irrecv.resume();
    }
    if (millis() - cTime > 1000)
      {
        moveMode = 0;
        }
    
   if(moveMode == 1)
   {
    forward();
    }
    if(moveMode == 2)
   {
    backward();
    }
    if(moveMode == 3)  
    {
      left();           
    }
    if(moveMode == 4)
   {
    right();
    }
}
