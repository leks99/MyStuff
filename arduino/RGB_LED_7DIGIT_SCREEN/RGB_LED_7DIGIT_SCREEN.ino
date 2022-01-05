int receiverpin = 2;
int r = 3;
int g = 4;
int b = 5;
int delayFade = 20;
int delayMultiplier = 10;
int modeRGB = 0;
int pilotOne = 12495;
int pilotTwo = 6375;
int pilotThree = 31365;
int pilotFor = 25979;
int pilotFive = 14535;
int pilotSix = 23205;
int pilotSeven = 17085;
int pilotEight = 19125;
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
int resetMode = 0;
int modeRGBFix = 0;
int la = 6;
int lb = 7;
int lc = 8;
int ld = 9;
int le = 10;
int lf = 11;
int lg = 12;

void displayZero()
{
  digitalWrite(la, LOW);
  digitalWrite(lb, LOW);
  digitalWrite(lc, LOW);
  digitalWrite(ld, LOW);
  digitalWrite(le, LOW);
  digitalWrite(lf, LOW);
  digitalWrite(lg, HIGH);
  
  }
void displayOne()
{
  digitalWrite(la, HIGH);
  digitalWrite(lb, LOW);
  digitalWrite(lc, LOW);
  digitalWrite(ld, HIGH);
  digitalWrite(le, HIGH);
  digitalWrite(lf, HIGH);
  digitalWrite(lg, HIGH);
  
  }
void displayTwo()
{
  digitalWrite(la, LOW);
  digitalWrite(lb, LOW);
  digitalWrite(lc, HIGH);
  digitalWrite(ld, LOW);
  digitalWrite(le, LOW);
  digitalWrite(lf, HIGH);
  digitalWrite(lg, LOW);
  
  }
void displayThree()
{
  digitalWrite(la, LOW);
  digitalWrite(lb, LOW);
  digitalWrite(lc, LOW);
  digitalWrite(ld, LOW);
  digitalWrite(le, HIGH);
  digitalWrite(lf, HIGH);
  digitalWrite(lg, LOW);
  
  }
void displayFor()
{
  digitalWrite(la, HIGH);
  digitalWrite(lb, LOW);
  digitalWrite(lc, LOW);
  digitalWrite(ld, HIGH);
  digitalWrite(le, HIGH);
  digitalWrite(lf, LOW);
  digitalWrite(lg, LOW);
  
  }
void displayFive()
{
  digitalWrite(la, LOW);
  digitalWrite(lb, HIGH);
  digitalWrite(lc, LOW);
  digitalWrite(ld, LOW);
  digitalWrite(le, HIGH);
  digitalWrite(lf, LOW);
  digitalWrite(lg, LOW);
  
  }
void displaySix()
{
  digitalWrite(la, LOW);
  digitalWrite(lb, HIGH);
  digitalWrite(lc, LOW);
  digitalWrite(ld, LOW);
  digitalWrite(le, LOW);
  digitalWrite(lf, LOW);
  digitalWrite(lg, LOW);
  
  }
void displaySeven()
{
  digitalWrite(la, LOW);
  digitalWrite(lb, LOW);
  digitalWrite(lc, LOW);
  digitalWrite(ld, HIGH);
  digitalWrite(le, HIGH);
  digitalWrite(lf, HIGH);
  digitalWrite(lg, HIGH);
  
  }
void displayEight()
{
  digitalWrite(la, LOW);
  digitalWrite(lb, LOW);
  digitalWrite(lc, LOW);
  digitalWrite(ld, LOW);
  digitalWrite(le, LOW);
  digitalWrite(lf, LOW);
  digitalWrite(lg, LOW);
  
  }
void displayNine()
{
  digitalWrite(la, LOW);
  digitalWrite(lb, LOW);
  digitalWrite(lc, LOW);
  digitalWrite(ld, LOW);
  digitalWrite(le, HIGH);
  digitalWrite(lf, LOW);
  digitalWrite(lg, LOW);
  
  }
#include <IRremote.h>
IRrecv irrecv(receiverpin);
decode_results results;

void setup() {
 Serial.begin(9600);
 irrecv.enableIRIn();
 pinMode(r, OUTPUT);
 pinMode(g, OUTPUT);
 pinMode(b, OUTPUT);
 pinMode(la, OUTPUT);
 pinMode(lb, OUTPUT);
 pinMode(lc, OUTPUT);
 pinMode(ld, OUTPUT);
 pinMode(le, OUTPUT);
 pinMode(lf, OUTPUT);
 pinMode(lg, OUTPUT);

 displayZero();
 delay(250);
 displayOne();
 delay(250);
 displayTwo();
 delay(250);
 displayThree();
 delay(250);
 displayFor();
 delay(250);
 displayFive();
 delay(250);
 displaySix();
 delay(250);
 displaySeven();
 delay(250);
 displayEight();
 delay(250);
 displayNine();
 delay(250);
 displayZero();
 delay(250);
}

void loop() {
  Serial.print(modeRGB);
  Serial.println(modeRGBFix);
  if(irrecv.decode(&results))
  {
    int pilot = results.value;
    Serial.println(pilot);
    Serial.println(" ");
    irrecv.resume();
    switch(pilot)
    {
      case 12495:
          modeRGB = 1;
          displayOne();
          break;
      case 6375:
          modeRGB = 2;
          displayTwo();
          break;
      case 31365:
          modeRGB = 3;
          displayThree();
          break;
      default:
          modeRGB = modeRGBFix;
          break;
      }
      modeRGBFix = modeRGB;
    }
    if (modeRGB == modeRGB)
    {
      switch(modeRGB) // --------------------------------------------------swich mode--------------------------------------
      {
            case 2:  //------------------------------------------------------------------2--------------------------------------------
               digitalWrite(r, HIGH);
               digitalWrite(g, HIGH);
               digitalWrite(b, HIGH);
               delay(delayFade * delayMultiplier);
                if (irrecv.decode(&results))
                {
                  int currentV = results.value;
                  irrecv.resume();
                  if(currentV == pilotEQ)
                  {
                    resetMode = 1;
                    }
                  if(currentV == pilotPlus)
                  {
                    delayFade = delayFade + 5;
                    }
                  if(currentV == pilotMinus)
                  {
                    delayFade = delayFade - 5;
                    if (delayFade < 5)
                    {
                      delayFade = 5;
                      digitalWrite(r, HIGH);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      delay(500);
                      digitalWrite(r, LOW);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      }
                    }}
               digitalWrite(r, LOW);
               digitalWrite(g, HIGH);
               digitalWrite(b, HIGH);
               delay(delayFade * delayMultiplier);
               digitalWrite(r, HIGH);
               digitalWrite(g, LOW);
               digitalWrite(b, HIGH);
               delay(delayFade * delayMultiplier);
                if (irrecv.decode(&results))
                {
                  int currentV = results.value;
                  irrecv.resume();
                  if(currentV == pilotEQ)
                  {
                    resetMode = 1;
                    }
                  if(currentV == pilotPlus)
                  {
                    delayFade = delayFade + 5;
                    }
                  if(currentV == pilotMinus)
                  {
                    delayFade = delayFade - 5;
                    if (delayFade < 5)
                    {
                      delayFade = 5;
                      digitalWrite(r, HIGH);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      delay(500);
                      digitalWrite(r, LOW);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      }
                    }
                  }
               digitalWrite(r, HIGH);
               digitalWrite(g, HIGH);
               digitalWrite(b, LOW);
               delay(delayFade * delayMultiplier);
               digitalWrite(r, LOW);
               digitalWrite(g, LOW);
               digitalWrite(b, HIGH);
               delay(delayFade * delayMultiplier);
               digitalWrite(r, HIGH);
               digitalWrite(g, LOW);
               digitalWrite(b, LOW);
               delay(delayFade * delayMultiplier);
                if (irrecv.decode(&results))
                {
                  int currentV = results.value;
                  irrecv.resume();
                  if(currentV == pilotEQ)
                  {
                    resetMode = 1;
                    }
                  }
               digitalWrite(r, LOW);
               digitalWrite(g, HIGH);
               digitalWrite(b, LOW);
               delay(delayFade * delayMultiplier);
               break;
             case 3:  //--------------------------------------------------------------3--------------------------------------------------
                for(int i = 0; i < 256; i++)
              {
                analogWrite(r, i);
                if (irrecv.decode(&results))
                {
                  int currentV = results.value;
                  irrecv.resume();
                  if(currentV == pilotEQ)
                  {
                    resetMode = 1;
                    }
                  if(currentV == pilotPlus)
                  {
                    delayFade = delayFade + 5;
                    }
                  if(currentV == pilotMinus)
                  {
                    delayFade = delayFade - 5;
                    if (delayFade < 5)
                    {
                      delayFade = 5;
                      digitalWrite(r, HIGH);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      delay(500);
                      digitalWrite(r, LOW);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      }
                    }
                  }
                analogWrite(b, (255 - i));
                delay(delayFade);
                }
                for(int i = 255; i == 0; i--)
              {
                analogWrite(r, (255 - i));
                if (irrecv.decode(&results))
                {
                  int currentV = results.value;
                  irrecv.resume();
                  if(currentV == pilotEQ)
                  {
                    resetMode = 1;
                    }
                  if(currentV == pilotPlus)
                  {
                    delayFade = delayFade + 5;
                    }
                  if(currentV == pilotMinus)
                  {
                    delayFade = delayFade - 5;
                    if (delayFade < 5)
                    {
                      delayFade = 5;
                      digitalWrite(r, HIGH);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      delay(500);
                      digitalWrite(r, LOW);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      }
                    }
                  }
                analogWrite(b, i);
                delay(delayFade);
                }
                break;
                case 1://-------------------------------------------------------------1----------------------------------------
              int breakMod = 1;
              Serial.print("  HERE   ");
              for(int i = 0; i < 256; i++)
              {
                analogWrite(r, i);
                if (irrecv.decode(&results))
                {
                  int currentV = results.value;
                  irrecv.resume();
                  if(currentV == pilotEQ)
                  {
                    breakMod = 200;
                    resetMode = 1;
                    }
                  if(currentV == pilotPlus)
                  {
                    delayFade = delayFade + 5;
                    }
                  if(currentV == pilotMinus)
                  {
                    delayFade = delayFade - 5;
                    if (delayFade < 5)
                    {
                      delayFade = 5;
                      digitalWrite(r, HIGH);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      delay(500);
                      digitalWrite(r, LOW);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      }
                    }
                  }
                delay(delayFade);
                i = i * breakMod;
                }
              for(int i = 0; i < 256; i++)
              {
                analogWrite(g, i);
                if (irrecv.decode(&results))
                {
                  int currentV = results.value;
                  irrecv.resume();
                  if(currentV == pilotEQ)
                  {
                    breakMod = 200;
                    resetMode = 1;
                    }
                  if(currentV == pilotPlus)
                  {
                    delayFade = delayFade + 5;
                    }
                  if(currentV == pilotMinus)
                  {
                    delayFade = delayFade - 5;
                    if (delayFade < 5)
                    {
                      delayFade = 5;
                      digitalWrite(r, HIGH);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      delay(500);
                      digitalWrite(r, LOW);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      }
                    }
                  }
                delay(delayFade);
                i = i * breakMod;
                }
              for(int i = 0; i < 256; i++)
              {
                analogWrite(b, i);
                if (irrecv.decode(&results))
                {
                  int currentV = results.value;
                  irrecv.resume();
                  if(currentV == pilotEQ)
                  {
                    breakMod = 200;
                    resetMode = 1;
                    }
                  if(currentV == pilotPlus)
                  {
                    delayFade = delayFade + 5;
                    }
                  if(currentV == pilotMinus)
                  {
                    delayFade = delayFade - 5;
                    if (delayFade < 5)
                    {
                      delayFade = 5;
                      digitalWrite(r, HIGH);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      delay(500);
                      digitalWrite(r, LOW);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      }
                    }
                  }
                delay(delayFade);
                i = i * breakMod;
                }
              for(int i = 255; i == 0; i--)
              {
                analogWrite(r, i);
                if (irrecv.decode(&results))
                {
                  int currentV = results.value;
                  irrecv.resume();
                  if(currentV == pilotEQ)
                  {
                    breakMod = 200;
                    resetMode = 1;
                    }
                  if(currentV == pilotPlus)
                  {
                    delayFade = delayFade + 5;
                    }
                  if(currentV == pilotMinus)
                  {
                    delayFade = delayFade - 5;
                    if (delayFade < 5)
                    {
                      delayFade = 5;
                      digitalWrite(r, HIGH);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      delay(500);
                      digitalWrite(r, LOW);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      }
                    }
                  }
                delay(delayFade);
                i = i * breakMod;
                }
              for(int i = 255; i == 0; i--)
              {
                analogWrite(g, i);
                if (irrecv.decode(&results))
                {
                  int currentV = results.value;
                  irrecv.resume();
                  if(currentV == pilotEQ)
                  {
                    breakMod = 200;
                    resetMode = 1;
                    }
                  if(currentV == pilotPlus)
                  {
                    delayFade = delayFade + 5;
                    }
                  if(currentV == pilotMinus)
                  {
                    delayFade = delayFade - 5;
                    if (delayFade < 5)
                    {
                      delayFade = 5;
                      digitalWrite(r, HIGH);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      delay(500);
                      digitalWrite(r, LOW);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      }
                    }
                  }
                delay(delayFade);
                i = i * breakMod;
                }
              for(int i = 255; i == 0; i--)
              {
                analogWrite(b, i);
                if (irrecv.decode(&results))
                {
                  int currentV = results.value;
                  irrecv.resume();
                  if(currentV == pilotEQ)
                  {
                    breakMod = 200;
                    resetMode = 1;
                    }
                  if(currentV == pilotPlus)
                  {
                    delayFade = delayFade + 5;
                    }
                  if(currentV == pilotMinus)
                  {
                    delayFade = delayFade - 5;
                    if (delayFade < 5)
                    {
                      delayFade = 5;
                      digitalWrite(r, HIGH);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      delay(500);
                      digitalWrite(r, LOW);
                      digitalWrite(g, LOW);
                      digitalWrite(b, LOW);
                      }
                    }
                  }
                delay(delayFade);
                i = i * breakMod;
                }
                if(breakMod > 1)
                {
                  delay(500);
                  }
                breakMod = 1;
                break;
              default:// -----------------------------------------------------------------def---------------------------------------
              digitalWrite(r, HIGH);
               digitalWrite(g, LOW);
               digitalWrite(b, LOW);
               delay(200);
               break;
           }}
         modeRGB = modeRGBFix;
         if (resetMode == 1)
         {
            modeRGB = 0;
            resetMode = 0;
            modeRGBFix = 0;
            displayZero();
            delay(1000);
         }
             digitalWrite(r, LOW);
             digitalWrite(g, LOW);
             digitalWrite(b, LOW);
}
