from cont import *
from temp import *
import datetime

now = datetime.datetime.now()
w = now.weekday()
h = float(now.hour)+float(now.minute)/100.0

WaterTemp = TempSensor('28-021463ed2cff')
RoomTemp = TempSensor('28-0214638225ff')
BedRTemp = TempSensor('28-021463eaa0ff', True)
LivingRTemp = TempSensor('28-02146384abff',True)

HeatCont = Output(21)
WaterCont = Output2v(22,23)
NoOp = Output(24)

wt = WaterTemp
sr = RoomTemp
br = BedRTemp
lr = LivingRTemp

wt.name = 'Water Tank'
sr.name = 'Spare Room'
br.name = 'Bedroom'
lr.name = 'Living Room'

#lrt = LivingRoomTemp.temp()
#brt = BedroomTemo.temp()

Water = \
[
[wt,[5,6],[0 ,24],[40.0,40.7]],
[wt,[]   ,[5 , 8],[40.0,40.7]],
[wt,[]   ,[18,22],[40.0,40.7]]
]

Heating = \
[
[br,[   ],[23,    5],[19.0,19.5]],
[br,[5,6],[5 ,    7],[19.0,10.0]],
[lr,[5,6],[7 ,   21],[21.0,21.2]],
[br,[]   ,[ 5.30, 7],[22.0,22.2]],
[lr,[]   ,[18,   21],[21.0,21.2]],
[br,[]   ,[21,   23],[21.0,21.2]],
[lr,[]   ,[18,   24],[21.0,21.2]],
[lr,[]   ,[        ],[20.0,20.2]]
]

log = now.isoformat()+','

log += 'BR' + str(br.temp()) + ','
log += 'LR' + str(lr.temp()) + ','
log += 'SR' + str(sr.temp()) + ','
log += 'WT' + str(wt.temp()) + ','

def check(l,ctrl,code):
  global log
  line = 0
  for s in l:
    line+=1
    for i in s[2:]:
      i.append(None)
      i.append(None)
    ref = s[0].temp()
    name = s[0].name
    wds = s[1]
    hf  = s[2][0]
    ht  = s[2][1]
    tf  = s[3][0]
    tt  = s[3][1]
    
    if w in wds or len(wds)==0 :
      if (hf == None or h>=hf) and (ht == None or h<=ht) : 
        print 'Match in line:', line
        log += code+'l:'+str(line)
        if ref<tf:
          print name, ':', ref, '<', tf
          print 'turning on...'
	  ctrl.on()
          log += 'ON'
        elif ref>tt:
          print name, ':', ref, '>', tt
          print 'turning off...'
          ctrl.off()
          log += 'OFF'
        log += ','
        return 

print 'Water Check', wt.temp()	 	
check(Water,WaterCont,'W')

print 'Heating Check', br.temp() 
check(Heating,HeatCont,'H')

f = open('/home/pi/contlog.log','a+t')
f.write(log+'\n')
f.close()

