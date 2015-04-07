import re

class TempSensor:

  def __init__(self, id):
    self.id = id
    self.value = None 
    self.read()

  def read(self):
    f = open('/sys/bus/w1/devices/%s/w1_slave' % self.id, 'rt')
    self.value = f.read()
    f.close()	

  def temp(self):
    return float(re.match('.*crc=.. YES.*t=([0-9]+).*',self.value,re.S).group(1))/1000


WaterTemp = TempSensor('28-021463ed2cff')

print WaterTemp.temp() 
