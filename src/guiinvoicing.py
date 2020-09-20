# This file contains gui pages of main stack: Ver sep 2020

import sys
import gi
from submods import functions
from submods import guicommon
from submods import guiprocessor
from datetime import datetime

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkInvoicing():

    #---------------------------Billbox contents start     
     
    def billingpage(self):
        #print('billing page coding start')        
        
        self.guiprocessor_ins=guiprocessor.GtkProcessor()
        
        
        invoicingmasterbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)    
        billbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        
        invoicingstack = Gtk.Stack()
        invoicingstack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        invoicingstack.set_transition_duration(1000)
            
        gridheader = Gtk.Grid()
        gridheader.set_column_homogeneous(False)
        billbox.pack_start(gridheader, True, True, 0)

        bbhseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)  
        billbox.pack_start(bbhseparator, True, True, 0)              
                       
        billboxmat = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        billbox.pack_start(billboxmat, False, False, 0)
          
        gridfooter = Gtk.Grid()
        billbox.pack_start(gridfooter, True, True, 0)
        gridfooter.set_column_homogeneous(False)
        gridfooter.set_row_homogeneous(True)
                   
        invnolabel = Gtk.Label()
        invnolabel.set_markup("Invoice No.")
             
        self.invoicenmbr = Gtk.Entry()
        
        #self.invoicenmbr.set_text()       
        
        #invoicenmbr.compute_expand(hexpand)
                    
        invdatelabel = Gtk.Label()
        invdatelabel.set_markup("Invoice date")
        
        self.invoicedate = Gtk.Entry()
        self.invoicedate.set_text(functions.todaysdate_string)
        self.invoicedate.set_width_chars(10)
               
        invcompanylabel = Gtk.Label()
        invcompanylabel.set_markup("Company")
                   
        self.invcompany = Gtk.Entry()
        self.invcompany.set_width_chars(32)
        self.invcompany.set_text('')
        nciname_completion = Gtk.EntryCompletion()
        nciname_completion.set_model(guicommon.companyname_store)
        nciname_completion.set_text_column(0)
        self.invcompany.set_completion(nciname_completion)      
            
        polabel = Gtk.Label()
        polabel.set_markup("Purchase order No.")        
            
        self.ponmbr = Gtk.Entry()
        self.ponmbr.set_width_chars(16)
                    
        taxlabel = Gtk.Label()
        taxlabel.set_markup("Tax slab")       
            
        name_store = Gtk.ListStore(int, str)
        name_store.append([1, "Billy Bob"])
        name_store.append([11, "Billy Bob Junior"])
        name_store.append([12, "Sue Bob"])
        name_store.append([2, "Joey Jojo"])
        name_store.append([3, "Rob McRoberts"])
        name_store.append([31, "Xavier McRoberts"])
            
        
        taxcombo = Gtk.ComboBoxText.new_with_entry()
        taxcombo.insert(position=0, id="g12", text="GST-12%")
        taxcombo.insert(position=1, id="g18", text="GST-18%")
        taxcombo.set_active(1)
        taxcombo.get_child().set_width_chars(16)       
            
        taxontaxlabel = Gtk.Label() # comments
        taxontaxlabel.set_markup("Tax on Tax slab")
        
        self.taxontaxcombo = Gtk.ComboBoxText.new_with_entry()
        self.taxontaxcombo.insert(position=0, id="taxontaxnone", text="None")
        self.taxontaxcombo.insert(position=1, id="taxontaxeducess2p", text="Education Cess 2%")
        self.taxontaxcombo.set_active(0)
        self.taxontaxcombo.get_child().set_width_chars(16)              
            
        self.comentry = Gtk.Entry()
        self.comentry.set_width_chars(16)
        self.comentry.set_text("")            
            
        gridheader.add(invnolabel)
        gridheader.attach(self.invoicenmbr, 0, 1, 1, 1)
        gridheader.attach(invdatelabel, 1, 0, 1, 1)
        gridheader.attach(self.invoicedate, 1, 1, 1, 1)
        gridheader.attach(invcompanylabel, 2, 0, 1, 1)
        gridheader.attach(self.invcompany, 2, 1, 1, 1)
        gridheader.attach(polabel, 4, 0, 1, 1)
        gridheader.attach(self.ponmbr, 4, 1, 1, 1)
        gridheader.attach(taxlabel, 5, 0, 1, 1)
        gridheader.attach(taxcombo, 5, 1, 1, 1)
        gridheader.attach(taxontaxlabel, 6, 0, 1, 1)
        gridheader.attach(self.taxontaxcombo, 6, 1, 1, 1)
        #grid.attach_next_to(invnolabel, invnolabel, Gtk.PositionType.RIGHT, 1, 1)
          
            # Items to be billed below
        billitems_headerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)    
        bihb_srlabel = Gtk.Label(label="Sr. No.", xalign=0)
        bihb_srlabel.set_width_chars(8)
        bihb_inamelabel = Gtk.Label(label="Item name           ")
        bihb_inamelabel.set_width_chars(47)
        bihb_iqtylabel = Gtk.Label(label="Quantity")
        bihb_iqtylabel.set_width_chars(10)
        bihb_isplabel = Gtk.Label(label="Selling price")
        bihb_isplabel.set_width_chars(15)
        bihb_idisclabel = Gtk.Label(label="Discount")
        bihb_idisclabel.set_width_chars(8)
        bihb_iamtlabel = Gtk.Label(label="Amount")
        bihb_iamtlabel.set_width_chars(16)
        bihb_icommentlabel = Gtk.Label(label="  Short comments")
        bihb_icommentlabel.set_width_chars(16)
        bihb_icommentlabel.set_margin_left(20)
        
       # item1label.set_markup("Item 1 to be billed")
        billitems_headerbox.pack_start(bihb_srlabel, False, False, 0)
        billitems_headerbox.pack_start(bihb_inamelabel, False, False, 0)
        billitems_headerbox.pack_start(bihb_iqtylabel, False, False, 0)
        billitems_headerbox.pack_start(bihb_isplabel, False, False, 0)
        billitems_headerbox.pack_start(bihb_idisclabel, False, False, 0)
        billitems_headerbox.pack_start(bihb_iamtlabel, False, False, 0)
        billitems_headerbox.pack_start(bihb_icommentlabel, False, False, 0)
        billboxmat.pack_start(billitems_headerbox, True, True, 0)
       
        def createinvoicerows(howmany):
            ncii_listbox = Gtk.ListBox() #ncii=new customer invoice items
            ncii_listbox.set_selection_mode(Gtk.SelectionMode.NONE)
            #inventorystore=Gtk.ListStore(str)
            #print (len(self.itemtableins.rowlist))
            ncii_tempcount=0
            self.nciilb_inamelist=[]
            self.nciilb_iqtylist=[]
            self.nciilb_isplist=[]
            self.nciilb_idiscountlist=[]
            self.nciilb_iamtlist=[]
            self.nciilb_icommlist=[]
            self.nciilb_ihsnlist=[]
            while ncii_tempcount<howmany:
                           
                nciilb_temprow = Gtk.ListBoxRow()
                #nciilb_temprow.set_hexpand(False)
                #nciilb_temprow.get_style_context().add_class("testareaanother")
                nciilbvr_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
                nciilbvr_box.set_hexpand(False)
                nciilbvr_box.set_halign(Gtk.Align.CENTER) # to avoid expansion horizontally
                #nciilbvr_box.get_style_context().add_class("testarea")
                
                nciiserial_templabel = Gtk.Label(label=ncii_tempcount+1)
                nciiserial_templabel.set_width_chars(4)
                nciiname_tempentry = Gtk.Entry()
                nciiname_tempentry.set_width_chars(47)                                
                invitemname_completion = Gtk.EntryCompletion()
                invitemname_completion.set_model(guicommon.itemname_store)
                invitemname_completion.set_text_column(0)
                nciiname_tempentry.set_completion(invitemname_completion)               
                nciicomm_tempentry = Gtk.Entry() # for more item description/change
                nciicomm_tempentry.set_width_chars(18)
                nciiqty_tempentry = Gtk.Entry()
                nciiqty_tempentry.set_width_chars(10)
                nciisp_tempentry = Gtk.Entry() # item selling price
                nciisp_tempentry.set_width_chars(12)
                nciidiscount_tempentry = Gtk.Entry() # item selling price
                nciidiscount_tempentry.set_width_chars(6)                        
                nciiamt_templabel = Gtk.Label(label='0.00')
                nciiamt_templabel.set_width_chars(16)
                nciiamt_templabel.set_margin_left(10)
                nciiamt_templabel.set_margin_right(10)
                
                nciilbvr_box.pack_start(nciiserial_templabel, False, False, 0)
                nciilbvr_box.pack_start(nciiname_tempentry, False, False, 0)
                nciilbvr_box.pack_start(nciiqty_tempentry, False, False, 0)
                nciilbvr_box.pack_start(nciisp_tempentry, False, False, 0)
                nciilbvr_box.pack_start(nciidiscount_tempentry, False, False, 0)
                nciilbvr_box.pack_start(nciiamt_templabel, False, False, 0)
                nciilbvr_box.pack_start(nciicomm_tempentry, False, False, 0) # for more item description/change
                
                nciilb_temprow.add(nciilbvr_box) 
                ncii_listbox.add(nciilb_temprow)
                ncii_listbox.show_all()
                #print('listrow calld')
                
                # for accessing - fetching data
                self.nciilb_inamelist.append(nciiname_tempentry) 
                self.nciilb_isplist.append(nciisp_tempentry)
                self.nciilb_iqtylist.append(nciiqty_tempentry)
                self.nciilb_iamtlist.append(nciiamt_templabel)
                self.nciilb_icommlist.append(nciicomm_tempentry)
                
                def ncii_settempamt(ncii_valuesig):
                    tempindex=self.nciilb_iqtylist.index(ncii_valuesig)
                    self.nciilb_iamtlist[tempindex].set_markup(ncii_valuesig.get_text()) 
                    print(ncii_valuesig.get_text())
                    #print('====below is index of text field')
                    
                    #print(self.nciilb_iqtylist[ncii_tempcount].get_text())  
                nciiqty_tempentry.connect("changed", ncii_settempamt)      
                
                
                ncii_tempcount=ncii_tempcount+1
            return ncii_listbox
            
        def addmoreitems(event):
            invoicesw.remove(invoicesw.get_child())
            print('removed previous')
            invoicesw.add(createinvoicerows("blankevent"))
            print('added new')                
        
        itemstobebilled=createinvoicerows(100)
            
        amibutton = Gtk.Button.new_with_label("Add more items") #add more items
        amibutton.set_name('amibut')
        #amibutton.get_style_context().add_class("dangerbutton")    
        amibutton.connect("clicked", addmoreitems)
       
        iisw = Gtk.ScrolledWindow() #invoice items scroll window
        #iisw.set_min_content_width(720)      
        #iisw.set_max_content_width(768)
        iisw.set_min_content_height(390)
        #iisw.set_max_content_height(720)
        iisw.get_style_context().add_class("lightgreymedborder")
        iisw.set_policy(Gtk.PolicyType.NEVER,
                               Gtk.PolicyType.AUTOMATIC)
        #print(iisw.get_propagate_natural_width())
        iisw.set_halign(Gtk.Align.START) # to avoid expansion horizontally
        
        iisw.add(itemstobebilled)
        billboxmat.pack_start(iisw, False, False, 0)
                   
        # billbox Footer coding below    
            
        basicamtlabel = Gtk.Label()
        basicamtlabel.set_markup("Basic amount")
           
        self.basicamtdisp = Gtk.Label()
        self.basicamtdisp.set_width_chars(16)
        self.basicamtdisp.set_margin_right(10)
        self.basicamtdisp.set_markup("0.0")        
            
        discountlabel = Gtk.Label() # discount applicable
        discountlabel.set_markup("Discount")
           
        self.discountentry = Gtk.Entry()
        #self.discountentry.set_text("10")
        self.discountentry.set_width_chars(8)
        
        freightlabel = Gtk.Label() # freight courier charges
        freightlabel.set_markup("Freight")
           
        self.freightentry = Gtk.Entry()
        #self.freightentry.set_text("")
        self.freightentry.set_width_chars(8)
           
        mischlabel = Gtk.Label() # miscellaneous charges
        mischlabel.set_markup("Other charges")        
            
        self.mischentry = Gtk.Entry()
        #self.mischentry.set_text("200")
        self.mischentry.set_width_chars(8)
        
        taxlabel = Gtk.Label() # tax
        taxlabel.set_margin_left(10)
        taxlabel.set_margin_right(5)
        taxlabel.set_markup("Tax")
        
        self.taxamount = Gtk.Label() # tax
        self.taxamount.set_markup("0.0")
        self.taxamount.set_width_chars(16)
        self.taxamount.set_margin_left(10)
        self.taxamount.set_margin_right(5)
        
        taxontaxlabel = Gtk.Label() # tax on tax
        taxontaxlabel.set_margin_left(10)
        taxontaxlabel.set_margin_right(10)
        taxontaxlabel.set_markup("Tax on Tax amount")
        
        self.taxontaxamount = Gtk.Label() # tax
        self.taxontaxamount.set_markup("0.0")
        self.taxontaxamount.set_width_chars(12)
        self.taxontaxamount.set_margin_left(5)
        self.taxontaxamount.set_margin_right(10)
           
        gtotallabel = Gtk.Label() #grand total
        
        gtotallabel.set_markup("Grand total")
        #gtotallabel.get_style_context().add_class("boldsimplelabel")    
        self.gtotaldisp = Gtk.Label()
        self.gtotaldisp.get_style_context().add_class("boldgreenlabel")
        self.gtotaldisp.set_width_chars(16)
        self.gtotaldisp.set_margin_left(10)
        self.gtotaldisp.set_margin_right(10)
        self.gtotaldisp.set_markup("0.0")
        
        offsetterlabel1 = Gtk.Label() #
        offsetterlabel1.set_markup("        ")
        offsetterlabel1.set_width_chars(8)
        
        offsetterlabel2 = Gtk.Label() #
        offsetterlabel2.set_markup("        ")
        offsetterlabel2.set_width_chars(8)
        
        
        def processnci(butonevent):
            self.guiprocessor_ins.cni_processnci(self.nciilb_inamelist, self.nciilb_iqtylist, self.nciilb_isplist, self.nciilb_idiscountlist, self.nciilb_iamtlist, self.nciilb_icommlist, self.nciilb_ihsnlist)
        
        def resetncifields(butonevent):
            nciname_completion.set_model(guicommon.companyname_store)
                       
        invoiceresetbutton = Gtk.Button.new_with_label("Reset")
        invoiceresetbutton.get_style_context().add_class("dangerbutton")
        invoiceresetbutton.connect("clicked", resetncifields)
        invoiceresetbutton.set_margin_left(20)
        
        nextbutton = Gtk.Button.new_with_label("Next")
        nextbutton.get_style_context().add_class("suggested-action")
        nextbutton.connect("clicked", processnci)
            
        #billboxfooter.add(resetbutton)
            
        gridfooter.add(basicamtlabel)
        gridfooter.attach(self.basicamtdisp, 0, 1, 1, 1)
        gridfooter.attach(discountlabel, 1, 0, 1, 1)
        gridfooter.attach(self.discountentry, 1, 1, 1, 1)
        gridfooter.attach(freightlabel, 2, 0, 1, 1)
        gridfooter.attach(self.freightentry, 2, 1, 1, 1)
        gridfooter.attach(mischlabel, 3, 0, 1, 1)
        gridfooter.attach(self.mischentry, 3, 1, 1, 1)
        gridfooter.attach(taxlabel, 4, 0, 1, 1)
        gridfooter.attach(self.taxamount, 4, 1, 1, 1)
        gridfooter.attach(taxontaxlabel, 5, 0, 1, 1)
        gridfooter.attach(self.taxontaxamount, 5, 1, 1, 1)
        
        gridfooter.attach(gtotallabel, 6, 0, 2, 1)
        gridfooter.attach(self.gtotaldisp, 6, 1, 2, 1)
        
        gridfooter.attach(offsetterlabel1, 8, 0, 1, 1)
        gridfooter.attach(offsetterlabel2, 8, 1, 1, 1)
        
        gridfooter.attach(invoiceresetbutton, 9, 1, 1, 1)
        gridfooter.attach(nextbutton, 10, 1, 1, 1)
        #gridfooter.attach(gtotaldisp, 3, 1, 1, 1)
        
        #print('above adding box to stack') 
        invoicingstack.add_titled(billbox, "custinvbox", "New Customer invoice")
        
        invoicingstack_switcher = Gtk.StackSwitcher()
        invoicingstack_switcher.set_stack(invoicingstack)
        invoicingstack_switcher.set_margin_bottom(8)
        
        #print("Packing of invoicing stack started")  
        invoicingmasterbox.pack_start(invoicingstack_switcher, False, False, 5)
        invoicingmasterbox.pack_start(invoicingstack, True, True, 0)        
        
        #self.invoicenmbr.grab_focus() trying to auto activate
        return invoicingmasterbox
            
        #---------------------------Billbox contents end    
        
 
