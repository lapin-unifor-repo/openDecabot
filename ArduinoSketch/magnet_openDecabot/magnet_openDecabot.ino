/*
===============================================================================================================
Based on QMC5883LCompass.h Library XYZ Example Sketch
Learn more at [https://github.com/mprograms/QMC5883LCompass]

Release under the GNU General Public License v3
[https://www.gnu.org/licenses/gpl-3.0.en.html]
===============================================================================================================
*/
#include <QMC5883LCompass.h>
#include <Adafruit_GFX.h>       //tested on version 1.11.10
#include <WEMOS_Matrix_GFX.h>   //tested on version 1.4.0

MLED matrix(7); //set intensity=7 (maximum)

QMC5883LCompass compass;

int x, y = 1500;
int maxX,maxY = 0;
int minX,minY = 6000;
int valueX,valueY = 0;

void setup() {
  //
  matrix.setRotation(2);
  Serial.begin(115200);
  compass.setADDR(0x0D); //check yours with I2Cscanner
  compass.init();
  compass.setSmoothing(5,true);  
  Serial.println("iniciando...");
  matrix.clear();
  matrix.drawLine(2,2,5,2, LED_ON);
  matrix.drawLine(2,2,2,5, LED_ON);
  matrix.drawLine(5,2,5,5, LED_ON);
  matrix.drawLine(5,5,2,5, LED_ON);
  matrix.writeDisplay();
  for(int i=0;i<15;i++){
    compass.read();
    delay(250);
  }
}

void loop() {
  // Read compass values
  compass.read();

  // Return XYZ readings
  x = compass.getX();
  y = compass.getY();
  
  //debug?!
  if(minX==0) minX = maxX;

  if(x!=0){
    if(x>maxX) maxX = x;
    if(x<minX) minX = x;
  }
  if(y!=0){
    if(y>maxY) maxY = y;
    if(y<minY) minY = y;
  }

  Serial.print("| " + (String)minX + "\t" + (String)x + "\t" + (String)maxX + " |");
  Serial.print("| " + (String)minY + "\t" + (String)y + "\t" + (String)maxY + " |");

  //wait values to stabilize before calculus
  if(millis()>4000) valueX = map(x,minX,maxX,7,0);
  if(millis()>4000) valueY = map(y,minY,maxY,7,0);
  
  Serial.print("X: ");
  Serial.print(valueX);
  Serial.print(" Y: ");
  Serial.print(valueY);
  Serial.println();

  matrix.clear();
  //vertical
  matrix.drawLine(valueX,0,valueX,7, LED_ON);
  //horizontal
  matrix.drawLine(0,valueY,7,valueY, LED_ON);
  matrix.writeDisplay();
  delay(250);
}
