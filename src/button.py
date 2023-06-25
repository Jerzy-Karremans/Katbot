import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
from enum import Enum

class pushDuration(Enum):
    reset = 3
    LongPush = 2
    ShortPush = 1
    NoPush = 0
    
class Button:
    def __init__(self, button_pin):
        self.button_pin = button_pin
        self.is_pushed = False
        self.time_last_pushed = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def get_press(self):
        while True:
            button_state = GPIO.input(self.button_pin)
            if not self.is_pushed and button_state == GPIO.HIGH:
                self.is_pushed = True
                self.time_last_pushed = time.time()
            elif button_state == GPIO.LOW:
                if self.is_pushed:
                    self.is_pushed = False
                    push_duration = time.time() - self.time_last_pushed
                    if push_duration > 0.5:
                        return pushDuration.LongPush
                    else:
                        return pushDuration.ShortPush
                self.is_pushed = False
            elif time.time() - self.time_last_pushed > 2.5:
                return pushDuration.reset
            time.sleep(0.1)  # Delay to avoid excessive CPU usage
    
if __name__ == '__main__':
    button = Button(21)
    while True:
        Duration = button.update()
        if Duration == pushDuration.ShortPush:
            print("short press")
        elif Duration == pushDuration.LongPush:
            print("long press")
        elif Duration == pushDuration.reset:
            break