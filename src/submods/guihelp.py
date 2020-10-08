from submods import functions
from submods import guicommon
import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk




#===================================================== SCROLL BOX FOR COMPANIES VIEWING ====================


def loadtips():
    tbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20) 
    switchtext_label = Gtk.Label(label='Press tab to switch between input fields.')
    cnamelimit_label = Gtk.Label(label='Company name limit: 47 characters')
    inamelimit_label = Gtk.Label(label='Item name limit: 47 characters')
    commentslimit_label = Gtk.Label(label='Comments limit: 47 characters')
    personnamelimit_label = Gtk.Label(label='Person name limit: 32 characters')
    
    tbox.pack_start(switchtext_label, False, False, 0)    
    tbox.pack_start(cnamelimit_label, False, False, 0)   
    tbox.pack_start(inamelimit_label, False, False, 0)  
    tbox.pack_start(commentslimit_label, False, False, 0)  
    tbox.pack_start(personnamelimit_label, False, False, 0)                
                
    tbox.show_all()
    return tbox


def helptips():
    htb=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20) #help tips box

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






