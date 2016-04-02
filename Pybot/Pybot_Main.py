#Main module for pybot

try:
    import time
    import sys
    import math
    import os
    import datetime
except ImportError:
    pass


class Pybot:
    def __init__ (self, botUsername, channelToJoin,frontend):
        #Legacy debug shit, unittests will probably be better but sometimes having this could assist with debug
        self.isDebug = 1

        if frontend:
            self.frontend = frontend

        if botUsername:
            self.botUsername = botUsername  #Used as a pass down from the IRC code
        else:
            #TODO: Replace the print function for a pipe to the IRC client
            print ("No botUsername Given- Defaulting")
            self.botUsername = "PyBot"

        for i in channelToJoin:
            if (i == " "):
                raise NameError("channelToJoin contains spaces")

    def debug (self, message):
        if self.isDebug == 1:
            print (message)