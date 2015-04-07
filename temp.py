import re

class TempSensor:

  def __init__(self, id, local=False):
    self.id = id
    self.value = None
    self.local = local 
    self.read()

  def read(self):
    if self.local:
      f = open('/home/pi/%s.txt' % self.id, 'rt')
    else:
      f = open('/sys/bus/w1/devices/%s/w1_slave' % self.id, 'rt')
    self.value = f.read()
    f.close()	

  def temp(self):
    return float(re.match('.*crc=.. YES.*t=([0-9]+).*',self.value,re.S).group(1))/1000

