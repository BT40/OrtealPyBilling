from submods import functions
from submods import guicommon
from submods import statementprocessor
import sys
import gi
import operator

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkStatements():


    def generatepage(self, mainwindow):
        statementsmasterbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        
        #s_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        svheaderbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6) 
        #svheaderbox.set_vexpand(False)
        #svheaderbox.get_style_context().add_class("testarea") 
        
        gridsb = Gtk.Grid()
        #gridsb.set_vexpand(False)
        gridsb.set_margin_bottom(20)
        
        forparty_label = Gtk.Label(label="Type and select party")
        forparty_label.set_width_chars(16)
        self.pnameentry = Gtk.Entry()
        self.pnameentry.set_width_chars(47)
        self.cname_completion = Gtk.EntryCompletion()
        self.cname_completion.set_model(guicommon.companyname_store)
        self.cname_completion.set_text_column(0)
        self.pnameentry.set_completion(self.cname_completion)  
        
        periodlabel = Gtk.Label(label="Select period")
        periodlabel.set_width_chars(16)
        
        self.tscombo = Gtk.ComboBoxText.new()
        periodlist=["Full year"]
        #periodlist=["Full year", "Quarter 1", "Quarter 2", "Quarter 3", "Quarter 4", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec" ]
        for ets in periodlist:
            self.tscombo.append_text(ets)        
        self.tscombo.set_active(0)
        self.tscombo.set_hexpand(False)
        self.tscombo.set_halign(Gtk.Align.CENTER)
        #self.tscombo.get_child().set_width_chars(32)     #only for combobox new with entry
        
        displaybutton = Gtk.Button.new_with_label("Display")
        #displaybutton.get_style_context().add_class("dangerbutton")
        displaybutton.connect("clicked", self.generate_statement )
        displaybutton.set_halign(Gtk.Align.CENTER) # to avoid expansion horizontally
        displaybutton.set_margin_left(20)
        
        gridsb.add(forparty_label)
        gridsb.attach(self.pnameentry, 1, 0, 1, 1)
        gridsb.attach(periodlabel, 2, 0, 1, 1)
        gridsb.attach(self.tscombo, 3, 0, 1, 1)
        gridsb.attach(displaybutton, 4, 0, 1, 1)
        
        svheaderbox.pack_start(gridsb, False, False, 0)   
        
        # scrollbox labelling-header
        items_headerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)    
        datelabel = Gtk.Label(label="Date")
        datelabel.set_width_chars(12)
        vnamelabel = Gtk.Label(label="Document No.")
        vnamelabel.set_width_chars(20)
        debitlabel = Gtk.Label(label="Debit ")
        debitlabel.set_width_chars(20)
        debitlabel.set_margin_left(10)
        creditlabel = Gtk.Label(label="Credit ")
        creditlabel.set_width_chars(20)
        creditlabel.set_margin_left(10)
        typelabel = Gtk.Label(label="Type ")
        typelabel.set_width_chars(16)
        typelabel.set_margin_left(5)
        instabalancelabel = Gtk.Label(label="Balance")
        instabalancelabel.set_width_chars(20)      
        typelabel.set_margin_left(50)
        
        items_headerbox.pack_start(datelabel, False, False, 0)
        items_headerbox.pack_start(vnamelabel, False, False, 0)
        items_headerbox.pack_start(debitlabel, False, False, 0)
        items_headerbox.pack_start(creditlabel, False, False, 0)
        items_headerbox.pack_start(typelabel, False, False, 0)
        items_headerbox.pack_start(instabalancelabel, False, False, 0)                
      
        self.sw = Gtk.ScrolledWindow(hexpand=False) 
        #self.sw.set_min_content_width(560)      
        #self.sw.set_max_content_width(800)
        self.sw.set_min_content_height(360)
        #self.sw.set_max_content_height(720)
        self.sw.get_style_context().add_class("lightgreymedborder")
        self.sw.set_policy(Gtk.PolicyType.NEVER,
                               Gtk.PolicyType.AUTOMATIC)     
                                  
        view_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6) 
        view_box.pack_start(svheaderbox, False, False, 0)
        view_box.pack_start(items_headerbox, False, False, 0)
        view_box.pack_start(self.sw, False, False, True)        
        view_box.show_all()
        statementsmasterbox.pack_start(view_box, False, False, True) 
          
        return statementsmasterbox
        
    
    def loadlist(self, selectedparty):        
        se_collection=guicommon.statementstableins.readrow(selectedparty) 
        #print(se_collection)
        se_collection_alphabetic=se_collection.copy()
        se_collection_alphabetic.sort(key=operator.itemgetter(1, 8))
        balance=0
                         
        listbox = Gtk.ListBox() 
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        
        for eachitem in se_collection_alphabetic:      
            #print(eachitem)     
            iblb_temprow = Gtk.ListBoxRow()
            iblbvr_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
            iblbvr_box.set_hexpand(True)            
            iblbvr_box.get_style_context().add_class("inventoryviewrb")
            
            date_templabel = Gtk.Label(label=eachitem[1], xalign=0)#date
            date_templabel.set_width_chars(10)
            ref_templabel = Gtk.Label(label=eachitem[2])#ref no.
            ref_templabel.set_width_chars(20)
            debit_templabel = Gtk.Label(label=eachitem[3])#debit
            debit_templabel.set_width_chars(20)
            credit_templabel = Gtk.Label(label=eachitem[4])#credit
            credit_templabel.set_width_chars(20)
            type_templabel = Gtk.Label(label=eachitem[5])#type
            type_templabel.set_width_chars(20)
            if debit_templabel=='':
                float_debit=0
            else:        
                float_debit_raw=float(eachitem[3])
                float_debit=round( float_debit_raw, 2)
                
            if credit_templabel=='':
                float_credit=0
            else:        
                float_credit_raw=float(eachitem[4])
                float_credit=round( float_credit_raw, 2)    
            balance_temp=balance+float_debit-float_credit
            balance=balance_temp
            balance_templabel = Gtk.Label(label=balance_temp)#per transaction balance
            balance_templabel.set_width_chars(20)
           
            iblbvr_box.pack_start(date_templabel, False, False, 0)
            iblbvr_box.pack_start(ref_templabel, False, False, 0)
            iblbvr_box.pack_start(debit_templabel, False, False, 0)
            iblbvr_box.pack_start(credit_templabel, False, False, 0)
            iblbvr_box.pack_start(type_templabel, False, False, 0)
            iblbvr_box.pack_start(balance_templabel, False, False, 0)
            iblb_temprow.add(iblbvr_box) 
            listbox.add(iblb_temprow)
            listbox.show_all()       
        return listbox
        
        
    def generate_statement(self, trigger):       
        partyname=self.pnameentry.get_text()   
        children_sw=self.sw.get_children()
        for each_child in children_sw:
            self.sw.remove(each_child)
            each_child.destroy()            
        self.sw.add(self.loadlist(partyname))
        self.sw.show_all()   
