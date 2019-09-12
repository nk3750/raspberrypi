#!/usr/bin/python3
import vcgencmd
import requests
import json
import time
import datetime
from random import randint
from sense_hat import SenseHat
from PIL import Image
sense = SenseHat()
from resizeimage import resizeimage
# Define the colours red and green
red = (255, 0, 0)
green = (0, 255, 0)
sense.set_rotation(180)

def lowLighttrue():
      sense.low_light = True 

def lowLightfalse():
      sense.low_light = False

while True:

  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()
  CPUc=vcgencmd.measure_temp()
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)

  CPUc = round(CPUc,1)
  r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=5134086&APPID=616ffe1395e0e036d47b0e5982b5bc80')
  result=r.json() 
  main=result["weather"][0]["main"]
  desc=result["weather"][0]["description"]
  icon=result["weather"][0]["icon"]
  icon_request=requests.get("http://openweathermap.org/img/w/"+icon+".png")
  with open(icon+'.png', 'wb') as f:
        f.write(icon_request.content)
  with open(icon+'.png', 'r+b') as f:
    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [8,8])
        cover.save('icon.png', image.format)
  room_conditions = " Humidity: " + str(h) +" Temp: " +str(t)
  message=main.upper()+" --> "+desc.upper()
  if h > 30 and (t>19 and t<26) :
    tg = green
    
  else:
    tg=red
  
  num1 = randint(0, 255)
  num2 = randint(0, 255)
  num3 = randint(0, 255)
  color = (num1, num2, num3)  
  bg = color 
  
  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.05, text_colour=bg)
  sense.load_image('icon.png') 
  time.sleep(5)
  sense.show_message(room_conditions,scroll_speed=0.05, text_colour=tg)
  
  now = datetime.datetime.now()
  sense.show_message("Time "+str(now.hour)+":"+str(now.minute),scroll_speed=0.05, text_colour=bg)
  sense.stick.direction_up = lowLighttrue
  sense.stick.direction_down = lowLightfalse

