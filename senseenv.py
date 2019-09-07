#!/usr/bin/python3
import vcgencmd
import requests
import json
import time
from random import randint
from sense_hat import SenseHat
from PIL import Image
sense = SenseHat()
from resizeimage import resizeimage
# Define the colours red and green
red = (randint(0,255), 0, 0)
green = (0, 255, 0)

while True:

  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()
  CPUc=vcgencmd.measure_temp()
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)

  CPUc = round(CPUc,1)
  t_calibrated=t-((CPUc-t)/5.466)
  t_calibrated=round(t_calibrated,1)
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
  room_conditions = "Temperature Inside: " + str(t_calibrated) + " Pressure: " + str(p) + " Humidity: " + str(h)
  message=main+" --> "+desc
  if t_calibrated > 18.3 and t_calibrated < 26.7:
    bg = green
  else:
    num1 = randint(0, 255)
    num2 = randint(0, 255)
    num3 = randint(0, 255)
    color = (num1, num2, num3)  
    bg = color 
  
  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.05, text_colour=bg)
  sense.load_image('icon.png') 
  time.sleep(5)
  sense.show_message(room_conditions,scroll_speed=0.05, text_colour=bg)
