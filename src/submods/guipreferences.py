from submods import functions
from submods import guicommon
import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkPreferences():


    def generatepage(self, mainwindow):
        
        pref_mainbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10) 
        
        prefgrid = Gtk.Grid() #tax on tax slab
        pref_mainbox.pack_start(prefgrid, True, True, 0)
        
        blank_label = Gtk.Label()
        blank_label.set_markup(" ")
        #blank_label.set_margin_top(10)
       
        autoinvoice_label = Gtk.Label()
        autoinvoice_label.set_markup("Automatic invoice numbering  ")
        autoinvoice_label.set_margin_top(2)
        autoinvoice_label.set_sensitive(False)
        
        self.autoinv_button = Gtk.CheckButton()
        self.autoinv_button.set_margin_top(2)
        self.autoinv_button.set_active(False) # By default true
        self.autoinv_button.set_sensitive(False)
        
        round_label = Gtk.Label()
        round_label.set_markup("Roundoff by default ")
        #round_label.set_margin_top(10)
        
        self.round_button = Gtk.CheckButton()
        self.round_button.set_margin_top(10)
        self.round_button.set_margin_bottom(10)
        self.round_button.set_active(True) # By default true
        
        #other_label = Gtk.Label()
        #other_label.set_markup("Other toggle for future ")
        #other_label.set_margin_top(10)
        
        #self.toggle_button = Gtk.CheckButton()
        #self.toggle_button.set_margin_top(10)
        #self.toggle_button.set_margin_bottom(10)
        #self.toggle_button.set_active(False) # By default true
        
        #hidepurchase_label = Gtk.Label()
        #hidepurchase_label.set_markup("Hide purchase data ")
        #hidepurchase_label.set_margin_top(10)
        #hidepurchase_label.set_sensitive(False)
        
        self.hp_button = Gtk.CheckButton()
        #self.hp_button.set_margin_top(10)
        self.hp_button.set_active(False) # By default true
        #self.hp_button.set_margin_bottom(10)
        self.hp_button.set_sensitive(False)        
        #add reading from miscdb here, password for purchase hiding
                
        inv_prefixlabel = Gtk.Label() 
        inv_prefixlabel.set_markup("Invoice numbering prefix ")        
        self.inv_prefixentry = Gtk.Entry()
        self.inv_prefixentry.set_hexpand(False)
        self.inv_prefixentry.set_halign(Gtk.Align.START)
        self.inv_prefixentry.set_width_chars(10)
        self.inv_prefixentry.set_max_length(8)
       
        tl1_label = Gtk.Label() #Terms line 1
        tl1_label.set_markup("Terms and conditions line 1 ")        
        self.tl1_entry = Gtk.Entry()
        self.tl1_entry.set_max_length(47)
        self.tl1_entry.set_width_chars(47)
        
        tl2_label = Gtk.Label() #Terms line 2
        tl2_label.set_markup("Terms and conditions line 2 ")        
        self.tl2_entry = Gtk.Entry()
        self.tl2_entry.set_max_length(47)
        
        tl3_label = Gtk.Label() #Terms line 3
        tl3_label.set_markup("Terms and conditions line 3 ")        
        self.tl3_entry = Gtk.Entry()
        self.tl3_entry.set_max_length(47)
        
        tl4_label = Gtk.Label() #Terms line 4
        tl4_label.set_markup("Terms and conditions line 4 ")        
        self.tl4_entry = Gtk.Entry()
        self.tl4_entry.set_max_length(47)
        
        tl5_label = Gtk.Label() #Terms line 5
        tl5_label.set_markup("Terms and conditions line 5 ")        
        self.tl5_entry = Gtk.Entry()
        self.tl5_entry.set_max_length(47)
       
        bank_details_label = Gtk.Label() 
        bank_details_label.set_markup("Bank details: A/c no.  ")        
        self.bankacc_entry = Gtk.Entry()
        self.bankacc_entry.set_max_length(47)
        
        bankifsc_label = Gtk.Label()
        bankifsc_label.set_markup("Bank details: IFSC  ")        
        self.ifsc_entry = Gtk.Entry()
        self.ifsc_entry.set_max_length(47)
        
        bankname_label = Gtk.Label()
        bankname_label.set_markup("Additional bank details ")        
        self.bankname_entry = Gtk.Entry()
        self.bankname_entry.set_max_length(47)
      
        
        pcancelbutton = Gtk.Button.new_with_label("Cancel")
        #pcancelbutton.get_style_context().add_class("suggested-action")
        pcancelbutton.set_margin_top(20)
        pcancelbutton.connect("clicked", self.load_preferences)           
        
        psavebutton = Gtk.Button.new_with_label("Save changes")
        psavebutton.get_style_context().add_class("suggested-action")
        psavebutton.set_margin_top(20)
        psavebutton.connect("clicked", self.process_preferences)               
        
        prefgrid.add(blank_label)
        prefgrid.attach(autoinvoice_label, 0, 1, 1, 1)
        prefgrid.attach(self.autoinv_button, 1, 1, 1, 1)
        #prefgrid.attach(hidepurchase_label, 0, 1, 1, 1)
        #prefgrid.attach(self.hp_button, 1, 1, 1, 1)
        prefgrid.attach(round_label, 0, 2, 1, 1)
        prefgrid.attach(self.round_button, 1, 2, 1, 1)
        #prefgrid.attach(other_label, 0, 3, 1, 1)
        #prefgrid.attach(self.toggle_button, 1, 3, 1, 1)
       
        prefgrid.attach(inv_prefixlabel, 0, 5, 1, 1)
        prefgrid.attach(self.inv_prefixentry, 1, 5, 1, 1)
        prefgrid.attach(tl1_label, 0, 6, 1, 1)
        prefgrid.attach(self.tl1_entry, 1, 6, 1, 1)      
        prefgrid.attach(tl2_label, 0, 7, 1, 1)
        prefgrid.attach(self.tl2_entry, 1, 7, 1, 1)
        prefgrid.attach(tl3_label, 0, 8, 1, 1)
        prefgrid.attach(self.tl3_entry, 1, 8, 1, 1)
        prefgrid.attach(tl4_label, 0, 9, 1, 1)
        prefgrid.attach(self.tl4_entry, 1, 9, 1, 1)
        prefgrid.attach(tl5_label, 0, 10, 1, 1)
        prefgrid.attach(self.tl5_entry, 1, 10, 1, 1)
        prefgrid.attach(bank_details_label, 0, 12, 1, 1)
        prefgrid.attach(self.bankacc_entry, 1, 12, 1, 1)
        prefgrid.attach(bankifsc_label, 0, 13, 1, 1)
        prefgrid.attach(self.ifsc_entry, 1, 13, 1, 1)
        prefgrid.attach(bankname_label, 0, 14, 1, 1)
        prefgrid.attach(self.bankname_entry, 1, 14, 1, 1)
       
        ph_box= Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0) 
        ph_box.set_hexpand(False)
        ph_box.set_halign(Gtk.Align.START)
        ph_box.pack_start(pcancelbutton, False, False, 0)     
        ph_box.pack_start(psavebutton, False, False, 0)  
        pref_mainbox.pack_start(ph_box, False, False, 10)
         
        preflabel = Gtk.Label()
        preflabel.set_markup("Some features will be enabled in future.")
        pref_mainbox.pack_start(preflabel, False, False, 10)
        
        self.load_preferences('mimicbutton')
                   
        pref_mainbox.show_all()
        return pref_mainbox


    def process_preferences(self, button):
        #self.autoinv_button, self.round_button, self.hp_button, self.inv_prefixentry, self.tl1_entry, self.tl2_entry, self.tl3_entry, self.tl4_entry   

        guicommon.miscdbins.set('invoiceprefix', self.inv_prefixentry.get_text())
        guicommon.miscdbins.set('termsline1', self.tl1_entry.get_text())
        guicommon.miscdbins.set('termsline2', self.tl2_entry.get_text())
        guicommon.miscdbins.set('termsline3', self.tl3_entry.get_text())
        guicommon.miscdbins.set('termsline4', self.tl4_entry.get_text())
        guicommon.miscdbins.set('termsline5', self.tl5_entry.get_text())
        guicommon.miscdbins.set('mybankaccountnmbr', self.bankacc_entry.get_text())
        guicommon.miscdbins.set('mybankifsc', self.ifsc_entry.get_text())
        guicommon.miscdbins.set('mybankname', self.bankname_entry.get_text())
        
        if self.round_button.get_active():
            guicommon.miscdbins.set('roundoffenabled', 'yes')
        else:    
            guicommon.miscdbins.set('roundoffenabled', 'no')  
            
        if self.autoinv_button.get_active():    
            guicommon.miscdbins.set('autoinvoice_numbering', 'yes')
        else:
            guicommon.miscdbins.set('autoinvoice_numbering', 'no')
            
        if self.hp_button.get_active():    
            guicommon.miscdbins.set('hidepurchasedata', 'yes')
        else:
            guicommon.miscdbins.set('hidepurchasedata', 'no')    
        guicommon.miscdbins.dump()

    def load_preferences(self, button):
    
        if guicommon.miscdbins.get('autoinvoice_numbering')=='yes':                
            self.autoinv_button.set_active(True)
            invoiceprefix_val=guicommon.miscdbins.get('invoiceprefix')
            self.inv_prefixentry.set_sensitive(True)
        else:
            self.autoinv_button.set_active(False)
            invoiceprefix_val='Disabled'
            self.inv_prefixentry.set_sensitive(False)
            
        self.inv_prefixentry.set_text(invoiceprefix_val)
        self.tl1_entry.set_text(guicommon.miscdbins.get('termsline1'))
        self.tl2_entry.set_text(guicommon.miscdbins.get('termsline2'))
        self.tl3_entry.set_text(guicommon.miscdbins.get('termsline3'))
        self.tl4_entry.set_text(guicommon.miscdbins.get('termsline4'))
        self.tl5_entry.set_text(guicommon.miscdbins.get('termsline5'))
        self.bankacc_entry.set_text(guicommon.miscdbins.get('mybankaccountnmbr'))
        self.ifsc_entry.set_text(guicommon.miscdbins.get('mybankifsc'))
        self.bankname_entry.set_text(guicommon.miscdbins.get('mybankname'))
        
        
        if guicommon.miscdbins.get('roundoffenabled')=='yes':                
            self.round_button.set_active(True)
        else:
            self.round_button.set_active(False)
            

