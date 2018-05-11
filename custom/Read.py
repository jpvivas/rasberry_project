import RPi.GPIO as GPIO
#import SimpleMFRC522
from pi_rc522.pirc522.rfid import RFID
#reader = SimpleMFRC522.SimpleMFRC522()

reader = RFID()

try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()
