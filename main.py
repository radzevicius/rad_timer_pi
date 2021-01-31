import RPi.GPIO as GPIO
from RPLCD import CharLCD
import time

GPIO.setmode(GPIO.BOARD)

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD)
backslash = (0b00000,0b10000,0b01000,0b00100,0b00010,0b00001,0b00000,0b00000)
lcd.create_char(0,backslash)

gaming_animation = (' o_          _o /\x00   GAMING   /\x00',
                    ' o_.         _o /\x00   GAMING   /\x00',
                    ' o_  .       _o /\x00   GAMING   /\x00',
                    ' o_    .     _o /\x00   GAMING   /\x00',
                    ' o_      .   _o /\x00   GAMING   /\x00',
                    ' o_        . _o /\x00   GAMING   /\x00',
                    ' o_          _* /\x00   GAMING   /\x00',
                    ' o_  .       _\\ /\x00   GAMING   /\x00',
                    '\x00o/             /\x00    YEAH   >->o',
                    '\x00o/             /\x00    YEAH!  >->o',
                    '\x00o/             /\x00   !YEAH!  >->o')

def writeToLCD(text):
    lcd.clear()
    lcd.write_string(text)

def animator(animation, fps):
    sleep_time = 1/fps
    for i in animation:
        time.sleep(sleep_time)
        writeToLCD(animation[i])
    writeToLCD('')


animator(gaming_animation,2)
