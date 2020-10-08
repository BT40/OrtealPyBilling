from submods import functions
from submods import guicommon
import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkTaxSlabs():


    def generatepage(self):
        tmbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20) #taxmain box
        
        tcreate_label = Gtk.Label()
        tcreate_label.set_markup("Create a new tax slab")   
        tcreate_label.set_halign(Gtk.Align.START) 
        tcreate_label.set_hexpand(False)     
        tmbox.pack_start(tcreate_label, False, False, 10)
        
        gridcts = Gtk.Grid() #custom tax slab
        tmbox.pack_start(gridcts, True, True, 0)

        tnamelabel = Gtk.Label()
        tnamelabel.set_markup("Tax slab name")        
        self.tnameentry = Gtk.Entry()

        
        #==============================================
        
        enable_firsttax_label = Gtk.Label()
        enable_firsttax_label.set_markup("Enable first tax column ")
        enable_firsttax_label.set_margin_top(10)
        
        self.firsttax_button = Gtk.CheckButton()
        self.firsttax_button.set_margin_top(10)
        self.firsttax_button.set_active(True) # By default true
        
        enable_secondtax_label = Gtk.Label()
        enable_secondtax_label.set_markup("Enable second tax column ")
        enable_secondtax_label.set_margin_top(10)
        
        self.secondtax_button = Gtk.CheckButton()
        self.secondtax_button.set_margin_top(10)
        self.secondtax_button.set_active(False) # By default false
        
        enable_thirdtax_label = Gtk.Label()
        enable_thirdtax_label.set_markup("Enable third tax column ")
        enable_thirdtax_label.set_margin_top(10)

        self.thirdtax_button = Gtk.CheckButton()
        self.thirdtax_button.set_margin_top(10)
        self.thirdtax_button.set_margin_bottom(10)
        self.thirdtax_button.set_active(False) # By default false

        #==============================================   
             
        #----------------------------------------------
                
        ftrlabel = Gtk.Label() #first tax rate 
        ftrlabel.set_markup("First tax rate")        
        self.ftrentry = Gtk.Entry()
        
        strlabel = Gtk.Label() #second tax rate
        strlabel.set_markup("Second tax rate")        
        self.strentry = Gtk.Entry()
        
        ttrlabel = Gtk.Label() #third tax rate 
        ttrlabel.set_markup("Third tax rate")        
        self.ttrentry = Gtk.Entry()
        #-----------------------------------------------
        
        #----------------------------------------------
                
        ftname_label = Gtk.Label() #first tax 
        ftname_label.set_markup("First tax column name")        
        self.ftname_entry = Gtk.Entry()
        
        stname_label = Gtk.Label() #second tax 
        stname_label.set_markup("Second tax column name")        
        self.stname_entry = Gtk.Entry()
        
        ttname_label = Gtk.Label() #thirdd tax
        ttname_label.set_markup("Third tax column name")        
        self.ttname_entry = Gtk.Entry()
        
        #-----------------------------------------------
        
        tresetbutton = Gtk.Button.new_with_label("Reset")
        #tresetbutton.get_style_context().add_class("suggested-action")
        tresetbutton.set_margin_top(20)
        #tresetbutton.connect("clicked", self.processtslab, self.ctwidgets, guiinvoicingins)     
        
        tcreatebutton = Gtk.Button.new_with_label("Create slab")
        tcreatebutton.get_style_context().add_class("suggested-action")
        tcreatebutton.set_margin_top(20)
        #tcreatebutton.connect("clicked", self.processtslab, self.ctwidgets, guiinvoicingins)       
        
        
        #####################
        
        tslabs_offsetter = Gtk.Label()
        tslabs_offsetter.set_markup('           ') 
        tslabs_offsetter.set_width_chars(16) 
        #tslabs_offsetter.set_margin_top(20)
        
        tslabs_listlabel = Gtk.Label()
        tslabs_listlabel.set_markup('List of tax slabs') 
        #tslabs_listlabel.set_margin_bottom(20)
        
        self.tscombo = Gtk.ComboBoxText.new_with_entry()
        for ets in guicommon.taxtableins.rowlist:
            self.tscombo.append_text(ets)
            #print (ets)
        self.tscombo.set_active(0)
        self.tscombo.set_hexpand(False)
        self.tscombo.set_halign(Gtk.Align.CENTER)
        self.tscombo.get_child().set_width_chars(32)     
        
        tsdeletebutton = Gtk.Button.new_with_label("Delete")
        tsdeletebutton.get_style_context().add_class("dangerbutton")
        tsdeletebutton.set_margin_top(20)
        #tsdeletebutton.connect("clicked", self.deletets)
        tsdeletebutton.set_halign(Gtk.Align.CENTER) # to avoid expansion horizontally
        
        #######################
        
        
        gridcts.add(tnamelabel)
        gridcts.attach(self.tnameentry, 1, 0, 1, 1)
        gridcts.attach(enable_firsttax_label, 0, 1, 1, 1)
        gridcts.attach(self.firsttax_button, 1, 1, 1, 1)
        gridcts.attach(enable_secondtax_label, 0, 2, 1, 1)
        gridcts.attach(self.secondtax_button, 1, 2, 1, 1)
        gridcts.attach(enable_thirdtax_label, 0, 3, 1, 1)
        gridcts.attach(self.thirdtax_button, 1, 3, 1, 1)
        
        gridcts.attach(ftrlabel, 0, 4, 1, 1)
        gridcts.attach(self.ftrentry, 1, 4, 1, 1)
        gridcts.attach(strlabel, 0, 5, 1, 1)
        gridcts.attach(self.strentry, 1, 5, 1, 1)
        gridcts.attach(ttrlabel, 0, 6, 1, 1)
        gridcts.attach(self.ttrentry, 1, 6, 1, 1)
        
        
        gridcts.attach(ftname_label, 0, 8, 1, 1)
        gridcts.attach(self.ftname_entry, 1, 8, 1, 1)
        gridcts.attach(stname_label, 0, 9, 1, 1)
        gridcts.attach(self.stname_entry, 1, 9, 1, 1)
        gridcts.attach(ttname_label, 0, 10, 1, 1)
        gridcts.attach(self.ttname_entry, 1, 10, 1, 1)
        
        gridcts.attach(tresetbutton, 0, 11, 1, 1)
        gridcts.attach(tcreatebutton, 1, 11, 1, 1)        
        
        gridcts.attach(tslabs_offsetter, 2, 0, 1, 1)
        gridcts.attach(tslabs_listlabel, 3, 0, 1, 1)
        gridcts.attach(self.tscombo, 3, 1, 1, 1)
        gridcts.attach(tsdeletebutton, 3, 2, 1, 1)
                   
        tmbox.show_all()
        return tmbox






