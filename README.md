# Raspberry-pi


## Table of Content
  * [Room temperature](#room_temperature)
  * [Motion detection](#motion_detection)
  * [Sound detection](#sound_detection)
  * [Requirements](#requirements)
  * [License](#license)
  * [Technology Used](#technology_used)

## Room temperature <a href='room_temperature'></a>

The adafruit library is required for detecting the temperature and humidity, so the module is imported, then in an infinite loop the values of the temperature and the humidity are read from the functions of the module, if both the inputs are not none then the value of the temperature and the humidity are printed else it is printed as no input.

## Motion detection <a href='motion_detection'></a>

Motion detection algorithm works on the basis of detecting the heat waves on the body, which is used to detect the motion of the body, here RPi module is used to detect the motion of the body, then the mode of the board, the setup of the pin at pin 29, then an infinite loop is made to run to detect the motion, if there is an input in the pin, then there is motion, else there is no motion.

## Sound detection <a href='sound_detection'></a>

Sound detection is very similar to motion detection since the same Rpi module is used to find the sound waves, initially the board is set and the pins of the board are set, the input and the output pins, then if the input pin is true and the output pin is tends to false then there is no sound waves, and if the input pin in false and output pin is tends to be true, then there is a sound wave detected.

## Requirements

  * Raspberry-pi 3
  * Python 
  * Linux operating system
  * Breadboard, jumper wires and other components required to build a circuit.
  
## License

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/Vedakeerthi/FLIGHT_FARE_PREDICTION/blob/main/LICENSE)

## Technology Used <a name='technology_used'></a>

<a href="https://www.raspberrypi.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/raspberrypi/raspberrypi-ar21.svg" alt="raspberry-pi" width="70" height="50"/> </a>
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> &nbsp;
