import sys
import gi
from submods import dbmani
#import functions

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk



class GtkProcessor():
    
    #def __init__(self):
    
       # self.dbase_maniins=dbmani.DbaseMani()
       # self.miscdb, self.itemgroups=self.dbase_maniins.loadidbase()
       # self.itemtableins=self.dbase_maniins.itemtableins
       # self.companytableins=self.dbase_maniins.companytableins
       # self.invoicetableins=self.dbase_maniins.invoicetableins
        
        
    def cni_processnci(self, nciilb_inamelist, nciilb_iqtylist, nciilb_isplist, nciilb_idiscountlist, nciilb_iamtlist, nciilb_icommlist, nciilb_ihsnlist):
            self.nci_inameholder=[]
            self.nci_iqtyholder=[]
            self.nci_ispholder=[]
            self.nci_idischolder=[]
            self.nci_iamtholder=[]
            self.nci_icommholder=[]
            #self.nci_ihsnholder=[]
            
            i=0
            while i<100:
                iname=nciilb_inamelist[i].get_text()
                iqty=nciilb_iqtylist[i].get_text()
                isp=nciilb_isplist[i].get_text()
                #idisc=nciilb_idiscountlist[i].get_text()
                iamt=nciilb_iamtlist[i].get_text()
                icomm=nciilb_icommlist[i].get_text()                
                #ihsn=nciilb_ihsnlist[i].get_text()
                
                
                self.nci_inameholder.append(iname)
                self.nci_iqtyholder.append(iqty)
                self.nci_ispholder.append(isp)
                #self.nci_idischolder.append(idisc)
                self.nci_iamtholder.append(iamt)
                self.nci_icommholder.append(icomm)
                #self.nci_ihsnholder.append(ihsn)
                i=i+1
            print (self.nci_inameholder)


