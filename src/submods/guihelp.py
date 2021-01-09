from submods import functions
from submods import guicommon
import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk



def loadtips():
    tbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20) 
    
    switchtext_label = Gtk.Label(label='Press tab to switch between input fields.')
    enableinv_label = Gtk.Label(label='Future option: Enable xyz from preferences if needed')
    cnamelimit_label = Gtk.Label(label='Company name, item name, comments, email, address line limit: 47 characters')
    inamelimit_label = Gtk.Label(label=' Qty and price limit: 11 characters')
    commentslimit_label = Gtk.Label(label='HSN limit: 9 characters')
    addresslimit_label = Gtk.Label(label='Flag, PIN, mobile  limit: 16 characters')
    personnamelimit_label = Gtk.Label(label='Person name,city, state, website, sub group limit: 32 characters')
    limit24_label = Gtk.Label(label='Phone 24')
    invitemslimit_label = Gtk.Label(label='Items in sales invoice: 25; in purchase invoice: 50')
    
    tbox.pack_start(switchtext_label, False, False, 0)    
    tbox.pack_start(cnamelimit_label, False, False, 0)   
    tbox.pack_start(inamelimit_label, False, False, 0)  
    tbox.pack_start(commentslimit_label, False, False, 0)  
    tbox.pack_start(addresslimit_label, False, False, 0)  
    tbox.pack_start(personnamelimit_label, False, False, 0)    
    tbox.pack_start(invitemslimit_label, False, False, 0)    
    tbox.pack_start(limit24_label, False, False, 0)    
    tbox.pack_start(enableinv_label, False, False, 0)                  
                
    tbox.show_all()
    return tbox


def helptips():
    htb=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20) #help tips box
    
    aboutlabel = Gtk.Label()
    aboutlabel.set_markup("Version Jan 2021. Try at your own risk. Software is open source.")
    htb.pack_start(aboutlabel, False, False, 0)    
    
    htsw = Gtk.ScrolledWindow(hexpand=False) #help tips scroll window
    htsw.set_min_content_width(560)      
    #htsw.set_max_content_width(800)
    htsw.set_min_content_height(360)
    #htsw.set_max_content_height(720)
    htsw.get_style_context().add_class("lightgreymedborder")
    htsw.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)        
    htsw.add(loadtips())
    htb.pack_start(htsw, False, False, True) 
    return htb






