# This file contains gui for simple popup

#from submods import functions
from submods import guicommon

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class SimpleGtkDialog():
     

    def display_message (self, parentwindow, dialogheading, msg_one, msg_two, msg_three ):

        mdialog = Gtk.Dialog(dialogheading, parentwindow, Gtk.DialogFlags.MODAL)
        
        contentbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)             
        contentbox.set_margin_top(10)
        contentbox.set_margin_bottom(10)
        contentbox.set_margin_right(40)
        contentbox.set_margin_left(40)
        
        m_label = Gtk.Label() 
        m_label.set_margin_top(20) 
        m_label.set_markup(msg_one)          
        
        m2_label = Gtk.Label(msg_two)  
        m2_label.set_margin_top(10)   
        
        m3_label = Gtk.Label(msg_three)  
        #m3_label.set_margin_top(1)  
        
        #msg 1 and msg2 are spaced
        #msg 2 and msg 3 are not spaced.
        #use msg 2 & 3 if space in lines not reqd, use 1 & 2 if space/differentiation is reqd
        
        contentbox.pack_start(m_label, False, False, 0)   
        contentbox.pack_start(m2_label, False, False, 0)  
        contentbox.pack_start(m3_label, False, False, 0)  
        contentbox.show_all()         
               
        mdialog.vbox.add(contentbox)          
        
        okbutton= mdialog.add_button('Ok', 1)
        okbutton.set_margin_top(20)
        okbutton.set_margin_bottom(20)
        okbutton.get_parent().set_halign(Gtk.Align.CENTER)
        #okbutton.get_style_context().add_class("suggested-action")       
                
        response = mdialog.run()
        if response==1:           
            pass
                        
        else:
            pass           

        mdialog.destroy()
        #print('dialog complete') 
  

