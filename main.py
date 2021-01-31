import RPi.GPIO as GPIO
from RPLCD import CharLCD

GPIO.setmode(GPIO.BOARD)

lcd = CharLCD(cols=12, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD)


def writeToLCD(text):
    lcd.write_string(text)


writeToLCD('External variable')
