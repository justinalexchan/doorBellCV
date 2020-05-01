
const int buzzer = 9; //buzzer to arduino pin 9
char input = '0';
int trigger = 0;
void setup() 
{
  Serial.begin(9600);
  pinMode(buzzer, OUTPUT); // Set buzzer - pin 9 as an output
}

void loop() 
{
  if(Serial.available() > 0)
  {
    input = Serial.read();

    if(input == '1' && trigger == 0)
    {
        tone(buzzer, 1000); 
        delay(500);
        noTone(buzzer);
        delay(500);
        tone(buzzer, 1000); 
        delay(500);
        noTone(buzzer);
        trigger = 1;
    }
    if(input == '0'){
        noTone(buzzer);  
        trigger = 0;
    }
  }  
}
