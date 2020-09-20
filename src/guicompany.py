# This file contains company gui page of main stack: Ver sep 2020

import sys
import gi
from submods import functions
from submods import dbmani
from submods import guicommon
from submods import guiprocessor
from datetime import datetime

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkCompany():
            
    def generatepage(self, invoicingbox, bph, guiinvoicingins):
    
        #some initializations
        #self.itemtableins=dbmani.itemtableins        
        self.companytableins=dbmani.companytableins
        #self.invoicetableins=dbmani.invoicetableins       
        self.miscdb=dbmani.miscdb       
        #self.itemgroups=dbmani.itemgroups  
        #guicommon.loadguicommon()              
        self.guiprocessor_ins=guiprocessor.GtkProcessor()        
        
        #gui starts here      
        self.companymasterbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
                
        self.companystack = Gtk.Stack()
        self.companystack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.companystack.set_transition_duration(1000)
        	    
        # Create Company pane coding starts here ####################
        #print("Started company pane coding")   
        ccbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
        gridccbox = Gtk.Grid()
        ccbox.pack_start(gridccbox, True, True, 0)
        #print("added basic grid to create company box")          
        
        ccnamelabel = Gtk.Label()
        ccnamelabel.set_markup("Company name")
        
        self.ccnameentry = Gtk.Entry()
        
        ccgstlabel = Gtk.Label()
        ccgstlabel.set_markup("GSTIN")
        
        self.ccgstentry = Gtk.Entry()
        
        ccaddresslabel = Gtk.Label()
        ccaddresslabel.set_markup("Address")
        
        self.ccaddressentry = Gtk.Entry()
        
        cccitylabel = Gtk.Label()
        cccitylabel.set_markup("City")
        
        self.cccityentry = Gtk.Entry()
        
        ccstatelabel = Gtk.Label()
        ccstatelabel.set_markup("State")
        
        self.ccstateentry = Gtk.Entry()
        
        cccountrylabel = Gtk.Label()
        cccountrylabel.set_markup("Country")
        
        self.ccccombo = Gtk.ComboBoxText.new_with_entry()
        for countryname in functions.countrieslist:
            self.ccccombo.append_text(countryname)
        self.ccccombo.set_active(0)
        
        completer = Gtk.EntryCompletion()
        completer.set_model(self.ccccombo.get_model())
        completer.set_text_column(0)
        self.ccccombo.get_child().set_completion(completer)
                
        ccpinlabel = Gtk.Label()
        ccpinlabel.set_markup("PIN Code")
        
        self.ccpinentry = Gtk.Entry()
        
        ccphonelabel = Gtk.Label()
        ccphonelabel.set_markup("Office Phone")
        
        self.ccphoneentry = Gtk.Entry()
        
        ccmobilelabel = Gtk.Label()
        ccmobilelabel.set_markup("Mobile ")
        
        self.ccmobileentry = Gtk.Entry()
        
        ccemaillabel = Gtk.Label()
        ccemaillabel.set_markup("Email ")
        
        self.ccemailentry = Gtk.Entry()
        
        ccwebsitelabel = Gtk.Label()
        ccwebsitelabel.set_markup("Website ")
        
        self.ccwebsiteentry = Gtk.Entry()
        
        cccpersonlabel = Gtk.Label()
        cccpersonlabel.set_markup("Contact Person ")
        
        self.cccpersonentry = Gtk.Entry()
        
        ccbankaccountlabel = Gtk.Label()
        #ccbankaccountlabel.set_margin_top(20)
        ccbankaccountlabel.set_markup("Primary Bank A/c No. ")        
        self.ccbankaccountentry = Gtk.Entry()
        #self.ccbankaccountentry.set_margin_top(20)
        
        ccbankifsclabel = Gtk.Label()
        ccbankifsclabel.set_markup("IFSC")        
        self.ccbankifscentry = Gtk.Entry()
        
        ccbanknamelabel = Gtk.Label()
        ccbanknamelabel.set_markup("Bank Name/Other details  ")        
        self.ccbanknameentry = Gtk.Entry()
        
        ccbankaddilabel = Gtk.Label()
        ccbankaddilabel.set_markup("UPI/IMPS/Misc. ")        
        self.ccbankaddientry = Gtk.Entry()
            
        ccdistancelabel = Gtk.Label()
        ccdistancelabel.set_markup("Distance in Kms ")
        
        self.ccdistanceentry = Gtk.Entry()
        
        ccdosplabel = Gtk.Label()
        ccdosplabel.set_markup("Discount on selling price ")
        
        self.ccdospentry = Gtk.Entry()
        
        ccseplabel = Gtk.Label() # separator for grid columns
        ccseplabel.set_markup("  ")
        ccseplabel.set_width_chars(16)
        
        ccminiseplabel = Gtk.Label() # payment block separator for second row columns
        ccminiseplabel.set_markup("     ")
        ccminiseplabel.set_width_chars(16)
        
        
        # do not temper below section, compatibility mode start
        # sec bank widgets start
        
        ccsecbankwarning = Gtk.Label()
        ccsecbankwarning.set_markup(" Don't alter this section ")
        ccsecbankwarning.set_sensitive(False)
        ccsecbankwarning.set_no_show_all(True)
        ccsecbankwarning.hide()
               
        ccsecbanklabel = Gtk.Label()
        ccsecbanklabel.set_markup(" (Sec. or Int'l) ")
        ccsecbanklabel.set_sensitive(False)
        ccsecbanklabel.set_no_show_all(True)
        ccsecbanklabel.hide()      
                
        ccsecbankaccountlabel = Gtk.Label()
        ccsecbankaccountlabel.set_markup("Bank account No. ")
        ccsecbankaccountlabel.set_sensitive(False) 
        ccsecbankaccountlabel.set_no_show_all(True)
        ccsecbankaccountlabel.hide()
                   
        self.ccsecbankaccountentry = Gtk.Entry()
        self.ccsecbankaccountentry.set_sensitive(False)
        self.ccsecbankaccountentry.set_no_show_all(True)
        self.ccsecbankaccountentry.hide()     
        
        ccsecbankifsclabel = Gtk.Label()
        ccsecbankifsclabel.set_markup("IFSC/SWIFT/BIC ")
        ccsecbankifsclabel.set_sensitive(False) 
        ccsecbankifsclabel.set_no_show_all(True)
        ccsecbankifsclabel.hide()    
               
        self.ccsecbankifscentry = Gtk.Entry()
        self.ccsecbankifscentry.set_sensitive(False)
        self.ccsecbankifscentry.set_no_show_all(True)
        self.ccsecbankifscentry.hide() 
        
        
        ccsecbanknamelabel = Gtk.Label()
        ccsecbanknamelabel.set_markup("Bank Name ")
        ccsecbanknamelabel.set_sensitive(False) 
        ccsecbanknamelabel.set_no_show_all(True)
        ccsecbanknamelabel.hide()     
              
        self.ccsecbanknameentry = Gtk.Entry()
        self.ccsecbanknameentry.set_sensitive(False) 
        self.ccsecbanknameentry.set_no_show_all(True)
        self.ccsecbanknameentry.hide()    
        
        ccsecbankaddilabel = Gtk.Label()
        ccsecbankaddilabel.set_markup("Additional banking details  ")
        ccsecbankaddilabel.set_sensitive(False)  
        ccsecbankaddilabel.set_no_show_all(True)
        ccsecbankaddilabel.hide()    
               
        self.ccsecbankaddientry = Gtk.Entry()
        self.ccsecbankaddientry.set_sensitive(False)
        self.ccsecbankaddientry.set_no_show_all(True)
        self.ccsecbankaddientry.hide()     
        # sec bank widgets end
        # From now u can make changes, compatibility mode ends
        
        
        cccreditlimitlabel = Gtk.Label()
        cccreditlimitlabel.set_markup("Credit Limit ")
        
        self.cccreditlimitentry = Gtk.Entry()
        
        ccpaydayslabel = Gtk.Label()
        ccpaydayslabel.set_markup("Payment terms ")
        
        self.ccpaydaysentry = Gtk.Entry()
        
        ccbusinessarealabel = Gtk.Label()
        ccbusinessarealabel.set_markup("Business area/Focus ")
        
        self.ccbusinessareaentry = Gtk.Entry()   
        
        cccommentslabel = Gtk.Label()
        cccommentslabel.set_markup("Comments ")
        
        self.cccommentsentry = Gtk.Entry()
        
        ccflaglabel = Gtk.Label()
        ccflaglabel.set_markup("Flag ")
        
        self.ccflagentry = Gtk.Entry()      
        
        ccinstapaylabel = Gtk.Label()
        ccinstapaylabel.set_markup("Immediate payment ")
        
        self.ccinstapaybutton = Gtk.CheckButton() # use this to give reminder during bill generation with this company
        #self.ccinstapaybutton.set_label("  (Reminder only)")
        self.ccinstapaybutton.set_active(False)
        
        ccblacklistlabel = Gtk.Label()
        ccblacklistlabel.set_markup("Blacklist this company ")
        ccblacklistlabel.set_margin_top(10)
        
        ccblacklist='notset' 
        self.ccblacklistbutton = Gtk.CheckButton()
        self.ccblacklistbutton.set_margin_top(10)
        #self.ccblacklistbutton.set_label("  (Reminder only)")    
        self.ccblacklistbutton.set_active(False) # By default false
        #self.ccblacklistbutton.connect("toggled", self.toggleblacklist)
        
        
            
        self.ccvarg=[self.ccnameentry, self.ccgstentry, self.ccaddressentry, self.cccityentry, self.ccstateentry, self.ccccombo, self.ccpinentry, self.ccphoneentry, self.cccpersonentry, self.ccmobileentry, self.ccemailentry, self.ccwebsiteentry,  self.ccbankaccountentry, self.ccbankifscentry, self.ccbanknameentry, self.ccbankaddientry,  self.ccdistanceentry, self.ccbusinessareaentry, self.cccommentsentry, self.ccflagentry,  self.ccdospentry, self.cccreditlimitentry, self.ccpaydaysentry,  self.ccinstapaybutton, self.ccblacklistbutton]
        
        self.ccentries=[self.ccnameentry, self.ccgstentry, self.ccaddressentry, self.cccityentry, self.ccstateentry, self.ccpinentry, self.ccphoneentry, self.cccpersonentry, self.ccmobileentry, self.ccemailentry, self.ccwebsiteentry,  self.ccbankaccountentry, self.ccbankifscentry, self.ccbanknameentry, self.ccbankaddientry,  self.ccdistanceentry, self.ccbusinessareaentry, self.cccommentsentry, self.ccflagentry, self.ccdospentry, self.cccreditlimitentry, self.ccpaydaysentry]
        
        cccreatebutton = Gtk.Button.new_with_label("Create")
        cccreatebutton.set_name('cccb')
        cccreatebutton.get_style_context().add_class("suggested-action")
        cccreatebutton.connect("clicked", self.processccompany, self.ccvarg, invoicingbox, bph, guiinvoicingins)
        
        style_provider = Gtk.CssProvider()      
        style_provider.load_from_path("submods/styl.css")
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
                    
        ccresetbutton = Gtk.Button.new_with_label("Reset")
        ccresetbutton.connect("clicked", self.ccresetfields, self.ccentries)
        ccresetbutton.get_style_context().add_class("dangerbutton")       
            
        gridccbox.add(ccnamelabel)
        gridccbox.attach(self.ccnameentry, 1, 0, 1, 1)
        gridccbox.attach(ccgstlabel, 0, 1, 1, 1)
        gridccbox.attach(self.ccgstentry, 1, 1, 1, 1)
        gridccbox.attach(ccaddresslabel, 0, 2, 1, 1)
        gridccbox.attach(self.ccaddressentry, 1, 2, 1, 1)
        gridccbox.attach(cccitylabel, 0, 3, 1, 1)
        gridccbox.attach(self.cccityentry, 1, 3, 1, 1)
        gridccbox.attach(ccstatelabel, 0, 4, 1, 1)
        gridccbox.attach(self.ccstateentry, 1, 4, 1, 1)
        gridccbox.attach(cccountrylabel, 0, 5, 1, 1)
        gridccbox.attach(self.ccccombo, 1, 5, 1, 1)
        gridccbox.attach(ccpinlabel, 0, 6, 1, 1)
        gridccbox.attach(self.ccpinentry, 1, 6, 1, 1)
        gridccbox.attach(ccphonelabel, 0, 7, 1, 1)
        gridccbox.attach(self.ccphoneentry, 1, 7, 1, 1)
        gridccbox.attach(cccpersonlabel, 0, 8, 1, 1)
        gridccbox.attach(self.cccpersonentry, 1, 8, 1, 1)        
        gridccbox.attach(ccmobilelabel, 0, 9, 1, 1)
        gridccbox.attach(self.ccmobileentry, 1, 9, 1, 1)
        gridccbox.attach(ccemaillabel, 0, 10, 1, 1)
        gridccbox.attach(self.ccemailentry, 1, 10, 1, 1)
        gridccbox.attach(ccwebsitelabel, 0, 11, 1, 1)
        gridccbox.attach(self.ccwebsiteentry, 1, 11, 1, 1) 
        gridccbox.attach(ccbankaccountlabel, 0, 13, 1, 1)
        gridccbox.attach(self.ccbankaccountentry, 1, 13, 1, 1)
        gridccbox.attach(ccbankifsclabel, 0, 14, 1, 1)
        gridccbox.attach(self.ccbankifscentry, 1, 14, 1, 1)
        gridccbox.attach(ccbanknamelabel, 0, 15, 1, 1)
        gridccbox.attach(self.ccbanknameentry, 1, 15, 1, 1)
        gridccbox.attach(ccbankaddilabel, 0, 16, 1, 1)
        gridccbox.attach(self.ccbankaddientry, 1, 16, 1, 1)               
        
        # NOTE Some space is reserved for future elements, plus some other important reason
        # Do not try to use this space::: Second half (RHS) column top side 5 grid rows
                
        # Secondary banking details starts, don't alter this section for compatibility reasons
        gridccbox.attach(ccsecbankwarning, 5, 2, 1, 1) 
        gridccbox.attach(ccsecbankaccountlabel, 3, 0, 1, 1)
        gridccbox.attach(self.ccsecbankaccountentry, 4, 0, 1, 1)
        gridccbox.attach(ccsecbankifsclabel, 3, 1, 1, 1)
        gridccbox.attach(self.ccsecbankifscentry, 4, 1, 1, 1)
        gridccbox.attach(ccsecbanknamelabel, 3, 2, 1, 1)
        gridccbox.attach(self.ccsecbanknameentry, 4, 2, 1, 1)
        gridccbox.attach(ccsecbankaddilabel, 3, 3, 1, 1)
        gridccbox.attach(self.ccsecbankaddientry, 4, 3, 1, 1)
        gridccbox.attach(ccsecbanklabel, 5, 0, 1, 1)
        # Secondary banking details end, from now u can change      
        
        gridccbox.attach(ccseplabel, 2, 0, 1, 1)
        gridccbox.attach(ccdistancelabel, 3, 5, 1, 1)
        gridccbox.attach(self.ccdistanceentry, 4, 5, 1, 1)
        gridccbox.attach(ccbusinessarealabel, 3, 6, 1, 1)
        gridccbox.attach(self.ccbusinessareaentry, 4, 6, 1, 1) 
        gridccbox.attach(cccommentslabel, 3, 7, 1, 1)
        gridccbox.attach(self.cccommentsentry, 4, 7, 1, 1) 
        gridccbox.attach(ccflaglabel, 3, 8, 1, 1)
        gridccbox.attach(self.ccflagentry, 4, 8, 1, 1)         
        
        gridccbox.attach(ccdosplabel, 3, 9, 1, 1)
        gridccbox.attach(self.ccdospentry, 4, 9, 1, 1)
        gridccbox.attach(cccreditlimitlabel, 3, 10, 1, 1)
        gridccbox.attach(self.cccreditlimitentry, 4, 10, 1, 1)
        gridccbox.attach(ccpaydayslabel, 3, 11, 1, 1)
        gridccbox.attach(self.ccpaydaysentry, 4, 11, 1, 1)
        
        gridccbox.attach(ccminiseplabel, 3, 12, 1, 1) 
        gridccbox.attach(ccinstapaylabel, 3, 13, 1, 1)
        gridccbox.attach(self.ccinstapaybutton, 4, 13, 1, 1)
        gridccbox.attach(ccblacklistlabel, 3, 14, 1, 1)
        gridccbox.attach(self.ccblacklistbutton, 4, 14, 1, 1)
      
        gridccbox.attach(cccreatebutton, 4, 16, 1, 1)
        gridccbox.attach(ccresetbutton, 3, 16, 1, 1)
        
        self.companystack.add_titled(ccbox, "createcompanymain", "Create Company")
       
    #Create company code ends     
    
      
        #print("Packing of stack switcher in Create pane started")  
        self.companystack_switcher = Gtk.StackSwitcher()
        self.companystack_switcher.set_stack(self.companystack)
        
        #print("Packing of stack started")  
        self.companymasterbox.pack_start(self.companystack_switcher, False, False, 10)
        self.companymasterbox.pack_start(self.companystack, False, False, 10)
           
        return self.companymasterbox       
            
    #-------- Functions used in Create pane 

    def blankfunc(self):
        print("hello, this is blank function")   
    
       
    def processccompany(self, widget, ccvarg, invoicingbox, bph, guiinvoicingins):
        cdata=self.extractccdata(ccvarg)
        #print(cdata)
        self.companytableins.createrow(cdata[0], cdata)
        #cteminstance.createitem(cdata)
        self.ccresetfields('mimicevent', self.ccentries)    # set form fields to blank fields
        guicommon.loadguicommon()     
        children=invoicingbox.get_children()
        for eachchild in children:
            invoicingbox.remove(eachchild)
            eachchild.destroy()
        bph=guiinvoicingins.billingpage()
        invoicingbox.add(bph)
        invoicingbox.show_all()
           
        print("Successfully created company")
        return 1    


    def extractccdata(self, ccvarg):
        cname=ccvarg[0].get_text()
        cgst=ccvarg[1].get_text()
        caddress=ccvarg[2].get_text()
        ccity=ccvarg[3].get_text()
        cstate=ccvarg[4].get_text()
        ccountry=ccvarg[5].get_active_text()
        cpin=ccvarg[6].get_text()
        cphone=ccvarg[7].get_text()
        cperson=ccvarg[8].get_text()
        cmobile=ccvarg[9].get_text()
        cemail=ccvarg[10].get_text()
        cwebsite=ccvarg[11].get_text()
        cbankaccount=ccvarg[12].get_text()
        cbankifsc=ccvarg[13].get_text()
        cbankname=ccvarg[14].get_text()
        cbankupi=ccvarg[15].get_text()       
        cdistance=ccvarg[16].get_text()
        cfocus=ccvarg[17].get_text()
        ccomments=ccvarg[18].get_text()
        cflag=ccvarg[19].get_text()
        cdiscount=ccvarg[20].get_text()
        ccreditlimit=ccvarg[21].get_text()
        ccpaymentindays=ccvarg[22].get_text()
        rawcinstapay=ccvarg[23]
        rawcblacklisted=ccvarg[24]
        
        if rawcinstapay.get_active():
            #print ('retrieving immediate payment checkbutton... activated')
            cinstapay='y'       
        else:        
            #print ('retrieving immediate payment checkbutton... dactivated')
            cinstapay='n'
            
        
        if rawcblacklisted.get_active():
            #print ('retrieving blacklist activated')
            cblacklisted='y'       
        else:        
            #print ('retrieving blacklist dactivated')
            cblacklisted='n'  
        
        ccreatedate= functions.todaysdate_string
           
        # do not temper with below in any means, for compatibility 
        csbac='disabled'
        csbifsc='disabled'
        csbname='disabled'
        csbaddi='disabled'
        cemer='' 
        # compatibily safe code ends, now can be changed        
        
        cdata=[cname, cgst, cemer, csbac, csbifsc, csbname, csbaddi, ccreatedate, caddress, ccity, cstate, ccountry, cpin, cphone, cperson, cmobile, cemail, cwebsite, cbankaccount, cbankifsc, cbankname, cbankupi, cdistance, cfocus, ccomments, cflag, cdiscount, ccreditlimit, ccpaymentindays,  cinstapay, cblacklisted ]
        #print(cdata)
        return cdata        

    def ccresetfields(self, eventsignal, ccfields):
        for eachentry in ccfields:
            eachentry.set_text('')
        self.ccblacklistbutton.set_active(False) # By default false
        self.ccinstapaybutton.set_active(False)
        return 2 


    # callback function for blacklist checkbutton, for compatibility
    def toggleblacklist(self, togglesignal):
        
        if self.ccblacklistbutton.get_active():
            print ('blacklist activated')       
        else:        
            print ('blacklist dactivated')

