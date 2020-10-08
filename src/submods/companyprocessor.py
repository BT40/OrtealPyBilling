from submods import functions
from submods import guicommon
import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


def extractccdata(ccvarg):
        cname=ccvarg[0].get_text().capitalize()
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


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def extractecdata(ecvarg):
        cname=ecvarg[0].get_text().capitalize()
        cgst=ecvarg[1].get_text()
        caddress=ecvarg[2].get_text()
        ccity=ecvarg[3].get_text()
        cstate=ecvarg[4].get_text()
        ccountry=ecvarg[5].get_active_text()
        cpin=ecvarg[6].get_text()
        cphone=ecvarg[7].get_text()
        cperson=ecvarg[8].get_text()
        cmobile=ecvarg[9].get_text()
        cemail=ecvarg[10].get_text()
        cwebsite=ecvarg[11].get_text()
        cbankaccount=ecvarg[12].get_text()
        cbankifsc=ecvarg[13].get_text()
        cbankname=ecvarg[14].get_text()
        cbankupi=ecvarg[15].get_text()       
        cdistance=ecvarg[16].get_text()
        cfocus=ecvarg[17].get_text()
        ccomments=ecvarg[18].get_text()
        cflag=ecvarg[19].get_text()
        cdiscount=ecvarg[20].get_text()
        ccreditlimit=ecvarg[21].get_text()
        ccpaymentindays=ecvarg[22].get_text()
        rawcinstapay=ecvarg[23]
        rawcblacklisted=ecvarg[24]
        
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


#===================================================== SCROLL BOX FOR COMPANIES VIEWING ====================


def generate_companieslist(event):
            cvlistbox = Gtk.ListBox() 
            cvlistbox.set_selection_mode(Gtk.SelectionMode.NONE)
            #print (len(self.companytableins.rowlist))
            for eachitem in guicommon.companies_alphabetic:
            #pointitem=comstore.append(eachitem)               
                cvlb_temprow = Gtk.ListBoxRow()
                cvlbvr_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
                cvlbvr_box.set_hexpand(False)              
                cvlbvr_box.get_style_context().add_class("inventoryviewrb")
                
                csrn_templabel = Gtk.Label(label=guicommon.companies_alphabetic.index(eachitem)+1, xalign=0)
                csrn_templabel.set_width_chars(8)
                
                cname_templabel = Gtk.Label(label=eachitem[0], xalign=0)
                cname_templabel.set_width_chars(47)
                
                ccity_templabel = Gtk.Label(label=eachitem[9])
                ccity_templabel.set_width_chars(16)
                
                cperson_templabel = Gtk.Label(label=eachitem[14])
                cperson_templabel.set_width_chars(16)
               
                cmobile_templabel = Gtk.Label(label=eachitem[15])
                cmobile_templabel.set_width_chars(12)
                
                
                cvlbvr_box.pack_start(csrn_templabel, False, False, 0)
                cvlbvr_box.pack_start(cname_templabel, False, False, 0)
                cvlbvr_box.pack_start(ccity_templabel, False, False, 0)
                cvlbvr_box.pack_start(cperson_templabel, False, False, 0)
                cvlbvr_box.pack_start(cmobile_templabel, False, False, 0)
                
                cvlb_temprow.add(cvlbvr_box) 
                cvlistbox.add(cvlb_temprow)
            cvlistbox.show_all()
            #print('listrow called')
            return cvlistbox

################################  Scroll box headings ###############

def sbh(): # companies list scrollbox labelling-header
        clhb = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0) #companies list heading box    
        clhb_srlabel = Gtk.Label(label="Sr. No.", xalign=0)
        clhb_srlabel.set_width_chars(8)
        clhb_cnamelabel = Gtk.Label(label="Party name   ")
        clhb_cnamelabel.set_width_chars(47)
        clhb_citylabel = Gtk.Label(label="City")
        clhb_citylabel.set_width_chars(16)   
        clhb_personlabel = Gtk.Label(label="Contact Person")
        clhb_personlabel.set_width_chars(16)      
        clhb_mobilelabel = Gtk.Label(label="Mobile")
        clhb_mobilelabel.set_width_chars(16)           
        
       # item1label.set_markup("Item 1 to be billed")
        clhb.pack_start(clhb_srlabel, False, False, 0)
        clhb.pack_start(clhb_cnamelabel, False, False, 0)
        clhb.pack_start(clhb_citylabel, False, False, 0)
        clhb.pack_start(clhb_personlabel, False, False, 0)
        clhb.pack_start(clhb_mobilelabel, False, False, 0)
        return clhb



