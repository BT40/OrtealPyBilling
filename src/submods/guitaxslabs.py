from submods import functions
from submods import guicommon
import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkTaxSlabs():


    def generatepage(self, invoicingbox, bph, guiinvoicingins, mainwindow):
        self.invoicingbox=invoicingbox
        self.bph=bph
        self.guiinvoicingins=guiinvoicingins
        self.mainwindow=mainwindow
        
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
        self.ftrentry.set_text('0')
                
        strlabel = Gtk.Label() #second tax rate
        strlabel.set_markup("Second tax rate")        
        self.strentry = Gtk.Entry()
        self.strentry.set_text('0')
                
        ttrlabel = Gtk.Label() #third tax rate 
        ttrlabel.set_markup("Third tax rate")        
        self.ttrentry = Gtk.Entry()
        self.ttrentry.set_text('0')
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
        tresetbutton.connect("clicked", self.reset_fields)     
        
        tcreatebutton = Gtk.Button.new_with_label("Create slab")
        tcreatebutton.get_style_context().add_class("suggested-action")
        tcreatebutton.set_margin_top(20)
        tcreatebutton.connect("clicked", self.process_taxnewslab)       
        
        
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
        tsdeletebutton.connect("clicked", self.delete_slab)
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


    def process_taxnewslab(self, event):
        
        if self.firsttax_button.get_active():
            ftenabled='y'
        else:
            ftenabled='n' 
           
        if self.secondtax_button.get_active():
            stenabled='y'
        else:
            stenabled='n'     
         
        if self.thirdtax_button.get_active():
            ttenabled='y'
        else:
            ttenabled='n'        
        
        ft_rate=float(self.ftrentry.get_text())
        st_rate=float(self.strentry.get_text())
        tt_rate=float(self.ttrentry.get_text())
        total_t_rate=ft_rate+st_rate+tt_rate
        
        newslab_data=[self.tnameentry.get_text(), ftenabled, stenabled , ttenabled, self.ftname_entry.get_text(), self.stname_entry.get_text(), self.ttname_entry.get_text(), ft_rate, st_rate, tt_rate, total_t_rate]       
        print(newslab_data)
        guicommon.taxtableins.createrow(self.tnameentry.get_text(), newslab_data)
        guicommon.loadguicommon()
        
        self.tscombo.append_text(self.tnameentry.get_text())
        print('Added new tax slab')
        self.tnameentry.set_text('')
        self.ftname_entry.set_text('')
        self.stname_entry.set_text('')
        self.ttname_entry.set_text('')
        self.ftrentry.set_text('0')
        self.strentry.set_text('0')
        self.ttrentry.set_text('0')
        self.secondtax_button.set_active(False)
        self.thirdtax_button.set_active(False)
        
        children=self.invoicingbox.get_children()
        for eachchild in children:
            self.invoicingbox.remove(eachchild)
            eachchild.destroy()
        self.bph=self.guiinvoicingins.generatepage(self.mainwindow, self.guiinvoicingins)
        self.invoicingbox.add(self.bph)
        self.invoicingbox.show_all()        


    def delete_slab(self, button):
        td=self.tscombo.get_active_text()
        guicommon.taxtableins.deleterow(td)
        guicommon.loadguicommon()
        
        self.tscombo.remove_all()       
        for ets in guicommon.taxtableins.rowlist:
            self.tscombo.append_text(ets)
        self.tscombo.get_child().set_text('Select')
        
        children=self.invoicingbox.get_children()
        for eachchild in children:
            self.invoicingbox.remove(eachchild)
            eachchild.destroy()
        self.bph=self.guiinvoicingins.generatepage(self.mainwindow, self.guiinvoicingins)
        self.invoicingbox.add(self.bph)
        self.invoicingbox.show_all()        


    def reset_fields(self, button):
        
        self.firsttax_button.set_active(True)
        self.secondtax_button.set_active(False)
        self.thirdtax_button.set_active(False)
        
        self.tnameentry.set_text('')
        self.ftname_entry.set_text('')
        self.stname_entry.set_text('')
        self.ttname_entry.set_text('')        
        self.ftrentry.set_text('')
        self.strentry.set_text('')
        self.ttrentry.set_text('')
       
        
        

