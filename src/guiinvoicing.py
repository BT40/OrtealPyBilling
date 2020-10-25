# This file contains gui pages of main stack: Ver sep 2020

import sys
import gi
from submods import functions
from submods import guicommon
from submods import guiprocessor
from submods import saleinvoicingprocessor
from submods import pdfsaleinvoice
from submods import printsihandler
from datetime import datetime

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkInvoicing():

    #---------------------------Billbox contents start     
     
    def billingpage(self, mainwindow):
        #print('billing page coding start')        
        self.mainwindow=mainwindow
        self.temp_basicamt=0 #initializing for tax combo compatibility
        self.taxable_amount=0
        self.roundoff_enabled='n'
        self.roundoff_amt=0
        
        self.guiprocessor_ins=guiprocessor.GtkProcessor()        
        
        invoicingmasterbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)    
        billbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        
        invoicingstack = Gtk.Stack()
        invoicingstack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        invoicingstack.set_transition_duration(1000)
            
        gridheader = Gtk.Grid()
        gridheader.set_column_homogeneous(False)
        billbox.pack_start(gridheader, True, True, 0)

        #bbhseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)  
        #billbox.pack_start(bbhseparator, True, True, 0)              
                       
        billboxmat = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        billbox.pack_start(billboxmat, False, False, 0)
          
        gridfooter = Gtk.Grid()
        billbox.pack_start(gridfooter, True, True, 0)
        gridfooter.set_column_homogeneous(False)
        gridfooter.set_row_homogeneous(True)
                   
        invnolabel = Gtk.Label()
        invnolabel.set_markup("Invoice No.")
             
        self.invoicenmbr = Gtk.Entry()
        self.invoicenmbr.set_max_length(16)
        
        #self.invoicenmbr.set_text()       
        
        #invoicenmbr.compute_expand(hexpand)
                    
        invdatelabel = Gtk.Label()
        invdatelabel.set_markup("Invoice date")
        
        self.invoicedate = Gtk.Entry()
        self.invoicedate.set_text(functions.todaysdate_string)
        self.invoicedate.set_width_chars(10)
        self.invoicedate.set_max_length(10)
               
        invcompanylabel = Gtk.Label()
        invcompanylabel.set_markup("Company")
                   
        self.invcompany = Gtk.Entry()
        self.invcompany.set_width_chars(32)
        self.invcompany.set_max_length(47)
        self.invcompany.set_text('')
        self.nciname_completion = Gtk.EntryCompletion()
        self.nciname_completion.set_model(guicommon.companyname_store)
        self.nciname_completion.set_text_column(0)
        self.invcompany.set_completion(self.nciname_completion)      
            
        polabel = Gtk.Label()
        polabel.set_markup("Purchase order No.")        
            
        self.ponmbr = Gtk.Entry()
        self.ponmbr.set_width_chars(16)
        self.ponmbr.set_max_length(16)
                    
        taxlabel = Gtk.Label()
        taxlabel.set_markup("Tax slab")       
                  
        self.taxcombo = Gtk.ComboBoxText.new_with_entry()
        for ets in guicommon.taxtableins.rowlist:
            self.taxcombo.append_text(ets)        
        self.taxcombo.set_active(3)
        self.taxcombo.get_child().set_width_chars(18)   
        self.taxcombo.connect("changed", self.grandcaller)     
            
        taxontaxlabel = Gtk.Label() # comments
        taxontaxlabel.set_markup("Tax on Tax slab")
        
        self.taxontaxcombo = Gtk.ComboBoxText.new_with_entry()
        for etots in guicommon.taxontax_list:
            self.taxontaxcombo.append_text(etots)
        self.taxontaxcombo.set_active(0)
        self.taxontaxcombo.get_child().set_width_chars(16)  
        self.taxontaxcombo.connect("changed", self.grandcaller)                
            
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
        gridheader.attach(self.taxcombo, 5, 1, 1, 1)
        gridheader.attach(taxontaxlabel, 6, 0, 1, 1)
        gridheader.attach(self.taxontaxcombo, 6, 1, 1, 1)
        #grid.attach_next_to(invnolabel, invnolabel, Gtk.PositionType.RIGHT, 1, 1)
          
            # Items to be billed below
        billitems_headerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)  
        billitems_headerbox.set_margin_top(8)  
        bihb_srlabel = Gtk.Label(label="Sr. No.", xalign=0)
        bihb_srlabel.set_width_chars(8)
        bihb_inamelabel = Gtk.Label(label="Item name           ")
        bihb_inamelabel.set_width_chars(47)
        bihb_iqtylabel = Gtk.Label(label="Quantity")
        bihb_iqtylabel.set_width_chars(9)
        bihb_isplabel = Gtk.Label(label="Selling price")
        bihb_isplabel.set_margin_left(35)
        bihb_idisclabel = Gtk.Label(label="Discount %")
        bihb_idisclabel.set_margin_left(22)
        bihb_icommentlabel = Gtk.Label(label="Short comments")
        bihb_icommentlabel.set_sensitive(False)
        bihb_icommentlabel.set_margin_left(22)
        bihb_icommentlabel.set_margin_right(25)
        bihb_iamtlabel = Gtk.Label(label="Amount")
        bihb_iamtlabel.set_margin_left(75)
        
       # item1label.set_markup("Item 1 to be billed")
        billitems_headerbox.pack_start(bihb_srlabel, False, False, 0)
        billitems_headerbox.pack_start(bihb_inamelabel, False, False, 0)
        billitems_headerbox.pack_start(bihb_iqtylabel, False, False, 0)
        billitems_headerbox.pack_start(bihb_isplabel, False, False, 0)
        billitems_headerbox.pack_start(bihb_idisclabel, False, False, 0)
        billitems_headerbox.pack_start(bihb_icommentlabel, False, False, 0)
        billitems_headerbox.pack_start(bihb_iamtlabel, False, False, 0)       
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
            self.nciilb_icommlist=[]
            self.nciilb_iamtlist=[]
            
            while ncii_tempcount<howmany:
                           
                nciilb_temprow = Gtk.ListBoxRow()
                #nciilb_temprow.set_hexpand(False)
                #nciilb_temprow.get_style_context().add_class("testareaanother")
                nciilbvr_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
                nciilbvr_box.set_hexpand(False)
                nciilbvr_box.set_halign(Gtk.Align.START) # to avoid expansion horizontally
                #nciilbvr_box.get_style_context().add_class("testarea")
                
                nciiserial_templabel = Gtk.Label(label=ncii_tempcount+1)
                nciiserial_templabel.set_width_chars(4)
                nciiname_tempentry = Gtk.Entry()
                nciiname_tempentry.set_width_chars(47)    
                nciiname_tempentry.set_max_length(47)                            
                invitemname_completion = Gtk.EntryCompletion()
                invitemname_completion.set_model(guicommon.itemname_store)
                invitemname_completion.set_text_column(0)
                nciiname_tempentry.set_completion(invitemname_completion)               
                nciicomm_tempentry = Gtk.Entry() # for more item description/change
                nciicomm_tempentry.set_width_chars(16)
                nciicomm_tempentry.set_max_length(47)   
                nciicomm_tempentry.set_sensitive(False)
                #nciicomm_tempentry.set_editable(False)
                nciiqty_tempentry = Gtk.Entry()
                nciiqty_tempentry.set_width_chars(10)
                nciiqty_tempentry.set_max_length(11)   
                nciisp_tempentry = Gtk.Entry() # item selling price
                nciisp_tempentry.set_width_chars(12)
                nciisp_tempentry.set_max_length(11)   
                nciidiscount_tempentry = Gtk.Entry() # item selling price
                nciidiscount_tempentry.set_width_chars(6)  
                nciidiscount_tempentry.set_max_length(5)                         
                nciiamt_templabel = Gtk.Label(label='0.00')
                nciiamt_templabel.set_width_chars(21)
                nciiamt_templabel.set_margin_left(8)
                nciiamt_templabel.set_margin_right(8)
                
                nciilbvr_box.pack_start(nciiserial_templabel, False, False, 0)
                nciilbvr_box.pack_start(nciiname_tempentry, False, False, 0)
                nciilbvr_box.pack_start(nciiqty_tempentry, False, False, 0)
                nciilbvr_box.pack_start(nciisp_tempentry, False, False, 0)
                nciilbvr_box.pack_start(nciidiscount_tempentry, False, False, 0)
                nciilbvr_box.pack_start(nciicomm_tempentry, False, False, 0) # for more item description/change
                nciilbvr_box.pack_start(nciiamt_templabel, False, False, 0)
                
                
                nciilb_temprow.add(nciilbvr_box) 
                ncii_listbox.add(nciilb_temprow)
                ncii_listbox.show_all()
                #print('listrow calld')
                
                # for accessing - fetching data
                self.nciilb_inamelist.append(nciiname_tempentry) 
                self.nciilb_isplist.append(nciisp_tempentry)
                self.nciilb_iqtylist.append(nciiqty_tempentry)
                self.nciilb_idiscountlist.append(nciidiscount_tempentry)
                self.nciilb_icommlist.append(nciicomm_tempentry)
                self.nciilb_iamtlist.append(nciiamt_templabel)
                
                
                def ncii_calcu(tempindex, temprate_str, tempqty_str, tempdisc_str):
                    if tempqty_str=='' or temprate_str=='': 
                        #print('qty or rate not present')
                        pass
                    
                    else:
                        #print('conditions met, now calculating') 
                        #print(tempqty_str)  
                        #print('above is tempqty str')
                        tempqty_int=int(tempqty_str)
                        temprate_int=float(temprate_str)                       
                        if tempdisc_str=='':
                            tempdisc_float=0
                            #print('discount not set')
                        else:    
                            tempdisc_float=float(tempdisc_str)
                            #print('discount set')
                        tempamt=temprate_int*tempqty_int*((100-tempdisc_float)/100)
                        
                        self.nciilb_iamtlist[tempindex].set_markup(str(tempamt)) 
                        self.temp_basicamt=saleinvoicingprocessor.saleamounting(self.nciilb_iamtlist)
                        self.basicamtdisp.set_markup(str(self.temp_basicamt))
                        
                        self.grandcaller('mimicevent')
                        
                    
              
                def ncii_setterini(ncii_valuesig):
                    tempindex=self.nciilb_inamelist.index(ncii_valuesig)
                    tempname=ncii_valuesig.get_text()
                    tempdbindex=guicommon.itemtableins.rowlist.index(tempname)
                    tempmrp=guicommon.itemtableins.rowcollection[tempdbindex][17]
                    self.nciilb_isplist[tempindex].set_text(str(tempmrp))
                nciiname_tempentry.connect("changed", ncii_setterini) 
                
                def ncii_changedqty(ncii_valuesig):
                    tempindex=self.nciilb_iqtylist.index(ncii_valuesig)
                    tempqty_str=ncii_valuesig.get_text()
                    temprate_str=self.nciilb_isplist[tempindex].get_text()
                    tempdisc_str=self.nciilb_idiscountlist[tempindex].get_text()
                    ncii_calcu(tempindex, temprate_str, tempqty_str, tempdisc_str)
                    
                nciiqty_tempentry.connect("changed", ncii_changedqty)      
                
                def ncii_changedsp(ncii_valuesig):
                    tempindex=self.nciilb_isplist.index(ncii_valuesig)
                    temprate_str=ncii_valuesig.get_text()
                    tempqty_str=self.nciilb_iqtylist[tempindex].get_text()
                    tempdisc_str=self.nciilb_idiscountlist[tempindex].get_text()
                    ncii_calcu(tempindex, temprate_str, tempqty_str, tempdisc_str)
               
                nciisp_tempentry.connect("changed", ncii_changedsp)  
                
                def ncii_changedisc(ncii_valuesig):
                    tempindex=self.nciilb_idiscountlist.index(ncii_valuesig)
                    tempdisc_str=ncii_valuesig.get_text()
                    temprate_str=self.nciilb_isplist[tempindex].get_text()
                    tempqty_str=self.nciilb_iqtylist[tempindex].get_text()
                    ncii_calcu(tempindex, temprate_str, tempqty_str, tempdisc_str)
               
                nciidiscount_tempentry.connect("changed", ncii_changedisc)          
               
                ncii_tempcount=ncii_tempcount+1
            return ncii_listbox
            
        def addmoreitems(event):
            invoicesw.remove(invoicesw.get_child())
            print('removed previous')
            invoicesw.add(createinvoicerows("blankevent"))
            print('added new')                
        
        itemstobebilled=createinvoicerows(25) #25 invoice items support
            
        amibutton = Gtk.Button.new_with_label("Add more items") #add more items
        amibutton.set_name('amibut')
        #amibutton.get_style_context().add_class("dangerbutton")    
        amibutton.connect("clicked", addmoreitems)
       
        iisw = Gtk.ScrolledWindow() #invoice items scroll window
        #iisw.set_min_content_width(720)      
        #iisw.set_max_content_width(768)
        iisw.set_min_content_height(380)
        iisw.set_max_content_height(381)
        iisw.get_style_context().add_class("lightgreymedborder")
        iisw.set_policy(Gtk.PolicyType.NEVER,
                               Gtk.PolicyType.AUTOMATIC)
        #print(iisw.get_propagate_natural_width())
        iisw.set_halign(Gtk.Align.START) # to avoid expansion horizontally
        
        iisw.add(itemstobebilled)
        billboxmat.pack_start(iisw, False, False, 0)
                   
        # billbox Footer grid coding below    
            
        discountlabel = Gtk.Label() # discount applicable
        discountlabel.set_markup("Discount")
           
        self.discountentry = Gtk.Entry()
        #self.discountentry.set_text("10")
        self.discountentry.set_width_chars(8)
        self.discountentry.set_max_length(11)
        self.discountentry.connect("changed", self.grandcaller) 
        
        freightlabel = Gtk.Label() # freight courier charges
        freightlabel.set_markup("Freight")
           
        self.freightentry = Gtk.Entry()
        #self.freightentry.set_text("")
        self.freightentry.set_width_chars(8)
        self.freightentry.set_max_length(11)
        self.freightentry.connect("changed", self.grandcaller) 
           
        mischlabel = Gtk.Label() # miscellaneous charges
        mischlabel.set_markup("Other charges")        
            
        self.mischentry = Gtk.Entry()
        #self.mischentry.set_text("200")
        self.mischentry.set_width_chars(10)
        self.mischentry.set_max_length(11)
        self.mischentry.connect("changed", self.grandcaller) 
        
        billcommentslabel = Gtk.Label() # invoice comments
        billcommentslabel.set_markup("Comments")                    
        self.bcommentry = Gtk.Entry() #Bill comments entry
        self.bcommentry.set_width_chars(20)
        self.bcommentry.set_max_length(47)
        
        ewaybill_label = Gtk.Label() # eway
        ewaybill_label.set_markup("E-WayBill No.")                    
        self.ewayentry = Gtk.Entry() #Bill comments entry
        self.ewayentry.set_width_chars(18)
        self.ewayentry.set_max_length(16)
        
        roundofflabel = Gtk.Label() # tax on tax
        roundofflabel.set_margin_left(10)
        roundofflabel.set_margin_right(10)
        roundofflabel.set_markup("Roundoff")
        self.roundoff_button = Gtk.CheckButton()
        self.roundoff_button.set_margin_left(33)
        self.roundoff_button.set_margin_right(20)
        self.roundoff_button.set_active(False) # By default false
        self.roundoff_button.connect("toggled", self.roundoff_toggled)
        
        same_address_label = Gtk.Label() # tax on tax
        same_address_label.set_margin_left(12)
        same_address_label.set_margin_right(10)
        same_address_label.set_markup("Same shipping address")
        self.shipping_button = Gtk.CheckButton()
        self.shipping_button.set_margin_left(80)
        self.shipping_button.set_margin_right(20)
        self.shipping_button.set_active(True) # By default Same
        #self.shipping_button.connect("toggled", self.roundoff_toggled)
        
        invoiceresetbutton = Gtk.Button.new_with_label("Reset")
        invoiceresetbutton.get_child().set_width_chars(5)
        invoiceresetbutton.get_style_context().add_class("dangerbutton")
        invoiceresetbutton.connect("clicked", self.resetncifields)
        invoiceresetbutton.set_margin_left(80)
        
        nextbutton = Gtk.Button.new_with_label("Next")
        nextbutton.get_child().set_width_chars(5)
        nextbutton.get_style_context().add_class("suggested-action")
        nextbutton.connect("clicked", self.processnci)
        #nextbutton.set_margin_left(10)           
        
        gridfooter.add(discountlabel)
        gridfooter.attach(self.discountentry, 0, 1, 1, 1)
        gridfooter.attach(freightlabel, 1, 0, 1, 1)
        gridfooter.attach(self.freightentry, 1, 1, 1, 1)
        gridfooter.attach(mischlabel, 2, 0, 1, 1)
        gridfooter.attach(self.mischentry, 2, 1, 1, 1)
        gridfooter.attach(billcommentslabel, 3, 0, 1, 1)
        gridfooter.attach(self.bcommentry, 3, 1, 1, 1) 
        gridfooter.attach(ewaybill_label, 4, 0, 1, 1)
        gridfooter.attach(self.ewayentry, 4, 1, 1, 1) 
        gridfooter.attach(roundofflabel, 6, 0, 1, 1)
        gridfooter.attach(self.roundoff_button, 6, 1, 1, 1)
        gridfooter.attach(same_address_label, 5, 0, 1, 1)
        gridfooter.attach(self.shipping_button, 5, 1, 1, 1)        
        gridfooter.attach(invoiceresetbutton, 10, 1, 1, 1)
        gridfooter.attach(nextbutton, 11, 1, 1, 1)
            
        basicamtlabel = Gtk.Label()
        basicamtlabel.set_markup("Basic amt")
           
        self.basicamtdisp = Gtk.Label()
        self.basicamtdisp.set_halign(Gtk.Align.START)
        #self.basicamtdisp.set_margin_left(10)
        self.basicamtdisp.set_markup("0.00")  
              
        taxlabel = Gtk.Label() # tax
        taxlabel.set_margin_left(20)
        taxlabel.set_markup("Tax amt")
        
        self.taxamount = Gtk.Label() # tax
        self.taxamount.set_markup("0.00")
        #self.taxamount.set_margin_left(5)
        
        taxontaxlabel = Gtk.Label() # tax on tax
        taxontaxlabel.set_margin_left(20)
        taxontaxlabel.set_markup("Tax on Tax amt")
        
        self.taxontaxamount = Gtk.Label() # tax
        self.taxontaxamount.set_markup("0.00")
        #self.taxontaxamount.set_margin_left(5)
        #self.taxontaxamount.set_margin_right(10)
           
        gtotallabel = Gtk.Label() #grand total        
        gtotallabel.set_markup("G. total")
        gtotallabel.set_margin_left(20)
        #gtotallabel.get_style_context().add_class("boldsimplelabel")    
        self.gtotaldisp = Gtk.Label()
        self.gtotaldisp.get_style_context().add_class("boldgreenlabel")
        #self.gtotaldisp.set_margin_left(5)
        self.gtotaldisp.set_markup("0.00")        
      
        amt_footerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)  
        amt_footerbox.set_margin_top(0) 
        amt_footerbox.get_style_context().add_class("nsiamountdisplaybox")   
        amt_footerbox.pack_start(basicamtlabel, False, False, 5)
        amt_footerbox.pack_start(self.basicamtdisp, False, False, 5)
        amt_footerbox.pack_start(taxlabel, False, False, 5)
        amt_footerbox.pack_start(self.taxamount, False, False, 5)
        amt_footerbox.pack_start(taxontaxlabel, False, False, 5)
        amt_footerbox.pack_start(self.taxontaxamount, False, False, 5)
        amt_footerbox.pack_start(gtotallabel, False, False, 5)
        amt_footerbox.pack_start(self.gtotaldisp, False, False, 5)       
        billbox.pack_end(amt_footerbox, False, False, 0)
        
        self.nsi_header_widgets=[self.invoicenmbr, self.invoicedate, self.invcompany, self.ponmbr, self.taxcombo, self.taxontaxcombo]
        
        self.nsi_footer_widgets=[self.basicamtdisp, self.discountentry, self.freightentry, self.mischentry, self.bcommentry, self.taxamount, self.taxontaxamount, self.gtotaldisp]
         
        self.nsi_itemswidgets=[self.nciilb_inamelist, self.nciilb_iqtylist, self.nciilb_isplist, self.nciilb_idiscountlist,self.nciilb_icommlist, self.nciilb_iamtlist]   
        
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
        
    def roundoff_toggled(self, togglebutton):  
        if togglebutton.get_active():
            self.roundoff_enabled='y'
        else:
            self.roundoff_enabled='n'  
        self.grandcaller('mimicevent')
         
    
    def estimate_tax(self, changedevent):         
        self.estd_tax, self.taxable_amount =saleinvoicingprocessor.estimatetax(self.taxcombo, self.temp_basicamt, self.discountentry, self.freightentry, self.mischentry)
        self.taxamount.set_markup(str(self.estd_tax))     
    
        
    def grandcaller(self, changedevent):        
        self.estimate_tax('mimicevent')
        self.estd_taxontax=saleinvoicingprocessor.estimate_taxontax(self.taxontaxcombo, self.estd_tax) 
        self.taxontaxamount.set_markup(str(self.estd_taxontax))
        geetotal=saleinvoicingprocessor.grand_saleamounting(self.temp_basicamt, self.discountentry, self.freightentry, self.mischentry, self.estd_tax, self.estd_taxontax, self.roundoff_enabled, self.roundoff_amt)
        self.gtotaldisp.set_markup(str(geetotal))  
        
           
    def processnci(self, nextbutton):
        self.invoicedata_temp=saleinvoicingprocessor.processnci(self.nsi_header_widgets, self.nsi_footer_widgets, self.nsi_itemswidgets, self.taxable_amount,  self.roundoff_enabled, self.roundoff_amt )
        self.pdfsi_ins=pdfsaleinvoice.PdfSI()
        self.pdfsi_ins.printable_saleinvoice('2020-10-11', '1', self.invoicedata_temp)
    
        
    def resetncifields(self, butonevent):
        self.nciname_completion.set_model(guicommon.companyname_store)  
 
    def print_sinvoice(self, buttonevent):
        #printsi_handlerins=printsihandler.PrintSaleInvoiceHander()
        #printsi_handlerins.print_dialog(self.mainwindow, 'invno')
        pass
