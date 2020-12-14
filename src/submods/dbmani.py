# This file contains initializations and functions accessing tealordb: Ver Oct 2020

import sys
import os
import signal
import pickledb
from submods import tealordb
from submods import stddata
from datetime import datetime


itemtableins=tealordb.Tealor()
companytableins=tealordb.Tealor()
invoicetableins=tealordb.Tealor()
taxtableins=tealordb.Tealor()


    

def loadidbase():     
    itemtableins.loaddata('items')
    tmp_itemtable_colheadingslength=len(itemtableins.getcollist())
    if tmp_itemtable_colheadingslength==0:           
        items_colheadingslist=['name', 'phasedout', 'emerg', 'creationdate', 'creationstock', 'softwareversion', 'hsn', 'group', 'subgroup', 'unit', 'tax', 'taxinclusive', 'lastmodified', 'openingstock', 'unitssold', 'currentstock', 'criticallevel', 'listprice', 'stddiscount', 'sellingprice', 'purchaseprice', 'comments', 'flag'] 
        
        itemtableins.setcolumnheadings(items_colheadingslist)
        #print('item table column headings not found, created')  
        
    elif tmp_itemtable_colheadingslength==23:               
        #print ('Already set column headings for item table')
        pass
        
    else:
        print('need to inspect item table column headings')
                 
        
    companytableins.loaddata('companies')
    tmp_companytable_colheadingslength=len(companytableins.getcollist())
    if tmp_companytable_colheadingslength==0:           
        companies_colheadingslist=['name', 'hsn', 'creationdate', 'creationstock', 'group', 'subgroup', 'unit', 'tax', 'phasedout', 'openingstock', 'currentstock', 'criticallevel', 'listprice', 'stddiscount', 'sellingprice', 'purchaseprice', 'comments'] 
        companytableins.setcolumnheadings(companies_colheadingslist)
        #print('companies table column headings not found, created')  
        
    elif tmp_companytable_colheadingslength==17:               
        #print ('Already set column headings for companies table')
        pass
        
    else:
        print('need to inspect companies table column headings')        
    
    
    taxtableins.loaddata('taxslabs')
    tmp_taxtable_colheadingslength=len(taxtableins.getcollist())
    if tmp_taxtable_colheadingslength==0:           
        taxslabs_colheadingslist=['nameofslab', 'enablefirst', 'enablesecond', 'enablethird', 'firsttaxname', 'secondtaxname', 'thirdtaxname',  'firsttaxrate', 'secondtaxrate', 'thirdtaxrate', 'totaltaxrate' ] 
        taxtableins.setcolumnheadings(taxslabs_colheadingslist)
        print('tax slabs table column headings not found, created')  
        
        for each_taxslab_name in stddata.gstslabs_list_std:
            tindex_temp=stddata.gstslabs_list_std.index(each_taxslab_name)
            taxslabdata_temp=stddata.gstslabs_data_std[tindex_temp]
            taxtableins.createrow(each_taxslab_name, taxslabdata_temp)      
        
    elif tmp_taxtable_colheadingslength==11:               
        #print ('Already set column headings for tax table')
        pass
        
    else:
        print('need to inspect tax table column headings')            
               
    invoicetableins.loaddata('invoices')
    tmp_invoicetable_colheadingslength=len(invoicetableins.getcollist())
    #print (tmp_invoicetable_colheadingslength)
    if tmp_invoicetable_colheadingslength==0:           
        invoice_colheadingslist=[ 'invoicename','softwareversion', 'invoicenumber', 'invoicedate', 'invoicetime', 'fy', 'invoicetype', 'sourcecompany', 'toparty', 'ponumber', 'taxcategory', 'taxontax', 'invoicecomments', 'basicamount', 'amountdiscount', 'freight', 'othercharges', 'taxamount', 'taxontaxamount', 'roundoff', 'grandtotal', 'numberofitems', 'itemlist', 'qtylist', 'splist', 'itemdiscountlist', 'amountlist', 'itemcommentslist', 'itemhsnlist'] 
            #sversion (storageversion) necessary in case format-tax changes in future, this can provide compatibility
            #invoice type is selling or purchase
            #invoice name is key value which is combination of inv number plus invoice date plus sourcecompany
        invoicetableins.setcolumnheadings(invoice_colheadingslist)
        #print('invoice table column headings not found, created')  
        
    elif tmp_invoicetable_colheadingslength==29:               
        #print ('Already set column headings for invoice table')
        pass
        
    else:
        print('need to inspect invoice table column headings')
            
    global miscdb    
    global itemgroups
    global taxontax_list
    global taxontax_data
    
    if not os.path.exists('udat'): # check folder udat exist, if not create
        os.makedirs('udat')
            
    miscdb= pickledb.load('udat/miscellaneous.db', False)
    miscdb_checkpresence=miscdb.get('checkpresence')
    if miscdb_checkpresence==False: 
        print ('Not found miscdb on disk, creating it')
        miscdb.set('checkpresence', 'present')    
        miscdb.set('itemgroups', ['none'])
        miscdb.set('taxontaxslabslist', stddata.taxontax_list_std)
        miscdb.set('taxontaxslabsdata', stddata.taxontax_data_std)        
        miscdb.set('roundoffenabled', 'yes')
        miscdb.set('autoinvoice_numbering', 'no')
        miscdb.set('hidepurchasedata', 'no')
        miscdb.set('invoiceprefix', '')
        miscdb.set('termsline1', 'Some terms')
        miscdb.set('termsline2', '')
        miscdb.set('termsline3', '')
        miscdb.set('termsline4', '')
        miscdb.set('currentfinancialyear', 'Disabled')
        
        miscdb.set('mycompanyname', '')        
        miscdb.set('mycompanyaddress', '')
        miscdb.set('mycompanygstin', '')
        miscdb.set('mycompanycity', '')
        miscdb.set('mycompanypin', '')
        miscdb.set('mycompanystate', '')
        miscdb.set('mycompanycountry', '')
        miscdb.set('mycompanystatecode', '')
        miscdb.set('mycompanyphone', '')
        miscdb.set('mycompanyemail', '')
        
                
        miscdb.dump()
        itemgroups=miscdb.get('itemgroups')
    elif miscdb_checkpresence=='present':    
            itemgroups=miscdb.get('itemgroups')         
            print ('loaded miscdb from disk')
        
      
