# Source: https://ozzmaker.com/using-python-with-a-gps-receiver-on-a-raspberry-pi/

from gps import *
import time
    
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE) 
print("latitude\t longitude       time utc\t\t\t altitude\t epv\t\t ept\t speed\t climb")
   
while True:

	report = gpsd.next() #
	if report["class"] == "TPV":

		print(getattr(report,"lat",0.0),"\t", getattr(report,"lon",0.0),"\t",
		      getattr(report,"time",""),"\t", getattr(report,"alt","nan"),"\t",
		      getattr(report,"epv","nan"),"\t", getattr(report,"ept","nan"),"\t",
		      getattr(report,"speed","nan"),"\t", getattr(report,"climb","nan"),"\t")

	time.sleep(1)