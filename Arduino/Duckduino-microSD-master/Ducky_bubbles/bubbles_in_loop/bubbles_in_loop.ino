/*
 * Generated with <3 by Dckuino.js, an open source project !
 */

#include "Keyboard.h"

void typeKey(int key)
{
  Keyboard.press(key);
  delay(50);
  Keyboard.release(key);
}

/* Init function */
void setup()
{

}

/* Unused endless loop */
void loop() {
    // Begining the Keyboard stream
  Keyboard.begin();

  delay(1000);
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  Keyboard.releaseAll();
  delay(100);

/*C:\Windows\System32\Bubbles.scr*/
  
Keyboard.print("C:");
  delay(10);
Keyboard.write(92);
  delay(10);
Keyboard.print("Windows");
  delay(10);
Keyboard.write(92);
  delay(10);
Keyboard.print("System32");
delay(10);
Keyboard.write(92);
  delay(10);
Keyboard.print("Bubbles.scr");
  delay(10);

typeKey(KEY_RETURN);

  // Ending stream
  Keyboard.end();

    delay(3000);
  
  }
