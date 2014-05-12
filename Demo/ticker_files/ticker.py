#!/usr/bin/python

#Stig atle steffensen, http://stigatle.net | https://bitbucket.org/stigatle/pylcdbitcoin
#Greg Ledet, http://www.gregledet.net

#handle the imports needed
from pylcdsysinfo import BackgroundColours, COL2LEFT, TextColours, TextAlignment, TextLines, LCDSysInfo
from time import sleep

#used to communicate with bitcoind rpc
import bitcoinrpc
from bitcoinrpc.exceptions import InsufficientFunds

#used to parse the webpage ticker data.
import urllib
import urllib2
import re

# Init the LCD screen
display = LCDSysInfo()
display.dim_when_idle(False)
display.clear_lines(TextLines.ALL, BackgroundColours.BLACK)
display.set_brightness(255)
display.save_brightness(100, 255)

#Grab the latest price from mtgox
aResp = urllib2.urlopen("http://data.mtgox.com/api/1/BTCUSD/ticker");
web_pg = aResp.read();

#read and 'strip' the resulting string so that it can be used.
#this is the response as string
str1 = str(web_pg);
#get the last price
str2 ="last_all"
#look for it in the result
subStringFindInt = str1.find(str2);
#strip the string to 'keep' the price
substringprice = str1[subStringFindInt + 20:];
#extract the price
price =  substringprice[0 : 0 +6];
#get the volume
str3 ="vol"
#Look for it in the result
subStringFindVol = str1.find(str3);
#strip it
substringvolume = str1[subStringFindVol + 15:];
#extract it
volume = substringvolume[0 : 0 +10];
#get the low price
str4 ="low"
#look for it
subStringFindLow = str1.find(str4);
#strip it
substringlow = str1[subStringFindLow + 15:];
#extract it
low = substringlow[0 : 0 +6];
#get the average price
str5 = "avg"
#look for it
subStringFindAvg = str1.find(str5);
#strip it
substringavg = str1[subStringFindAvg + 15:];
#extract it
avg = substringavg[0 : 0 +6];
#get the weighted average price
str6 = "vwap"
#look for it
subStringFindVwap = str1.find(str6);
#strip it
substringvwap = str1[subStringFindVwap + 16:];
#extract it
vwap = substringvwap[0 : 0 +6];
#get the high price
str7 = "high"
#look for it
subStringFindHigh = str1.find(str7);
#strip it
substringhigh = str1[subStringFindHigh + 16:];
#extract it
high = substringhigh[0 : 0 +6];

# Refresh the background and make it black
display.set_text_background_colour(BackgroundColours.BLACK)

#loop through each line to display, filling in the variables.
for line in range(1, 7):
    if line == 1:
        display.display_text_on_line(line, '1 BTC at MtGox', True, (TextAlignment.RIGHT, TextAlignment.RIGHT), TextColours.LIGHT_BLUE)
    elif line == 2:
        display.display_text_on_line(line, 'Last $' + str(price) + " USD", True, (TextAlignment.LEFT, TextAlignment.LEFT), TextColours.GREEN)
    elif line == 3:
        display.display_text_on_line(line, 'Volume: ' + str(volume), True, (TextAlignment.RIGHT, TextAlignment.RIGHT), TextColours.RED)
    elif line == 4:
        display.display_text_on_line(line, 'High $' + str(high), True, (TextAlignment.RIGHT, TextAlignment.RIGHT), TextColours.GREEN)
    elif line == 5:
        display.display_text_on_line(line, 'Low $' + str(low), True, (TextAlignment.RIGHT, TextAlignment.RIGHT), TextColours.GREEN)
    elif line == 6:
	    display.display_text_on_line(line, 'Avg $' + str(vwap), True, (TextAlignment.RIGHT, TextAlignment.RIGHT), TextColours.GREEN)
