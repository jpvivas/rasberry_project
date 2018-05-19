#!/usr/bin/env python
import os
import sys
#import spi
#import signal
#import time


#def end_read(signal,frame):
    #global continue_reading
    #print ("Ctrl+C captured, ending read.")
    #continue_reading = False
    #GPIO.cleanup()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rasberry_project.settings")
    try:
        from django.core.management import execute_from_command_line
        #signal.signal(signal.SIGINT, end_read)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
