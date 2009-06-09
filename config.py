# -*- coding: utf-8 -*-
class Size(object):
    def __init__(self, screen, bigfont, mediumfont, smallfont, tinyfont,
                       message_top, time_top, time_desc_top,
                       timeline_sprint_top, timeline_left, timeline_linetop, 
                       timeline_dayline, timeline_width, timeline_datelist_top):
        self.screen = screen
        self.bigfont = bigfont
        self.mediumfont = mediumfont
        self.smallfont = smallfont
        self.tinyfont = tinyfont
        self.message_top = message_top
        self.time_top = time_top
        self.time_desc_top = time_desc_top
        
        self.timeline_sprint_top = timeline_sprint_top
        
        self.timeline_left = timeline_left
        self.timeline_linetop = timeline_linetop
        self.timeline_dayline = timeline_dayline
        self.timeline_width = timeline_width
        self.timeline_datelist_top = timeline_datelist_top

SIZES =  {
    "640x480": Size((640, 480), 90, 40, 20, 10, 120, 240, 305, 370, 45, 400, 46, 2, 410),
    "800x600": Size((800, 600), 90, 40, 20, 10, 120, 240, 305, 370, 45, 400, 46, 2, 410),
    "1200x800": Size((1200, 800), 90, 40, 20, 10, 120, 240, 305, 370, 45, 400, 46, 2, 410),
    "1600x1200": Size((1600, 1200), 250, 220, 70, 25, 120, 440, 650, 870, 65, 950, 120, 4, 960),
}        
