# This file contains gui pages of main stack: Ver sep 2020

import sys
import gi
from submods import functions
from submods import guicommon
from submods import guiprocessor
from submods import guinewsale
from submods import guieditsale
from submods import saleinvoicingprocessor
from submods import cimoredialog
from submods import pdfsaleinvoice
from submods import printsihandler
from datetime import datetime

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkInvoicing():

    #---------------------------Billbox contents start     
     
    def generatepage(self, mainwindow, guiinvoicingins):
       
        self.mainwindow=mainwindow
        self.newsaleins=guinewsale.GtkNewSale()
        self.editsaleins=guieditsale.GtkEditSale()
        
        self.invopage_main=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
        self.invostack = Gtk.Stack()
        self.invostack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.invostack.set_transition_duration(1000)        
        
        newsibox=self.newsaleins.billingpage(self.mainwindow, guiinvoicingins)        
        self.invostack.add_titled(newsibox, "newsaleinvoice", "New Sale invoice")
        
        editsibox=self.editsaleins.billedit(self.mainwindow)        
        self.invostack.add_titled(editsibox, "editsaleinvoice", "Edit Sale invoice")
        
        self.invostack_switcher = Gtk.StackSwitcher()
        self.invostack_switcher.set_stack(self.invostack)

        self.invopage_main.pack_start(self.invostack_switcher, False, False, 10)
        self.invopage_main.pack_start(self.invostack, False, False, 10)
        
        return self.invopage_main
                    
        
