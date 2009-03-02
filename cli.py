from optparse import OptionParser

class Cli (object):

    def __init__(self):
        self.__config_parser()

    def __config_parser(self):
        self.__parser = OptionParser()

        self.__parser.add_option("-t", "--text",
                dest="text",
                default="",
                help="Blink your message on the top of the clock")
                
        self.__parser.add_option("-s", "--soundfile",
                dest="soundfile",
                default=None, 
                help="Will play this file at startup")

        self.__parser.add_option("-f", "--fullscreen",
                dest="fullscreen",
                action="store_true",
                default=False, 
                help="Show the clock on fullscreen")
                
        self.__parser.add_option("-l", "--timeline",
                dest="timeline",
                action="store_true",
                default=False, 
                help="Show the Sprint Timeline (need to config wikipage)")                
                
    def get_parser(self):
        return self.__parser

    def parse(self):
        return self.__parser.parse_args()
