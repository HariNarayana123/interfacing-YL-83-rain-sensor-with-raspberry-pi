Import spidev
Import time
Spi=spidev.SpiDev()
Spi.open(0,0)

channel=0
vref=3.3v

def read_adc(channel):
      adc =spi.xfer2([1,(8+channel)<<4,0])
      data=((adc[1] & ob11) <<8) + adc[2])
       voltage= (adc_value * vref) / 1023.0
       return round(voltage,2)

def check_rainfall():
     voltage = read_adc(channel)
     if (voltage> Dry_voltage-Rain_threshold ):
           return False
    elif (voltage < wet_voltage+Rain_threshold ):
          return True
    else:
         return None
     
while True:
     res=check_rainfall()
     time.sleep(0.5)
spi.close()
