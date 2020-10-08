from submods import functions
from submods import guicommon
import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


def saleamounting(iamtlist):
    basicamt=0     
    for eachammount_label in iamtlist:
        if eachammount_label.get_text() =='':
            #print('blank')
            pass
        else:
            intamount_temp=float(eachammount_label.get_text())
            #print (intamount_temp)
            basicamt=basicamt+intamount_temp
    #print('Final amount')
    #print(basicamt)     
    return basicamt
    
    
def grand_saleamounting(basicamt_float, discountentry, freightentry, mischentry, estd_tax):
    grandamt=0      
    if discountentry.get_text()=='':
        discountamount_float=0
    else:
        discountamount_float= float(discountentry.get_text())  
            
    if freightentry.get_text()=='':
        freightamount_float=0
    else:
        freightamount_float= float(freightentry.get_text())   
            
    if mischentry.get_text()=='':
        mischamount_float=0
    else:
        mischamount_float= float(mischentry.get_text())    
        
    grandamt=basicamt_float-discountamount_float+freightamount_float+mischamount_float+estd_tax
    return grandamt  
    
    
def taxable_value (basicamt_float, discountentry, freightentry, mischentry):
    taxableamt=0      
    if discountentry.get_text()=='':
        discountamount_float=0
    else:
        discountamount_float= float(discountentry.get_text())  
            
    if freightentry.get_text()=='':
        freightamount_float=0
    else:
        freightamount_float= float(freightentry.get_text())   
            
    if mischentry.get_text()=='':
        mischamount_float=0
    else:
        mischamount_float= float(mischentry.get_text())    
        
    taxableamt=basicamt_float-discountamount_float+freightamount_float+mischamount_float 
    return taxableamt      
    
     
    
def processnci(nsi_header_widgets, nsi_footer_widgets, nsi_itemswidgets):

    inv_nmbr=nsi_header_widgets[0].get_text()
    inv_date=nsi_header_widgets[1].get_text()
    inv_toparty=nsi_header_widgets[2].get_text()
    inv_po=nsi_header_widgets[3].get_text()
    inv_taxslab=nsi_header_widgets[4].get_active_text()
    inv_taxontaxslab=nsi_header_widgets[5].get_active_text()
    
    inv_basicamt=nsi_footer_widgets[0].get_text()
    inv_discount=nsi_footer_widgets[1].get_text()
    inv_freight=nsi_footer_widgets[2].get_text()
    inv_othercharges=nsi_footer_widgets[3].get_text()
    inv_taxamount=nsi_footer_widgets[4].get_text()
    inv_taxontaxamount=nsi_footer_widgets[5].get_text()
    inv_grandamount=nsi_footer_widgets[6].get_text()
    
    inv_firsttax_enabled, inv_secondtax_enabled, inv_thirdtax_enabled,inv_firsttax_colname, inv_secondtax_colname, inv_thirdtax_colname, inv_firsttax_rate, inv_secondtax_rate, inv_thirdtax_rate, inv_totaltax_rate=fetch_taxslab_details(inv_taxslab)
    
    inv_iname_widgets=nsi_itemswidgets[0]
    inv_iqty_widgets=nsi_itemswidgets[1]
    inv_isp_widgets=nsi_itemswidgets[2]
    inv_idiscount_widgets=nsi_itemswidgets[3]
    inv_iamount_widgets=nsi_itemswidgets[4]
    inv_icomments_widgets=nsi_itemswidgets[5]
    
    nci_inameholder=[]
    nci_iqtyholder=[]
    nci_ispholder=[]
    nci_idischolder=[]
    nci_iamtholder=[]
    nci_icommholder=[]
    nci_ihsnholder=[]
    ifirsttax_holder=[]
    isecondtax_holder=[]
    ithirdtax_holder=[]
    
    float_inv_firsttax_rate=float(inv_firsttax_rate)
    float_inv_secondtax_rate=float(inv_secondtax_rate)
    float_inv_thirdtax_rate=float(inv_thirdtax_rate)
    i=0
    numberofitems=0
    while i<50:
        iname=inv_iname_widgets[i].get_text()
        iqty=inv_iqty_widgets[i].get_text()
        isp=inv_isp_widgets[i].get_text()
        idisc=inv_idiscount_widgets[i].get_text()
        iamt=inv_iamount_widgets[i].get_text()
        icomm=inv_icomments_widgets[i].get_text()  
                      
        
        if iname=='':
            hsn_temp=''
            ifirsttax_value=''
            isecondtax_value=''
            ithirdtax_value=''
            if numberofitems==0:
                numberofitems=str(i) #setting number of invoice items
                
            else:   
                pass 
            #print('running if block hsn')
        else:    
            hsn_temp=guicommon.itemtableins.getval(iname, "hsn")
            ifirsttax_value=float(iamt)*float_inv_firsttax_rate/100
            isecondtax_value=float(iamt)*float_inv_secondtax_rate/100
            ithirdtax_value=float(iamt)*float_inv_thirdtax_rate/100
            #print('running else block hsn')
            #print(hsn_temp)              
                
        nci_inameholder.append(iname)
        nci_iqtyholder.append(iqty)
        nci_ispholder.append(isp)
        nci_idischolder.append(idisc)
        nci_iamtholder.append(iamt)
        nci_icommholder.append(icomm)
        nci_ihsnholder.append(hsn_temp)
        ifirsttax_holder.append(ifirsttax_value)
        isecondtax_holder.append(isecondtax_value)
        ithirdtax_holder.append(ithirdtax_value)
        i=i+1
    #print (inv_nmbr)    
    #print (nci_inameholder)
    #print (nci_iqtyholder)
    #print (nci_iamtholder)
    #print ('below is hsn')
    #print (nci_ihsnholder)
    
    invid=inv_date+inv_nmbr
    softwareversion=1
    inv_time=functions.currenttime_string
    fy=guicommon.miscdbins.get('currentfinancialyear')
    invoicetype='salesinvoice'
    sourcecompany=guicommon.miscdbins.get('mycompanyname')
    
    

################### YET to implement
    inv_taxontaxname='None'
    inv_taxontaxrate='0'
    inv_comments='no invoice comments'
    roundoff='notimplemented'
#============================
    
    invoice_data=[invid, softwareversion, inv_nmbr, inv_date, inv_time, fy, invoicetype, sourcecompany, inv_toparty, inv_po, inv_taxslab, inv_firsttax_enabled, inv_secondtax_enabled, inv_thirdtax_enabled,inv_firsttax_colname, inv_secondtax_colname, inv_thirdtax_colname, inv_firsttax_rate, inv_secondtax_rate, inv_thirdtax_rate, inv_totaltax_rate,  inv_taxontaxslab, inv_taxontaxname, inv_taxontaxrate, inv_comments,  inv_basicamt, inv_discount, inv_freight, inv_othercharges, inv_taxamount, inv_taxontaxamount, roundoff, inv_grandamount,  numberofitems, nci_inameholder, nci_iqtyholder, nci_ispholder, nci_idischolder,nci_iamtholder, nci_icommholder, nci_ihsnholder, ifirsttax_holder, isecondtax_holder, ithirdtax_holder]
    
    guicommon.invoicetableins.createrow(invid, invoice_data)
    print('invoice successfully created')
    #reset fields

def applytax(taxslab):
    tax__index_temp=guicommon.taxtableins.rowlist.index(taxslab)
    taxdata_temp=guicommon.taxtableins.rowcollection[tax_index_temp]
    print (taxdata_temp)
    return taxdata_temp
    

def fetch_taxslab_details (inv_taxslab):
    tax_index_temp=guicommon.taxtableins.rowlist.index(inv_taxslab)
    taxdata_temp=guicommon.taxtableins.rowcollection[tax_index_temp]
    inv_firsttax_enabled=taxdata_temp[1]
    inv_secondtax_enabled=taxdata_temp[2]
    inv_thirdtax_enabled=taxdata_temp[3]
    inv_firsttax_colname=taxdata_temp[4]
    inv_secondtax_colname=taxdata_temp[5]
    inv_thirdtax_colname=taxdata_temp[6]
    inv_firsttax_rate=taxdata_temp[7]
    inv_secondtax_rate=taxdata_temp[8]
    inv_thirdtax_rate=taxdata_temp[9]
    inv_totaltax_rate=taxdata_temp[10]
    #print (taxdata_temp)
    return inv_firsttax_enabled, inv_secondtax_enabled, inv_thirdtax_enabled,inv_firsttax_colname, inv_secondtax_colname, inv_thirdtax_colname, inv_firsttax_rate, inv_secondtax_rate, inv_thirdtax_rate, inv_totaltax_rate


def estimatetax(taxslab_combo, basicamt_float, discountentry, freightentry, mischentry):

    taxslab_name=taxslab_combo.get_active_text()

    tax_index_temp=guicommon.taxtableins.rowlist.index(taxslab_name)
    overalltax_float=float(guicommon.taxtableins.rowcollection[tax_index_temp][10])
    #print (overalltax_float)
    
    taxable_val=taxable_value(basicamt_float, discountentry, freightentry, mischentry)
    taxamount_estd=taxable_val*overalltax_float/100
    return taxamount_estd
