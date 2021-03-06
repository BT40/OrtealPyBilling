# This file contains gui pages of main stack: Ver sep 2020

import sys
import gi
from submods import functions
from submods import dbmani
from submods import guicommon
from submods import guihelp
from submods import guitaxslabs
from submods import guitaxontaxslabs
from submods import guimanage
from submods import guipreferences
from submods import guiprocessor
from datetime import datetime

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkMore():
      
    #----------------------------------More box contents start         
        
    def generatepage(self, applic, invoicingbox, bph, guiinvoicingins, companybox, cph, guicompanyins, mainwindow):
           
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
        guipref_ins=guipreferences.GtkPreferences()
        prefholder=guipref_ins.generatepage(mainwindow)
        prefbox.pack_start(prefholder, False, False, 0)
        #print("Loaded pref pane")   
        
        ctaxbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        guitaxslabsins=guitaxslabs.GtkTaxSlabs()
        cth=guitaxslabsins.generatepage(invoicingbox, bph, guiinvoicingins, mainwindow) #customtax holder
        ctaxbox.pack_start(cth, False, False, 0)
        
        ctaxontax_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        guitaxontaxslabs_ins=guitaxontaxslabs.GtkTaxonTaxSlabs()
        ctoth=guitaxontaxslabs_ins.generatepage(invoicingbox, bph, guiinvoicingins, mainwindow) #custom tax on tax holder
        ctaxontax_box.pack_start(ctoth, False, False, 0)
        
        helpbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        hth=guihelp.helptips() #help tips holder
        helpbox.pack_start(hth, False, False, 0)
        
        managebox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        guimanageins=guimanage.GtkManage()
        mbh=guimanageins.generatepage(invoicingbox, bph, guiinvoicingins,  companybox, cph, guicompanyins, mainwindow)
        managebox.pack_start(mbh, False, False, 0)
        
        #exitbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        #mbexitbutton = Gtk.Button.new_with_label("Click here to close the app")
        #mbexitbutton.set_halign(Gtk.Align.CENTER) # to avoid expansion horizontally
        #mbexitbutton.connect("clicked", self.exittheapp, applic)
        #mbexitbutton.get_style_context().add_class("dangerbutton") 
        #exitbox.pack_start(mbexitbutton, False, False, 0)      
        
        #morestack.add_titled(fybox, "fysettingsbox", "FY Settings")
        morestack.add_titled(prefbox, "preferencesbox", "Preferences")
        morestack.add_titled(ctaxbox, "customtaxslabsbox", "Tax slabs")
        morestack.add_titled(ctaxontax_box, "ctaxontaxslabsmbox", "Tax on Tax slabs")                
        morestack.add_titled(managebox, "managebox", "Manage")
        morestack.add_titled(helpbox, "helpguidebox", "Help")
        #morestack.add_titled(exitbox, "exitappbox", "Exit")

        #print("Packing of stack switcher in More pane started")  
        morestack_switcher = Gtk.StackSwitcher()
        morestack_switcher.set_stack(morestack)
         
        moremasterbox.pack_start(morestack_switcher, False, False, 10)
        moremasterbox.pack_start(morestack, True, True, 10)
            
        return moremasterbox
            

    def exittheapp(self, exitbutton, applic):
        applic.quit() # automatically reference to global one. If not uncomment the line above.
    


