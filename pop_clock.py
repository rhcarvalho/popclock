## Digital clock with message and sound
## Evandro Flores - eof@eof.com.br
## Special thanks to:
## Guilherme Chapiewski - chapa@gc.blog.br
## The Knights who say Ni! - knights@whosay.ni

import pygame
from pygame.locals import *
import os
import time
from time import gmtime, strftime, sleep
import sys
import locale
import getopt
import urllib2
import re


class PopClock (object):

    def __init__(self, options, args):
        pygame.init()
        self.init_time = time.time()

        # If you don't have DejaVuSans font: use this file 
        # or 'sudo apt-get install mscoretruefont' or
        #self.bigfont = pygame.font.Font("DejaVuSans.ttf", 90)
        self.bigfont = pygame.font.SysFont("DejaVuSans", 90)
        self.smallfont = pygame.font.SysFont("DejaVuSans", 20)
        self.tinyfont = pygame.font.SysFont("DejaVuSans", 10)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (55, 55, 55)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)

        self.quit = False
        self.time = " -- : -- : -- "
        self.timedesc = "..."
        self.timecolor = self.WHITE
        self.msgcolor = self.WHITE
        self.bgcolor = self.BLACK
        self.verbose = False
        self.timelimit = options.exitat
        self.message = ""
        self.timeline = False
        self.debug = options.debug
        self.alarm = options.alarm

        if self.debug:
            print "Options %s" % options

        if options.message:
            self.message = options.message

        if options.timeline:
            self.timeline = True
            self.wikinfo = WikiInfo()

        if options.fullscreen:
            self.screen = pygame.display.set_mode((640, 480), FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((640, 480))

        if options.soundfile:
            self.sound = pygame.mixer.Sound(options.soundfile)
            self.sound.play()

        pygame.display.set_caption("PopClock")

    def update(self):
        if ((time.time() - self.init_time)/60) >= self.timelimit:
            self.quit = True

        self.time = strftime(" %H: %M:%S ")
        self.timedesc = strftime(" %A, %d %B %Y")

        if self.msgcolor == self.WHITE:
            self.msgcolor = self.BLACK
        else:
            self.msgcolor = self.WHITE

        if self.alarm:
            if self.bgcolor == self.RED:
                self.bgcolor = self.YELLOW
                self.msgcolor = self.RED
                self.timecolor = self.RED
            else:
                self.bgcolor = self.RED
                self.msgcolor = self.YELLOW
                self.timecolor = self.YELLOW

        return

    def draw(self):
        self.screen.fill(self.bgcolor)

        msgrender = self.bigfont.render(self.message, True, self.msgcolor)
        msgpos = msgrender.get_rect()
        msgpos.centerx = self.screen.get_rect().centerx
        msgpos.centery = self.screen.get_rect().centery-120
        self.screen.blit(msgrender, msgpos)

        timerender = self.bigfont.render(self.time, True, self.timecolor)
        timepos = timerender.get_rect()
        timepos.centerx = self.screen.get_rect().centerx
        timepos.centery = self.screen.get_rect().centery
        self.screen.blit(timerender, timepos)

        timedescrender = self.smallfont.render(self.timedesc, True, self.timecolor)
        timedescpos = timedescrender.get_rect()
        timedescpos.centerx = self.screen.get_rect().centerx
        timedescpos.centery = self.screen.get_rect().centery+65
        self.screen.blit(timedescrender, timedescpos)

        if self.timeline:
            sprintrender = self.smallfont.render(self.wikinfo.sprint,
                                                        True, self.WHITE)
            self.screen.blit(sprintrender, (100, 370))

            pygame.draw.line(self.screen, self.GRAY, (100, 400), (560, 400), 2)

            qtd=0
            pastdays=0
            today = strftime("%d %b")
            future = False
            for day in self.wikinfo.datelist:
                if (future):
                    datarender = self.tinyfont.render(day, True, self.GRAY)
                else:
                    datarender = self.tinyfont.render(day, True, self.WHITE)
                    pastdays+=1

                datapos = timedescrender.get_rect()
                datapos.x = 100+(47*qtd)
                datapos.y = 410
                self.screen.blit(datarender, datapos)
                qtd+=1
                if day == today:
                    future = True

            pygame.draw.line(self.screen, self.RED, (100, 400),
                             (100+(46*(pastdays)), 400), 2)

        pygame.display.flip()

    def run(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit = True
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.quit = True
            self.update()
            self.draw()
            sleep(0.3)

#TODO: Make a plugin with WikiInfo 
class WikiInfo:

    def __init__(self):
        self.sprint = "Sprint XX"
        self.datelist = ['00 Ooo', '00 Ooo', '00 Ooo', '00 Ooo', '00 Ooo',
                         '00 Ooo', '00 Ooo', '00 Ooo', '00 Ooo', '00 Ooo']

        wiki = 'http://wiki.globoi.com/view'

        wiki_header = urllib2.urlopen('%s/A3/SprintAtual?cover=print'%wiki)
        html_header = wiki_header.read()
        current_sprint = re.compile("location.href='/A3/(.*)';").findall(html_header)
        if current_sprint:
            self.sprint = current_sprint[0].replace("A3Sprint", "Sprint ")

        wiki_current_sprint = '%s/A3/%s?cover=print' % (wiki, current_sprint)

        wiki_current_sprint = urllib2.urlopen(wiki_current_sprint)
        html_sprint = wiki_current_sprint.read()

        pattern = '<li> ([0-9]{2} [A-Za-z]{3}) [0-9]{4} - [Daily Meeting|Sprint Planning|Review].*[^<]\n</li>'

        dailys = re.compile(pattern).findall(html_sprint)

        if dailys:
            #remove next planning
            dailys.pop()
            self.datelist = dailys

