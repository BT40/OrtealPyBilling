# This file contains mechanism for printing sale invoice
import sys
import os
import signal
from submods import functions
from submods import fpdfclass
from submods import guicommon
from submods import checkersalepdf
from submods import pdfsaleinvoicehfr as phf
from fpdf import FPDF


class PdfSI():
      
    def some_initialisations(self):
        document=fpdfclass.PDFD (orientation = 'P', unit = 'mm', format='A4')
        document.set_title("Tax invoice-Original")
        document.set_margins(20, 20, 20) # left, top, right...... Define before creating page, otherwise will ruin formatting
        
        #Libreoffice ref: 11pt=3.88mm, 48 lines @1.2, 50 lines @1.15, 38 lines @1.5 line spacing
        # big character to font height is 75% approx. 
        #space to char ht: 89%, 99%, 75%, 153% respectively for 1.15, 1.2, 1 and 1.5 line spacing
        #net char height for 11pt is 3.88*.75=2.91 mm
        #net space height for 11pt is 2.59 @1.15, 2.88 @1.2, 2.18 @1, 4.45 @1.5
        # cell ht: 5.5 @1.15, 5.8 @1.2, 5.1 @1, 7.35 @1.5 

        #There is no page for the moment, so we have to add one with add_page. 
        document.add_page()
        document.set_font("Times", size=11)
        document.set_text_color(20, 20, 20)        
        document.set_fill_color(255, 255, 255)
        # cell fill colour, visible if cell property fill set to true
        document.set_draw_color(175, 175, 175)
        # border color, used for all drawing operations (lines, rectangles and cell borders)
        return document
        

    def printable_saleinvoice (self, invoiceid, invoicedata_temp):
        
        if not os.path.exists('invoices'): # check folder exist, if not create
            os.makedirs('invoices')
        invoice_filename=invoiceid+ '.pdf'
        invoice_output='invoices/' + invoice_filename
        
        document=self.some_initialisations()    
        self.pagecount=1

        #Align is wrt cell, not page or margins
        #ln Indicates where current position should go after call. Possible values are:0- to the right, 1- beginning of next line, 2: below
        
        hfi=phf.Pdfsihfr()
        hfi.create_header (invoicedata_temp, document)
        
        document.set_font("Times", size=11)
        # invoice items
        isome, activerows, rowcapability_current, items_remaining, items_reqd=0, 0, 17, int(invoicedata_temp[72]), int(invoicedata_temp[72])
        proceed_signal='yes'
        
        while proceed_signal=='yes':
            #print(isome)
            checker=checkersalepdf.item_lines_reqd(invoicedata_temp, isome)                       
            rows_consumed =hfi.create_irow(document, isome, invoicedata_temp, checker)            
            activerows=activerows+rows_consumed   
            rowcapability_current=rowcapability_current-rows_consumed
            items_remaining=items_remaining-1
            isome=isome+1
            aloop_limit_p1=min(rowcapability_current, items_remaining) #aloop is activeloop for page 1
            
            if aloop_limit_p1==0:
                proceed_signal='no'
            
            elif aloop_limit_p1>0:
                temp_next_row_size=checkersalepdf.item_lines_reqd(invoicedata_temp, isome)
                if temp_next_row_size>rowcapability_current:
                    proceed_signal='no' #two rows needed but one available
                    document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                    document.cell(w=77, h= 5.4, txt='Continued on next page', border='LR', fill=False, ln=0, align="L")
                    document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                    document.cell(w=15, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                    document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                    document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                    document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")    
                    rows_consumed=1
                    activerows=activerows+rows_consumed    
                    rowcapability_current=rowcapability_current-rows_consumed    
                elif rowcapability_current==2:
                    if temp_next_row_size==2 and items_remaining>1: #two items remain, first one will occup two
                        proceed_signal='no' #two rows needed but one available
                        document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=77, h= 5.4, txt='Continued on next page', border='LR', fill=False, ln=0, align="L")
                        document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=15, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")    
                        rows_consumed=1
                        activerows=activerows+rows_consumed    
                        rowcapability_current=rowcapability_current-rows_consumed        
                
                elif rowcapability_current==1:
                    if temp_next_row_size==1 and items_remaining>1: #two items remain, one line to go
                        proceed_signal='no' #more rows needed but one available
                        document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=77, h= 5.4, txt='Continued on next page', border='LR', fill=False, ln=0, align="L")
                        document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=15, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")    
                        rows_consumed=1
                        activerows=activerows+rows_consumed    
                        rowcapability_current=rowcapability_current-rows_consumed        
                
                else:
                    proceed_signal='yes'                
        
        howmany_blankrows=rowcapability_current  
        ianot=0
        while ianot<(howmany_blankrows):
            hfi.create_blankrow(document)
            ianot=ianot+1    
        
        hfi.create_footer (invoicedata_temp, document)   
        
        # second page mechanism starts here
        if items_remaining>0:
            #print('another page reqd')
            self.pagecount=2             
       
        if self.pagecount==2:
            document.add_page()
            hfi.create_header (invoicedata_temp, document)            
            document.set_font("Times", size=11)
            # invoice items page 2
            activerows2, rowcapability_current2= 1, 16
            
            document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=77, h= 5.4, txt='Continued from page 1', border='LR', fill=False, ln=0, align="L")
            document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=15, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")   
             
            proceed_signal='yes'
            
            while proceed_signal=='yes':

                checker=checkersalepdf.item_lines_reqd(invoicedata_temp, isome)                
                rows_consumed =hfi.create_irow(document, isome, invoicedata_temp, checker)               
                activerows2=activerows2+rows_consumed                
                rowcapability_current2=rowcapability_current2-rows_consumed
                #print(rowcapability_current2)
                items_remaining=items_remaining-1
                isome=isome+1
                aloop_limit_p2=min(rowcapability_current2, items_remaining) #aloop is activeloop for page 2
                
                if aloop_limit_p2==0:
                    proceed_signal='no'
            
                elif aloop_limit_p1>0:
                    temp_next_row_size=checkersalepdf.item_lines_reqd(invoicedata_temp, isome)
                    if temp_next_row_size>rowcapability_current2:
                        proceed_signal='no' #two rows needed but one available
                        document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=77, h= 5.4, txt='Continued on next page', border='LR', fill=False, ln=0, align="L")
                        document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=15, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")    
                        rows_consumed=1
                        activerows2=activerows2+rows_consumed    
                        rowcapability_current2=rowcapability_current2-rows_consumed    
                elif rowcapability_current2==2:
                    if temp_next_row_size==2 and items_remaining>1: #two items remain, first one will occup two
                        proceed_signal='no' #two rows needed but one available
                        document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=77, h= 5.4, txt='Continued on next page', border='LR', fill=False, ln=0, align="L")
                        document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=15, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")    
                        rows_consumed=1
                        activerows2=activerows2+rows_consumed    
                        rowcapability_current2=rowcapability_current2-rows_consumed        
                
                elif rowcapability_current2==1:
                    if temp_next_row_size==1 and items_remaining>1: #two items remain, one line to go
                        proceed_signal='no' #more rows needed but one available
                        document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=77, h= 5.4, txt='Continued on next page', border='LR', fill=False, ln=0, align="L")
                        document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=15, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")    
                        rows_consumed=1
                        activerows2=activerows2+rows_consumed    
                        rowcapability_current2=rowcapability_current2-rows_consumed        
                
                else:
                    proceed_signal='yes'         
            
            howmany_blankrows=rowcapability_current2  
            ianot=0
            while ianot<(howmany_blankrows):
                hfi.create_blankrow(document)
                ianot=ianot+1    
            
            hfi.create_footer (invoicedata_temp, document)   
        
        # third page mechanism starts here
        if items_remaining>0:
            #print('another page reqd')
            self.pagecount=3             
       
        if self.pagecount==3:
            document.add_page()
            hfi.create_header (invoicedata_temp, document)            
            document.set_font("Times", size=11)
            # invoice items page 3
            activerows3, rowcapability_current3= 1, 16
            
            document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=77, h= 5.4, txt='Continued from page 2', border='LR', fill=False, ln=0, align="L")
            document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=15, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")   
             
            proceed_signal='yes'
            
            while proceed_signal=='yes':

                checker=checkersalepdf.item_lines_reqd(invoicedata_temp, isome)                
                rows_consumed =hfi.create_irow(document, isome, invoicedata_temp, checker)               
                activerows3=activerows3+rows_consumed                
                rowcapability_current3=rowcapability_current3-rows_consumed
                #print(rowcapability_current3)
                items_remaining=items_remaining-1
                isome=isome+1
                aloop_limit_p3=min(rowcapability_current3, items_remaining) #aloop is activeloop for page 3
                
                if aloop_limit_p3==0:
                    proceed_signal='no'
            
                elif aloop_limit_p3>0:
                    temp_next_row_size=checkersalepdf.item_lines_reqd(invoicedata_temp, isome)
                    if temp_next_row_size>rowcapability_current3:
                        proceed_signal='no' #two rows needed but one available
                        document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=77, h= 5.4, txt='Print limit reached, reduce items', border='LR', fill=False, ln=0, align="L")
                        document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=15, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")    
                        rows_consumed=1
                        activerows3=activerows3+rows_consumed    
                        rowcapability_current3=rowcapability_current3-rows_consumed    
                elif rowcapability_current3==2:
                    if temp_next_row_size==2 and items_remaining>1: #two items remain, first one will occup two
                        proceed_signal='no' #two rows needed but one available
                        document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=77, h= 5.4, txt='Printing limit reached, reduce items', border='LR', fill=False, ln=0, align="L")
                        document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=15, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")    
                        rows_consumed=1
                        activerows3=activerows3+rows_consumed    
                        rowcapability_current3=rowcapability_current3-rows_consumed        
                
                elif rowcapability_current3==1:
                    if temp_next_row_size==1 and items_remaining>1: #two items remain, one line to go
                        proceed_signal='no' #more rows needed but one available
                        document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=77, h= 5.4, txt='Print limit reached, reduce items', border='LR', fill=False, ln=0, align="L")
                        document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=15, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
                        document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")    
                        rows_consumed=1
                        activerows3=activerows3+rows_consumed    
                        rowcapability_current3=rowcapability_current3-rows_consumed        
                
                else:
                    proceed_signal='yes'         
            
            howmany_blankrows=rowcapability_current3  
            ianot=0
            while ianot<(howmany_blankrows):
                hfi.create_blankrow(document)
                ianot=ianot+1    
            
            hfi.create_footer (invoicedata_temp, document)   
               
        
            
        document.output(invoice_output)
        print('successfully printed')
        
         
        #invoice_data=[invid, softwareversion, inv_nmbr, inv_date, inv_time, fy, invoicetype, sourcecompany, sourceaddress, sourcepin, 10 sourcephone, sourceemail, sourcetaxid, originstate, originstatecode, reverse_charge, ewaybill_nmbr, inv_po, inv_toparty,partyaddress,partypin 21, partyphone,  partytaxid, partystate, partystatecode, handovername, shippingaddress,shippingpin,shippingphone,shippingstate, shippingstatecode 31, transport_mode, payment_mode, terms, inv_taxslab, inv_firsttax_enabled, inv_secondtax_enabled, inv_thirdtax_enabled, inv_firsttax_colname,39 inv_secondtax_colname, inv_thirdtax_colname, inv_firsttax_rate, inv_secondtax_rate, inv_thirdtax_rate, inv_totaltax_rate,  inv_taxontaxslab46, inv_firsttot_enabled, inv_secondtot_enabled, inv_thirdtot_enabled,inv_firsttot_name, inv_secondtot_name, inv_thirdtot_name, inv_firsttot_rate53, inv_secondtot_rate, inv_thirdtot_rate, inv_totaltot_rate, inv_comments,  inv_basicamt, inv_discount, inv_freight, inv_othercharges,61,  inv_taxamount, inv_firsttaxamount, inv_secondtaxamount, inv_thirdtaxamount, inv_taxontaxamount, inv_firsttotamount, inv_secondtotamount,68,  inv_thirdtotamount, roundoff_enable, roundoff_amt, inv_grandamount,  numberofitems, nci_inameholder, nci_iqtyholder, nci_ispholder,76, nci_idischolder,nci_iamtholder, nci_icholder, nci_ihsnholder, nci_iunitholder, nsi_taxable_amount,placeofsupply, pos_code, 84 gst_compliances_expansion, misc, futureslot, g_fobli, rsim, emer] 90
