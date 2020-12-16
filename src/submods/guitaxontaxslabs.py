from submods import functions
from submods import guicommon
import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkTaxonTaxSlabs():


    def generatepage(self, invoicingbox, bph, guiinvoicingins, mainwindow):
        
        self.invoicingbox=invoicingbox
        self.bph=bph
        self.guiinvoicingins=guiinvoicingins
        self.mainwindow=mainwindow
        
        tot_mainbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20) #taxontax_main box
        
        totcreate_label = Gtk.Label()
        totcreate_label.set_markup("Create a new tax on tax slab")   
        totcreate_label.set_halign(Gtk.Align.START) 
        totcreate_label.set_hexpand(False)     
        tot_mainbox.pack_start(totcreate_label, False, False, 10)
        
        gridtots = Gtk.Grid() #tax on tax slab
        tot_mainbox.pack_start(gridtots, True, True, 0)

        snamelabel = Gtk.Label()
        snamelabel.set_markup("Slab name")        
        self.snameentry = Gtk.Entry()

        
        #==============================================
        
        enable_firsttax_label = Gtk.Label()
        enable_firsttax_label.set_markup("Enable first tax ")
        enable_firsttax_label.set_margin_top(10)
        
        self.firsttax_button = Gtk.CheckButton()
        self.firsttax_button.set_margin_top(10)
        self.firsttax_button.set_active(True) # By default true
        
        enable_secondtax_label = Gtk.Label()
        enable_secondtax_label.set_markup("Enable second tax ")
        enable_secondtax_label.set_margin_top(10)
        
        self.secondtax_button = Gtk.CheckButton()
        self.secondtax_button.set_margin_top(10)
        self.secondtax_button.set_active(False) # By default false
        
        enable_thirdtax_label = Gtk.Label()
        enable_thirdtax_label.set_markup("Enable third tax  ")
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
        ftname_label.set_markup("First tax name")        
        self.ftname_entry = Gtk.Entry()
        
        stname_label = Gtk.Label() #second tax 
        stname_label.set_markup("Second tax name")        
        self.stname_entry = Gtk.Entry()
        
        ttname_label = Gtk.Label() #thirdd tax
        ttname_label.set_markup("Third tax name")        
        self.ttname_entry = Gtk.Entry()
        
        #-----------------------------------------------
        
        tresetbutton = Gtk.Button.new_with_label("Reset")
        #tresetbutton.get_style_context().add_class("suggested-action")
        tresetbutton.set_margin_top(20)
        #tresetbutton.connect("clicked", self.processtslab, self.ctwidgets, guiinvoicingins)     
        
        tcreatebutton = Gtk.Button.new_with_label("Create slab")
        tcreatebutton.get_style_context().add_class("suggested-action")
        tcreatebutton.set_margin_top(20)
        tcreatebutton.connect("clicked", self.process_taxnewslab)       
        
        
        #####################
        
        tslabs_offsetter = Gtk.Label()
        tslabs_offsetter.set_markup('           ') 
        tslabs_offsetter.set_width_chars(16) 
        #tslabs_offsetter.set_margin_top(20)
        
        totslabs_listlabel = Gtk.Label()
        totslabs_listlabel.set_markup('List of tax on tax slabs') 
        #totslabs_listlabel.set_margin_bottom(20)
        
        self.totl_combo = Gtk.ComboBoxText.new_with_entry() #tax on tax list
        for etots in guicommon.taxontax_list:
            self.totl_combo.append_text(etots)
            #print (etots)
        self.totl_combo.set_active(0)
        self.totl_combo.set_hexpand(False)
        self.totl_combo.set_halign(Gtk.Align.CENTER)
        self.totl_combo.get_child().set_width_chars(32)     
        
        totsdeletebutton = Gtk.Button.new_with_label("Delete") #taxontax slab
        totsdeletebutton.get_style_context().add_class("dangerbutton")
        totsdeletebutton.set_margin_top(20)
        totsdeletebutton.connect("clicked", self.delete_slab)
        totsdeletebutton.set_halign(Gtk.Align.CENTER) # to avoid expansion horizontally
        
        #######################
        
        
        gridtots.add(snamelabel)
        gridtots.attach(self.snameentry, 1, 0, 1, 1)
        gridtots.attach(enable_firsttax_label, 0, 1, 1, 1)
        gridtots.attach(self.firsttax_button, 1, 1, 1, 1)
        gridtots.attach(enable_secondtax_label, 0, 2, 1, 1)
        gridtots.attach(self.secondtax_button, 1, 2, 1, 1)
        gridtots.attach(enable_thirdtax_label, 0, 3, 1, 1)
        gridtots.attach(self.thirdtax_button, 1, 3, 1, 1)
        
        gridtots.attach(ftrlabel, 0, 4, 1, 1)
        gridtots.attach(self.ftrentry, 1, 4, 1, 1)
        gridtots.attach(strlabel, 0, 5, 1, 1)
        gridtots.attach(self.strentry, 1, 5, 1, 1)
        gridtots.attach(ttrlabel, 0, 6, 1, 1)
        gridtots.attach(self.ttrentry, 1, 6, 1, 1)
        
        
        gridtots.attach(ftname_label, 0, 8, 1, 1)
        gridtots.attach(self.ftname_entry, 1, 8, 1, 1)
        gridtots.attach(stname_label, 0, 9, 1, 1)
        gridtots.attach(self.stname_entry, 1, 9, 1, 1)
        gridtots.attach(ttname_label, 0, 10, 1, 1)
        gridtots.attach(self.ttname_entry, 1, 10, 1, 1)
        
        gridtots.attach(tresetbutton, 0, 11, 1, 1)
        gridtots.attach(tcreatebutton, 1, 11, 1, 1)        
        
        gridtots.attach(tslabs_offsetter, 2, 0, 1, 1)
        gridtots.attach(totslabs_listlabel, 3, 0, 1, 1)
        gridtots.attach(self.totl_combo, 3, 1, 1, 1)
        gridtots.attach(totsdeletebutton, 3, 2, 1, 1)
                   
        tot_mainbox.show_all()
        return tot_mainbox


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
        
        f_tot_rate=float(self.ftrentry.get_text())
        s_tot_rate=float(self.strentry.get_text())
        t_tot_rate=float(self.ttrentry.get_text())
        total_tot_rate=f_tot_rate+s_tot_rate+t_tot_rate
        
        newslab_data=[self.snameentry.get_text(), ftenabled, stenabled , ttenabled, self.ftname_entry.get_text(), self.stname_entry.get_text(), self.ttname_entry.get_text(), f_tot_rate, s_tot_rate, t_tot_rate, total_tot_rate]
        
        slabslist=guicommon.miscdbins.get('taxontaxslabsdata') #this one is previous
        slabslist.append(newslab_data) #do not use another variable for updated list, it will delete all data & return none
        guicommon.taxontax_list.append(self.snameentry.get_text())
        guicommon.miscdbins.set('taxontaxslabsdata', slabslist) 
        guicommon.miscdbins.dump()
        self.totl_combo.append_text(self.snameentry.get_text())

        print('Added new tax on tax slab')
        self.snameentry.set_text('')
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
        self.bph=self.guiinvoicingins.generatepage(self.mainwindow)
        self.invoicingbox.add(self.bph)
        self.invoicingbox.show_all()        


    def delete_slab(self, button):
        td=self.totl_combo.get_active_text()
        td_index=guicommon.taxontax_list.index(td)
        del guicommon.taxontax_list[td_index]
        del guicommon.taxontax_data[td_index]
        guicommon.miscdbins.dump()
        guicommon.loadguicommon()
        
        self.totl_combo.remove_all()
        for etots in guicommon.taxontax_list:
            self.totl_combo.append_text(etots)
        self.totl_combo.get_child().set_text('Select')
        
        children=self.invoicingbox.get_children()
        for eachchild in children:
            self.invoicingbox.remove(eachchild)
            eachchild.destroy()
        self.bph=self.guiinvoicingins.generatepage(self.mainwindow)
        self.invoicingbox.add(self.bph)
        self.invoicingbox.show_all()        

