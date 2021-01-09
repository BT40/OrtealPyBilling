from submods import functions
from submods import guicommon
import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


def saleamounting(iamtlist):
    basicamt_raw=0     
    for eachammount_label in iamtlist:
        if eachammount_label.get_text() =='':
            #print('blank')
            pass
        else:
            intamount_temp=float(eachammount_label.get_text())
            #print (intamount_temp)
            basicamt_raw=basicamt_raw+intamount_temp
    basicamt_final=round( basicamt_raw, 2)
    #print('Final amount')
    #print(basicamt_final)     
    return basicamt_final   
        
    
def taxable_value (basicamt_float, discountentry, mischentry):
    taxableamt=0      
    if discountentry.get_text()=='':
        discountamount_float=0
    else:
        discountamount_float= float(discountentry.get_text())  
            
            
    if mischentry.get_text()=='':
        mischamount_float=0
    else:
        mischamount_float= float(mischentry.get_text())    
        
    taxableamt=basicamt_float-discountamount_float+mischamount_float 
    return taxableamt          
     

def estimatetax(taxslab_combo, basicamt_float, discountentry, mischentry):

    taxslab_name=taxslab_combo.get_active_text()

    tax_index_temp=guicommon.taxtableins.rowlist.index(taxslab_name)
    overalltax_float=float(guicommon.taxtableins.rowcollection[tax_index_temp][10])
    #print (overalltax_float)
    
    taxable_val=taxable_value(basicamt_float, discountentry, mischentry)
    taxamount_estd=taxable_val*overalltax_float/100
    return taxamount_estd, taxable_val
    
    
def estimate_taxontax(taxontaxslab_combo, taxamount_float):

    taxontaxslab_name=taxontaxslab_combo.get_active_text()
    tot_index_temp=guicommon.taxontax_list.index(taxontaxslab_name)
    overalltaxontax_float=float(guicommon.taxontax_data[tot_index_temp][10])
    #print (overalltax_float)    
    taxontaxamount_estd=taxamount_float*overalltaxontax_float/100
    #print(taxontaxamount_estd)
    return taxontaxamount_estd    
    
    
def grand_saleamounting(basicamt_float, discountentry, mischentry, estd_tax, estd_taxontax, roundoff_enabled, roundoff_amt_float):
    grandamt=0      
    
    if discountentry.get_text()=='':
        discountamount_float=0
    else:
        discountamount_float= float(discountentry.get_text())  
            
    
    if mischentry.get_text()=='':
        mischamount_float=0
    else:
        mischamount_float= float(mischentry.get_text())  
 
  
    if roundoff_enabled =='no':
        grandamt_raw=basicamt_float-discountamount_float+mischamount_float+estd_tax+estd_taxontax
 

        grandamt=round(grandamt_raw, 2) #2 decimal places
        roundoff_amt_float=0.00
        
    elif roundoff_enabled =='yes':    
        grandamt_raw=basicamt_float-discountamount_float+mischamount_float+estd_tax+estd_taxontax


        grandamt=round(grandamt_raw) #integer rounding
        roundoff_amt_float=round( (grandamt_raw-grandamt) , 2)
    else:
        print('something went wrong in roundoff if-else')    

    #print('grand calculation complete')
    return grandamt, roundoff_amt_float 

    
def processnci(ssignaltype, nsi_header_widgets, nsi_footer_widgets, nsi_oth_val, nsi_itemswidgets, nsi_taxable_amount, roundoff_enabled, roundoff_amt_float ): #signal type whether to edit to create new

    inv_nmbr=nsi_header_widgets[0].get_text()
    inv_date=nsi_header_widgets[1].get_text()
    inv_toparty=nsi_header_widgets[2].get_text()
    inv_po=nsi_header_widgets[3].get_text()
    inv_taxslab=nsi_header_widgets[4].get_active_text()
    inv_taxontaxslab=nsi_header_widgets[5].get_active_text()
    
    inv_basicamt=nsi_footer_widgets[0].get_text()
    inv_discount=nsi_footer_widgets[1].get_text()
    placeofsupply=nsi_footer_widgets[2].get_text()
    inv_othercharges=nsi_footer_widgets[3].get_text()
    payment_mode=nsi_footer_widgets[4].get_text()
    inv_taxamount=nsi_footer_widgets[5].get_text()
    inv_taxontaxamount=nsi_footer_widgets[6].get_text()
    inv_grandamount=nsi_footer_widgets[7].get_text()
    transport_mode=nsi_footer_widgets[8].get_text()
    
    inv_comments=nsi_oth_val[0]
    
    ewaybill_nmbr=nsi_oth_val[2]
    furtherterms=nsi_oth_val[3]
    #print(ewaybill_nmbr)
    #print(furtherterms)
    #print('above eway, further term')
    reverse_charge=nsi_oth_val[9]
    
    sourcecompany=guicommon.miscdbins.get('mycompanyname')
    
    sourceaddress, sourcepin, sourcephone, sourceemail, sourcetaxid, originstate, originstatecode, partyaddress, partypin, partyphone, partytaxid, partystate, partystatecode = get_company_details(sourcecompany, inv_toparty)  
    
    if nsi_oth_val[10]=='yes': #more opened is yes
        handovername=nsi_oth_val[4]
        shippingaddress=nsi_oth_val[5]
        shippingpin=nsi_oth_val[8]
        shippingphone=nsi_oth_val[7]
        shippingstate=nsi_oth_val[6]
        shippingstatecode='na'
        
    else: #more not opened, use default  
        handovername=inv_toparty
        shippingaddress=partyaddress
        shippingpin=partypin
        shippingphone=partyphone
        shippingstate=partystate
        shippingstatecode=partystatecode
    
    tl1=guicommon.miscdbins.get('termsline1')
    tl2=guicommon.miscdbins.get('termsline2')
    tl3=guicommon.miscdbins.get('termsline3')
    tl4=guicommon.miscdbins.get('termsline4')
    tl5=guicommon.miscdbins.get('termsline5')
    terms=[tl1, tl2, tl3, tl4, tl5, furtherterms]
    amount_words='Implement One lac sixty six thousand five hundred sixty nine only'
    
    inv_firsttax_enabled, inv_secondtax_enabled, inv_thirdtax_enabled,inv_firsttax_colname, inv_secondtax_colname, inv_thirdtax_colname, inv_firsttax_rate, inv_secondtax_rate, inv_thirdtax_rate, inv_totaltax_rate=fetch_taxslab_details(inv_taxslab)
    
    inv_firsttot_enabled, inv_secondtot_enabled, inv_thirdtot_enabled,inv_firsttot_name, inv_secondtot_name, inv_thirdtot_name, inv_firsttot_rate, inv_secondtot_rate, inv_thirdtot_rate, inv_totaltot_rate=fetch_totslab_details(inv_taxontaxslab)
    
    inv_firsttotamount=round(float(inv_taxamount)*float(inv_firsttot_rate)/100 , 2)
    inv_secondtotamount=float(inv_taxamount)*float(inv_secondtot_rate)/100
    inv_thirdtotamount=float(inv_taxamount)*float(inv_thirdtot_rate)/100
    
    inv_iname_widgets=nsi_itemswidgets[0]
    inv_iqty_widgets=nsi_itemswidgets[1]
    inv_isp_widgets=nsi_itemswidgets[2]
    inv_idiscount_widgets=nsi_itemswidgets[3]
    inv_ic_widgets=nsi_itemswidgets[4]
    inv_iamount_widgets=nsi_itemswidgets[5]    
    
    nci_inameholder=[]
    nci_iqtyholder=[]
    nci_ispholder=[]
    nci_idischolder=[]
    nci_iamtholder=[]
    nci_icholder=[''] #remove blank quotes when this feature is enabled
    nci_ihsnholder=[]
    nci_iunitholder=[]
    ifirsttax_holder=[]
    isecondtax_holder=[]
    ithirdtax_holder=[]
    
    float_inv_firsttax_rate=float(inv_firsttax_rate)
    float_inv_secondtax_rate=float(inv_secondtax_rate)
    float_inv_thirdtax_rate=float(inv_thirdtax_rate)
    
    inv_firsttaxamount=nsi_taxable_amount*float_inv_firsttax_rate/100
    inv_secondtaxamount=nsi_taxable_amount*float_inv_secondtax_rate/100    
    inv_thirdtaxamount=nsi_taxable_amount*float_inv_thirdtax_rate/100
    
    
    i=0
    numberofitems=0
    while i<25:
        iname=inv_iname_widgets[i].get_text()
        iqty=inv_iqty_widgets[i].get_text()
        isp=inv_isp_widgets[i].get_text()
        idisc=inv_idiscount_widgets[i].get_text()
        iamt=inv_iamount_widgets[i].get_text()
        #ic=inv_ic_widgets[i].get_text()  
                      
        
        if iname=='':
            hsn_temp=''
            #ifirsttax_value=''  #If each item tax value needed
            #isecondtax_value=''  #If each item tax value needed
            #ithirdtax_value=''  #If each item tax value needed
            if numberofitems==0:
                numberofitems=str(i) #setting number of invoice items
                
            else:   
                pass 
            #print('running if block hsn')
        else:    
            hsn_temp=guicommon.itemtableins.getval(iname, "hsn")
            unit_temp=guicommon.itemtableins.getval(iname, "unit")
            #ifirsttax_value=float(iamt)*float_inv_firsttax_rate/100  #If each item tax value needed
            #isecondtax_value=float(iamt)*float_inv_secondtax_rate/100  #If each item tax value needed
            #ithirdtax_value=float(iamt)*float_inv_thirdtax_rate/100  #If each item tax value needed
            #print('running else block hsn')
            #print(hsn_temp)              
                
        nci_inameholder.append(iname)
        nci_iqtyholder.append(iqty)
        nci_ispholder.append(isp)
        nci_idischolder.append(idisc)
        nci_iamtholder.append(iamt)
        #nci_icholder.append(ic)
        nci_ihsnholder.append(hsn_temp)
        nci_iunitholder.append(unit_temp)
        #ifirsttax_holder.append(ifirsttax_value) #If each item tax value needed
        #isecondtax_holder.append(isecondtax_value)  #If each item tax value needed
        #ithirdtax_holder.append(ithirdtax_value)  #If each item tax value needed
        i=i+1  
    
    
    pos_code='98'
    inv_something=''
    gst_compliances_expansion=[ '', '', '', '', '']
    invid=str(inv_date)+ ',' + str(inv_nmbr)
    softwareversion=1
    inv_time=functions.currenttime_string
    fy=guicommon.miscdbins.get('currentfinancialyear')
    invoicetype='salesinvoice'
    misc=['', '', '', '', '']    
    futureslot=''      #for future expansion
    g_fobli=['', '', '', '', ''] #distant future obligations for tax compatibily, locked currently, do not use
    rsim, emer= '', '' #do not temper with these two variables at any cost
    
    roundoff_amt=roundoff_amt_float
    roundoff_enable=roundoff_enabled    
        
    
    invoice_data=[invid, softwareversion, inv_nmbr, inv_date, inv_time, fy, invoicetype, sourcecompany, sourceaddress, sourcepin, sourcephone, sourceemail, sourcetaxid, originstate, originstatecode, reverse_charge, ewaybill_nmbr, inv_po, inv_toparty, partyaddress, partypin, partyphone,  partytaxid, partystate, partystatecode, handovername, shippingaddress, shippingpin, shippingphone, shippingstate, shippingstatecode, transport_mode, payment_mode, terms, inv_taxslab, inv_firsttax_enabled, inv_secondtax_enabled, inv_thirdtax_enabled, inv_firsttax_colname, inv_secondtax_colname, inv_thirdtax_colname, inv_firsttax_rate, inv_secondtax_rate, inv_thirdtax_rate, inv_totaltax_rate,  inv_taxontaxslab, inv_firsttot_enabled, inv_secondtot_enabled, inv_thirdtot_enabled,inv_firsttot_name, inv_secondtot_name, inv_thirdtot_name, inv_firsttot_rate, inv_secondtot_rate, inv_thirdtot_rate, inv_totaltot_rate, inv_comments,  inv_basicamt, inv_discount, inv_something, inv_othercharges, inv_taxamount, inv_firsttaxamount, inv_secondtaxamount, inv_thirdtaxamount, inv_taxontaxamount, inv_firsttotamount, inv_secondtotamount, inv_thirdtotamount, roundoff_enable, roundoff_amt, inv_grandamount,  numberofitems, nci_inameholder, nci_iqtyholder, nci_ispholder, nci_idischolder,nci_iamtholder, nci_icholder, nci_ihsnholder, nci_iunitholder, nsi_taxable_amount, placeofsupply, pos_code, misc, gst_compliances_expansion, futureslot, g_fobli, rsim, emer]
    
    if ssignaltype=='edit':
        guicommon.invoicetableins.editrow(invid, invoice_data)
        #print('invoice successfully modified')
    else:
        guicommon.invoicetableins.createrow(invid, invoice_data)
        #print('invoice successfully created')
            
    #reset fields
    #print(invoice_data)
    return invoice_data

def applytax(taxslab):
    tax__index_temp=guicommon.taxtableins.rowlist.index(taxslab)
    taxdata_temp=guicommon.taxtableins.rowcollection[tax_index_temp]
    #print (taxdata_temp)
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
    
    
def fetch_totslab_details (inv_taxontaxslab):
    tot_index_temp=guicommon.taxontax_list.index(inv_taxontaxslab)
    totdata_temp=guicommon.taxontax_data[tot_index_temp]
    inv_firsttot_enabled=totdata_temp[1]
    inv_secondtot_enabled=totdata_temp[2]
    inv_thirdtot_enabled=totdata_temp[3]
    inv_firsttot_name=totdata_temp[4]
    inv_secondtot_name=totdata_temp[5]
    inv_thirdtot_name=totdata_temp[6]
    inv_firsttot_rate=totdata_temp[7]
    inv_secondtot_rate=totdata_temp[8]
    inv_thirdtot_rate=totdata_temp[9]
    inv_totaltot_rate=totdata_temp[10]
    #print (totdata_temp)
    return inv_firsttot_enabled, inv_secondtot_enabled, inv_thirdtot_enabled,inv_firsttot_name, inv_secondtot_name, inv_thirdtot_name, inv_firsttot_rate, inv_secondtot_rate, inv_thirdtot_rate, inv_totaltot_rate 
    
    
def get_company_details (sourcecompany, inv_toparty):
    supplier_name=guicommon.miscdbins.get('mycompanyname')
    supplier_address=guicommon.miscdbins.get('mycompanyaddress')
    supplier_gst=guicommon.miscdbins.get('mycompanygstin')
    supplier_pin=guicommon.miscdbins.get('mycompanycity') + ', ' + guicommon.miscdbins.get('mycompanypin') 
    supplier_state=guicommon.miscdbins.get('mycompanystate')
    supplier_statecode=guicommon.miscdbins.get('mycompanystatecode')
    supplier_phone=guicommon.miscdbins.get('mycompanyphone')
    supplier_email=guicommon.miscdbins.get('mycompanyemail')
    
    customer_details=guicommon.companytableins.readrow(inv_toparty)
    customer_name=customer_details[0]
    customer_address=customer_details[8]
    customer_gst=customer_details[1]
    customer_pin=customer_details[9] + ', ' + customer_details[12]
    customer_state=customer_details[10]
    customer_statecode='1220'
    customer_phone=customer_details[13]
    
    return supplier_address, supplier_pin, supplier_phone, supplier_email, supplier_gst, supplier_state, supplier_statecode, customer_address, customer_pin, customer_phone, customer_gst, customer_state, customer_statecode 
    


