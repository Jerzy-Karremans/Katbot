from src.lcd import LCD
import src.speechEngine as se
from src.button import Button,pushDuration
import time
import multiprocessing
from pydub import AudioSegment
from pydub.playback import play



if __name__ == '__main__':
    lcd = LCD() 
    bt = Button(21)
    lcd.network_check_screen()
    while True:
        lcd.display_main_screen()
        Duration = bt.get_press()
        if Duration == pushDuration.ShortPush:
            lcd.message("KatBot running\n try saying hi!",2)
            introAudio = AudioSegment.from_wav("./fixtures/introduction.wav")
            play(introAudio)
            p1 = multiprocessing.Process(target=se.main)
            p2 = multiprocessing.Process(target=bt.get_press)
            p2.start()
            p1.start()
            p2.join()
            p1.kill()
        elif Duration == pushDuration.reset:
            break
        time.sleep(0.1)
    lcd.clear()
    lcd.message("Program exited\nrestart pi",2)