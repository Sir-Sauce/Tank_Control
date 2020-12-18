int ledPin [] = {2, 3, 4, 5, 6, 7, 8, 9};
int buzPin = 10;
int butPin = 12;

int addata;
int fillSet = 1;
int lastFillSet = 6;


unsigned long previousTime = 0;
unsigned long previousTime2 = 0;
unsigned long currentTime = 0;
unsigned long currentTime2 = 0;
unsigned long counter = 0;
unsigned long counter2 = 1;
char serialData;
boolean buzzOp = false;

int WarningFlag = 2;
int HeightFlag = 3;
int DispenseState = 9;


#define WarningHigh 0;
#define WarningLow 1;
#define WarningOff 2;
#define TankEmpty 3;
#define Tank20 4;
#define Tank40 5;
#define Tank60 6;
#define Tank80 7;
#define Tank100 8;
#define DispenseOff 9;
#define DispenseOn 10;


void setup() {
  Serial.begin(38400);                    //initializes serial communication
  for (int i = 0; i < 8; i++) {
    pinMode(ledPin[i], OUTPUT);           //initializing all ledPins as OUTPUT
    for (int i = 0; i < 8; i++) {
      digitalWrite(ledPin[i], LOW);
    }
  }
}

void loop() {
  currentTime = millis();                           //Start Timer
  currentTime2 = millis();
  Timer_Counter();                                  //Timer & Counter for Dispense LED blink
  Timer_Counter2();
  delay(10);










  //potentiometer code - discretizes readout into 5 unique values
  
  //Serial.println(addata);
  //Serial.println(fillSet);
  //Serial.println(lastFillSet);  
  
  addata = analogRead(0);
  fillSet = map(addata, 0 ,1023, 1, 5);         //5 and 4 will equal same serial byte

  FillSetting();
 
  
 

  



  if (Serial.available() > 0) {          //Waiting State - Checks for serial data
    serialData = Serial.read();          //Gets Task command from python
    if (serialData == '0') {
      SetWarning();
    }
    else if (serialData == '1') {
      HeightIndicator();
    }
    else if (serialData == '2') {
      SetDispenseState();
    }
    else if (serialData == '3') {
      tone(10, 392, 3000);
      //      currentTime2 = millis();
      //      previousTime2 = currentTime2;
      //      digitalWrite(buzPin, HIGH);

    }
    else if (serialData == '4') {
      buzzOp = true;
      counter2 = 1;
    }

    else { }
  }
  DispenseIndicator();


  //Serial.print(buzzOp); Serial.println(" buzzer state");
  //Serial.println(counter2);
  if (buzzOp == true) {
    if (counter2 % 2 == 0) {
      tone(10, 392);
    }
    else {
      noTone(10);
    }
  }

}


//void FillSetting() {    //sends serial byte to python
//    //delay(150);
//    if (lastFillSet != fillSet){
//      if(fillSet == 1){
//        Serial.write(1);
//      }
//      else if (fillSet == 2){
//        Serial.write(3);
//      }
//      else if (fillSet == 3){
//        Serial.write(3);
//      }
//      else if (fillSet == 4){
//        Serial.write(4);
//      }
//      else {
//        Serial.write(4);
//      }
//    lastFillSet = fillSet;
//    }
//    }


void FillSetting() {                  //sends serial byte to python
    if (lastFillSet != fillSet){
      switch(fillSet) {
        case 1:
          Serial.write(1);
          lastFillSet = 1;
          break;
        case 2:
          Serial.write(2);
          lastFillSet = 2;
          break;
        case 3:
          Serial.write(3);
          lastFillSet = 3;
          break;
        case 4:
          Serial.write(4);
          lastFillSet = 4;
          break;
        case 5:
          Serial.write(4);
          lastFillSet = 5;
          break;
        }
        fillSet = lastFillSet; 
       } 
    }








void SetWarning() {
  serialData = Serial.read();
  switch (serialData) {            //Switch case for warning state
    case '0':                         //High level warning
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
      break;
    case '1':                         //low level warning
      digitalWrite(7, HIGH);
      digitalWrite(8, LOW);
      break;
    case '2':                         //nominal tank level
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
      break;
  }
}










void HeightIndicator() {
  serialData = Serial.read();
  switch (serialData) {             //Switch case for warning state
    case '0':                         //Tank 0%
      for (int i = 0; i < 5; i++) {
        digitalWrite(ledPin[i], LOW);
      }
      break;

    case '1':                         //Tank <20%
      digitalWrite(2, HIGH);
      digitalWrite(3, LOW);
      break;

    case '2':                         //Tank <40%
      digitalWrite(3, HIGH);
      digitalWrite(4, LOW);
      break;

    case '3':                         //Tank <60%
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
      digitalWrite(4, HIGH);
      digitalWrite(5, LOW);
      break;

    case '4':                         //Tank <80%
      digitalWrite(5, HIGH);
      digitalWrite(6, LOW);
      break;

    case '5':                         //Tank >= 80%
      for (int i = 0; i < 5; i++) {
        digitalWrite(ledPin[i], HIGH);
      }
      break;
  }
}


void SetDispenseState() {
  serialData = Serial.read();
  switch (serialData) {
    case '0':
      DispenseState = DispenseOff;
    case '1':
      DispenseState = DispenseOn;
  }
}








void DispenseIndicator() {
  //Serial.println(DispenseState);
  if (DispenseState == 10 && counter == 0) {           //Switch case for dispense state
    digitalWrite(9, LOW);                                   //LED blink Off
  }
  else if (DispenseState == 10 && counter == 1) {           //LED blink On
    digitalWrite(9, HIGH);
  }
  else {
    digitalWrite(9, LOW);                                   //LED Off
  }
  if (counter == 2) {
    counter = 0;
  }
}











void Timer_Counter() {
  if ((currentTime - previousTime) >= 1000) {      
    counter++;
    previousTime = currentTime;
  }
}
void Timer_Counter2() {
  if ((currentTime2 - previousTime2) >= 400) {      
    counter2++;
    previousTime2 = currentTime2;
  }
  if (counter2 >= 9) {
    buzzOp = false;
    counter2 = 1;
    noTone(10);
    //return buzzOp;
  }
}
