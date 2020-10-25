import sys
import gi
from submods import dbmani
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
    
    #print('above was guicommon initialisation')      
