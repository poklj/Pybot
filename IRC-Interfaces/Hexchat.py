__module_name__ = "Pybot-Hexchat-FE"
__module_version__ = "latest" #TODO: Make this less vague
__module_description__ = "Pybot's Hexchat frontend"

try:
    import hexchat
    from Pybot import Pybot_Main
except ImportError:
    pass


class Hexchat_frontend:

    def __init__(self):
        self.channel = "ChannelName"
        pass #TODO: Create a way to define what channel to join

    def main(self):
        Pybot_Main(hexchat.get_info("nick"),self.channel)

    def Say(self,message):
        hexchat.command("say {}".format(message))

if __name__ == "__main__":
    Hexchat_frontend.main()

