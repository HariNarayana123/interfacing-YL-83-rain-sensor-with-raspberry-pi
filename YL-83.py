Import spidev
Import time
Spi=spidev.SpiDev()
Spi.open(0,0)

channel=1
vref=3.3v

Dry_voltage=3.3  #close to supply voltage when there is no rainfall
wet_volatge=1.5  # when sensor get resistance decreases, so voltage decreases
Rain_threshold=0.5

def read_adc(channel):
      adc =spi.xfer2([1,(8+channel)<<4,0])
      data=((adc[1] & ob11) <<8) + adc[2])
      voltage= (adc_value * vref) / 1023.0
      # Calculate rainfall in mm/hour (adjust calibration factor as needed)
      calibration_factor =1.0
      rainfall= voltage / calibration_factor
      return round(rainfall,2)

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
     if(res == True):
            rainfall = read_adc(channel)
            print("rainfall is: %.2f mm/hour" % rainfall)
     elif(res == False):
             print("There is no rainfall")
     else:       
          print("unable to predict")  
     time.sleep(1)
spi.close()
