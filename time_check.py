from time import sleep
from datetime import datetime

while True:
    now = datetime.now()
    sleep(1)
    later = datetime.now()
    print(later - now)
