import sys
import gi
from submods import dbmani
from submods import simpledialog
import operator
#from submods import functions

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk

 
def loadguicommon():
       
    #print('below is guicommon initialisatiin') 
    global itemtableins   
    itemtableins=dbmani.itemtableins
    global companytableins
    companytableins=dbmani.companytableins
    global taxtableins   
    taxtableins=dbmani.taxtableins
    global invoicetableins
    invoicetableins=dbmani.invoicetableins
    global statementstableins
    statementstableins=dbmani.statementstableins
    global miscdbins
    miscdbins=dbmani.miscdb
    global itemgroups
    itemgroups=miscdbins.get('itemgroups')
    
    global taxontax_list
    taxontax_list=miscdbins.get('taxontaxslabslist')   
    
    global taxontax_data
    taxontax_data=miscdbins.get('taxontaxslabsdata')    
    
    global items_alphabetic
    items_alphabetic=itemtableins.rowcollection.copy()
    items_alphabetic.sort(key=operator.itemgetter(0))
    
    global companies_alphabetic
    companies_alphabetic=companytableins.rowcollection.copy()
    companies_alphabetic.sort(key=operator.itemgetter(0))
      
    #use for company name completion everywhere 
    global companyname_store
    companyname_store = Gtk.ListStore(str)
    for eachcompany_tmp in companytableins.rowlist:
        companyname_store.append([eachcompany_tmp])
        #print (eachcompany_tmp)   
        
     #use for item name completion everywhere 
    global itemname_store    
    itemname_store = Gtk.ListStore(str)
    for eachitem_tmp in itemtableins.rowlist:
        itemname_store.append([eachitem_tmp])
        #print (eachitem_tmp)  
    
    global itemgroup_store    
    itemgroup_store = Gtk.ListStore(str)
    for eachitem_tmp in itemgroups:
        itemgroup_store.append([eachitem_tmp])
        #print (eachitem_tmp)  
        
    global taxslabs_store 
    taxslabs_store=Gtk.ListStore(str)
    for eachtslab_tmp in taxtableins.rowlist:
        taxslabs_store.append([eachtslab_tmp])
        #print (eachtslab_tmp)   
    
    global invoicename_store    
    invoicename_store = Gtk.ListStore(str)
    for eachinv_tmp in invoicetableins.rowlist:
        invoicename_store.append([eachinv_tmp])
    #    print (eachinv_tmp)  
    
    global state_list
    state_list=miscdbins.get('statelisthome')     
    
    global statecodes_list
    statecodes_list=miscdbins.get('statecodesgsthome')   
    
    global simpledialogins
    simpledialogins=simpledialog.SimpleGtkDialog()
    #def display_message (parentwindow, dialogheading, msg_one, msg_two, msg_three ):
    #msg 21&2 are spaced while 2 & 3 are not
    
      
