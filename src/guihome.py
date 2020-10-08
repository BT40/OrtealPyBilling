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


class GtkHome():

    #--------------------------------- box contents start

        
        
    def some_initialisations(self):
        dbmani.loadidbase()       
        
        self.itemtableins=dbmani.itemtableins        
        self.companytableins=dbmani.companytableins
        self.invoicetableins=dbmani.invoicetableins       
        self.miscdb=dbmani.miscdb       
        self.itemgroups=dbmani.itemgroups
        
        
        self.dobj = datetime.now() #object for datetime class accessing
        self.todayobj=self.dobj.date()
        self.todaysdate_string=str(self.todayobj) 
        
        guicommon.loadguicommon()
        self.guiprocessor_ins=guiprocessor.GtkProcessor()
        
        
        
        self.companyname_store = Gtk.ListStore(str)
        for eachcompany_tmp in self.companytableins.rowlist:
            self.companyname_store.append([eachcompany_tmp])
            #print (eachcompany_tmp)   
        
        #use for item name completion everywhere    
        self.itemname_store = Gtk.ListStore(str)
        for eachitem_tmp in self.itemtableins.rowlist:
            self.itemname_store.append([eachitem_tmp])
            #print (eachitem_tmp)               
       

    def generatepage(self):
        
        self.some_initialisations()    
        homemasterbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
        hp_wlabel = Gtk.Label() #welcome label
        hp_wlabel.set_markup("Welcome to Orteal billing")
        
        hp_tilabel = Gtk.Label() #total invoices
        hp_tilabel.set_margin_top(50)
        hp_tilabel.set_markup("Total number of invoices")
        
        hp_mbalabel = Gtk.Label() #this month billing amount
        hp_mbalabel.set_markup("This month sale: ")
        
        hp_yclabel = Gtk.Label() #your company
        hp_yclabel.set_markup("Your company: ")
        hp_yclabel.set_margin_top(50)
        
             
        
        hpcombo = Gtk.ComboBoxText()
        hpcombo.set_halign(Gtk.Align.CENTER)
        companylist=['Default', 'Demo']
        hpcombo.append_text(companylist[0])
        hpcombo.append_text(companylist[1])
        hpcombo.set_active(0)
        #hcomcombo = Gtk.ComboBox.new_with_model()
        
        homemasterbox.pack_start(hp_wlabel, True, True, 0)
        homemasterbox.pack_start(hp_yclabel, True, True, 0)
        homemasterbox.pack_start(hpcombo, False, False, True)
        homemasterbox.pack_start(hp_tilabel, True, True, 0)
        homemasterbox.pack_start(hp_mbalabel, True, True, 0)
        return homemasterbox
            
