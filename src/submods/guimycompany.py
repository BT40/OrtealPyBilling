# This file contains gui for more section dialogs


#from submods import guicommon

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk
from submods import guicommon
from submods import functions



class GtkMyComp():
     

    def editcompany_dialog (self, parentwindow):

        edit_dialog = Gtk.Dialog('Edit your company details', parentwindow, Gtk.DialogFlags.MODAL)
        contentgrid = Gtk.Grid()     
        contentgrid.set_column_homogeneous(False)
        contentgrid.set_row_homogeneous(True)       
        contentgrid.set_margin_top(10)
        contentgrid.set_margin_bottom(10)
        contentgrid.set_margin_right(40)
        contentgrid.set_margin_left(40)
        
        mode_label = Gtk.Label() 
        mode_label.set_markup("Add details of your company ")          
        
        companynamelabel = Gtk.Label() 
        companynamelabel.set_markup("Name  ")                    
        self.cnentry = Gtk.Entry() #company name
        self.cnentry.set_width_chars(47)
        self.cnentry.set_max_length(47)
        
        
        companygst_label = Gtk.Label() 
        companygst_label.set_markup("Tax ID or GST ")                    
        self.gst_entry = Gtk.Entry() 
        self.gst_entry.set_width_chars(32)
        self.gst_entry.set_max_length(32)  
        self.gst_entry.set_halign(Gtk.Align.START)  
        self.gst_entry.set_hexpand(False) 
        
        companyaddress_label = Gtk.Label() 
        companyaddress_label.set_markup("Address  ")                    
        self.ca_entry = Gtk.Entry() #company address
        self.ca_entry.set_width_chars(47)
        self.ca_entry.set_max_length(47)
        
        companycity_label = Gtk.Label() 
        companycity_label.set_markup("City  ")                    
        self.ccity_entry = Gtk.Entry() #company city
        self.ccity_entry.set_width_chars(32)
        self.ccity_entry.set_max_length(32)
        
        cpin_label = Gtk.Label() #company pin
        cpin_label.set_markup("PIN ")                    
        self.cpin_entry = Gtk.Entry() 
        self.cpin_entry.set_width_chars(16)
        self.cpin_entry.set_max_length(16)  
        self.cpin_entry.set_halign(Gtk.Align.START)  
        

        cstate_label = Gtk.Label() 
        cstate_label.set_markup("State ")                    
        self.cstate_combo = Gtk.ComboBoxText.new_with_entry() 
        for es in guicommon.state_list:
            self.cstate_combo.append_text(es)
        self.cstate_combo.set_hexpand(False)
        self.cstate_combo.set_halign(Gtk.Align.CENTER)
        self.cstate_combo.get_child().set_width_chars(24)     
        self.cstate_combo.set_halign(Gtk.Align.START)        
        
        ccountry_label = Gtk.Label() 
        ccountry_label.set_markup("Country ")                    
        
        
        self.cccombo = Gtk.ComboBoxText.new_with_entry()
        for countryname in functions.countrieslist:
            self.cccombo.append_text(countryname)
        self.cccombo.set_active(75)
        
        ccompleter = Gtk.EntryCompletion()
        ccompleter.set_model(self.cccombo.get_model())
        ccompleter.set_text_column(0)
        self.cccombo.get_child().set_completion(ccompleter)     
        
        cphone_label = Gtk.Label() 
        cphone_label.set_markup("Phone ")                    
        self.cphone_entry = Gtk.Entry() 
        self.cphone_entry.set_width_chars(18)
        self.cphone_entry.set_max_length(16)    
        self.cphone_entry.set_halign(Gtk.Align.START)    
        
        cmail_label = Gtk.Label() 
        cmail_label.set_markup("Email ")                    
        self.cmail_entry = Gtk.Entry() 
        self.cmail_entry.set_width_chars(32)
        self.cmail_entry.set_max_length(32)    
        self.cmail_entry.set_halign(Gtk.Align.START)   
        
        
        cstatecode_label = Gtk.Label() 
        cstatecode_label.set_markup("State code GST ")                    
        self.cstatecode_entry = Gtk.Entry() 
        self.cstatecode_entry.set_width_chars(8)
        self.cstatecode_entry.set_max_length(2)    
        self.cstatecode_entry.set_halign(Gtk.Align.START)                                        
        
        contentgrid.add(mode_label)
        contentgrid.attach(companynamelabel, 0, 1, 1, 1)
        contentgrid.attach(self.cnentry, 1, 1, 1, 1)       
        contentgrid.attach(companygst_label, 0, 2, 1, 1)
        contentgrid.attach(self.gst_entry, 1, 2, 1, 1)        
        contentgrid.attach(companyaddress_label, 0, 3, 1, 1)
        contentgrid.attach(self.ca_entry, 1, 3, 1, 1)
        contentgrid.attach(companycity_label, 0, 5, 1, 1)
        contentgrid.attach(self.ccity_entry, 1, 5, 1, 1)
        contentgrid.attach(cpin_label, 0, 6, 1, 1)
        contentgrid.attach(self.cpin_entry, 1, 6, 1, 1)
        contentgrid.attach(cstate_label, 0, 7, 1, 1)
        contentgrid.attach(self.cstate_combo, 1, 7, 1, 1)
        contentgrid.attach(ccountry_label , 0, 8, 1, 1)
        contentgrid.attach(self.cccombo, 1, 8, 1, 1)
        contentgrid.attach(cphone_label, 0, 9, 1, 1)
        contentgrid.attach(self.cphone_entry, 1, 9, 1, 1)
        contentgrid.attach(cmail_label, 0, 10, 1, 1)
        contentgrid.attach(self.cmail_entry, 1, 10, 1, 1)
        contentgrid.attach(cstatecode_label, 0, 12, 1, 1)
        contentgrid.attach(self.cstatecode_entry, 1, 12, 1, 1)
        
        edit_dialog.vbox.add(contentgrid)
        contentgrid.show_all()    
        
        donebutton= edit_dialog.add_button('Done', 1)
        donebutton.set_margin_bottom(20)
        donebutton.get_parent().set_halign(Gtk.Align.CENTER)
        #donebutton.get_style_context().add_class("suggested-action")
        
        self.load_mycompany_data()    
            
        response = edit_dialog.run()
        if response==1:           
            guicommon.miscdbins.set('mycompanyname', self.cnentry.get_text())
            guicommon.miscdbins.set('mycompanyaddress', self.ca_entry.get_text())
            guicommon.miscdbins.set('mycompanygstin', self.gst_entry.get_text())
            guicommon.miscdbins.set('mycompanycity', self.ccity_entry.get_text())
            guicommon.miscdbins.set('mycompanypin', self.cpin_entry.get_text())
            guicommon.miscdbins.set('mycompanystate', self.cstate_combo.get_active_text())
            guicommon.miscdbins.set('mycompanycountry', self.cccombo.get_active_text())
            guicommon.miscdbins.set('mycompanystatecode', self.cstatecode_entry.get_text())
            guicommon.miscdbins.set('mycompanyphone', self.cphone_entry.get_text())
            guicommon.miscdbins.set('mycompanyemail', self.cmail_entry.get_text())            
            guicommon.miscdbins.dump()
                       
        else:
            pass    
        

        edit_dialog.destroy()
        #print('edit mycompany dialog complete')
    
    
    def load_mycompany_data(self):  
    
        self.cnentry.set_text(guicommon.miscdbins.get('mycompanyname'))
        self.gst_entry.set_text(guicommon.miscdbins.get('mycompanygstin'))
        self.ca_entry.set_text(guicommon.miscdbins.get('mycompanyaddress'))
        self.ccity_entry.set_text(guicommon.miscdbins.get('mycompanycity'))
        self.cpin_entry.set_text(guicommon.miscdbins.get('mycompanypin'))
        self.cstate_combo.get_child().set_text(guicommon.miscdbins.get('mycompanystate'))
        self.cccombo.get_child().set_text(guicommon.miscdbins.get('mycompanycountry'))
        self.cphone_entry.set_text(guicommon.miscdbins.get('mycompanyphone'))
        self.cmail_entry.set_text(guicommon.miscdbins.get('mycompanyemail'))
        self.cstatecode_entry.set_text(guicommon.miscdbins.get('mycompanystatecode'))
    
            

