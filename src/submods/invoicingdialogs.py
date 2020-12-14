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
     

    def more_things (self, parentwindow, billcomments, transmode, ewaybill, furtherterms, rcvalue, companyname):
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
        
        rc_label = Gtk.Label("Reverse charge")       
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
        
        shippingname_label = Gtk.Label() 
        shippingname_label.set_markup("Shipped to:")                    
        self.shippingname_entry = Gtk.Entry() 
        self.shippingname_entry.set_width_chars(32)
        self.shippingname_entry.set_max_length(32)  
        self.shippingname_entry.set_halign(Gtk.Align.START)  
        self.shippingname_entry.set_hexpand(False) 
        self.shippingname_entry.set_text(companyname)
        
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
        
        shippingpin_label = Gtk.Label() 
        shippingpin_label.set_markup("Shipping area PIN")                    
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
        contentgrid.attach(shippingname_label, 0, 5, 1, 1)
        contentgrid.attach(self.shippingname_entry, 1, 5, 1, 1)
        contentgrid.attach(shippingadd_label, 0, 6, 1, 1)
        contentgrid.attach(self.shippingadd_entry, 1, 6, 1, 1)
        contentgrid.attach(shippingstate_label, 0, 7, 1, 1)
        contentgrid.attach(self.shippingstate_entry, 1, 7, 1, 1)
        contentgrid.attach(shippingpin_label, 0, 8, 1, 1)
        contentgrid.attach(self.shippingpin_entry, 1, 8, 1, 1)
        contentgrid.attach(sphone_label, 0, 9, 1, 1)
        contentgrid.attach(self.sphone_entry, 1, 9, 1, 1)
        contentgrid.attach(rc_label, 0, 10, 1, 1)
        contentgrid.attach(self.rccombo, 1, 10, 1, 1)
        
        more_dialog.vbox.add(contentgrid)
        contentgrid.show_all()    
        
        donebutton= more_dialog.add_button('Done', 1)
        donebutton.set_margin_bottom(20)
        donebutton.get_parent().set_halign(Gtk.Align.CENTER)
        #donebutton.get_style_context().add_class("suggested-action")
        
        print('stage1')
        customer_details=guicommon.companytableins.readrow(companyname)
        print(customer_details)
        self.shippingadd_entry.set_text(customer_details[8]+customer_details[9])
        self.shippingpin_entry.set_text(customer_details[10])
        self.shippingstate_entry.set_text(customer_details[12])
        self.sphone_entry.set_text(customer_details[13])
        print(self.shippingadd_entry.get_text())
        print('stage3')
               
        response = more_dialog.run()
        if response==1:
            billcomments=self.bcommentry.get_text()
            transmode=''
            ewaybill=self.ewayentry.get_text()
            furtherterms=self.furthertermsline1_entry.get_text()
            rcvalue=self.rccombo.get_active_text()
                        
        else:
            pass    
        

        more_dialog.destroy()
        #print('more dialog complete')
        return billcomments, transmode, ewaybill, furtherterms, rcvalue
    
    
       
  

