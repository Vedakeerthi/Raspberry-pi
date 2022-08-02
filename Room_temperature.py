import Adafruit_DHT
s = Adafruit_DHT.DHT11
p = 4
while True:
    h,t = Adafruit_DHT.read(s,p)
    if h is not None and p is not None:
        print('Humidity : ',h,'Temperature : ',t,'C')
    else:
        print('No input')