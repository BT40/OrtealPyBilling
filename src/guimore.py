# This file contains gui pages of main stack: Ver sep 2020

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


class GtkMore():
      
    #----------------------------------More box contents start         
        
    def generatepage(self, applic):
           
        moremasterbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
                
        morestack = Gtk.Stack()
        morestack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        morestack.set_transition_duration(1000)
        
        #fybox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        #fylabel = Gtk.Label()
        #fylabel.set_markup("Financial year settings will be added here.")
        #fybox.pack_start(fylabel, True, True, 0)
        #print("Loaded FY pane")   
            
        # Preferences pane coding starts here 
        #print("Started item pane coding in Preferences pane")   
        
        prefbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        preflabel = Gtk.Label()
        preflabel.set_markup("Automatic invoice numbering option, tax slabs, invoice number prefix, hide purchases, will be added in future.")
        prefbox.pack_start(preflabel, True, True, 0)
        #print("Loaded pref pane")   
        
        helpbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        helplabel = Gtk.Label()
        helplabel.set_margin_top(100)
        helplabel.set_markup("Press tab to switch between input fields.")
        helplabel2 = Gtk.Label()
        helplabel2.set_markup("Rest is self explanatory being a simple software.")
        helpbox.pack_start(helplabel, False, False, 0)
        helpbox.pack_start(helplabel2, False, False, 0)
        
        aboutbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        aboutlabel = Gtk.Label()
        aboutlabel.set_markup("Alpha Version September 2020, Try at your own risk. Software is open source.")
        aboutbox.pack_start(aboutlabel, True, True, 0)
        #print("Loaded about pane")  
        
        exitbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        exitlabel = Gtk.Label()
        exitlabel.set_markup("Press this button to exit")
        exitbox.pack_start(exitlabel, False, False, 0)
        mbexitbutton = Gtk.Button.new_with_label("Exit the app")
        mbexitbutton.set_halign(Gtk.Align.CENTER) # to avoid expansion horizontally
        mbexitbutton.connect("clicked", self.exittheapp, applic)
        mbexitbutton.get_style_context().add_class("dangerbutton") 
        exitbox.pack_start(mbexitbutton, False, False, 0)      
        #print("Loaded exit pane")  
        
        #morestack.add_titled(fybox, "fysettingsbox", "FY Settings")
        morestack.add_titled(prefbox, "preferencesbox", "Preferences")
        morestack.add_titled(helpbox, "helpguidebox", "Help")
        morestack.add_titled(aboutbox, "aboutinfobox", "About")
        morestack.add_titled(exitbox, "exitappbox", "Exit")

        #print("Packing of stack switcher in More pane started")  
        morestack_switcher = Gtk.StackSwitcher()
        morestack_switcher.set_stack(morestack)
        
        #print("Packing of more stack started")  
        moremasterbox.pack_start(morestack_switcher, False, False, 10)
        moremasterbox.pack_start(morestack, True, True, 10)
        #print("Just above return statement in more pane")  
            
        return moremasterbox
            

    def exittheapp(self, exitbutton, applic):
        #global applica
        applic.quit() # automatically reference to global one. If not uncomment the line above.
    #----------------------------------More box contents end         
        


