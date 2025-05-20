import time
from alarms.alarm import start_alarm, stop_alarm  # adjust if path differs

print("Starting alarm for 5 seconds...")
start_alarm()

time.sleep(5)  # Let the alarm play for 5 seconds

print("Stopping alarm.")
stop_alarm()

time.sleep(2)  # Give time for the thread to cleanly stop
print("Done.")
