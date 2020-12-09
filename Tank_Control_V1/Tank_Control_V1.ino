int ledPin [] = {2, 3, 4, 5, 6, 7, 8, 9};
int buzPin = 10;
int butPin = 12;

unsigned long previousTime = 0;
unsigned long previousTime2 = 0;
unsigned long currentTime = 0;
unsigned long counter = 0;
//unsigned long counter2 = 0;
char serialData;
int SerialData;
//int Task1State = 0;
//int Task2State = 0;
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
  Serial.begin(38400);                //initializes serial communication
  for (int i = 0; i < 8; i++) {
    pinMode(ledPin[i], OUTPUT);     //initializing all ledPins as OUTPUT
    for (int i = 0; i < 8; i++) {
      digitalWrite(ledPin[i], LOW);
    }
  }
}

void loop() {
  currentTime = millis();                           //Start Timer
  Timer_Counter();                                  //Timer & Counter for Dispense LED blink
  delay(100);


  if (Serial.available() > 0) {          //Waiting State - Checks for serial data
    serialData = Serial.read();          //Gets Task command from python
    Serial.print(serialData); Serial.println(" Serial Data Received");
    SerialData = int(serialData);
    Serial.println(SerialData);
    if (SerialData <= 2) {
      Serial.println(SerialData);
      switch (serialData) {             //Switch case for warning state
        case 0:                         //High level warning
          Serial.println("test");
          digitalWrite(7, HIGH);
          digitalWrite(8, HIGH);
          break;
        case 1:                         //low level warning
          digitalWrite(7, HIGH);
          digitalWrite(8, LOW);
          break;
        case 2:                         //nominal tank level
          digitalWrite(7, LOW);
          digitalWrite(8, LOW);
          break;
    }
    }
  }
}


    //    switch (serialData) {             //Sets Task State based on serial data
    //      case 0:
    //        //WarningFlag = WarningHigh;
    //        SetWarning(0);
    //        break;
    //      case 1:
    //        WarningFlag = WarningLow;
    //        break;
    //      case 2:
    //        WarningFlag = WarningOff;
    //        break;
    //        //      case 3:
    //        //        HeightFlag = TankEmpty;
    //        //        break;
    //        //      case 4:
    //        //        HeightFlag = Tank20;
    //        //        break;
    //        //      case 5:
    //        //        HeightFlag = Tank40;
    //        //        break;
    //        //      case 6:
    //        //        HeightFlag = Tank60;
    //        //        break;
    //        //      case 7:
    //        //        HeightFlag = Tank80;
    //        //        break;
    //        //      case 8:
    //        //        HeightFlag = Tank100;
    //        //        break;
    //        //      case 9:
    //        //        DispenseState = DispenseOff;
    //        //        break;
    //        //      case 10:
    //        //        DispenseState = DispenseOn;
    //        //        break;
    //    }
    //    //Serial.print(DispenseState); Serial.println(" test");
    //    //SetWarning();
    //    //HeightIndicator();
    //  }
    //DispenseIndicator();
    //This is where button and potentiometer logic go
//
//
//void SetWarning(int WarningFlag) {
//  Serial.print(WarningFlag); Serial.println(" warning case");
//  switch (WarningFlag) {            //Switch case for warning state
//    case 0:                         //High level warning
//      digitalWrite(7, HIGH);
//      digitalWrite(8, HIGH);
//      break;
//    case 1:                         //low level warning
//      digitalWrite(7, HIGH);
//      break;
//    case 2:                         //nominal tank level
//      digitalWrite(7, LOW);
//      digitalWrite(8, LOW);
//      break;
//  }
//}
//
//void HeightIndicator() {
//  switch (HeightFlag) {             //Switch case for warning state
//    case 3:                         //Tank 0%
//      for (int i = 0; i < 5; i++) {
//        digitalWrite(ledPin[i], LOW);
//      }
//      break;
//
//    case 4:                         //Tank <20%
//      digitalWrite(2, HIGH);
//      digitalWrite(3, LOW);
//      break;
//
//    case 5:                         //Tank <40%
//      digitalWrite(3, HIGH);
//      digitalWrite(4, LOW);
//      break;
//
//    case 6:                         //Tank <60%
//      digitalWrite(2, HIGH);
//      digitalWrite(3, HIGH);
//      digitalWrite(4, HIGH);
//      digitalWrite(5, LOW);
//      break;
//
//    case 7:                         //Tank <80%
//      digitalWrite(5, HIGH);
//      digitalWrite(6, LOW);
//      break;
//
//    case 8:                         //Tank >= 80%
//      for (int i = 0; i < 5; i++) {
//        digitalWrite(ledPin[i], HIGH);
//      }
//      break;
//
//  }
//}
//void DispenseIndicator() {
//  //Serial.println(counter);
//  Serial.println(DispenseState);
//  if (DispenseState == 10 && counter == 0) {           //Switch case for dispense state
//    digitalWrite(9, LOW);                                   //LED blink Off
//  }
//  else if (DispenseState == 10 && counter == 1) {           //LED blink On
//    digitalWrite(9, HIGH);
//  }
//  else {
//    digitalWrite(9, LOW);                                   //LED Off
//  }
//  if (counter == 2) {
//    counter = 0;
//  }
//}

void Timer_Counter() {
  if ((currentTime - previousTime) >= 1000) {      //Sets Task2 counter
    counter++;
    previousTime = currentTime;
  }
}
