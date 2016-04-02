#-------------------------------------------------------------------------------
# Name:        Twitch pybot
# Purpose:     A Twitch bot using Hexchat as its connector
#
# Author:      kickguy223
#
# Created:     03/12/2014
# Copyright:   (c) kickguy223 2014
# Licence:
#-------------------------------------------------------------------------------

#NOTICE TO USERS
# Look down to USER SETTINGS and change those to what you need from this
# Script/Bot


#DO NOT EDIT from here-

__module_name__ = "Pybot"
__module_version__ = "prealpha"
__module_description__ = "python Twitch bot"

try:
    import hexchat
except:
    raise NameError('Error 100: Run this in Hexchat')
import time
import sys
import math
import os
import datetime
# - To here

#User settings Edit these as needed

#Name of YOUR channel
channeltoJoin = "kickguy223"

#Developer setting, Don't touch unless you want lots of Debug messages :P
# 1= on 0=off
debug = 0


mynick = hexchat.get_info("nick")

#Debug
def debug(message):
    if(debug == 1):
        print(message)


#Run on initiate
def initi():
    print("\002 Pybot Initialized")
    print("I am pybot")
    channelCheck = 0
    #check to make sure Channel is valid
   # while (channelCheck == 0):
        #debug("begin channel check")
       # b = 0
       # debug(b)
       # debug(channeltoJoin[b])
    for i in channeltoJoin:
        if(i == " "):
            raise NameError('Error 101: Channel contains Space')


       # if(channeltoJoin[b] == " "):
       #   raise NameError('Error 101: Channel contains a space
       #  else:
       #     if(b != len(channeltoJoin)):
       #         b = b + 1
       #         channelCheck = 1
    debug("Channel check complete")
    #Once Channel check is done, join channel
    #if (debug != 1):
    hexchat.command("join #{}".format(channeltoJoin))
    #then introduce
    time.sleep(2)
    hexchat.command("say Hello I am Pybot, there is no {} anymore...".format(mynick))

#grab chat events
def read_eCommand(word, word_eol, userdata):
    #send to Command event
    debug("input :74")
    w = word[1]

    if(w=="!test"):
        test()
    elif(w=="!help"):
        helpi()
    elif(w=="!points"):
        call_points(word[0])
    elif(w=="!weallkreygasm"):
        kreygasm()



def userleave(word, word_eol, userdata):
    debug("{} left".format(word[0]))
    ulist.remove(word[0])


#command Definitions
def test():
    hexchat.command("say Test command called")
    debug("test :85")
def helpi():
    hexchat.command("say (working) commands are: !test, !help ")
    debug("help :88")
def kreygasm():
    hexchat.command("say We all must Kreygasm , Hggnnnnn!")
#Generate working Filepath
def file_path():
    global userhome
    userhome = os.path.expanduser('~')
    useh = os.path.split(userhome)[-1]
    #bhomepath = "C:\Users\{}\Documents\pybot_files".format(userhome)

    debug(os.path.expanduser('~'))
    debug("User's home Dir: " + userhome)
    debug("username: " + os.path.split(userhome)[-1])

#Handle points
def load_points():
    #TODO: Create the Load point function
    #NOTE: This will be used to load the points into the script from the file(?) that contains them and will send it off to read_points()
    global filep
    filep = open("pybot_files\points.txt".format(userhome),"r+")

def read_points():
    #TODO: create the read points function
    #NOTE: This will be used to read the Points and Dump them into the variables required to interact with them later
    global lPointU
    global lPointP
    debug(filep.read())
    lPointU = []
    lPointP = []
    #dump values
    for line in filep:
        i = line
        debug(i)
        s = i.split(":")
        debug(s)
        lPointU.append(s[0])
        lPointP.append(s[1])
        debug(lPointU)
        debug(lPointP)

def call_points():
    #TODO: Create the Call points function
    #NOTE: This will be used to Print the functions when the users ask the Bot for their point totals
    pass

def do_Points():
    #TODO: Create the Points function
    #NOTE: This will contain the Point earning method and also Interact with the Point spending Definitions
    global ulist
    usersin = hexchat.get_list('users')
    ulist = []
    utime = []
    if usersin:
        for i in list:
            debug("%a" % (usersin.nick))
            ulist.append(usersin.nick)

            #Create timestamps when a new user joins
            utime.append(datetime.time(2))

        for index, x in enumerate(utime):
            if(x==x+5):
                lPointP[index] += 1
                utime[index] = datetime.time(2)

        #TODO: Create a method to Calculate the time that a specific user has been in the chat, and give points per a specified amount of time



def write_Points():
    #TODO: Create the Write Points function
    #NOTE: |This will contain the Point file write function and Will be interacted with on shut-down or by do_Points during Auto-saves | IN PROGRESS
    pass

#Beginning of call

initi()
hexchat.hook_print("Channel Message", read_eCommand)
    #hexchat.hook_print("Part", userleave)
