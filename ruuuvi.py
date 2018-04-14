from ruuvitag_sensor.ruuvitag import RuuviTag
import threading
from time import gmtime, strftime
#D31FACAA0C9E
sensor = RuuviTag('D1:98:7E:8C:B4:5B')

temp=[]
pres=[]
acc=[]
time=[]

##def requestRuuvi():
##    threading.Timer(3,requestRuuvi).start()

for i in range(0,10):    
    # update state from the device
    state = sensor.update()

    # get latest state (does not get it from the device)
    state = sensor.state
    time.append(strftime("%Y-%m-%d %H:%M:%S",gmtime()))
    temp.append(state['temperature'])
    pres.append(state['pressure'])
    acc.append(state['acceleration'])

    print(strftime("%Y-%m-%d %H:%M:%S",gmtime()))
    print(state['temperature'])
    print(state['pressure'])
    print(state['acceleration'])
    

    i=i+1
print("Average temperature: "+str(sum(temp)/float(len(temp)))+"ºC")
print("Average pressure: "+str(sum(pres)/float(len(pres)))+" mbar")
print("Average acceleration: "+str(sum(acc)/float(len(acc)))+" ?")

##requestRuuvi()

