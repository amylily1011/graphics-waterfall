# Single Pin control of IO Pi board mcp23017 on address 0x20 and 0x21  ( AB Electronics IO Pi )
# run using sudo python singlepin.py
import wiringpi2
import time
import timeit
from pylab import*

pin_base = 65
i2c_addr = 0x20
i2c_addr_2 = 0x21
wiringpi2.wiringPiSetup()
wiringpi2.mcp23017Setup(pin_base,i2c_addr)
wiringpi2.mcp23017Setup(pin_base+16,i2c_addr_2)

# reset all pins as outputs and turn off
for pin in range(65,97):
    wiringpi2.pinMode(pin,1)
    wiringpi2.digitalWrite(pin,0)

inputt = raw_input('type something\n')
for i in range(0,len(inputt)):
	path='./TextfileWF/'+str.upper(inputt[i])
	print(str.upper(inputt[i]))
    x=file(path,'r+',255);
    a=x.readlines(255);
    flip_a= flipud(a);
    
    starttime = time.time()
    for i in range(0,len(a)):
        pin=65;
        for j in flip_a[i]:
            if j!='\n':
                wiringpi2.digitalWrite(pin,(int(j)))
            pin+=1;
        wiringpi2.delay(65)
    for pin in range(65,97):
        wiringpi2.digitalWrite(pin,0)
    wiringpi2.delay(800)

stoptime = time.time()
runtime = timeit.timeit(number=1)
print stoptime - starttime
print runtime
