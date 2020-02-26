import os
import time
import mysql.connector
import telepot
import RPi.GPIO as GPIO
import requests
import json
import calendar
import pyowm
from datetime import datetime
from telepot.loop import MessageLoop

LANG = 'en'




current_date = ''
def get_weather():
    owm = pyowm.OWM('d45a4689c7ff92c093ee18f3c3dafac9')
    obs = owm.weather_at_place('Oulu')
    w = obs.get_weather()
    wind = w.get_wind()
    humidity = w.get_humidity()
    temperature = w.get_temperature('celsius')
    temp =temperature["temp"]
    rain = w.get_rain()
    if len(rain)==0:
        lastrain=0
    else:
        lastrain = rain["3h"]
#     print('Lampotila: ' + str(temp)+ "Celsius")
#     print("Sade: " + str(lastrain) + " mm")
    
    return temp


ledPin = 18
lukitus = 0

sql = "INSERT INTO lampotila (lampotila, date) VALUES (%s, %s)"

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_sensor = '/sys/bus/w1/devices/22-00000057310a/w1_slave'
 
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print('Received: %s' % command)
    
    if command == '/temp':
        telegram_bot.sendMessage(chat_id,str(read_temp())+str("°C"))
    if command == '/weather':
        telegram_bot.sendMessage(chat_id,str(get_weather())+str("°C"))
        
telegram_bot = telepot.Bot('1025221521:AAELhOd7goe4ySkGZbfM5i3IYUmGyzg9m1Y')
#print(telegram_bot.getMe())
MessageLoop(telegram_bot,action).run_as_thread()
print('Up andRunning..')

def temp_raw():
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = temp_raw()
    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
    
try:
    mydb = mysql.connector.connect(
        host="database-1.cgs0pj4eh3aw.us-east-1.rds.amazonaws.com",
        user = "admin",
        passwd="raspberry",
        database="raspberry_database",
    )
    mycursor = mydb.cursor()
except mysql.connector.Error as err:
    print("something went wrong: {}".format(err))
    
while True:
        rcv = str(read_temp())
        dtime = datetime.now()
        val = (rcv, dtime)
        mycursor.execute(sql, val)
        mydb.commit()
        
        print(read_temp())
        
        if read_temp() > 25 and lukitus == 0:
            telegram_bot.sendMessage(-231197051,str("Yikes! Nyt polttelee! :D ")+ str(read_temp())+str(" °C")) #231197051 1089913206
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(ledPin, GPIO.OUT)
            GPIO.output(ledPin, GPIO.HIGH)
            lukitus = 1
        elif read_temp() < 25 and lukitus == 1:
            GPIO.cleanup()
            lukitus = 0
        time.sleep(1)
