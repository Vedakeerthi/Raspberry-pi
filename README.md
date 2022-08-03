# Raspberry-pi

### Room temperature

The adafruit library is required for detecting the temperature and humidity, so the module is imported, then in an infinite loop the values of the temperature and the humidity are read from the functions of the module, if both the inputs are not none then the value of the temperature and the humidity are printed else it is printed as no input.

### Motion detection

Motion detection algorithm works on the basis of detecting the heat waves on the body, which is used to detect the motion of the body, here RPi module is used to detect the motion of the body, then the mode of the board, the setup of the pin at pin 29, then an infinite loop is made to run to detect the motion, if there is an input in the pin, then there is motion, else there is no motion.

### Sound detection

Sound detection is very similar to motion detection since the same Rpi module is used to find the sound waves, initially the board is set and the pins of the board are set, the input and the output pins, then if the input pin is true and the output pin is tends to false then there is no sound waves, and if the input pin in false and output pin is tends to be true, then there is a sound wave detected.
