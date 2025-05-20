import threading
import time
import os
from playsound import playsound

alarm_thread = None
alarm_active = False

def _play_alarm():
    global alarm_active
    while alarm_active:
        playsound("alarms/alarm.wav")  
        time.sleep(1)

def start_alarm():
    global alarm_thread, alarm_active
    if not alarm_active:
        alarm_active = True
        alarm_thread = threading.Thread(target=_play_alarm)
        alarm_thread.daemon = True
        alarm_thread.start()

def stop_alarm():
    global alarm_active
    alarm_active = False
