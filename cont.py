import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Output:
		
  def __init__(self,pin,rev=True, initial = None):
    self.pin = pin
    self.rev = True 
    #if GPIO.gpio_function(self.pin) != GPIO.OUT:
    self.setup(initial)   
    
  def setup(self, initial=None):
    GPIO.setup(self.pin, GPIO.OUT)
    if initial!=None:
      self.set(initial)  		

  def set(self, value):
    GPIO.output(self.pin, self.rev^value)

  def on(self):
    self.set(self.rev^False)

  def off(self):
    self.set(self.rev^True) 

class Output2v:

  def __init__(self, pin_on, pin_off):
    self.ono = Output(pin_on, initial=None)
    self.offo = Output(pin_off, initial=None)

  def set(self, value):
    self.ono.set(value)
    self.offo.set(not value)

  def on(self):
     self.set(True)

  def off(self):
     self.set(False) 

