# This file contains gui page inventory

import sys
import gi
from submods import functions
from submods import dbmani
from submods import guicommon
#from submods import guiprocessor
from datetime import datetime

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkInventory():
        
    def generatepage(self, invoicingbox, bph, guiinvoicingins, mainwindow): #mainwindow is for guiinvoicing reference
        
        #some initializations
        self.mainwindow=mainwindow
        self.itemtableins=dbmani.itemtableins        
        self.companytableins=dbmani.companytableins
        self.invoicetableins=dbmani.invoicetableins       
        self.miscdb=dbmani.miscdb       
        self.itemgroups=dbmani.itemgroups                
        #self.guiprocessor_ins=guiprocessor.GtkProcessor()
        
        #gui starts here   
        self.inventorymasterbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
                
        self.inventorystack = Gtk.Stack()
        self.inventorystack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.inventorystack.set_transition_duration(1000)

#================================================= current stock box ==========================================

        inventoryview_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
                
        #print("Started all inventory pane coding in inventory page")   
        ivheaderbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6) #iv=inventory viewer
        ivheaderbox.set_vexpand(False)
        #ivheaderbox.get_style_context().add_class("testarea") 
        
        gridib = Gtk.Grid()
        gridib.set_vexpand(False)
        ivheaderbox.pack_start(gridib, False, False, 0)   
        
        #ihb_filterbutton = Gtk.Button.new_with_label("Filter")
        #ihb_filterbutton.connect("clicked", self.blankfunc)           
        #ihb_sortbynamebutton = Gtk.Button.new_with_label("Sort by name")
        #ihb_sortbynamebutton.connect("clicked", self.blankfunc)         
        #ihb_sortbyqtybutton = Gtk.Button.new_with_label("Sort by name")
        #ihb_sortbyqtybutton.connect("clicked", self.blankfunc)         
        ihb_loadbutton = Gtk.Button.new_with_label("Refresh")
        ihb_loadbutton.set_name('loaditemsbutton')
        #ihb_loadbutton.get_style_context().add_class("dangerbutton")        
        
        def loaditems(event):
            iblistbox = Gtk.ListBox() #ib=inventory box
            iblistbox.set_selection_mode(Gtk.SelectionMode.NONE)
            #inventorystore=Gtk.ListStore(str)
            #print (len(self.itemtableins.rowlist))
            for eachitem in guicommon.items_alphabetic:
                #pointitem=inventorystore.append(eachitem)               
                iblb_temprow = Gtk.ListBoxRow()
                iblbvr_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
                iblbvr_box.set_hexpand(True)
                #iblbvr_box.get_style_context().add_class("testarea")
                iblbvr_box.get_style_context().add_class("inventoryviewrb")
                isrn_templabel = Gtk.Label(label=guicommon.items_alphabetic.index(eachitem)+1, xalign=0)
                isrn_templabel.set_width_chars(8)
                iname_templabel = Gtk.Label(label=eachitem[0], xalign=0)
                iname_templabel.set_width_chars(47)
                iqty_templabel = Gtk.Label(label=eachitem[15])
                iqty_templabel.set_width_chars(16)
                #iqty_templabel.get_style_context().add_class("testarea")
                iblbvr_box.pack_start(isrn_templabel, False, False, 0)
                iblbvr_box.pack_start(iname_templabel, False, False, 0)
                iblbvr_box.pack_start(iqty_templabel, False, False, 0)
                iblb_temprow.add(iblbvr_box) 
                iblistbox.add(iblb_temprow)
                iblistbox.show_all()
                #print('listrow calld')
            return iblistbox
            
        def refreshil(event):
            ipsw.remove(ipsw.get_child())
            print('removed previous')
            ipsw.add(loaditems("blankevent"))
            print('added new')               
            
        ihb_loadbutton.connect("clicked", refreshil)
        
        gridib.add(ihb_loadbutton)
        #gridib.attach(ihb_sortbynamebutton, 1, 0, 1, 1) 
        #gridib.attach(ihb_sortbyqtybutton, 2, 0, 1, 1) 
        #gridib.attach(ihb_filterbutton, 3, 0, 1, 1) 
        
        inventoryview_box.pack_start(ivheaderbox, False, False, 0)
        
        # inventory scrollbox labelling-header
        inventoryitems_headerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)    
        iihb_srlabel = Gtk.Label(label="Sr. No.", xalign=0)
        iihb_srlabel.set_width_chars(8)
        iihb_inamelabel = Gtk.Label(label="Item name           ")
        iihb_inamelabel.set_width_chars(47)
        iihb_iqtylabel = Gtk.Label(label="Available Quantity")
        #iihb_iqtylabel.set_width_chars(16)        
        
       # item1label.set_markup("Item 1 to be billed")
        inventoryitems_headerbox.pack_start(iihb_srlabel, False, False, 0)
        inventoryitems_headerbox.pack_start(iihb_inamelabel, False, False, 0)
        inventoryitems_headerbox.pack_end(iihb_iqtylabel, False, False, 0)
        
        inventoryview_box.pack_start(inventoryitems_headerbox, False, False, 0)
      
        ipsw = Gtk.ScrolledWindow(hexpand=False) #inventory page scroll window
        #ipsw.set_min_content_width(560)      
        #ipsw.set_max_content_width(800)
        ipsw.set_min_content_height(360)
        #ipsw.set_max_content_height(720)
        ipsw.get_style_context().add_class("lightgreymedborder")
        ipsw.set_policy(Gtk.PolicyType.NEVER,
                               Gtk.PolicyType.AUTOMATIC)        
        ipsw.add(loaditems("blankevent"))
        inventoryview_box.pack_start(ipsw, False, False, True)        

#==================================== Create Item pane  ========================================================        
      
        #print("Started item pane coding in Create pane")   
        createitembox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)        
        gridcib = Gtk.Grid()
        createitembox.pack_start(gridcib, True, True, 0)

        cinamelabel = Gtk.Label()
        cinamelabel.set_markup("Item name")        
        self.cinameentry = Gtk.Entry()
        self.cinameentry.set_max_length(47)
               
        cigrouplabel = Gtk.Label()
        cigrouplabel.set_markup("Item group")        
        
        self.cigroupcombo = Gtk.ComboBoxText.new_with_entry()
        for eachig in self.itemgroups:
            eachigid=eachig + 'gtkid'
            self.cigroupcombo.append(eachigid, eachig)
        self.cigroupcombo.set_active(0)
        
        cisubgroupseparator = Gtk.Label() # sub group separator blank label
        cisubgroupseparator.set_markup(" ")
        cisubgroupseparator.set_width_chars(16) 
        
        cisubgrouplabel = Gtk.Label()
        cisubgrouplabel.set_markup("Sub-group (Optional)  ")
        self.cisubgroupentry = Gtk.Entry()
        self.cisubgroupentry.set_max_length(32)
        
        cihsnlabel = Gtk.Label()
        cihsnlabel.set_markup("HSN code")
        self.cihsnentry = Gtk.Entry()
        self.cihsnentry.set_max_length(8)
        
        ciunitlabel = Gtk.Label()
        ciunitlabel.set_markup("Unit")
        
        self.ciunitcombo = Gtk.ComboBoxText.new_with_entry()
        self.ciunitcombo.insert(position=0, id="nosunit", text="Nos")
        self.ciunitcombo.insert(position=1, id="pcsunit", text="Pcs")        
        self.ciunitcombo.set_active(1)        
        
        ciopenstlabel = Gtk.Label()
        ciopenstlabel.set_markup("Opening stock")       
        self.ciopenstentry = Gtk.Entry()
        self.ciopenstentry.set_max_length(11)
        
        cicritlabel = Gtk.Label()
        cicritlabel.set_markup("Critical level")        
        self.cicritentry = Gtk.Entry()
        self.cicritentry.set_max_length(11)
        
        cilplabel = Gtk.Label()
        cilplabel.set_markup("List Price (MRP)") 
        self.cilpentry = Gtk.Entry()
        self.cilpentry.set_max_length(11)
        
        cisdlabel = Gtk.Label()
        cisdlabel.set_markup("Standard discount ")        
        self.cisdentry = Gtk.Entry()
        self.cisdentry.set_max_length(47)
        
        cisplabel = Gtk.Label()
        cisplabel.set_markup("Selling price")        
        self.cispentry = Gtk.Entry()
        self.cispentry.set_max_length(11)
        
        cipplabel = Gtk.Label()
        cipplabel.set_markup("Purchase price")       
        self.cippentry = Gtk.Entry()
        self.cippentry.set_max_length(11)
        
        cicommlabel = Gtk.Label()
        cicommlabel.set_markup("Comments")        
        self.cicommentry = Gtk.Entry()
        self.cicommentry.set_max_length(47)
        
        ciflaglabel = Gtk.Label()
        ciflaglabel.set_markup("Flag")        
        self.ciflagentry = Gtk.Entry()
        self.ciflagentry.set_max_length(16)
        
        ciblanklabel = Gtk.Label()
        ciblanklabel.set_markup(" ")
        
        cigstlabel = Gtk.Label()
        cigstlabel.set_markup("GST slab")
        
        self.citaxcombo = Gtk.ComboBoxText.new_with_entry()
        self.citaxcombo.insert(position=0, id="g12", text="GST-12%")
        self.citaxcombo.insert(position=1, id="g18", text="GST-18%")
        self.citaxcombo.set_active(1)
        
        citaxinclusive_label = Gtk.Label()
        citaxinclusive_label.set_markup("Tax inclusive ")
        citaxinclusive_label.set_margin_top(10)

        self.citaxinclusive_button = Gtk.CheckButton()
        self.citaxinclusive_button.set_margin_top(10)
        self.citaxinclusive_button.set_active(False) # By default false
        
        self.civarg=[self.cinameentry, self.cihsnentry, self.cigroupcombo, self.cisubgroupentry, self.ciunitcombo, self.citaxcombo, self.citaxinclusive_button, self.ciopenstentry, self.cicritentry, self.cilpentry, self.cisdentry, self.cispentry, self.cippentry, self.cicommentry, self.ciflagentry]        
        
        cicreatebutton = Gtk.Button.new_with_label("Create")
        cicreatebutton.get_style_context().add_class("suggested-action")
        cicreatebutton.connect("clicked", self.processcitem, self.civarg, invoicingbox, bph, guiinvoicingins)
                
        ciresetbutton = Gtk.Button.new_with_label("Reset")
        ciresetbutton.get_style_context().add_class("dangerbutton")
        ciresetbutton.connect("clicked", self.reset_cientries)
                
        gridcib.add(cinamelabel)
        gridcib.attach(self.cinameentry, 1, 0, 1, 1)
        gridcib.attach(cihsnlabel, 0, 1, 1, 1)
        gridcib.attach(self.cihsnentry, 1, 1, 1, 1)
        gridcib.attach(cigrouplabel, 0, 2, 1, 1)
        gridcib.attach(self.cigroupcombo, 1, 2, 1, 1)
        gridcib.attach(cisubgroupseparator, 2, 2, 1, 1)
        gridcib.attach(cisubgrouplabel, 3, 2, 1, 1)
        gridcib.attach(self.cisubgroupentry, 4, 2, 1, 1)
        gridcib.attach(ciunitlabel, 0, 3, 1, 1)
        gridcib.attach(self.ciunitcombo, 1, 3, 1, 1)
        gridcib.attach(cigstlabel, 0, 4, 1, 1)
        gridcib.attach(self.citaxcombo, 1, 4, 1, 1)
        gridcib.attach(citaxinclusive_label, 3, 4, 1, 1)
        gridcib.attach(self.citaxinclusive_button, 4, 4, 1, 1)
        gridcib.attach(ciopenstlabel, 0, 5, 1, 1)
        gridcib.attach(self.ciopenstentry, 1, 5, 1, 1)
        gridcib.attach(cicritlabel, 0, 6, 1, 1)
        gridcib.attach(self.cicritentry, 1, 6, 1, 1)
        gridcib.attach(cilplabel, 0, 7, 1, 1)
        gridcib.attach(self.cilpentry, 1, 7, 1, 1)
        gridcib.attach(cisdlabel, 0, 8, 1, 1)
        gridcib.attach(self.cisdentry, 1, 8, 1, 1)
        gridcib.attach(cisplabel, 0, 9, 1, 1)
        gridcib.attach(self.cispentry, 1, 9, 1, 1)
        gridcib.attach(cipplabel, 3, 9, 1, 1)
        gridcib.attach(self.cippentry, 4, 9, 1, 1)
        gridcib.attach(cicommlabel, 0, 10, 1, 1)
        gridcib.attach(self.cicommentry, 1, 10, 1, 1)
        gridcib.attach(ciflaglabel, 3, 10, 1, 1)
        gridcib.attach(self.ciflagentry, 4, 10, 1, 1)
        gridcib.attach(ciblanklabel, 1, 12, 1, 1)        
        gridcib.attach(cicreatebutton, 1, 13, 1, 1)
        gridcib.attach(ciresetbutton, 0, 13, 1, 1)               
        # Create Item pane coding ends here 
    
#===================================   Edit Item =============================================
       
        edititem_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
        ei_headerbox=Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        ei_headerbox.set_halign(Gtk.Align.START) 
        #ei_headerbox.set_margin_bottom(10)
        ei_headerbox.set_margin_left(38)
        ei_namelabel = Gtk.Label()
        ei_namelabel.set_markup("Select item ")
        
        ei_editbutton = Gtk.Button.new_with_label("Modify or View")
        
        ei_deletebutton = Gtk.Button.new_with_label("Delete item")
        ei_deletebutton.get_style_context().add_class("dangerbutton")
        
        
        self.ei_nameentry = Gtk.Entry()
        self.ei_nameentry.set_width_chars(32)
        self.ei_nameentry.set_max_length(47)
        self.einame_completion = Gtk.EntryCompletion()
        self.einame_completion.set_model(guicommon.itemname_store)
        self.einame_completion.set_text_column(0)
        self.ei_nameentry.set_completion(self.einame_completion)   
        ei_headerbox.pack_start(ei_namelabel, True, True, 0)
        ei_headerbox.pack_start(self.ei_nameentry, True, True, 0)         
        ei_headerbox.pack_start(ei_editbutton, True, True, 0) 
        ei_headerbox.pack_start(ei_deletebutton, True, True, 0) 
        edititem_box.pack_start(ei_headerbox, False, False, 0)
        
        ei_namewarning = Gtk.Label()
        ei_namewarning.set_halign(Gtk.Align.START) 
        ei_namewarning.set_margin_left(150)
        ei_namewarning.set_margin_bottom(15)
        ei_namewarning.get_style_context().add_class("adinfotext")
        ei_namewarning.set_markup(" (Type and select from dropdown only) ")
        edititem_box.pack_start(ei_namewarning, False, False, 0) 
        
        grideib = Gtk.Grid()
        edititem_box.pack_start(grideib, True, True, 0)

        einamelabel = Gtk.Label()
        einamelabel.set_markup("Item name (new) ")
        self.einameentry = Gtk.Entry()
        self.einameentry.set_max_length(47)
                      
        eigrouplabel = Gtk.Label()
        eigrouplabel.set_markup("Item group")
        
        self.eigroupcombo = Gtk.ComboBoxText.new_with_entry()
        
        self.eigroupcombo.set_active(0)#=======================================================================CHANGE
        
        eisubgroupseparator = Gtk.Label() # sub group separator blank label
        eisubgroupseparator.set_markup(" ")
        eisubgroupseparator.set_width_chars(16) 
        
        eisubgrouplabel = Gtk.Label()
        eisubgrouplabel.set_markup("Sub-group (Optional)  ")        
        self.eisubgroupentry = Gtk.Entry()
        self.eisubgroupentry.set_max_length(32)
        
        eihsnlabel = Gtk.Label()
        eihsnlabel.set_markup("HSN code")        
        self.eihsnentry = Gtk.Entry()
        self.eihsnentry.set_max_length(8)
        
        eiunitlabel = Gtk.Label()
        eiunitlabel.set_markup("Unit")
        
        self.eiunitcombo = Gtk.ComboBoxText.new_with_entry()
        self.eiunitcombo.insert(position=0, id="nosunit", text="Nos")
        self.eiunitcombo.insert(position=1, id="pcsunit", text="Pcs")
        self.eiunitcombo.insert(position=2, id="pksunit", text="Packet")
        self.eiunitcombo.insert(position=3, id="boxunit", text="Box")
        self.eiunitcombo.insert(position=4, id="kgunit", text="Kg")
        self.eiunitcombo.insert(position=5, id="gunit", text="g")
        self.eiunitcombo.insert(position=6, id="tonunit", text="ton")
        self.eiunitcombo.insert(position=7, id="quintalunit", text="Quintal")
        self.eiunitcombo.insert(position=8, id="munit", text="m")
        self.eiunitcombo.insert(position=9, id="cmunit", text="cm")
        self.eiunitcombo.insert(position=10, id="othunit", text="Other")      
        self.eiunitcombo.set_active(1)   
        
        eitaxinclusive_label = Gtk.Label()
        eitaxinclusive_label.set_markup("Tax inclusive ")
        eitaxinclusive_label.set_margin_top(10)

        self.eitaxinclusive_button = Gtk.CheckButton()
        self.eitaxinclusive_button.set_margin_top(10)
        self.eitaxinclusive_button.set_active(False) # By default false     
        
        eiopenstlabel = Gtk.Label()
        eiopenstlabel.set_markup("Opening stock")        
        self.eiopenstentry = Gtk.Entry()
        self.eiopenstentry.set_max_length(11)
        
        eicritlabel = Gtk.Label()
        eicritlabel.set_markup("Critical level") 
        self.eicritentry = Gtk.Entry()
        self.eicritentry.set_max_length(11)
        
        eilplabel = Gtk.Label()
        eilplabel.set_markup("List Price (MRP)")        
        self.eilpentry = Gtk.Entry()
        self.eilpentry.set_max_length(11)
        
        eisdlabel = Gtk.Label()
        eisdlabel.set_markup("Standard discount ")
        self.eisdentry = Gtk.Entry()
        self.eisdentry.set_max_length(47)
        
        eisplabel = Gtk.Label()
        eisplabel.set_markup("Selling price")
        self.eispentry = Gtk.Entry()
        self.eispentry.set_max_length(11)
        
        eipplabel = Gtk.Label()
        eipplabel.set_markup("Purchase price")
        self.eippentry = Gtk.Entry()
        self.cippentry.set_max_length(11)
        
        eicommlabel = Gtk.Label()
        eicommlabel.set_markup("Comments")       
        self.eicommentry = Gtk.Entry()
        self.eicommentry.set_max_length(47)
        
        eiflaglabel = Gtk.Label()
        eiflaglabel.set_markup("Flag")        
        self.eiflagentry = Gtk.Entry()
        self.eiflagentry.set_max_length(16)
        
        eiblanklabel = Gtk.Label()
        eiblanklabel.set_markup(" ")
        
        eigstlabel = Gtk.Label()
        eigstlabel.set_markup("GST slab")
        
        self.eitaxcombo = Gtk.ComboBoxText.new_with_entry()
        self.eitaxcombo.insert(position=0, id="g12", text="GST-12%")
        self.eitaxcombo.insert(position=1, id="g18", text="GST-18%")
        self.eitaxcombo.set_active(1)
        
        self.eivarg=[self.einameentry, self.eihsnentry, self.eigroupcombo, self.eisubgroupentry, self.eiunitcombo, self.eitaxcombo, self.eiopenstentry, self.eicritentry, self.eilpentry, self.eisdentry, self.eispentry, self.eippentry, self.eicommentry]        
        
        self.eientries=[self.einameentry, self.eihsnentry, self.eisubgroupentry, self.eiopenstentry, self.eicritentry, self.eilpentry, self.eisdentry, self.eispentry, self.eippentry, self.eicommentry] 
        
        for eachofentry in self.eivarg:
            eachofentry.set_sensitive(False)       
                
        eisavebutton = Gtk.Button.new_with_label("Save")
        eisavebutton.get_style_context().add_class("suggested-action")
        eisavebutton.connect("clicked", self.process_eitem, self.eivarg, invoicingbox, bph, guiinvoicingins)
                
        eiresetbutton = Gtk.Button.new_with_label("Cancel")
        eiresetbutton.connect("clicked", self.reset_eientries, self.eientries)
               
        grideib.add(einamelabel)
        grideib.attach(self.einameentry, 1, 0, 1, 1)
        grideib.attach(eihsnlabel, 0, 1, 1, 1)
        grideib.attach(self.eihsnentry, 1, 1, 1, 1)
        grideib.attach(eigrouplabel, 0, 2, 1, 1)
        grideib.attach(self.eigroupcombo, 1, 2, 1, 1)
        grideib.attach(eisubgroupseparator, 2, 2, 1, 1)
        grideib.attach(eisubgrouplabel, 3, 2, 1, 1)
        grideib.attach(self.eisubgroupentry, 4, 2, 1, 1)
        grideib.attach(eiunitlabel, 0, 3, 1, 1)
        grideib.attach(self.eiunitcombo, 1, 3, 1, 1)
        grideib.attach(eigstlabel, 0, 4, 1, 1)
        grideib.attach(self.eitaxcombo, 1, 4, 1, 1)
        grideib.attach(eitaxinclusive_label, 3, 4, 1, 1)
        grideib.attach(self.eitaxinclusive_button, 4, 4, 1, 1)
        grideib.attach(eiopenstlabel, 0, 5, 1, 1)
        grideib.attach(self.eiopenstentry, 1, 5, 1, 1)
        grideib.attach(eicritlabel, 0, 6, 1, 1)
        grideib.attach(self.eicritentry, 1, 6, 1, 1)
        grideib.attach(eilplabel, 0, 7, 1, 1)
        grideib.attach(self.eilpentry, 1, 7, 1, 1)
        grideib.attach(eisdlabel, 0, 8, 1, 1)
        grideib.attach(self.eisdentry, 1, 8, 1, 1)
        grideib.attach(eisplabel, 0, 9, 1, 1)
        grideib.attach(self.eispentry, 1, 9, 1, 1)
        grideib.attach(eipplabel, 3, 9, 1, 1)
        grideib.attach(self.eippentry, 4, 9, 1, 1)
        grideib.attach(eicommlabel, 0, 11, 1, 1)
        grideib.attach(self.eicommentry, 1, 11, 1, 1)
        grideib.attach(eiflaglabel, 3, 11, 1, 1)
        grideib.attach(self.eiflagentry, 4, 11, 1, 1)
        grideib.attach(eiblanklabel, 1, 12, 1, 1)        
        grideib.attach(eisavebutton, 1, 13, 1, 1)
        grideib.attach(eiresetbutton, 0, 13, 1, 1)  
        #grideib.attach(eideletebutton, 4, 13, 1, 1)  
        
        
        ei_editbutton.connect("clicked", self.set_eientries, self.eientries)  
        ei_deletebutton.connect("clicked", self.deleteitem, invoicingbox, bph, guiinvoicingins)              
        # Editem pane coding ends here 
    
    
#================================= Create Item Group ========================================== 
      
        migbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6) #create item group box        
                 
        cignamelabel = Gtk.Label()
        cignamelabel.set_markup("Name of group") 
        
        self.cignameentry = Gtk.Entry() 
        self.cignameentry.set_width_chars(25)
        self.cignameentry.set_max_length(32)
        self.cignameentry.set_hexpand(False)
        self.cignameentry.set_halign(Gtk.Align.CENTER) # to avoid expansion horizontally 
        
        cigemptylabel = Gtk.Label()
        cigemptylabel.set_markup("     ")
        
        cigresetbutton = Gtk.Button.new_with_label("Reset")
        #cigresetbutton.get_style_context().add_class("dangerbutton")
        cigresetbutton.connect("clicked", self.reset_cigentry) 
        cigresetbutton.set_halign(Gtk.Align.CENTER) # to avoid expansion horizontally
        
        cigcreatebutton = Gtk.Button.new_with_label("Create")
        cigcreatebutton.get_style_context().add_class("suggested-action")
        cigcreatebutton.connect("clicked", self.cigfunc)
        cigcreatebutton.set_halign(Gtk.Align.CENTER) # to avoid expansion horizontally
        
        migseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)         
        
        cigdeletebutton = Gtk.Button.new_with_label("Delete")
        cigdeletebutton.get_style_context().add_class("dangerbutton")
        cigdeletebutton.connect("clicked", self.deleteig)
        cigdeletebutton.set_halign(Gtk.Align.CENTER) # to avoid expansion horizontally
        
        ciglistlabel = Gtk.Label()
        ciglistlabel.set_markup('List of item groups') 
        ciglistlabel.set_margin_top(20)
        
        self.ciglcombo = Gtk.ComboBoxText.new_with_entry()
        for eg in guicommon.itemgroups:
            self.ciglcombo.append_text(eg)
        self.ciglcombo.set_active(0)
        self.ciglcombo.set_hexpand(False)
        self.ciglcombo.set_halign(Gtk.Align.CENTER)
        self.ciglcombo.get_child().set_width_chars(32)       
        
        migbox.pack_start(cignamelabel, False, False, 0)   
        migbox.pack_start(self.cignameentry, False, False, 0)
        migbox.pack_start(cigemptylabel, False, False, 0)
        migbox.pack_start(cigcreatebutton, False, False, 0)         
        migbox.pack_start(cigresetbutton, False, False, 0)   
        migbox.pack_start(migseparator, False, False, 25)       
        migbox.pack_start(ciglistlabel, False, False, 0) 
        migbox.pack_start(self.ciglcombo, False, False, 0)  
        migbox.pack_start(cigdeletebutton, False, False, 0)          
                
        self.inventorystack.add_titled(inventoryview_box, "viewinventorymain", "Current stock")
        self.inventorystack.add_titled(createitembox, "createitemmain", "Create item")
        self.inventorystack.add_titled(edititem_box, "edititemmain", "Edit or view Item")
        self.inventorystack.add_titled(migbox, "createitemgroupmain", "Manage item groups")        
        
        #print("Packing of stack switcher in Create pane started")  
        self.inventorystack_switcher = Gtk.StackSwitcher()
        self.inventorystack_switcher.set_stack(self.inventorystack)
        
        #print("Packing of stack started")  
        self.inventorymasterbox.pack_start(self.inventorystack_switcher, False, False, 10)
        self.inventorymasterbox.pack_start(self.inventorystack, False, False, 10)
        #print("Just above return statement in Create pane")  
           
        return self.inventorymasterbox 
              
            
    #-------- Functions used in inventory page ---------------------------------------------

    def blankfunc(self):
        print("hello, this is blank function")
        

    def processcitem(self, widget, civarg, invoicingbox, bph, guiinvoicingins):
    
        iname=self.cinameentry.get_text().capitalize()
        isoftversion='1'
        ihsn=self.cihsnentry.get_text()
        igroup=self.cigroupcombo.get_active_text()
        isubgroup=self.cisubgroupentry.get_text()
        iunit=self.ciunitcombo.get_active_text()
        itax=self.citaxcombo.get_active_text()
        
        if self.citaxinclusive_button.get_active():
            itaxinclusive='y'      
        else:        
            itaxinclusive='n'
        
        ilastmodified=functions.todaysdate_string
        iopstock=self.ciopenstentry.get_text() # opening stock of financial year
        isoldunits='0'
        icurrentstock=self.ciopenstentry.get_text()
        icritical=self.cicritentry.get_text()
        ilistprice=self.cilpentry.get_text()
        istddisc=self.cisdentry.get_text()
        isellprice=self.cispentry.get_text()
        ipurprice=self.cippentry.get_text()
        icomments=self.cicommentry.get_text()
        iflag=self.ciflagentry.get_text()
        
        #reserved for future implementation, dont mess with these 4, create new if required
        iphasedout='NA' 
        icreationdate='NA' # item creation date, keep for emergency and future features
        icreationstock='NA' #stock on item creation date
        iemerg='NA'
        #reserved variables end
        
        # iphasedout, iemerg, icreationdate, icreationstock  reserved for future features,dont use these. Create new if required.
        idata=[iname, iphasedout, iemerg, icreationdate, icreationstock, isoftversion, ihsn, igroup, isubgroup, iunit, itax, itaxinclusive,  ilastmodified, iopstock, isoldunits, icurrentstock, icritical, ilistprice, istddisc, isellprice, ipurprice, icomments, iflag]
                
        #print(idata)
        self.itemtableins.createrow(idata[0], idata)
        #iteminstance.createitem(idata)
        self.reset_cientries('nobuttonpress')
        guicommon.loadguicommon()
        
        self.einame_completion.set_model(guicommon.itemname_store)
        self.ei_nameentry.set_completion(self.einame_completion) 
        
        children=invoicingbox.get_children()
        for eachchild in children:
            invoicingbox.remove(eachchild)
            eachchild.destroy()
        bph=guiinvoicingins.billingpage(self.mainwindow)
        invoicingbox.add(bph)
        invoicingbox.show_all()        
        
        print("Successfully created item")
        return 1
  
  
    #function to clear entries for resetbutton
    def reset_cientries(self, ifbuttonevent):
        self.cinameentry.set_text('')
        self.cihsnentry.set_text(''),
        self.cigroupcombo.set_active(0)
        self.cisubgroupentry.set_text('')
        #ciunitcombo.set_active(1)
        #citaxcombo.set_active(0) 
        self.ciopenstentry.set_text('')
        self.cicritentry.set_text('')
        self.cilpentry.set_text('')
        self.cisdentry.set_text('')
        self.cispentry.set_text('')
        self.cippentry.set_text('')
        self.cicommentry.set_text('')

    
    
    def process_eitem(self, widget, eivarg, invoicingbox, bph, guiinvoicingins):
        print('process ei called')
        iname=self.einameentry.get_text()
        isoftversion='1'
        ihsn=self.eihsnentry.get_text()
        igroup=self.eigroupcombo.get_active_text()
        isubgroup=self.eisubgroupentry.get_text()
        iunit=self.eiunitcombo.get_active_text()
        itax=self.eitaxcombo.get_active_text()
        if self.citaxinclusive_button.get_active():
            itaxinclusive='y'      
        else:        
            itaxinclusive='n'
        ilastmodified=functions.todaysdate_string    
        iopstock=self.eiopenstentry.get_text() # opening stock of financial year
        isoldunits=self.ei_tempsoldunits
        icurrentstock=self.ei_tempcurrentstock
        icritical=self.eicritentry.get_text()
        ilistprice=self.eilpentry.get_text()
        istddisc=self.eisdentry.get_text()
        isellprice=self.eispentry.get_text()
        ipurprice=self.eippentry.get_text()
        icomments=self.eicommentry.get_text()
        iflag=self.eiflagentry.get_text()
        
         #reserved for future implementation, dont mess with these 4, create new if required
        iphasedout='NA' 
        icreationdate='NA' # item creation date, keep for emergency and future features
        icreationstock='NA' #stock on item creation date
        iemerg='NA'
        #reserved variables end
        
        # iphasedout, iemerg, icreationdate, icreationstock  reserved for future features,dont use these. Create new if required.
        idata=idata=[iname, iphasedout, iemerg, icreationdate, icreationstock, isoftversion, ihsn, igroup, isubgroup, iunit, itax, itaxinclusive,  ilastmodified, iopstock, isoldunits, icurrentstock, icritical, ilistprice, istddisc, isellprice, ipurprice, icomments, iflag]
         
        # Provided creation date and creationstock as failsafe, plus for future reference, can also be used to verify stocks

        self.itemtableins.editrow(self.noite, idata)
        self.reset_eientries('nobuttonpress', self.eientries)
        
        guicommon.loadguicommon()
        self.einame_completion.set_model(guicommon.itemname_store)
        self.ei_nameentry.set_completion(self.einame_completion) 
        
        children=invoicingbox.get_children()
        for eachchild in children:
            invoicingbox.remove(eachchild)
            eachchild.destroy()
        bph=guiinvoicingins.billingpage()
        invoicingbox.add(bph)
        invoicingbox.show_all()
        
        print("Successfully modified item")
        return 1 
    
        
    def reset_eientries(self, reseterwidget, entrieslist):
        for eachentry in entrieslist:
            eachentry.set_text('')
        self.eigroupcombo.set_active(0)
        self.ei_nameentry.set_text('')
        self.ei_tempsoldunits=0
        self.ei_tempcurrentstock=0  
        self.noite=''   
        for everyentry in self.eivarg:
            everyentry.set_sensitive(False)     
        return 1
                            
    
    def set_eientries(self, seterwidget, entrieslist):
        self.noite=self.ei_nameentry.get_text() #name of item to be edited
        eifetcheditem=self.itemtableins.readrow(self.noite)   
        self.ei_temprowindex=self.itemtableins.rowlist.index(self.noite)
        #print('row ei index is')
        #print(self.ei_temprowindex)
        
        for eachoftheentry in self.eivarg:
            eachoftheentry.set_sensitive(True)          
    
        self.einameentry.set_text(eifetcheditem[0])
        self.eihsnentry.set_text(eifetcheditem[6])
        self.eisubgroupentry.set_text(eifetcheditem[8])
        self.eiopenstentry.set_text(eifetcheditem[13])
        self.eicritentry.set_text(eifetcheditem[16])
        self.eilpentry.set_text(eifetcheditem[17])
        self.eisdentry.set_text(eifetcheditem[18])
        self.eispentry.set_text(eifetcheditem[19])
        self.eippentry.set_text(eifetcheditem[20])
        self.eicommentry.set_text(eifetcheditem[21])
        self.eiflagentry.set_text(eifetcheditem[22])
        
        for eachigroup in self.itemgroups:
            eachigroup_id=eachigroup + 'gtkid'
            self.eigroupcombo.append(eachigroup_id, eachigroup)
        self.eigroupcombo.get_child().set_text(eifetcheditem[7])
        self.eiunitcombo.get_child().set_text(eifetcheditem[9])
        self.eitaxcombo.get_child().set_text(eifetcheditem[10])
        if eifetcheditem[11]=='n':
            self.eitaxinclusive_button.set_active(False)
        elif eifetcheditem[11]=='y':
            self.eitaxinclusive_button.set_active(True)
        self.ei_tempsoldunits=eifetcheditem[14]
        self.ei_tempcurrentstock=eifetcheditem[15]     

        return 1
   
    def deleteitem (self, delbutton, invoicingbox, bph, guiinvoicingins):  
        self.noite=self.ei_nameentry.get_text() #name of item to be edited 
        self.itemtableins.deleterow(self.noite) 
        #self.reset_eientries('nobuttonpress', self.eientries)
        guicommon.loadguicommon()
        self.einame_completion.set_model(guicommon.itemname_store)
        self.ei_nameentry.set_completion(self.einame_completion) 
        children=invoicingbox.get_children()
        for eachchild in children:
            invoicingbox.remove(eachchild)
            eachchild.destroy()
        bph=guiinvoicingins.billingpage()
        invoicingbox.add(bph)
        invoicingbox.show_all()
        return 1                  
    
    def cigfunc(self, buttonsignal):
        newig=self.cignameentry.get_text()
        self.miscdb.ladd('itemgroups', newig)
        self.miscdb.dump()
        self.itemgroups=self.miscdb.get('itemgroups')
        self.reset_cigentry('mockevent')
        self.ciglcombo.append_text(newig)
        self.cigroupcombo.append_text(newig)
        self.reset_eientries('mockpress', self.eientries)
        print ('created new item group')
        
        
    def reset_cigentry(self, reseterwidget):    
        self.cignameentry.set_text('')
        
        
    def deleteig(self, buttonsignal):
        print('started processing delete')
        delig=self.ciglcombo.get_active_text()
        print(delig)
        delig_index=self.miscdb.get('itemgroups').index(delig)
        print('above pop command')
        self.miscdb.lpop('itemgroups', delig_index)
        self.miscdb.dump()
        self.itemgroups=self.miscdb.get('itemgroups')
        self.reset_cigentry('mockevent')
        self.ciglcombo.remove_all()
        #guicommon.loadguicommon()
        for eg in guicommon.itemgroups:
            self.ciglcombo.append_text(eg)
        self.ciglcombo.set_active(0)
        print ('deleted item group')    
