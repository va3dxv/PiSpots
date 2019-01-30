#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import datetime
import pytz
import requests
import xmltodict
from rpi_displays.sainsmart.displays import LCD2004

lcd=LCD2004()

vhfpin = 21
tenpin = 20
twntpin = 26
fortpin = 19

def __init__():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
    GPIO.setup(vhfpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(tenpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(twntpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(fortpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(vhfpin, GPIO.FALLING, callback=vhf, bouncetime=300)
    GPIO.add_event_detect(tenpin, GPIO.FALLING, callback=ten, bouncetime=300)
    GPIO.add_event_detect(twntpin, GPIO.FALLING, callback=twnt, bouncetime=300)
    GPIO.add_event_detect(fortpin, GPIO.FALLING, callback=fort, bouncetime=300)

    waitmsg()

def destroy():
    lcd.clear()
    lcd.display_string("PiSpots.py...", 1)
    lcd.display_string("Goodbye.", 2)
    print ("\nCleaning up...\n")
    GPIO.cleanup()
    time.sleep(.5)
    print ("\nGoodbye.\n")
    lcd.clear()
    lcd.switch_backlight(0)
    exit()

def waitmsg():
    lcd.clear()
    lcd.display_string("PiSpots.py...", 1)
    lcd.display_string("...waiting", 2)

def vhf(channel):
    lcd.clear()
    lcd.display_string("Showing last 5", 1)
    lcd.display_string("spots for 6Mtrs+", 2)
    xml_vhf = requests.get(
        url="http://dxlite.g7vjr.org/?xml=1&band=vhf&dxcc=001&limit=5")
    spots_vhf = xmltodict.parse(xml_vhf.text)
    time.sleep(3)
    for spots in spots_vhf["spots"]["spot"]:
        date_string = spots["time"]
        utc = pytz.utc
        est = pytz.timezone("US/Eastern")
        utc_datetime = utc.localize(
            datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
        lcd.clear()
        lcd.display_string(spots["spotter"] + "->" + spots["dx"], 1)
        lcd.display_string(spots["frequency"].split(".")[0] + " " + utc_datetime.astimezone(
            est).strftime("%d%b") + utc_datetime.astimezone(est).strftime("%H:%M"), 2)
        time.sleep(3)
    waitmsg()

def fort(channel):
    lcd.clear()
    lcd.display_string("Showing last 5", 1)
    lcd.display_string("spots for 40Mtrs", 2)
    xml_fort = requests.get(
        url="http://dxlite.g7vjr.org/?xml=1&band=40&dxcc=001&limit=5")
    spots_fort = xmltodict.parse(xml_fort.text)
    time.sleep(3)
    for spots in spots_fort["spots"]["spot"]:
        date_string = spots["time"]
        utc = pytz.utc
        est = pytz.timezone("US/Eastern")
        utc_datetime = utc.localize(
            datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
        lcd.clear()
        lcd.display_string(spots["spotter"] + "->" + spots["dx"], 1)
        lcd.display_string(spots["frequency"].split(".")[0] + " " + utc_datetime.astimezone(
            est).strftime("%d%b") + utc_datetime.astimezone(est).strftime("%H:%M"), 2)
        time.sleep(3)
    waitmsg()

def ten(channel):
    lcd.clear()
    lcd.display_string("Showing last 5", 1)
    lcd.display_string("spots for 10Mtrs", 2)
    xml_ten = requests.get(
        url="http://dxlite.g7vjr.org/?xml=1&band=10&dxcc=001&limit=5")
    spots_ten = xmltodict.parse(xml_ten.text)
    time.sleep(3)
    for spots in spots_ten["spots"]["spot"]:
        date_string = spots["time"]
        utc = pytz.utc
        est = pytz.timezone("US/Eastern")
        utc_datetime = utc.localize(
            datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
        lcd.clear()
        lcd.display_string(spots["spotter"] + "->" + spots["dx"], 1)
        lcd.display_string(spots["frequency"].split(".")[0] + " " + utc_datetime.astimezone(
            est).strftime("%d%b") + utc_datetime.astimezone(est).strftime("%H:%M"), 2)
        time.sleep(3)
    waitmsg()

def twnt(channel):
    lcd.clear()
    lcd.display_string("Showing last 5", 1)
    lcd.display_string("spots for 20Mtrs", 2)
    xml_twnt = requests.get(
        url="http://dxlite.g7vjr.org/?xml=1&band=20&dxcc=001&limit=5")
    spots_twnt = xmltodict.parse(xml_twnt.text)
    time.sleep(3)
    for spots in spots_twnt["spots"]["spot"]:
        date_string = spots["time"]
        utc = pytz.utc
        est = pytz.timezone("US/Eastern")
        utc_datetime = utc.localize(
            datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S"))
        lcd.clear()
        lcd.display_string(spots["spotter"] + "->" + spots["dx"], 1)
        lcd.display_string(spots["frequency"].split(".")[0] + " " + utc_datetime.astimezone(
            est).strftime("%d%b") + utc_datetime.astimezone(est).strftime("%H:%M"), 2)
        time.sleep(3)
    waitmsg()

if __name__ == '__main__':
    __init__()
    while True:
        try:
            time.sleep(1)
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except KeyboardInterrupt:
            destroy()

