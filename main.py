import RPi.GPIO as GPIO
from RPLCD import CharLCD

GPIO.setmode(GPIO.BOARD)

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD)
backslash = (0b00000,0b10000,0b01000,0b00100,0b00010,0b00001,0b00000,0b00000)
lcd.create_char(0,backslash)

def writeToLCD(text):
    lcd.clear()
    lcd.write_string(text)


writeToLCD(' o_ ....     _o /\x00 GAMING     /\x00')
