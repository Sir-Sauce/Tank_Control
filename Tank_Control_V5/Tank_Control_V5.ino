int ledPin [] = {2, 3, 4, 5, 6, 7, 8, 9};
int buzPin = 10;
int butPin = 12;
int WarningFlag = 2;
int HeightFlag = 3;
int SerialReadCount = 0;

int addata;
int fillSet = 1;
int lastFillSet = 6;

//int ButtonOn = 0;          

unsigned long previousTime = 0;
unsigned long previousTime2 = 0;
unsigned long currentTime = 0;
unsigned long currentTime2 = 0;
unsigned long counter = 0;
unsigned long counter2 = 1;
char serialData;
boolean buzzOp = false;
boolean DispenseOn = false;



// State1; //Next_State1;
//byte State2, Next_State2;
//byte State3, Next_State3;
//byte State4, Next_State4;
//byte State5, Next_State5;


#define StartState 1
#define InState 2
#define MidState 3
#define OutState 4
#define MoveState 5


#define WarningHigh 0
#define WarningLow 1
#define WarningOff 2
#define TankEmpty 3
#define Tank20 4
#define Tank40 5
#define Tank60 6
#define Tank80 7
#define Tank100 8


byte State1;
//byte State2 = StartState;
//byte State3 = StartState;
//byte State4 = StartState;
//byte State5 = StartState;

byte Next_State1;

void setup() {
  Serial.begin(38400);                    //initializes serial communication

  byte Next_State1 = StartState;


  pinMode(12, INPUT_PULLUP);

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
  serialData = '0';

  //potentiometer code - discretizes readout into 5 unique values

  //Serial.println(addata);
  //Serial.println(fillSet);
  //Serial.println(lastFillSet);

  addata = analogRead(0);
  fillSet = map(addata, 0 , 1023, 1, 5);        //5 and 4 will equal same serial byte

  FillSetting();


//  if (ButtonOn == 0) {
//    if (digitalRead(12) == LOW) {
//      ButtonOn = 1;
//      Serial.write(7);
//    }
//  }
//    else if (ButtonOn == 1) {
//      if (digitalRead(12) == HIGH){
//        ButtonOn = 0;
//        Serial.write(8);
//      }
//  }


  if (digitalRead(12) == HIGH) {
    delay(10);
    //Serial.println("Dispense Button Activated");
    Serial.write(7);
  }


  if (Serial.available() > 0) {          //Waiting State - Checks for serial data
    serialData = Serial.read();          //Gets Task command from python

    switch (serialData) {            //Switch case for warning state
      case '1':
        HeightIndicator();
        break;
      case '2':
        SetDispenseState();
        break;
      case '3':
        tone(10, 392, 12000);
        break;
      case '4':
        buzzOp = true;
        counter2 = 1;
        break;
      case '5':                         //High level warning
        digitalWrite(7, HIGH);
        digitalWrite(8, HIGH);
        break;
      case '6':                         //low level warning
        digitalWrite(7, HIGH);
        digitalWrite(8, LOW);
        break;
      case '7':                         //nominal tank level
        digitalWrite(7, LOW);
        digitalWrite(8, LOW);
        break;

    }
  }

  if (DispenseOn == true) {

  }

  DispenseIndicator();

  if (buzzOp == true) {
    if (counter2 % 2 == 0) {
      tone(10, 392);
    }
    else {
      noTone(10);
    }
  }
}



void FillSetting() {                  //sends serial byte to python
  if (lastFillSet != fillSet) {
    switch (fillSet) {
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













//### ---  Tank Height Warning --- ###
void SetWarning() {

  serialData = Serial.read();
  switch (serialData) {            //Switch case for warning state
    case '5':                         //High level warning
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
      break;
    case '6':                         //low level warning
      digitalWrite(7, HIGH);
      digitalWrite(8, LOW);
      break;
    case '7':                         //nominal tank level
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
      break;

  }
}



//### --- Tank Level Indicator --- ###
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
      DispenseOn = false;
      //Serial.println("Dispense OFF");
      break;
    case '1':
      DispenseOn = true;
      //Serial.println("Dispense ON");
      break;
  }
}

void DispenseIndicator() {
  //Serial.println(DispenseState);
  if (DispenseOn == true && counter == 0) {           //Switch case for dispense state
    digitalWrite(9, LOW);                                   //LED blink Off
  }
  else if (DispenseOn == true && counter == 1) {           //LED blink On
    digitalWrite(9, HIGH);
  }
  else if (DispenseOn == false || counter == 2) {
    digitalWrite(9, LOW);                                   //LED Off
    counter = 0;
  }
}

void Timer_Counter() {
  if ((currentTime - previousTime) >= 1000) {      //Sets Task2 counter
    counter++;
    previousTime = currentTime;
  }
}
void Timer_Counter2() {
  if ((currentTime2 - previousTime2) >= 400) {      //Sets Task2 counter
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
