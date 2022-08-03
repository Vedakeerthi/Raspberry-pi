import RPi.GPIO as GPIO
pir = 29
GPIO.setwarnings(False)
GPIO.setmode(GPIO.board)
GPIO.setup(pir,GPIO.IN)
while True:
    if(GPIO.input(pir)):
        print("Motion detected")
    else:
        print("No motion detected")