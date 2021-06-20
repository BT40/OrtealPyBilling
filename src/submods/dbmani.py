# This file contains initializations and functions accessing tealordb: Ver Oct 2020

import sys
import os
import signal
import pickledb
from submods import tealordb
from submods import stddata
from datetime import datetime
from os.path import dirname
from pathlib import Path


itemtableins=tealordb.Tealor()
companytableins=tealordb.Tealor()
invoicetableins=tealordb.Tealor()
taxtableins=tealordb.Tealor()
statementstableins=tealordb.Tealor()
    

def loadidbase(projectdirectory):   

    global miscdb    
    global itemgroups
    global taxontax_list
    global taxontax_data 
    
    home_dir=Path.home()
    user_dir=str(home_dir)+'/ortealbilling_data'     #change this address application wise 
    wd=user_dir + '/udat'
    mdb_pathname= wd + '/miscellaneous.db' 
    #print (self.pathname)   
            
    if not os.path.exists(wd): # check folder exist, if not create
        os.makedirs(wd)    

    #userdatapath=projectdirectory + '/userdata'
    #if not os.path.exists(userdatapath):
    #    os.makedirs(userdatapath)
    #    print('User data missing, new folder created')           
            
    miscdb= pickledb.load(mdb_pathname, False)
    miscdb_checkpresence=miscdb.get('checkpresence')
    if miscdb_checkpresence==False: 
        print ('Not found miscdb on disk, creating it')
        miscdb.set('checkpresence', 'present')    
        miscdb.set('itemgroups', ['none'])
        miscdb.set('taxontaxslabslist', stddata.taxontax_list_std)
        miscdb.set('taxontaxslabsdata', stddata.taxontax_data_std)    
        miscdb.set('statelisthome', stddata.statelist_india_std)    
        miscdb.set('statecodesgsthome', stddata.statecodesgst_india_std)        
        miscdb.set('roundoffenabled', 'yes')
        miscdb.set('autoinvoice_numbering', 'no')
        miscdb.set('hidepurchasedata', 'no')
        miscdb.set('invoiceprefix', '')
        miscdb.set('termsline1', 'Some terms')
        miscdb.set('termsline2', '')
        miscdb.set('termsline3', '')
        miscdb.set('termsline4', '')
        miscdb.set('termsline5', '')
        miscdb.set('mybankaccountnmbr', '')
        miscdb.set('mybankifsc', '')
        miscdb.set('mybankname', '')
        cystr=str(datetime.now().year)
        cyint=int(datetime.now().year)
        cmint=int(datetime.now().month)
        if cmint<4:
            fydef=str(cyint-1)+'-'+cystr
        else:
            fydef=cystr+"-"+str(cyint+1)
        miscdb.set('currentfinancialyear', fydef)
        miscdb.set('numberofinvcopies', '3')
        
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
            print ('Loaded miscdb from disk')


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
        companies_colheadingslist=['name', 'gst', 'cemer', 'csbac', 'csbifsc', 'csbname', 'csbaddi', 'creationdate', 'address',  'city', 'state', 'country', 'pin', 'companyphone', 'person', 'personmobile', 'email', 'website', 'bankaccount', 'bankifsc', 'bankname', 'bankupi', 'distance', 'focusbusiness', 'comments', 'flag', 'discount', 'creditlimit', 'paymentindays',  'instapay', 'blacklisted'] 
        companytableins.setcolumnheadings(companies_colheadingslist)
        #print('companies table column headings not found, created')  
        
    elif tmp_companytable_colheadingslength==31:               
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
        invoice_colheadingslist=[ 'invoicename','softwareversion', 'invoicenumber', 'invoicedate', 'invoicetime', 'fy', 'invoicetype', 'sourcecompany', 'sourceaddress', 'sourcepin', 'sourcephone', 'sourceemail', 'sourcetaxid', 'originstate', 'originstatecode', 'reversecharge', 'ewaybill', 'ponumber', 'toparty', 'partyaddress', 'partypin', 'partyphone',  'partytaxid', 'partystate', 'partystatecode', 'shippingname', 'shippingaddress', 'shippingpin', 'shippingphone', 'shippingstate', 'shippingstatecode', 'transportmode', 'paymentmode', 'terms', 'taxslab', 'firsttaxenabled', 'secondtaxenabled', 'thirdtaxenabled', 'firsttaxname', 'secondtaxname', 'thirdtaxname', 'firsttaxrate', 'secondtaxrate', 'thirdtaxrate', 'totaltaxrate',  'taxontaxslab', 'firsttotenabled', 'secondtotenabled', 'thirdtotenabled','firsttotname', 'secondtotname', 'thirdtotname', 'firsttotrate', 'secondtotrate', 'thirdtotrate', 'totaltotrate', 'invoicecomments', 'basicamount', 'amountdiscount', 'freight', 'othercharges', 'taxamount', 'firsttaxamount', 'secondtaxamount', 'thirdtaxamount', 'taxontaxamount', 'firsttotamount', 'secondtotamount', 'thirdtotamount', 'roundoffenabled', 'roundoffamount', 'grandamount',  'numberofitems', 'inamelist', 'iqtylist', 'isplist', 'idiscountlist','iamountlist', 'iclist', 'ihsnlist', 'iunitlist', 'taxableamount', 'misc', 'futureslot', 'rsim', 'emer']
        
            #sversion (storageversion) necessary in case format-tax changes in future, this can provide compatibility
            #invoice type is selling or purchase
            #invoice name is key value which is combination of inv number plus invoice date plus sourcecompany
        invoicetableins.setcolumnheadings(invoice_colheadingslist)
        #print('invoice table column headings not found, created')  
        
    elif tmp_invoicetable_colheadingslength==86:               
        #print ('Already set column headings for invoice table')
        pass
        
    else:
        print('need to inspect invoice table column headings')
    
    cfy= str(miscdb.get('currentfinancialyear'))
    statementstableins.loaddata('statements'+cfy)
    tmp_statementstable_colheadingslength=len(statementstableins.getcollist())
    if tmp_statementstable_colheadingslength==0:           
        statements_colheadingslist=['partyname', 'edate', 'vnumber', 'debitamount', 'creditamount', 'typetransaction', 'emonth', 'eyear', 'sortpriority', 'comments', 'misc']
       
        statementstableins.setcolumnheadings(statements_colheadingslist)
        #print('statements table column headings not found, created')  
    elif tmp_statementstable_colheadingslength==11:               
        #print ('Already set column headings for statements table')
        pass
        
    else:
        print('need to inspect statements table column headings')
        #print(tmp_statementstable_colheadingslength)
    
    
 
      
