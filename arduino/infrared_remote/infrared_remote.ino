int receiverpin = 2;
#include <IRremote.h>
IRrecv irrecv(receiverpin);
decode_results results;

void setup() {
 Serial.begin(9600);
 irrecv.enableIRIn();
}

void loop() {
  if(irrecv.decode(&results))
  {
    Serial.print(results.value);
    Serial.println(" ");
    irrecv.resume();
    }
}
