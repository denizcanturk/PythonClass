#pip install pywhatkit
# If not installed already...

import pywhatkit as kit
import datetime as dt
import time as t

while(True):
    now = dt.datetime.now()
    print(now)
    try:
        kit.sendwhatmsg()
        kit.sendwhatmsg("+5316774317", "These guys are scammer! They will steall your money! Stay Off.  ", now.hour, now.minute, 1,False,2)

    except Exception as e:
        print(str(e))
        print("Not This Time... ")

    print("Waiting for some time... >:)")
    t.sleep(0.5)