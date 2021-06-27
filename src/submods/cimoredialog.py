# This file contains gui for more button sale invoice

#from submods import functions
#from submods import guicommon

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk
from submods import guicommon



class CImore():
     

    def more_things (self, parentwindow, billcomments, ewaybill, furtherterms, rcvalue, transport_mode, companyname, ship_name, ship_addline, ship_state, ship_phone, ship_pin, more_opened, compchange_detector, ship_statecode):
        #this modifies the pre-initiated default values

        more_dialog = Gtk.Dialog('More options', parentwindow, Gtk.DialogFlags.MODAL)
        contentgrid = Gtk.Grid()     
        contentgrid.set_column_homogeneous(False)
        contentgrid.set_row_homogeneous(True)       
        contentgrid.set_margin_top(10)
        contentgrid.set_margin_bottom(10)
        contentgrid.set_margin_right(40)
        contentgrid.set_margin_left(40)
        
        mode_label = Gtk.Label() 
        mode_label.set_markup("  ")          
        
        rc_label = Gtk.Label("Reverse charge GST")       
        self.rccombo = Gtk.ComboBoxText()
        self.rccombo.set_halign(Gtk.Align.START)
        rclist=['No', 'Yes']
        self.rccombo.append_text(rclist[0])
        self.rccombo.append_text(rclist[1])
        if rcvalue=='No':
            self.rccombo.set_active(0)
        else: 
            self.rccombo.set_active(1) 
        
        ewaybill_label = Gtk.Label() # eway
        ewaybill_label.set_markup("E-WayBill No.")                    
        self.ewayentry = Gtk.Entry() #Bill comments entry
        self.ewayentry.set_text(ewaybill)
        self.ewayentry.set_width_chars(18)
        self.ewayentry.set_max_length(16)   
        self.ewayentry.set_hexpand(False)  
        self.ewayentry.set_halign(Gtk.Align.START)             
       
        billcommentslabel = Gtk.Label() # invoice comments
        billcommentslabel.set_markup("Comments")                    
        self.bcommentry = Gtk.Entry() #Bill comments entry
        self.bcommentry.set_width_chars(47)
        self.bcommentry.set_max_length(47)
        self.bcommentry.set_text(billcomments)
        
        furthertermsline1_label = Gtk.Label() 
        furthertermsline1_label.set_markup("Further terms")                    
        self.furthertermsline1_entry = Gtk.Entry() 
        self.furthertermsline1_entry.set_width_chars(47)
        self.furthertermsline1_entry.set_max_length(47)
        self.furthertermsline1_entry.set_text(furtherterms)
        
        transportmode_label = Gtk.Label() 
        transportmode_label.set_markup("Transport mode")                    
        self.transportmode_entry = Gtk.Entry() 
        self.transportmode_entry.set_width_chars(18)
        self.transportmode_entry.set_max_length(16)    
        self.transportmode_entry.set_halign(Gtk.Align.START)    
        self.transportmode_entry.set_text(transport_mode)           
        
        shippingname_label = Gtk.Label() 
        shippingname_label.set_markup("Shipped to:")                    
        self.shippingname_entry = Gtk.Entry() 
        self.shippingname_entry.set_width_chars(32)
        self.shippingname_entry.set_max_length(32)  
        self.shippingname_entry.set_halign(Gtk.Align.START)  
        self.shippingname_entry.set_hexpand(False) 
        
        shippingadd_label = Gtk.Label() 
        shippingadd_label.set_markup("Shipping address")                    
        self.shippingadd_entry = Gtk.Entry() 
        self.shippingadd_entry.set_width_chars(47)
        self.shippingadd_entry.set_max_length(80)   

        shippingstate_label = Gtk.Label() 
        shippingstate_label.set_markup("Shipping to state")                    
        self.shippingstate_entry = Gtk.Entry() 
        self.shippingstate_entry.set_width_chars(32)
        self.shippingstate_entry.set_max_length(32)  
        self.shippingstate_entry.set_halign(Gtk.Align.START)   
        
        self.state_combo = Gtk.ComboBoxText.new_with_entry() 
        for esn in guicommon.state_list:
            self.state_combo.append_text(esn)
        self.state_combo.set_hexpand(False)
        self.state_combo.set_halign(Gtk.Align.START)
        self.state_combo.get_child().set_width_chars(32)     
        
        shippingstatecode_label = Gtk.Label() 
        shippingstatecode_label.set_markup("State code (Shipping) ")                    
        self.shippingstatecode_entry = Gtk.Entry() 
        self.shippingstatecode_entry.set_width_chars(8)
        self.shippingstatecode_entry.set_max_length(2)  
        self.shippingstatecode_entry.set_halign(Gtk.Align.START)           
        
        shippingpin_label = Gtk.Label() 
        shippingpin_label.set_markup("Shipping city, PIN")                    
        self.shippingpin_entry = Gtk.Entry() 
        self.shippingpin_entry.set_width_chars(16)
        self.shippingpin_entry.set_max_length(16)  
        self.shippingpin_entry.set_halign(Gtk.Align.START)  
        
        sphone_label = Gtk.Label() 
        sphone_label.set_markup("Phone (shipped to) ")                    
        self.sphone_entry = Gtk.Entry() 
        self.sphone_entry.set_width_chars(18)
        self.sphone_entry.set_max_length(16)    
        self.sphone_entry.set_halign(Gtk.Align.START)                                         
        
        contentgrid.add(mode_label)
        contentgrid.attach(ewaybill_label, 0, 1, 1, 1)
        contentgrid.attach(self.ewayentry, 1, 1, 1, 1)       
        contentgrid.attach(billcommentslabel, 0, 2, 1, 1)
        contentgrid.attach(self.bcommentry, 1, 2, 1, 1)        
        contentgrid.attach(furthertermsline1_label, 0, 3, 1, 1)
        contentgrid.attach(self.furthertermsline1_entry, 1, 3, 1, 1)
        contentgrid.attach(transportmode_label, 0, 4, 1, 1)
        contentgrid.attach(self.transportmode_entry, 1, 4, 1, 1)
        contentgrid.attach(shippingname_label, 0, 5, 1, 1)
        contentgrid.attach(self.shippingname_entry, 1, 5, 1, 1)
        contentgrid.attach(shippingadd_label, 0, 6, 1, 1)
        contentgrid.attach(self.shippingadd_entry, 1, 6, 1, 1)
        contentgrid.attach(shippingstate_label, 0, 8, 1, 1)
        contentgrid.attach(self.state_combo, 1, 8, 1, 1)
        contentgrid.attach(shippingstatecode_label, 0, 9, 1, 1)
        contentgrid.attach(self.shippingstatecode_entry, 1, 9, 1, 1)
        contentgrid.attach(shippingpin_label, 0, 7, 1, 1)
        contentgrid.attach(self.shippingpin_entry, 1, 7, 1, 1)
        contentgrid.attach(sphone_label, 0, 10, 1, 1)
        contentgrid.attach(self.sphone_entry, 1, 10, 1, 1)
        contentgrid.attach(rc_label, 0, 12, 1, 1)
        contentgrid.attach(self.rccombo, 1, 12, 1, 1)
        
        more_dialog.vbox.add(contentgrid)
        contentgrid.show_all()    
        
        donebutton= more_dialog.add_button('Done', 1)
        donebutton.set_margin_bottom(20)
        donebutton.get_parent().set_halign(Gtk.Align.CENTER)
        #donebutton.get_style_context().add_class("suggested-action")
        
        
        
        if more_opened=='no': #load default values first time
            self.load_default_shipping(companyname)
            
        else: #if second time opening more dialog
            if compchange_detector==companyname: #load prev values if company name is unchanged
                self.load_prev_shipping(companyname, ship_name, ship_addline, ship_state, ship_phone, ship_pin, ship_statecode)          
            else: #reload new address as company is changed
                self.load_default_shipping(companyname)  
                
        response = more_dialog.run()
        if response==1:           
            ewaybill=self.ewayentry.get_text()
            billcomments=self.bcommentry.get_text()
            furtherterms=self.furthertermsline1_entry.get_text()
            transport_mode=self.transportmode_entry.get_text()
            ship_name=self.shippingname_entry.get_text()
            ship_addline=self.shippingadd_entry.get_text()
            ship_pin=self.shippingpin_entry.get_text()
            ship_state=self.state_combo.get_active_text()
            ship_statecode=self.shippingstatecode_entry.get_text()
            ship_phone=self.sphone_entry.get_text()
            rcvalue=self.rccombo.get_active_text()
                        
        else:  #same because closing dialog causes bug in which these parameters are set to 0
            ewaybill=self.ewayentry.get_text()
            billcomments=self.bcommentry.get_text()
            furtherterms=self.furthertermsline1_entry.get_text()
            transport_mode=self.transportmode_entry.get_text()
            ship_name=self.shippingname_entry.get_text()
            ship_addline=self.shippingadd_entry.get_text()
            ship_pin=self.shippingpin_entry.get_text()
            ship_state=self.state_combo.get_active_text()
            ship_statecode=self.shippingstatecode_entry.get_text()
            ship_phone=self.sphone_entry.get_text()
            rcvalue=self.rccombo.get_active_text()
            pass    
        

        more_dialog.destroy()
        #print('more dialog complete')
        return billcomments, ewaybill, furtherterms, rcvalue, transport_mode, ship_name, ship_addline, ship_state, ship_phone, ship_pin, companyname, ship_statecode
    
    
    def load_default_shipping(self, companyname):  #values same as original database
            customer_details=guicommon.companytableins.readrow(companyname)
            self.shippingname_entry.set_text(companyname)
            self.shippingadd_entry.set_text(customer_details[8])
            self.shippingpin_entry.set_text(customer_details[9]+','+ customer_details[12])
            self.state_combo.get_child().set_text(customer_details[10])
            self.shippingstatecode_entry.set_text(customer_details[17])
            self.sphone_entry.set_text(customer_details[13])
    
    
    def load_prev_shipping(self, companyname, ship_name, ship_addline, ship_state, ship_phone, ship_pin, ship_statecode): #load from prev values
            self.shippingname_entry.set_text(ship_name)
            self.shippingadd_entry.set_text(ship_addline)
            self.shippingpin_entry.set_text(ship_pin)
            self.state_combo.get_child().set_text(ship_state)
            self.shippingstatecode_entry.set_text(ship_statecode)
            self.sphone_entry.set_text(ship_phone)
            
    
    def not_more_things (self, parentwindow): #incorrect company name warning dialog
        
        not_more_dialog = Gtk.Dialog('Check company name', parentwindow, Gtk.DialogFlags.MODAL)
        
        nmt_labelbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)    
        nmt_labelbox.set_margin_top(20)
        nmt_labelbox.set_margin_left(20)
        nmt_labelbox.set_margin_right(20)
        
        companyerror_label=Gtk.Label() 
        companyerror_label.set_markup("Select company name from dropdown only.")   
        companyerror_label.set_halign(Gtk.Align.CENTER)
        nmt_labelbox.pack_start(companyerror_label, False, False, 5)
        
        companyerror_label2=Gtk.Label() 
        companyerror_label2.set_markup("Create new company if required.") 
        companyerror_label2.set_halign(Gtk.Align.CENTER)     
        nmt_labelbox.pack_start(companyerror_label2, False, False, 5)
        
        not_more_dialog.vbox.add(nmt_labelbox)
        
        okbutton= not_more_dialog.add_button('Ok', 1)
        okbutton.set_margin_top(20)
        okbutton.set_margin_bottom(20)
        okbutton.get_parent().set_halign(Gtk.Align.CENTER)
        #okbutton.get_style_context().add_class("suggested-action")
        
        not_more_dialog.show_all()
        
        print('Check company name')
        
        response = not_more_dialog.run()
        if response==1:
            pass
                        
        else:
            pass    
        

        not_more_dialog.destroy()
        #print('more dialog complete')
        
       
  

