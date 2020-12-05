int ledPin [] = {2,3,4,5,6,7,8,9};
int buzPin = 10;
int butPin = 12;

unsigned long previousTime = 0;
unsigned long previousTime2 = 0;
unsigned long currentTime = 0;
//unsigned long counter = 0;
//unsigned long counter2 = 0;
char serialData;
//int Task1State = 0;
//int Task2State = 0;
int WarningFlag = 2;

#define WarningHigh 0;
#define WarningLow 1;
#define WarningOff 2;

void setup() {
  Serial.begin(38400);                //initializes serial communication
  for (int i =0;i < 8; i++) {
      pinMode(ledPin[i], OUTPUT);     //initializing all ledPins as OUTPUT
  }
}

void loop() {
  currentTime = millis();                           //Start Timer
  //Timer_Counter();

  if(Serial.available() > 0) {      //Waiting State - Checks for serial data
    serialData = Serial.read();     //Gets Task command from python
  }
  switch (serialData) {             //Sets Task State based on serial data
    case '0':
      WarningFlag = WarningHigh;
      break;
    case '1':
      WarningFlag = WarningLow;
      break;
    case '2':
      WarningFlag = WarningOff;
      break;
  }
   SetWarning();
}



//void Timer_Counter() {
//  if((currentTime - previousTime)>=2000){           //Sets Task1 counter
//    counter++;
//    previousTime = currentTime;
//  }
//  
//  if((currentTime - previousTime2)>=3000){          //Sets Task2 counter
//    counter2++;
//    previousTime2 = currentTime;
//    if(counter2 >= 4){
//      counter2 = 1;
//    }
//  }
//}

void SetWarning() {
  switch (WarningFlag) {             //Task 1 Timing
    case 0:                         //Task 1 State On
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
    case 1:                         //Task 1 State Off
      digitalWrite(7, HIGH);
    case 2:
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
  }
}
 
