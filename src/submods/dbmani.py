# This file contains initializations and functions accessing tealordb: Ver sep 2020

import sys
from submods import tealordb
import pickledb
from datetime import datetime


itemtableins=tealordb.Tealor()
companytableins=tealordb.Tealor()
invoicetableins=tealordb.Tealor()


    

def loadidbase():     
    itemtableins.loaddata('items')
    tmp_itemtable_colheadingslength=len(itemtableins.getcollist())
    if tmp_itemtable_colheadingslength==0:           
        items_colheadingslist=['name', 'hsn', 'creationdate', 'creationstock', 'group', 'subgroup', 'unit', 'tax', 'phasedout', 'openingstock', 'currentstock', 'criticallevel', 'listprice', 'stddiscount', 'sellingprice', 'purchaseprice', 'comments'] 
        itemtableins.setcolumnheadings(items_colheadingslist)
        #print('item table column headings not found, created')  
        
    elif tmp_itemtable_colheadingslength==17:               
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
        
               
    invoicetableins.loaddata('invoices')
    tmp_invoicetable_colheadingslength=len(invoicetableins.getcollist())
    #print (tmp_invoicetable_colheadingslength)
    if tmp_invoicetable_colheadingslength==0:           
        invoice_colheadingslist=['sversion', 'invoicename', 'invoicenumber', 'invoicedate', 'invoicetime', 'fy', 'invoicetype', 'sourcecompany', 'toparty', 'ponumber', 'taxcategory', 'cess', 'invoicecomments', 'basicamount', 'amountdiscount', 'freight', 'othercharges', 'totaltax', 'roundoff', 'grandtotal', 'numberofitems', 'itemlist', 'qtylist', 'splist', 'itemdiscountlist', 'amountlist', 'itemcommentslist'] 
            #sversion (storageversion) necessary in case format-tax changes in future, this can provide compatibility
            #invoice type is selling or purchase
            #invoice name is key value which is combination of inv number plus invoice date plus sourcecompany
        invoicetableins.setcolumnheadings(invoice_colheadingslist)
        #print('invoice table column headings not found, created')  
        
    elif tmp_invoicetable_colheadingslength==27:               
        #print ('Already set column headings for invoice table')
        pass
        
    else:
        print('need to inspect invoice table column headings')
            
    global miscdb    
    global itemgroups
    miscdb= pickledb.load('miscellaneousdb.db', False)
    miscdb_checkpresence=miscdb.get('checkpresence')
    if miscdb_checkpresence==False: 
        print ('Not found miscdb on disk, creating it')
        miscdb.set('checkpresence', 'present')    
        miscdb.set('itemgroups', ['none'])
        miscdb.dump()
        itemgroups=miscdb.get('itemgroups')
    elif miscdb_checkpresence=='present':    
            itemgroups=miscdb.get('itemgroups')
            print ('loaded miscdb from disk')
        #print("loaded database , reporting from guisub")
        
        #return itemtableins, companytableins, invoicetableins, miscdb, itemgroups
        
