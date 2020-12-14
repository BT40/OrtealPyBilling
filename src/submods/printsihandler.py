# This file contains handler  for printing sale invoice

#from submods import functions
#from submods import guicommon

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk



class PrintSaleInvoiceHander():
     

    def print_dialog (self, parentwindow, invoiceid):
       
        p_dialog = Gtk.Dialog('DialogTitle', parentwindow, Gtk.DialogFlags.MODAL)
        
        label = Gtk.Label("Do you want to print invoice?")
        label.set_margin_top(40)
        label.set_margin_bottom(40)
        label.set_margin_right(40)
        label.set_margin_left(40)
        p_dialog.vbox.add(label)
        label.show()
        
        yesbutton= p_dialog.add_button('Yes', 1)
        #button1.set_margin_right(50)
        yesbutton.get_parent().set_halign(Gtk.Align.CENTER)
        yesbutton.get_style_context().add_class("suggested-action")
        
        
        nobutton= p_dialog.add_button('No', 2)
        
        response = p_dialog.run()
        if response==1:
            self.printdialog_yesbutton_pressed()
        elif response==2:
            self.printdialog_yesbutton_pressed()
        else:
            pass    
        p_dialog.destroy()
        print('dialog complete')
        
    
    def printdialog_yesbutton_pressed (self):   
        print('yes button detected') 
        #use this function to print
     
    
    def printdialog_nobutton_pressed (self):   
        print('no button  detected')
        # use this if no printing is required  
        
        

