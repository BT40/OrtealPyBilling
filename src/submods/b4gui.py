#This file loads first on software start, before gui creation

import sys
import gi
from submods import functions
from submods import dbmani
from submods import guicommon
from submods import guiprocessor
from datetime import datetime

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class Startt():
        
    def some_initialisations(self):
        dbmani.loadidbase()                           
        guicommon.loadguicommon()        
        #print('Completed b4gui')             

