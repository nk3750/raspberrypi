## Table of contents
* [General info](#general-info)
* [Openweather API setup](#API-setup)
* [Technologies](#technologies)
* [Python modules](#Dependency)
* [Informations Displayed](#Displayed info)
* [Setup](#setup)

## General info
This project helps you to setup a sensehat displaying the weather conditions outside as well as the readings of your sesehat sensors.
Getting the readings from the sensehat sensors is straight forward, if you have the hardware setup, that shouldn't be a problem.
I have used the OpenWeather free API to get the weather conditions for my locations, you can use any of the free API avaliable from any Weather prediction websites.

## Openweather API setup
Create a free account on openweather [Link to account creation] (https://home.openweathermap.org/users/sign_up)
Get your API key under the API keys tab [Link] (https://home.openweathermap.org/api_keys)
Search for your city id here [Link to city id json file] (http://bulk.openweathermap.org/sample/)
Replace {your city id} and {your api key} in the code with your city ID and API key.

	
## Technologies
Project is created with:
* Python Version 3

## Python modules
Use pip3 to install all these modules

vcgencmd

requests

json

time

sense_hat

PIL

resizeimage
	
## Informations Displayed

1) Current weather condition at your location

2) Detailed weather condition at your location

3) Weather Icon corresponding to the current conditions

4) Room Temperature

5) Pressure

6) Humidity

## Setup
git clone (repo address)

```
python3 senseenv.py
