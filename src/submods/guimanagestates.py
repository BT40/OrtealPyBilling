from submods import functions
from submods import guicommon
import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkGeoStates():


    def generatepage(self, parentwindow):
    
        sdialog = Gtk.Dialog('Manage states', parentwindow, Gtk.DialogFlags.MODAL)
        
        mbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20) #main box
        mbox.set_margin_top(20)
        mbox.set_margin_bottom(20)
        mbox.set_margin_left(20)
        mbox.set_margin_right(20)
        mbox.set_halign(Gtk.Align.CENTER) 
        
        newstatebox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0) 
        newstatebox.get_style_context().add_class("dialog_highlight_gborder")
        
        ministatbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        ministatbox.set_margin_top(20)
        ministatbox.set_margin_bottom(20)
        ministatbox.set_margin_left(20)
        ministatbox.set_margin_right(20)
        
        screate_label = Gtk.Label()
        screate_label.set_markup("Create new state  ")   
        screate_label.set_halign(Gtk.Align.CENTER) 
        screate_label.set_hexpand(False)   
        screate_label.set_margin_bottom(10)
        ministatbox.pack_start(screate_label, False, False, 0)        
        
        gridns = Gtk.Grid() 
        ministatbox.pack_start(gridns, False, False, 0)
       
        nstname_label = Gtk.Label()
        nstname_label.set_markup("New state name")           
        self.newstname_entry = Gtk.Entry()
        self.newstname_entry.set_max_length(24)
        
        nstcode_label = Gtk.Label()
        nstcode_label.set_markup("State code (gst) ")          
        self.newstcode_entry = Gtk.Entry()
        self.newstcode_entry.set_max_length(2)
          
        gridns.add(nstname_label)
        gridns.attach(self.newstname_entry, 1, 0, 1, 1)
        gridns.attach(nstcode_label, 0, 2, 1, 1)
        gridns.attach(self.newstcode_entry, 1, 2, 1, 1)
        
        tstatebutton = Gtk.Button.new_with_label("Create")
        tstatebutton.set_margin_top(20)
        tstatebutton.set_halign(Gtk.Align.CENTER) 
        tstatebutton.connect("clicked", self.create_state)  
        ministatbox.pack_start(tstatebutton, False, False, 0) 
        
        ministatbox.show_all()
        newstatebox.pack_start(ministatbox, False, False, 0) 
        
        ########################################################################
        
        delstatebox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0) 
        delstatebox.get_style_context().add_class("dialog_highlight_gborder")
        
        dstatbox=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        dstatbox.set_margin_top(20)
        dstatbox.set_margin_bottom(20)
        dstatbox.set_margin_left(20)
        dstatbox.set_margin_right(20)
        
        slistlabel = Gtk.Label()
        slistlabel.set_markup('List of states') 
        #slistlabel.set_margin_bottom(20)
        
        self.state_combo = Gtk.ComboBoxText.new_with_entry() 
        for es in guicommon.state_list:
            self.state_combo.append_text(es)
            #print (es)
        #self.state_combo.set_active(0)
        self.state_combo.set_hexpand(False)
        self.state_combo.set_halign(Gtk.Align.CENTER)
        self.state_combo.get_child().set_width_chars(32)     
        
        sdeletebutton = Gtk.Button.new_with_label("Delete") 
        sdeletebutton.get_style_context().add_class("dangerbutton")
        sdeletebutton.set_margin_top(20)
        sdeletebutton.connect("clicked", self.delete_state)
        sdeletebutton.set_halign(Gtk.Align.CENTER) # to avoid expansion horizontally
        
        dstatbox.pack_start(slistlabel, False, False, 0)  
        dstatbox.pack_start(self.state_combo, False, False, 0)  
        dstatbox.pack_start(sdeletebutton, False, False, 0)  
        
        delstatebox.pack_start(dstatbox, False, False, 0) 
                              
        mbox.pack_start(newstatebox, False, False, 10)       
        mbox.pack_start(delstatebox, False, False, 10)       
        mbox.show_all()       
        
        sdialog.vbox.add(mbox)    
        
        donebutton= sdialog.add_button('Close', 1)
        donebutton.set_margin_bottom(20)
        donebutton.get_parent().set_halign(Gtk.Align.CENTER)
        
        response = sdialog.run()
        if response==1:           
            pass
                        
        else:
            pass    
        
        sdialog.destroy()


    def create_state(self, button):
        temp_statename=[str(self.newstname_entry.get_text())]
        temp_statecode=[str(self.newstcode_entry.get_text())]
        guicommon.miscdbins.append('statelisthome', temp_statename )
        guicommon.miscdbins.append('statecodesgsthome', temp_statename )
        guicommon.miscdbins.dump()        
        guicommon.loadguicommon()
        self.state_combo.append_text(self.newstname_entry.get_text())
        self.newstname_entry.set_text('')
        self.newstcode_entry.set_text('')
        
        

    def delete_state(self, button):
        temp_statename=self.state_combo.get_active_text()
        s_list=guicommon.state_list
        s_list.remove(temp_statename)
        guicommon.miscdbins.set('statelisthome', s_list )
        guicommon.miscdbins.dump()
        guicommon.loadguicommon()
        
        
        self.state_combo.remove_all()
        for esv in guicommon.state_list:
            self.state_combo.append_text(esv)
        self.state_combo.get_child().set_text('Select')
        

