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
int HeightFlag = 3;

#define WarningHigh 0;
#define WarningLow 1;
#define WarningOff 2;
#define TankEmpty 3;
#define Tank20 4;
#define Tank40 5;
#define Tank60 6; 
#define Tank80 7; 
#define Tank100 8;


void setup() {
  Serial.begin(38400);                //initializes serial communication
  for (int i =0;i < 8; i++) {
      pinMode(ledPin[i], OUTPUT);     //initializing all ledPins as OUTPUT
  for (int i =0;i < 8; i++) {
      digitalWrite(ledPin[i], LOW);
  }
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
      //break;
    case '1':
      WarningFlag = WarningLow;
      //break;
    case '2':
      WarningFlag = WarningOff;
      //break;
    case '3':
      HeightFlag = TankEmpty;
      //break;
    case '4':
      HeightFlag = Tank20;
      //break;
    case '5':
      HeightFlag = Tank40;
      //break;
    case '6':
      HeightFlag = Tank60;
      //break;
    case '7':
      HeightFlag = Tank80;
      //break;
    case '8':
      HeightFlag = Tank100;
      break;
  }
   SetWarning();
   HeightIndicator();
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
  switch (WarningFlag) {            //Switch case for warning state
    case 0:                         //High level warning
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
    case 1:                         //low level warning
      digitalWrite(7, HIGH);
    case 2:                         //nominal tank level
      digitalWrite(7, LOW);
      digitalWrite(8, LOW);
  }
}

void HeightIndicator() {
  switch (HeightFlag) {             //Switch case for warning state
    case 3:                         //Tank 0%
      for (int i =0;i < 5; i++) {
        digitalWrite(ledPin[i], LOW); 
      }    
    case 4:                         //Tank <20%
      digitalWrite(2, HIGH);
      digitalWrite(3, LOW);
    case 5:                         //Tank <40%
      digitalWrite(3, HIGH);
      digitalWrite(4, LOW);
    case 6:                         //Tank <60%
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
      digitalWrite(4, HIGH);
      digitalWrite(5, LOW);
    case 7:                         //Tank <80%
      digitalWrite(5, HIGH);
      digitalWrite(6, LOW);
    case 8:                         //Tank >= 80%
      for (int i =0;i < 5; i++) {
        digitalWrite(ledPin[i], HIGH); 
      }
  }
}
 
