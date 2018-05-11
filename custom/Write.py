import RPi.GPIO as GPIO
from pi_rc522.pirc522.rfid import RFID


reader = RFID()
try:
        text = 'jpvivas'
        print("Ahora coloca tu tarjeta para escribir")
        reader.write(text)
        print("Usuario inscrito")
finally:
        GPIO.cleanup()
