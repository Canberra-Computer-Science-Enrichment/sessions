# Single-board computers

Paul Watson

Wikipedia has some good articles on [single-board computers](https://en.wikipedia.org/wiki/Single-board_computer) and [embedded systems](https://en.wikipedia.org/wiki/Embedded_system).

# TinkerCAD

TinkerCAD is a free collection of online tools for designing systems including embedded computing systems.
[Join our class on TinkerCAD](https://www.tinkercad.com/joinclass/ADDH5DTNWR15) using the nickname we give you during this session.

Select [Circuits](https://www.tinkercad.com/dashboard?type=circuits&collection=designs) and then [Try Circuits](https://www.tinkercad.com/learn/circuits/learning) for a gentle introduction.

Of, if you have some experience, try the following links:
- [Arduino RC Robot](https://www.tinkercad.com/things/38tyb8Jv6m3-arduino-rc-robot)
- [Tiny Piano - Mini breadboard](https://www.tinkercad.com/things/hPpVZd80QP8-tiny-piano-mini-breadboard)
- [Ultrasonic Distance Sensor LED Bar Graph (Blocks)](https://www.tinkercad.com/things/j0k4YgzXoDF-ultrasonic-distance-sensor-led-bar-graph-blocks)
- [Analog gas sensor](https://www.tinkercad.com/things/bf1fsEJnMFh-analog-gas-sensor)

# Building an Air Quality Monitor

Which leads me to the Smoke issue we had in January. Bombala’s asthmatics.


<image width="300" src="paul.jpg"/>
<image width="600" src="bombala.png" alt="Picture of smoke in sky above Bombala" />

### NSE Rural Fire Service *Fires Near Me* App

<image width="300" src="fire_map.png"/>

https://www.rfs.nsw.gov.au/

### IQAir

<image width="300" src="iqair_map.png"/>

https://www.iqair.com/

### Sensor.Community Open Environmental Data

<image width="300" src="pm10_map.png"/>

https://sensor.community/en/
 

## Client-Server Architecture for Distributed Collection and Analysis

https://luftdaten.info/

https://luftdaten.info/en/construction-manual/ 

https://sensor.community/en/sensors/airrohr/

https://firmware.sensor.community/airrohr/update/

https://github.com/opendata-stuttgart/airrohr-firmware-flasher/blob/master/airrohrFlasher/workers.py ->

https://github.com/opendata-stuttgart/airrohr-firmware-flasher/blob/master/airrohrFlasher/consts.py

https://firmware.sensor.community/airrohr/update/latest_en.bin 

Uses NodeMCU ESP8266 CPU/WLAN - https://en.wikipedia.org/wiki/NodeMCU#ESP8266_Arduino_Core

<image src="board1.png"/>
<image src="board2.png"/>
<image src="board3.jpg"/>

### Reverse Engineering

[Reverse Engineering ESP8266 Firmware](https://www.reddit.com/r/ReverseEngineering/comments/9r11uv/reverse_engineering_esp8266_firmware_part_1/)

IDA - https://boredpentester.com/reversing-esp8266-firmware-part-3/

Ghidra (plugins)

- https://github.com/yath/ghidra-xtensa
- https://github.com/hank/ghidra-esp8266/tree/master/GhidraESP8266_2

Radare2

https://www.onlinedisassembler.com/

### ... or software

https://github.com/opendata-stuttgart/sensors-software


## Projects of interest

Bushfire and particulate matter https://luftdaten.info/en/construction-manual/ 

Brasier, Owen. ‘Simulating Contact Tracing with Micro:Bit’. Medium, 2 July 2020. https://blog.aca.edu.au/simulating-contact-tracing-with-micro-bit-3bc2a5376546.

- See also https://www.coursera.org/learn/covid-19-contact-tracing?edocomorp=covid-19-contact-tracing

BSides Canberra badges

- 2016 - https://www.bsidesau.com.au/badge2016.html
- 2017 - https://github.com/BSidesCbr/BSidesCbrBadge2017 
- 2018 - http://busside.com.au/
- 2019 - https://github.com/BSidesCbr/2019badge

Reference material

- https://www.humblebundle.com/books/programming-for-makers-make-co-books
- https://www.humblebundle.com/books/raspberry-pi-raspberry-pi-press-books

## Some history

My work on transputers at Uni of Tas, on [simulation of networks using Object-Oriented Petri Nets](https://www.researchgate.net/publication/221249453_Object_Oriented_Modeling_with_Object_Petri_Nets) in 1992.
Some background https://en.wikipedia.org/wiki/Transputer, embedded computers with work - real-time operating systems, distributed processing for transcription of real-time audio, remote computing, then high-performance computing then ...

## ASD’s guidance for IoT - through Home Affairs

[Code of Practice: securing the Internet of Things for consumers](https://www.homeaffairs.gov.au/reports-and-publications/submissions-and-discussion-papers/code-of-practice)

download https://www.homeaffairs.gov.au/reports-and-pubs/files/code-of-practice.pdf

### Where to learn more

https://makehackvoid.com/ 


