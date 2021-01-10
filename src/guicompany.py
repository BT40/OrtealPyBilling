# This file contains company gui page of main stack: Ver sep 2020

import sys
import gi
from submods import functions
from submods import dbmani
from submods import guicommon
from submods import companyprocessor
from submods import guiprocessor
from datetime import datetime

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkCompany():
            
    def generatepage(self, invoicingbox, bph, guiinvoicingins, mainwindow):
           
        self.companytableins=dbmani.companytableins     
        self.miscdb=dbmani.miscdb                 
        self.guiprocessor_ins=guiprocessor.GtkProcessor()        
        self.mainwindow=mainwindow
        
        #gui starts here      
        self.companymasterbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
                
        self.companystack = Gtk.Stack()
        self.companystack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.companystack.set_transition_duration(1000)
        	    
        ccbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
        gridccbox = Gtk.Grid()
        ccbox.pack_start(gridccbox, True, True, 0)
        #print("added basic grid to create company box")          
        
        ccnamelabel = Gtk.Label()
        ccnamelabel.set_markup("Company name")        
        self.ccnameentry = Gtk.Entry()
        self.ccnameentry.set_max_length(47)
        
        ccgstlabel = Gtk.Label()
        ccgstlabel.set_markup("GSTIN")        
        self.ccgstentry = Gtk.Entry()
        self.ccgstentry.set_max_length(24)
        
        ccaddresslabel = Gtk.Label()
        ccaddresslabel.set_markup("Address")
        self.ccaddressentry = Gtk.Entry()
        self.ccaddressentry.set_max_length(47)
        
        cccitylabel = Gtk.Label()
        cccitylabel.set_markup("City")
        self.cccityentry = Gtk.Entry()
        self.cccityentry.set_max_length(32)
        
        ccstatelabel = Gtk.Label()
        ccstatelabel.set_markup("State")     
        
        self.ccstate_combo = Gtk.ComboBoxText.new_with_entry() 
        for es in guicommon.state_list:
            self.ccstate_combo.append_text(es)
        #self.ccstate_combo.set_active(0)
        self.ccstate_combo.set_hexpand(False)
        self.ccstate_combo.set_halign(Gtk.Align.CENTER)
        self.ccstate_combo.get_child().set_width_chars(32)     
        
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
        self.ccpinentry.set_max_length(16)
        
        ccphonelabel = Gtk.Label()
        ccphonelabel.set_markup("Office Phone")
        self.ccphoneentry = Gtk.Entry()
        self.ccphoneentry.set_max_length(24)
        
        ccmobilelabel = Gtk.Label()
        ccmobilelabel.set_markup("Mobile ")
        self.ccmobileentry = Gtk.Entry()
        self.ccmobileentry.set_max_length(16)
        
        ccemaillabel = Gtk.Label()
        ccemaillabel.set_markup("Email ")
        self.ccemailentry = Gtk.Entry()
        self.ccemailentry.set_max_length(47)
        
        ccstatecodelabel = Gtk.Label()
        ccstatecodelabel.set_markup("State code GST  ")
        self.ccstatecodeentry = Gtk.Entry()
        self.ccstatecodeentry.set_max_length(2)
        
        cccpersonlabel = Gtk.Label()
        cccpersonlabel.set_markup("Contact Person ")       
        self.cccpersonentry = Gtk.Entry()
        self.cccpersonentry.set_max_length(32)
        
        ccbankaccountlabel = Gtk.Label()
        #ccbankaccountlabel.set_margin_top(20)
        ccbankaccountlabel.set_markup("Primary Bank A/c No. ")        
        self.ccbankaccountentry = Gtk.Entry()
        self.ccbankaccountentry.set_max_length(24)
        #self.ccbankaccountentry.set_margin_top(20)
        
        ccbankifsclabel = Gtk.Label()
        ccbankifsclabel.set_markup("IFSC")        
        self.ccbankifscentry = Gtk.Entry()
        self.ccbankifscentry.set_max_length(24)
        
        ccbanknamelabel = Gtk.Label()
        ccbanknamelabel.set_markup("Bank Name/Other details  ")        
        self.ccbanknameentry = Gtk.Entry()
        self.ccbanknameentry.set_max_length(32)
        
        ccbankaddilabel = Gtk.Label()
        ccbankaddilabel.set_markup("UPI/IMPS/Misc. ")        
        self.ccbankaddientry = Gtk.Entry()
        self.ccbankaddientry.set_max_length(32)
            
        ccdistancelabel = Gtk.Label()
        ccdistancelabel.set_markup("Distance in Kms ")        
        self.ccdistanceentry = Gtk.Entry()
        self.ccdistanceentry.set_max_length(8)
        
        ccdosplabel = Gtk.Label()
        ccdosplabel.set_markup("Discount on selling price ")        
        self.ccdospentry = Gtk.Entry()
        self.ccdospentry.set_max_length(32)
        
        ccseplabel = Gtk.Label() # separator for grid columns
        ccseplabel.set_markup("  ")
        ccseplabel.set_width_chars(16)     
        ccminiseplabel = Gtk.Label() # payment block separator for second row columns
        ccminiseplabel.set_markup("     ")
        ccminiseplabel.set_width_chars(16)        
        
        # do not temper below section, compatibility mode start CMCMCMCMCMCMCMCMCMCMCMCMCMCMCMCMCMCM
        # sec bank widgets start
        
        #ccsecbankwarning = Gtk.Label()
        #ccsecbankwarning.set_markup(" Don't alter this section ")
        #ccsecbankwarning.set_sensitive(False)
        #ccsecbankwarning.set_no_show_all(True)
        #ccsecbankwarning.hide()
               
        #ccsecbanklabel = Gtk.Label()
        #ccsecbanklabel.set_markup(" (Sec. or Int'l) ")
        #ccsecbanklabel.set_sensitive(False)
        #ccsecbanklabel.set_no_show_all(True)
        #ccsecbanklabel.hide()      
                
        #ccsecbankaccountlabel = Gtk.Label()
        #ccsecbankaccountlabel.set_markup("Bank account No. ")
        #ccsecbankaccountlabel.set_sensitive(False) 
        #ccsecbankaccountlabel.set_no_show_all(True)
        #ccsecbankaccountlabel.hide()
                   
        #self.ccsecbankaccountentry = Gtk.Entry()
        #self.ccsecbankaccountentry.set_sensitive(False)
        #self.ccsecbankaccountentry.set_no_show_all(True)
        #self.ccsecbankaccountentry.hide()     
        
        #ccsecbankifsclabel = Gtk.Label()
        #ccsecbankifsclabel.set_markup("IFSC/SWIFT/BIC ")
        #ccsecbankifsclabel.set_sensitive(False) 
        #ccsecbankifsclabel.set_no_show_all(True)
        #ccsecbankifsclabel.hide()    
               
        #self.ccsecbankifscentry = Gtk.Entry()
        #self.ccsecbankifscentry.set_sensitive(False)
        #self.ccsecbankifscentry.set_no_show_all(True)
        #self.ccsecbankifscentry.hide()        
        
        #ccsecbanknamelabel = Gtk.Label()
        #ccsecbanknamelabel.set_markup("Bank Name ")
        #ccsecbanknamelabel.set_sensitive(False) 
        #ccsecbanknamelabel.set_no_show_all(True)
        #ccsecbanknamelabel.hide()     
              
        #self.ccsecbanknameentry = Gtk.Entry()
        #self.ccsecbanknameentry.set_sensitive(False) 
        #self.ccsecbanknameentry.set_no_show_all(True)
        #self.ccsecbanknameentry.hide()    
        
        #ccsecbankaddilabel = Gtk.Label()
        #ccsecbankaddilabel.set_markup("Additional banking details  ")
        #ccsecbankaddilabel.set_sensitive(False)  
        #ccsecbankaddilabel.set_no_show_all(True)
        #ccsecbankaddilabel.hide()    
               
        #self.ccsecbankaddientry = Gtk.Entry()
        #self.ccsecbankaddientry.set_sensitive(False)
        #self.ccsecbankaddientry.set_no_show_all(True)
        #self.ccsecbankaddientry.hide()     
        # sec bank widgets end
        # From now u can make changes, compatibility mode ends   CMECMECMECMECMECMECMECMECMECME       
        
        cccreditlimitlabel = Gtk.Label()
        cccreditlimitlabel.set_markup("Credit Limit ")       
        self.cccreditlimitentry = Gtk.Entry()
        self.cccreditlimitentry.set_max_length(11)
        
        ccpaydayslabel = Gtk.Label()
        ccpaydayslabel.set_markup("Payment terms ")        
        self.ccpaydaysentry = Gtk.Entry()
        self.ccpaydaysentry.set_max_length(32)
        
        ccbusinessarealabel = Gtk.Label()
        ccbusinessarealabel.set_markup("Business area/Focus ")       
        self.ccbusinessareaentry = Gtk.Entry() 
        self.ccbusinessareaentry.set_max_length(47) 
        
        cccommentslabel = Gtk.Label()
        cccommentslabel.set_markup("Comments ")        
        self.cccommentsentry = Gtk.Entry()
        self.cccommentsentry.set_max_length(47)
        
        ccflaglabel = Gtk.Label()
        ccflaglabel.set_markup("Flag ")       
        self.ccflagentry = Gtk.Entry()  
        self.ccflagentry.set_max_length(16)    
        
        ccinstapaylabel = Gtk.Label()
        ccinstapaylabel.set_markup("Immediate payment ")        
        self.ccinstapaybutton = Gtk.CheckButton() # use this to give reminder during bill generation with this company
        #self.ccinstapaybutton.set_label("  (Reminder only)")
        self.ccinstapaybutton.set_active(False)
        
        ccblacklistlabel = Gtk.Label()
        ccblacklistlabel.set_markup("Blacklist this company ")
        ccblacklistlabel.set_margin_top(10)
        self.ccblacklistbutton = Gtk.CheckButton()
        self.ccblacklistbutton.set_margin_top(10)
        #self.ccblacklistbutton.set_label("  (Reminder only)")    
        self.ccblacklistbutton.set_active(False) # By default false
        
        ccshippingaddress_label = Gtk.Label()
        ccshippingaddress_label.set_markup("Different shipping address  ")
        ccshippingaddress_label.set_margin_top(10)
        self.ccshippingaddress_button = Gtk.CheckButton()
        self.ccshippingaddress_button.set_margin_top(10)  
        self.ccshippingaddress_button.set_active(False) # By default false
            
        self.ccvarg=[self.ccnameentry, self.ccgstentry, self.ccaddressentry, self.cccityentry, self.ccstate_combo, self.ccccombo, self.ccpinentry, self.ccphoneentry, self.cccpersonentry, self.ccmobileentry, self.ccemailentry, self.ccstatecodeentry,  self.ccbankaccountentry, self.ccbankifscentry, self.ccbanknameentry, self.ccbankaddientry,  self.ccdistanceentry, self.ccbusinessareaentry, self.cccommentsentry, self.ccflagentry,  self.ccdospentry, self.cccreditlimitentry, self.ccpaydaysentry,  self.ccinstapaybutton, self.ccblacklistbutton]
        
        self.ccentries=[self.ccnameentry, self.ccgstentry, self.ccaddressentry, self.cccityentry, self.ccpinentry, self.ccphoneentry, self.cccpersonentry, self.ccmobileentry, self.ccemailentry, self.ccstatecodeentry,  self.ccbankaccountentry, self.ccbankifscentry, self.ccbanknameentry, self.ccbankaddientry,  self.ccdistanceentry, self.ccbusinessareaentry, self.cccommentsentry, self.ccflagentry, self.ccdospentry, self.cccreditlimitentry, self.ccpaydaysentry]
        
        cccreatebutton = Gtk.Button.new_with_label("Create")
        cccreatebutton.set_name('cccb')
        cccreatebutton.get_style_context().add_class("suggested-action")
        cccreatebutton.connect("clicked", self.processccompany, self.ccvarg, invoicingbox, bph, guiinvoicingins)
                    
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
        gridccbox.attach(self.ccstate_combo, 1, 4, 1, 1)
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
        gridccbox.attach(ccstatecodelabel, 0, 11, 1, 1)
        gridccbox.attach(self.ccstatecodeentry, 1, 11, 1, 1) 
        gridccbox.attach(ccbankaccountlabel, 0, 13, 1, 1)
        gridccbox.attach(self.ccbankaccountentry, 1, 13, 1, 1)
        gridccbox.attach(ccbankifsclabel, 0, 14, 1, 1)
        gridccbox.attach(self.ccbankifscentry, 1, 14, 1, 1)
        gridccbox.attach(ccbanknamelabel, 0, 15, 1, 1)
        gridccbox.attach(self.ccbanknameentry, 1, 15, 1, 1)
        gridccbox.attach(ccbankaddilabel, 0, 16, 1, 1)
        gridccbox.attach(self.ccbankaddientry, 1, 16, 1, 1)               
        
        # NOTE Some space is reserved for future elements, plus some other important reason    CMCMCMCMCMCMCMCMCM
        # Do not try to use this space::: Second half (RHS) column top side 5 grid rows
                
        # Secondary banking details starts, don't alter this section for compatibility reasons
        #gridccbox.attach(ccsecbankwarning, 5, 2, 1, 1) 
        #gridccbox.attach(ccsecbankaccountlabel, 3, 0, 1, 1)
        #gridccbox.attach(self.ccsecbankaccountentry, 4, 0, 1, 1)
        #gridccbox.attach(ccsecbankifsclabel, 3, 1, 1, 1)
        #gridccbox.attach(self.ccsecbankifscentry, 4, 1, 1, 1)
        #gridccbox.attach(ccsecbanknamelabel, 3, 2, 1, 1)
        #gridccbox.attach(self.ccsecbanknameentry, 4, 2, 1, 1)
        #gridccbox.attach(ccsecbankaddilabel, 3, 3, 1, 1)
        #gridccbox.attach(self.ccsecbankaddientry, 4, 3, 1, 1)
        #gridccbox.attach(ccsecbanklabel, 5, 0, 1, 1)
        # Secondary banking details end, from now u can change     CMECMECMECMECMECMECMECMECMECMECME 
        
        gridccbox.attach(ccseplabel, 2, 0, 1, 1)
        gridccbox.attach(ccdistancelabel, 3, 5, 1, 1)
        gridccbox.attach(self.ccdistanceentry, 4, 5, 1, 1)
        gridccbox.attach(ccbusinessarealabel, 3, 6, 1, 1)
        gridccbox.attach(self.ccbusinessareaentry, 4, 6, 1, 1) 
        gridccbox.attach(cccommentslabel, 3, 7, 1, 1)
        gridccbox.attach(self.cccommentsentry, 4, 7, 1, 1) 
        #gridccbox.attach(ccflaglabel, 3, 8, 1, 1)
        #gridccbox.attach(self.ccflagentry, 4, 8, 1, 1)                 
        gridccbox.attach(ccdosplabel, 3, 9, 1, 1)
        gridccbox.attach(self.ccdospentry, 4, 9, 1, 1)
        gridccbox.attach(cccreditlimitlabel, 3, 10, 1, 1)
        gridccbox.attach(self.cccreditlimitentry, 4, 10, 1, 1)
        gridccbox.attach(ccpaydayslabel, 3, 11, 1, 1)
        gridccbox.attach(self.ccpaydaysentry, 4, 11, 1, 1)        
        gridccbox.attach(ccminiseplabel, 3, 12, 1, 1) 
        #gridccbox.attach(ccinstapaylabel, 3, 13, 1, 1)
        #gridccbox.attach(self.ccinstapaybutton, 4, 13, 1, 1)
        #gridccbox.attach(ccblacklistlabel, 3, 14, 1, 1)
        #gridccbox.attach(self.ccblacklistbutton, 4, 14, 1, 1)  
        #gridccbox.attach(ccshippingaddress_label, 3, 15, 1, 1)
        #gridccbox.attach(self.ccshippingaddress_button, 4, 15, 1, 1)        
        gridccbox.attach(cccreatebutton, 4, 17, 1, 1)
        gridccbox.attach(ccresetbutton, 3, 17, 1, 1)
        
        self.companystack.add_titled(ccbox, "createcompanymain", "Create Company")
        
################################# Edit company code starts ##########################################

        ecbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        
        gridecbox = Gtk.Grid()
        ecbox.pack_start(gridecbox, True, True, 0)       
        
        ecnamelabel = Gtk.Label()
        ecnamelabel.set_markup("Company name")
        self.ecnameentry = Gtk.Entry()
        self.ecnameentry.set_max_length(47)
        self.ecname_completion = Gtk.EntryCompletion()
        self.ecname_completion.set_model(guicommon.companyname_store)
        self.ecname_completion.set_text_column(0)
        self.ecnameentry.set_completion(self.ecname_completion)  
        
        ec_editbutton = Gtk.Button.new_with_label("Modify") 
        ec_editbutton.get_child().set_width_chars(8)
        
        ecgstlabel = Gtk.Label()
        ecgstlabel.set_markup("GSTIN")
        self.ecgstentry = Gtk.Entry()
        self.ecgstentry.set_max_length(24)
        
        ecaddresslabel = Gtk.Label()
        ecaddresslabel.set_markup("Address")
        self.ecaddressentry = Gtk.Entry()
        self.ecaddressentry.set_max_length(47)
        
        eccitylabel = Gtk.Label()
        eccitylabel.set_markup("City")
        self.eccityentry = Gtk.Entry()
        self.eccityentry.set_max_length(32)
        
        ecstatelabel = Gtk.Label()
        ecstatelabel.set_markup("State")
        
        self.ecstate_combo = Gtk.ComboBoxText.new_with_entry() 
        for esn in guicommon.state_list:
            self.ecstate_combo.append_text(esn)
        self.ecstate_combo.set_hexpand(False)
        self.ecstate_combo.set_halign(Gtk.Align.CENTER)
        self.ecstate_combo.get_child().set_width_chars(32)     
        
        
        eccountrylabel = Gtk.Label()
        eccountrylabel.set_markup("Country")       
        self.ecccombo = Gtk.ComboBoxText.new_with_entry()
        for countryname in functions.countrieslist:
            self.ecccombo.append_text(countryname)
        self.ecccombo.set_active(0)
        
        eccompleter = Gtk.EntryCompletion()
        eccompleter.set_model(self.ecccombo.get_model())
        eccompleter.set_text_column(0)
        self.ecccombo.get_child().set_completion(eccompleter)
                
        ecpinlabel = Gtk.Label()
        ecpinlabel.set_markup("PIN Code")
        self.ecpinentry = Gtk.Entry()
        self.ecpinentry.set_max_length(16)
        
        ecphonelabel = Gtk.Label()
        ecphonelabel.set_markup("Office Phone")
        self.ecphoneentry = Gtk.Entry()
        self.ecphoneentry.set_max_length(24)
        
        ecmobilelabel = Gtk.Label()
        ecmobilelabel.set_markup("Mobile ")
        self.ecmobileentry = Gtk.Entry()
        self.ecmobileentry.set_max_length(16)
        
        ecemaillabel = Gtk.Label()
        ecemaillabel.set_markup("Email ")
        self.ecemailentry = Gtk.Entry()
        self.ecemailentry.set_max_length(47)
        
        ecstatecodelabel = Gtk.Label()
        ecstatecodelabel.set_markup("State code GST ")
        self.ecstatecodeentry = Gtk.Entry()
        self.ecstatecodeentry.set_max_length(2)
        
        eccpersonlabel = Gtk.Label()
        eccpersonlabel.set_markup("Contact Person ")
        self.eccpersonentry = Gtk.Entry()
        self.eccpersonentry.set_max_length(32)
        
        ecbankaccountlabel = Gtk.Label()
        #ecbankaccountlabel.set_margin_top(20)
        ecbankaccountlabel.set_markup("Primary Bank A/c No. ")        
        self.ecbankaccountentry = Gtk.Entry()
        self.ecbankaccountentry.set_max_length(24)
        #self.ecbankaccountentry.set_margin_top(20)
        
        ecbankifsclabel = Gtk.Label()
        ecbankifsclabel.set_markup("IFSC")        
        self.ecbankifscentry = Gtk.Entry()
        self.ecbankifscentry.set_max_length(24)
        
        ecbanknamelabel = Gtk.Label()
        ecbanknamelabel.set_markup("Bank Name/Other details  ")        
        self.ecbanknameentry = Gtk.Entry()
        self.ecbanknameentry.set_max_length(32)
        
        ecbankaddilabel = Gtk.Label()
        ecbankaddilabel.set_markup("UPI/IMPS/Misc. ")        
        self.ecbankaddientry = Gtk.Entry()
        self.ecbankaddientry.set_max_length(32)
            
        ecdistancelabel = Gtk.Label()
        ecdistancelabel.set_markup("Distance in Kms ")
        self.ecdistanceentry = Gtk.Entry()
        self.ecdistanceentry.set_max_length(8)
        
        ecdosplabel = Gtk.Label()
        ecdosplabel.set_markup("Discount on selling price ")
        self.ecdospentry = Gtk.Entry()
        self.ecdospentry.set_max_length(32)
        
        ecseplabel = Gtk.Label() # separator for grid columns
        ecseplabel.set_markup("  ")
        ecseplabel.set_width_chars(16)
        
        ecminiseplabel = Gtk.Label() # payment block separator for second row columns
        ecminiseplabel.set_markup("     ")
        ecminiseplabel.set_width_chars(16)        
        
        # do not temper below section, compatibility mode start      CMCMCMCMCMCMCMCMCMCMCMCM
        # sec bank widgets start
        
        #ecsecbankwarning = Gtk.Label()
        #ecsecbankwarning.set_markup(" Don't alter this section ")
        #ecsecbankwarning.set_sensitive(False)
        #ecsecbankwarning.set_no_show_all(True)
        #ecsecbankwarning.hide()
               
        #ecsecbanklabel = Gtk.Label()
        #ecsecbanklabel.set_markup(" (Sec. or Int'l) ")
        #ecsecbanklabel.set_sensitive(False)
        #ecsecbanklabel.set_no_show_all(True)
        #ecsecbanklabel.hide()      
                
        #ecsecbankaccountlabel = Gtk.Label()
        #ecsecbankaccountlabel.set_markup("Bank account No. ")
        #ecsecbankaccountlabel.set_sensitive(False) 
        #ecsecbankaccountlabel.set_no_show_all(True)
        #ecsecbankaccountlabel.hide()
                   
        #self.ecsecbankaccountentry = Gtk.Entry()
        #self.ecsecbankaccountentry.set_sensitive(False)
        #self.ecsecbankaccountentry.set_no_show_all(True)
        #self.ecsecbankaccountentry.hide()     
        
        #ecsecbankifsclabel = Gtk.Label()
        #ecsecbankifsclabel.set_markup("IFSC/SWIFT/BIC ")
        #ecsecbankifsclabel.set_sensitive(False) 
        #ecsecbankifsclabel.set_no_show_all(True)
        #ecsecbankifsclabel.hide()    
               
        #self.ecsecbankifscentry = Gtk.Entry()
        #self.ecsecbankifscentry.set_sensitive(False)
        #self.ecsecbankifscentry.set_no_show_all(True)
        #self.ecsecbankifscentry.hide() 
        
        #ecsecbanknamelabel = Gtk.Label()
        #ecsecbanknamelabel.set_markup("Bank Name ")
        #ecsecbanknamelabel.set_sensitive(False) 
        #ecsecbanknamelabel.set_no_show_all(True)
        #ecsecbanknamelabel.hide()     
              
        #self.ecsecbanknameentry = Gtk.Entry()
        #self.ecsecbanknameentry.set_sensitive(False) 
        #self.ecsecbanknameentry.set_no_show_all(True)
        #self.ecsecbanknameentry.hide()    
        
        #ecsecbankaddilabel = Gtk.Label()
        #ecsecbankaddilabel.set_markup("Additional banking details  ")
        #ecsecbankaddilabel.set_sensitive(False)  
        #ecsecbankaddilabel.set_no_show_all(True)
        #ecsecbankaddilabel.hide()    
               
        #self.ecsecbankaddientry = Gtk.Entry()
        #self.ecsecbankaddientry.set_sensitive(False)
        #self.ecsecbankaddientry.set_no_show_all(True)
        #self.ecsecbankaddientry.hide()     
        # sec bank widgets end
        # From now u can make changes, compatibility mode ends     CMECMECMECMECMECMECMECME
        
        eccreditlimitlabel = Gtk.Label()
        eccreditlimitlabel.set_markup("Credit Limit ")
        self.eccreditlimitentry = Gtk.Entry()
        self.eccreditlimitentry.set_max_length(11)
        
        ecpaydayslabel = Gtk.Label()
        ecpaydayslabel.set_markup("Payment terms ")
        self.ecpaydaysentry = Gtk.Entry()
        self.ecpaydaysentry.set_max_length(32)
        
        ecbusinessarealabel = Gtk.Label()
        ecbusinessarealabel.set_markup("Business area/Focus ")
        self.ecbusinessareaentry = Gtk.Entry()   
        self.ecbusinessareaentry.set_max_length(47)
        
        eccommentslabel = Gtk.Label()
        eccommentslabel.set_markup("Comments ")
        self.eccommentsentry = Gtk.Entry()
        self.eccommentsentry.set_max_length(47)
        
        ecflaglabel = Gtk.Label()
        ecflaglabel.set_markup("Flag ")
        self.ecflagentry = Gtk.Entry()  
        self.ecflagentry.set_max_length(16)       
        
        ecinstapaylabel = Gtk.Label()
        ecinstapaylabel.set_markup("Immediate payment ")       
        self.ecinstapaybutton = Gtk.CheckButton() # use this to give reminder during bill generation with this company
        #self.ecinstapaybutton.set_label("  (Reminder only)")
        self.ecinstapaybutton.set_active(False)
        
        ecblacklistlabel = Gtk.Label()
        ecblacklistlabel.set_markup("Blacklist this company ")
        ecblacklistlabel.set_margin_top(10)      
        self.ecblacklistbutton = Gtk.CheckButton()
        self.ecblacklistbutton.set_margin_top(10)   
        self.ecblacklistbutton.set_active(False) # By default false  
        
        ecshippingaddress_label = Gtk.Label()
        ecshippingaddress_label.set_markup("Different shipping address  ")
        ecshippingaddress_label.set_margin_top(10)
        self.ecshippingaddress_button = Gtk.CheckButton()
        self.ecshippingaddress_button.set_margin_top(10)  
        self.ecshippingaddress_button.set_active(False) # By default false  
            
        self.ecvarg=[self.ecnameentry, self.ecgstentry, self.ecaddressentry, self.eccityentry, self.ecstate_combo, self.ecccombo, self.ecpinentry, self.ecphoneentry, self.eccpersonentry, self.ecmobileentry, self.ecemailentry, self.ecstatecodeentry,  self.ecbankaccountentry, self.ecbankifscentry, self.ecbanknameentry, self.ecbankaddientry,  self.ecdistanceentry, self.ecbusinessareaentry, self.eccommentsentry, self.ecflagentry,  self.ecdospentry, self.eccreditlimitentry, self.ecpaydaysentry,  self.ecinstapaybutton, self.ecblacklistbutton]
        
        self.ecentries=[self.ecnameentry, self.ecgstentry, self.ecaddressentry, self.eccityentry, self.ecpinentry, self.ecphoneentry, self.eccpersonentry, self.ecmobileentry, self.ecemailentry, self.ecstatecodeentry,  self.ecbankaccountentry, self.ecbankifscentry, self.ecbanknameentry, self.ecbankaddientry,  self.ecdistanceentry, self.ecbusinessareaentry, self.eccommentsentry, self.ecflagentry, self.ecdospentry, self.eccreditlimitentry, self.ecpaydaysentry]
        
        ecsavebutton = Gtk.Button.new_with_label("Save")
        ecsavebutton.set_name('ecsb')
        ecsavebutton.get_style_context().add_class("suggested-action")
        ecsavebutton.connect("clicked", self.processecompany, self.ecvarg, invoicingbox, bph, guiinvoicingins)
                    
        ecresetbutton = Gtk.Button.new_with_label("Reset")
        ecresetbutton.connect("clicked", self.ecresetfields, self.ecentries)
        #ecresetbutton.get_style_context().add_class("dangerbutton")       
        
        ecdeletebutton = Gtk.Button.new_with_label("Delete company")
        ecdeletebutton.connect("clicked", self.ecdelete_func, invoicingbox, bph, guiinvoicingins)
        ecdeletebutton.get_style_context().add_class("dangerbutton")      
            
        gridecbox.add(ecnamelabel)
        gridecbox.attach(self.ecnameentry, 1, 0, 1, 1)
        gridecbox.attach(ec_editbutton, 2, 0, 1, 1)
        gridecbox.attach(ecgstlabel, 0, 1, 1, 1)
        gridecbox.attach(self.ecgstentry, 1, 1, 1, 1)
        gridecbox.attach(ecaddresslabel, 0, 2, 1, 1)
        gridecbox.attach(self.ecaddressentry, 1, 2, 1, 1)
        gridecbox.attach(eccitylabel, 0, 3, 1, 1)
        gridecbox.attach(self.eccityentry, 1, 3, 1, 1)
        gridecbox.attach(ecstatelabel, 0, 4, 1, 1)
        gridecbox.attach(self.ecstate_combo, 1, 4, 1, 1)
        gridecbox.attach(eccountrylabel, 0, 5, 1, 1)
        gridecbox.attach(self.ecccombo, 1, 5, 1, 1)
        gridecbox.attach(ecpinlabel, 0, 6, 1, 1)
        gridecbox.attach(self.ecpinentry, 1, 6, 1, 1)
        gridecbox.attach(ecphonelabel, 0, 7, 1, 1)
        gridecbox.attach(self.ecphoneentry, 1, 7, 1, 1)
        gridecbox.attach(eccpersonlabel, 0, 8, 1, 1)
        gridecbox.attach(self.eccpersonentry, 1, 8, 1, 1)        
        gridecbox.attach(ecmobilelabel, 0, 9, 1, 1)
        gridecbox.attach(self.ecmobileentry, 1, 9, 1, 1)
        gridecbox.attach(ecemaillabel, 0, 10, 1, 1)
        gridecbox.attach(self.ecemailentry, 1, 10, 1, 1)
        gridecbox.attach(ecstatecodelabel, 0, 11, 1, 1)
        gridecbox.attach(self.ecstatecodeentry, 1, 11, 1, 1) 
        gridecbox.attach(ecbankaccountlabel, 0, 13, 1, 1)
        gridecbox.attach(self.ecbankaccountentry, 1, 13, 1, 1)
        gridecbox.attach(ecbankifsclabel, 0, 14, 1, 1)
        gridecbox.attach(self.ecbankifscentry, 1, 14, 1, 1)
        gridecbox.attach(ecbanknamelabel, 0, 15, 1, 1)
        gridecbox.attach(self.ecbanknameentry, 1, 15, 1, 1)
        gridecbox.attach(ecbankaddilabel, 0, 16, 1, 1)
        gridecbox.attach(self.ecbankaddientry, 1, 16, 1, 1)               
        
        # NOTE Some space is reserved for future elements, plus some other important reason       CMCMCMCMCMCMCMCM
        # Do not try to use this space::: Second half (RHS) column top side 5 grid rows
                
        # Secondary banking details starts, don't alter this section for compatibility reasons
        #gridecbox.attach(ecsecbankwarning, 5, 2, 1, 1) 
        #gridecbox.attach(ecsecbankaccountlabel, 3, 0, 1, 1)
        #gridecbox.attach(self.ecsecbankaccountentry, 4, 0, 1, 1)
        #gridecbox.attach(ecsecbankifsclabel, 3, 1, 1, 1)
        #gridecbox.attach(self.ecsecbankifscentry, 4, 1, 1, 1)
        #gridecbox.attach(ecsecbanknamelabel, 3, 2, 1, 1)
        #gridecbox.attach(self.ecsecbanknameentry, 4, 2, 1, 1)
        #gridecbox.attach(ecsecbankaddilabel, 3, 3, 1, 1)
        #gridecbox.attach(self.ecsecbankaddientry, 4, 3, 1, 1)
        #gridecbox.attach(ecsecbanklabel, 5, 0, 1, 1)
        # Secondary banking details end, from now u can change        CMECMECMECMECMECMECMECMECMECMECMECME  
        
        gridecbox.attach(ecseplabel, 2, 0, 1, 1)
        gridecbox.attach(ecdistancelabel, 3, 5, 1, 1)
        gridecbox.attach(self.ecdistanceentry, 4, 5, 1, 1)
        gridecbox.attach(ecbusinessarealabel, 3, 6, 1, 1)
        gridecbox.attach(self.ecbusinessareaentry, 4, 6, 1, 1) 
        gridecbox.attach(eccommentslabel, 3, 7, 1, 1)
        gridecbox.attach(self.eccommentsentry, 4, 7, 1, 1) 
        #gridecbox.attach(ecflaglabel, 3, 8, 1, 1)
        #gridecbox.attach(self.ecflagentry, 4, 8, 1, 1)         
        gridecbox.attach(ecdosplabel, 3, 9, 1, 1)
        gridecbox.attach(self.ecdospentry, 4, 9, 1, 1)
        gridecbox.attach(eccreditlimitlabel, 3, 10, 1, 1)
        gridecbox.attach(self.eccreditlimitentry, 4, 10, 1, 1)
        gridecbox.attach(ecpaydayslabel, 3, 11, 1, 1)
        gridecbox.attach(self.ecpaydaysentry, 4, 11, 1, 1)        
        gridecbox.attach(ecminiseplabel, 3, 12, 1, 1) 
        #gridecbox.attach(ecinstapaylabel, 3, 13, 1, 1)
        #gridecbox.attach(self.ecinstapaybutton, 4, 13, 1, 1)
        #gridecbox.attach(ecblacklistlabel, 3, 14, 1, 1)
        #gridecbox.attach(self.ecblacklistbutton, 4, 14, 1, 1)  
        #gridecbox.attach(ecshippingaddress_label, 3, 15, 1, 1)
        #gridecbox.attach(self.ecshippingaddress_button, 4, 15, 1, 1)           
        gridecbox.attach(ecsavebutton, 4, 17, 1, 1)
        gridecbox.attach(ecresetbutton, 3, 17, 1, 1)
        gridecbox.attach(ecdeletebutton, 5, 17, 1, 1)
        
        ec_editbutton.connect("clicked", self.set_ecentries, self.ecentries)  
        
        self.companystack.add_titled(ecbox, "editcompanymain", "Edit Company")
              
 
#==================================== COMPANIES LIST =====================================================

        companiesview_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6) 
        cvheaderbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6) #cv=companies viewer
        cvheaderbox.set_vexpand(False)
        #cvheaderbox.get_style_context().add_class("testarea") 
        
        gridcv = Gtk.Grid() #cv=companies viewer
        gridcv.set_vexpand(False)
        cvheaderbox.pack_start(gridcv, False, False, 0)   
              
        cv_loadbutton = Gtk.Button.new_with_label("Refresh")
        cv_loadbutton.set_name('loadcompaniesbutton')                 
        cv_loadbutton.connect("clicked", self.refreshcl)        
        gridcv.add(cv_loadbutton)    
        
        companiesview_box.pack_start(cvheaderbox, False, False, 0)
        
        cvsw_headings=companyprocessor.sbh()        
        companiesview_box.pack_start(cvsw_headings, False, False, 0)
      
        self.cvsw = Gtk.ScrolledWindow(hexpand=False) #inventory page scroll window
        #self.cvsw.set_min_content_width(560)      
        #self.cvsw.set_max_content_width(800)
        self.cvsw.set_min_content_height(360)
        #self.cvsw.set_max_content_height(720)
        self.cvsw.get_style_context().add_class("lightgreymedborder")
        self.cvsw.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)        
        self.cvsw.add(companyprocessor.generate_companieslist('mimicevent'))
        companiesview_box.pack_start(self.cvsw, False, False, True) 
        
        self.companystack.add_titled(companiesview_box, "companieslistmain", "List of companies")

        self.companystack_switcher = Gtk.StackSwitcher()
        self.companystack_switcher.set_stack(self.companystack)
        
        #print("Packing of stack started")  
        self.companymasterbox.pack_start(self.companystack_switcher, False, False, 10)
        self.companymasterbox.pack_start(self.companystack, False, False, 10)
           
        return self.companymasterbox 

#=========================================================================================================  
          
    #-------- Functions used in Create pane  ----------------------------------------------------------------------
       
    def processccompany(self, widget, ccvarg, invoicingbox, bph, guiinvoicingins):
        cdata=companyprocessor.extractccdata(ccvarg)
        #print(cdata)
        self.companytableins.createrow(cdata[0], cdata)
        self.ccresetfields('mimicevent', self.ccentries)    # set form fields to blank fields
        guicommon.loadguicommon()    
        self.ecname_completion.set_model(guicommon.companyname_store)
        self.ecnameentry.set_completion(self.ecname_completion)   
        
        children=invoicingbox.get_children()
        for eachchild in children:
            invoicingbox.remove(eachchild)
            eachchild.destroy()
        bph=guiinvoicingins.generatepage(self.mainwindow)
        invoicingbox.add(bph)
        invoicingbox.show_all()        
        print("Successfully created company")
        return 1    


    def ccresetfields(self, eventsignal, ccfields):
        for eachentry in ccfields:
            eachentry.set_text('')
        self.ccblacklistbutton.set_active(False) # By default false
        self.ccinstapaybutton.set_active(False)
        return 2 


    def set_ecentries(self, seterwidget, entrieslist):
        self.nocte=self.ecnameentry.get_text() #name of company to be edited
        ecfetcheditem=self.companytableins.readrow(self.nocte)   
        self.ec_temprowindex=self.companytableins.rowlist.index(self.nocte)
        
        for anyentry in self.ecvarg:
            anyentry.set_sensitive(True)     
    
        self.ecnameentry.set_text(ecfetcheditem[0])
        self.ecgstentry.set_text(ecfetcheditem[1])
        self.ecaddressentry.set_text(ecfetcheditem[8])
        self.eccityentry.set_text(ecfetcheditem[9])
        self.ecstate_combo.get_child().set_text(ecfetcheditem[10])
        self.ecccombo.get_child().set_text(ecfetcheditem[11])
        self.ecpinentry.set_text(ecfetcheditem[12])
        self.ecphoneentry.set_text(ecfetcheditem[13])
        self.eccpersonentry.set_text(ecfetcheditem[14])
        self.ecmobileentry.set_text(ecfetcheditem[15])
        self.ecemailentry.set_text(ecfetcheditem[16])       
        self.ecstatecodeentry.set_text(ecfetcheditem[17])
        self.ecbankaccountentry.set_text(ecfetcheditem[18])
        self.ecbankifscentry.set_text(ecfetcheditem[19])
        self.ecbanknameentry.set_text(ecfetcheditem[20])
        self.ecbankaddientry.set_text(ecfetcheditem[21])       
        self.ecdistanceentry.set_text(ecfetcheditem[22])
        self.ecbusinessareaentry.set_text(ecfetcheditem[23])
        self.eccommentsentry.set_text(ecfetcheditem[24])       
        self.ecflagentry.set_text(ecfetcheditem[25])
        self.ecdospentry.set_text(ecfetcheditem[26])
        self.eccreditlimitentry.set_text(ecfetcheditem[27])
        self.ecpaydaysentry.set_text(ecfetcheditem[28])
        
        if ecfetcheditem[29]=='n':
            self.ecinstapaybutton.set_active(False)
        elif ecfetcheditem[29]=='y':
            self.ecinstapaybutton.set_active(True)
        if ecfetcheditem[30]=='n':
            self.ecinstapaybutton.set_active(False)
        elif ecfetcheditem[30]=='y':
            self.ecblacklistbutton.set_active(True)                 
       
        return 1
        
        
    def processecompany(self, widget, ecvarg, invoicingbox, bph, guiinvoicingins):
        cdata=companyprocessor.extractecdata(ecvarg)
        self.companytableins.editrow(self.nocte, cdata)
        self.ecresetfields('mimicevent', self.ecentries)    # set form fields to blank fields
        guicommon.loadguicommon()    
        self.ecname_completion.set_model(guicommon.companyname_store)
        self.ecnameentry.set_completion(self.ecname_completion)  
        
        children=invoicingbox.get_children()
        for eachchild in children:
            invoicingbox.remove(eachchild)
            eachchild.destroy()
        bph=guiinvoicingins.generatepage(self.mainwindow)
        invoicingbox.add(bph)
        invoicingbox.show_all()        
        
        self.nocte=''
        print("Successfully modified company")
        return 1        

    
    def ecdelete_func(self, deletebutton, invoicingbox, bph, guiinvoicingins):       
        self.nocte=self.ecnameentry.get_text() #name of company to be edited 
        self.companytableins.deleterow(self.nocte) 
        self.ecresetfields('delbuttonpress', self.ecentries)
        guicommon.loadguicommon()
        self.ecname_completion.set_model(guicommon.companyname_store)
        self.ecnameentry.set_completion(self.ecname_completion)   
              
        children=invoicingbox.get_children()
        for eachchild in children:
            invoicingbox.remove(eachchild)
            eachchild.destroy()
        bph=guiinvoicingins.generatepage(self.mainwindow)
        invoicingbox.add(bph)
        invoicingbox.show_all()        
        
        print('deleted company successfully')
        return 2 

        
    def ecresetfields(self, resetbutton, ecfields):
        for eachentry in ecfields:
            eachentry.set_text('')
        self.ecblacklistbutton.set_active(False) # By default false
        self.ecinstapaybutton.set_active(False)
        self.nocte=''
        return 2     
       
   
    def refreshcl(self, event):
        self.cvsw.remove(self.cvsw.get_child())
        print('removed previous')
        self.cvsw.add(companyprocessor.generate_companieslist('mimicevent'))
        print('added new')                 
       
