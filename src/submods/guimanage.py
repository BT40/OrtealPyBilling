from submods import functions
from submods import guicommon
from submods import guimanagestates 
from submods import guimycompany
import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkManage():


    def generatepage(self, invoicingbox, bph, guiinvoicingins,  companybox, cph, guicompanyins, mainwindow):
        self.invoicingbox=invoicingbox
        self.bph=bph
        self.guiinvoicingins=guiinvoicingins
        self.companybox=companybox
        self.cph=cph
        self.guicompanyins=guicompanyins
        self.mainwindow=mainwindow
        md=guimycompany.GtkMyComp() #instance
        
        
        tmbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10) #main box
        
        screate_label = Gtk.Label()
        screate_label.set_markup("Manage entities; Press relavant button ")   
        screate_label.set_halign(Gtk.Align.START) 
        screate_label.set_hexpand(False)     
        tmbox.pack_start(screate_label, False, False, 5)
        
        
        self.yourcompany_button = Gtk.Button.new_with_label("Your company details")
        #self.yourcompany_button.set_margin_top(1)
        self.yourcompany_button.set_halign(Gtk.Align.START)
        self.yourcompany_button.connect("clicked", self.edit_companydetails, mainwindow, md)   
        
        tmbox.pack_start(self.yourcompany_button, False, False, 0)   
        
        tstatebutton = Gtk.Button.new_with_label("Edit geographical states")
        #tstatebutton.set_margin_top(2)
        tstatebutton.set_halign(Gtk.Align.START) 
        tstatebutton.connect("clicked", self.manage_states)     
               
        #tcountrybutton = Gtk.Button.new_with_label("Edit countries")
        #tcountrybutton.set_margin_top(20)
        #tcountrybutton.connect("clicked", self.manage_countries)     
        
        tmbox.pack_start(tstatebutton, False, False, 0)       
                   
        tmbox.show_all()
        return tmbox


    def manage_states(self, button):
        
        gms=guimanagestates.GtkGeoStates()
        gms.generatepage(self.mainwindow)
        guicommon.loadguicommon()
        
        children=self.invoicingbox.get_children()
        for eachchild in children:
            self.invoicingbox.remove(eachchild)
            eachchild.destroy()
        self.bph=self.guiinvoicingins.generatepage(self.mainwindow, self.guiinvoicingins)
        self.invoicingbox.add(self.bph)
        self.invoicingbox.show_all()        
        
        cchildren=self.companybox.get_children()
        for eachcchild in cchildren:
            self.companybox.remove(eachcchild)
            eachcchild.destroy()
        self.cph=self.guicompanyins.generatepage(self.invoicingbox, self.bph, self.guiinvoicingins, self.mainwindow)
        self.companybox.add(self.cph)
        self.companybox.show_all()        


   
    def edit_companydetails(self, button, mainwindow, md):
        md.editcompany_dialog(mainwindow)
    

