# Project Title:- Electronic Anti Suffocation and Temperature(EAST)

## ABSTRACT
BELAGAVI: Two kids, aged four and two, died of suffocation on Thursday after they accidently switched on central locking system of their father's car and got trapped inside the vehicle at Madigunji in Karnataka's Khanapur taluk. The two were identified as Prem and Pritam. The boys shouted for help from within the car, but no one noticed rushed the boys to Khanapur hospital, where doctors declared them dead. A recent study conducted for the non-profit Safe Kids Worldwide found 14 percent of parents admitted they’ve left a child in the car alone and 11 percent acknowledged they’d done so because they forgot the child was in the car. Auto safety groups have called for manufacturers to do more, but for several reasons -- cost, technology, liability and privacy issues -- there is still no fool proof way of preventing overheating deaths or warning of the possibility before they happen.
There are a few aftermarket warning systems, such as the Child-minder Smart Clip System, which alerts a parent if they’ve inadvertently wandered away from a child left in a safety seat or shopping cart or somewhere else. But their efficiency is questionable.


## E.A.S.T (ELECTRONIC ANTI-SUFFOCATION & ANTI-TEMPERATURE)
It is an IOT device which serves as both environment monitoring system as well as alerting system which alerts the user about any abnormal gas detections or temperature rise.Temperature sensor and CO2 sensors are continuously running and monitoring the status of the car and also updating it to cloud for later reference. These ratings are compared with PIR sensor output determining whether there is someone inside or not. If someone’s presence is detected in car when the sensors are detecting something not normal then an immediate notification via SMS will be sent to the car owner alerting him and if he could not make it to the car in 10min an alarm will be set off alerting the nearby people. Also in the background it silently monitors interior conditions of the car and alerts about certain things such as when to change AC filter, etc… 
This system prevents suffocation by intelligent sensing which works efficiently, this is an economical system without any compromise on its functioning.
The system includes following components:                                                                              


List of Documents:-
1. Power_Point_Presentation.pptx - Ppt. for the project
2. Code.txt - Code of the project


Requirements:
1. Raspberry Pi-3 with Raspbian OS installed
2. Sensors :
	Carbon gas sensor        (MQ135) 
	Temperature sensor       (DHT11) 
	Motion sensor            (HC SR501 PIR) 
3. Python 3.6
4. Working Internet Connection
5. Packages mentioned in the code


Running the Program
1. Open command prompt
2. Go to file location
5. Execute command - "python east.py"