# This file contains mechanism for printing sale invoice

from submods import functions
from submods import fpdfclass
from submods import guicommon
from submods import checkersalepdf
from fpdf import FPDF


class Pdfsihfr():        

    def create_header (self, invoicedata_temp, document):

        longmyname=invoicedata_temp[7]
        
        if len(longmyname)>33:
        
            lineone_myname=longmyname[0:32]
            linetwo_myname=longmyname[32:]
  
        else:
            lineone_myname=longmyname
            linetwo_myname=''
            
        document.set_font("Times", style='B', size=16)
        document.cell(w=85, h= 6, txt=lineone_myname, border='TLR', fill=False, ln=0, align="L")
        
        document.set_font("Times", size=11)
        inv_no='Invoice no. ' + invoicedata_temp[2]
        document.cell(w=85, h= 5.6, txt=inv_no, border='TR', fill=False, ln=1, align="L")
        
        # company name line 2
        document.set_font("Times", style='B', size=16)
        document.cell(w=85, h= 6, txt=linetwo_myname, border='LR', fill=False, ln=0, align="L")
        
        document.set_font("Times", size=11)
        inv_date='Invoice date: ' + invoicedata_temp[3]
        document.cell(w=85, h= 5.4, txt=inv_date, border='R', fill=False, ln=1, align="L")
        
        document.cell(w=85, h= 5.4, txt=invoicedata_temp[8], border='LR', fill=False, ln=0, align="L")
        
        eway='EwayBill no.: '+ invoicedata_temp[16]
        document.cell(w=85, h= 5.4, txt=eway, border='R', fill=False, ln=1, align="L")        
        
        document.cell(w=85, h= 5.4, txt=invoicedata_temp[9], border='LR', fill=False, ln=0, align="L")
        revcharge='Reverse charge: '+ invoicedata_temp[15]
        document.cell(w=85, h= 5.4, txt=revcharge, border='LR', fill=False, ln=1, align="L")
        
        myphone='Phone: '+ invoicedata_temp[10]
        document.cell(w=85, h= 5.4, txt=myphone, border='LR', fill=False, ln=0, align="L")       
        po='PO: '+ invoicedata_temp[17]
        document.cell(w=85, h= 5.4, txt=po, border='LR', fill=False, ln=1, align="L")
        
        mymail='Email: '+ invoicedata_temp[11]
        document.cell(w=85, h= 5.4, txt=mymail, border='LR', fill=False, ln=0, align="L")        
        stateoforigin='State of origin: '+ invoicedata_temp[13]
        document.cell(w=60, h= 5.4, txt=stateoforigin, border='L', fill=False, ln=0, align="L")        
        stateoricode='State code: '+ invoicedata_temp[14]
        document.cell(w=0, h= 5.4, txt=stateoricode, border='R', fill=False, ln=1, align="R")
        
        mygst='GST: '+ invoicedata_temp[12]
        document.cell(w=85, h= 5.4, txt=mygst, border='LRB', fill=False, ln=0, align="L")        

        pos = 'Place of supply: ' + str(invoicedata_temp[82])
        document.cell(w=60, h= 5.5, txt=pos, border='LRB', fill=False, ln=0, align="L")
        poscode='State code: '+ str(invoicedata_temp[83])
        document.cell(w=0, h= 5.4, txt=poscode, border='R', fill=False, ln=1, align="R")
                
        #======================================================================================
        document.set_font("Times", style='B', size=11)
        document.cell(w=85, h= 5.4, txt='Details of receiver (Billed to)', border='TLR', fill=False, ln=0, align="L")
        document.cell(w=85, h= 5.4, txt='Details of consignee (Shipped to)', border='TLR', fill=False, ln=1, align="L")
        
        document.set_font("Times", size=11)
        partyname=str(invoicedata_temp[18])
        document.cell(w=85, h= 5.4, txt=partyname, border='LR', fill=False, ln=0, align="L")        
        #shipped to name
        document.cell(w=85, h= 5.4, txt=invoicedata_temp[25], border='LR', fill=False, ln=1, align="L")
        
        partyaddress=invoicedata_temp[19]
        document.cell(w=85, h= 5.4, txt=partyaddress, border='LR', fill=False, ln=0, align="L")        
        shippingaddress=invoicedata_temp[26]
        document.cell(w=85, h= 5.4, txt=shippingaddress, border='LR', fill=False, ln=1, align="L")
        #second line of address
        partycity=invoicedata_temp[20]
        document.cell(w=85, h= 5.4, txt=partycity, border='LR', fill=False, ln=0, align="L")        
        shippingcity=invoicedata_temp[27]
        document.cell(w=85, h= 5.4, txt=shippingcity, border='LR', fill=False, ln=1, align="L")
        
        partystate='State: '+ invoicedata_temp[23]
        document.cell(w=55, h= 5.4, txt=partystate, border='L', fill=False, ln=0, align="L")        
        partystatecode='State code: '+ invoicedata_temp[24]
        document.cell(w=30, h= 5.4, txt=partystatecode, border='R', fill=False, ln=0, align="R")
        shippingstate='State: '+ invoicedata_temp[29]
        document.cell(w=55, h= 5.4, txt=shippingstate, border='L', fill=False, ln=0, align="L")        
        shippingstatecode='State code: '+ invoicedata_temp[30]
        document.cell(w=30, h= 5.4, txt=shippingstatecode, border='R', fill=False, ln=1, align="R")
        
        partyphone='Phone: ' + invoicedata_temp[21]
        document.cell(w=85, h= 5.4, txt=partyphone, border='LR', fill=False, ln=0, align="L")        
        shippingphone='Phone: ' + invoicedata_temp[28]
        document.cell(w=85, h= 5.4, txt=shippingphone, border='LR', fill=False, ln=1, align="L")
        
        partygst='GSTIN: ' + invoicedata_temp[22]
        document.cell(w=85, h= 5.4, txt=partygst, border='LRB', fill=False, ln=0, align="L")        
        shippingmode='Transport mode: '+ invoicedata_temp[31]
        document.cell(w=85, h= 5.4, txt=shippingmode, border='LRB', fill=False, ln=1, align="L")
        
        #======================================================================================
        document.set_font("Times", style='B', size=11)
        document.cell(w=8, h= 5.4, txt='#', border='LRB', fill=False, ln=0, align="C")
        document.cell(w=77, h= 5.4, txt='Item description', border='LRB', fill=False, ln=0, align="C")
        document.cell(w=18, h= 5.4, txt='HSN/SAC', border='LRB', fill=False, ln=0, align="C")
        document.cell(w=15, h= 5.4, txt='Qty', border='LRB', fill=False, ln=0, align="C")
        document.cell(w=17, h= 5.4, txt='Rate', border='LRB', fill=False, ln=0, align="C")
        document.cell(w=13, h= 5.4, txt='Disc.%', border='LRB', fill=False, ln=0, align="C")
        document.cell(w=22, h= 5.4, txt='Amount', border='LRB', fill=False, ln=1, align="C" )       
        document.set_font("Times", size=11)
        
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++               
        
        
    def create_footer (self, invoicedata_temp, document):   
        
        #basic total
        document.cell(w=85, h= 5.4, txt='Terms and conditions', border='TLR', fill=False, ln=0, align="L")
        document.cell(w=53, h= 5.4, txt='Basic amount', border='TL', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=str(invoicedata_temp[57]), border='TR', fill=False, ln=1, align="R")
        
        inv_terms=invoicedata_temp[33]
        
         #terms line 1
        document.cell(w=85, h= 5.4, txt=str(inv_terms[0]), border='LR', fill=False, ln=0, align="L")
        document.cell(w=53, h= 5.4, txt='Other charges', border='L', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=str(invoicedata_temp[60]), border='R', fill=False, ln=1, align="R")
        
        document.cell(w=85, h= 5.4, txt=str(inv_terms[1]), border='LR', fill=False, ln=0, align="L")
        document.cell(w=53, h= 5.4, txt='Additional discount', border='L', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=str(invoicedata_temp[58]), border='R', fill=False, ln=1, align="R")
        
        document.cell(w=85, h= 5.4, txt=str(inv_terms[2]), border='LR', fill=False, ln=0, align="L")
        document.cell(w=53, h= 5.4, txt='Taxable value', border='L', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=str(invoicedata_temp[81]), border='R', fill=False, ln=1, align="R")        
        
        document.cell(w=85, h= 5.4, txt=str(inv_terms[3]), border='LR', fill=False, ln=0, align="L")
        #first tax
        ftax_label=str(invoicedata_temp[38]) + '@' + str(invoicedata_temp[41]) + '%'
        document.cell(w=53, h= 5.4, txt=str(ftax_label), border='L', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=str(invoicedata_temp[62]), border='R', fill=False, ln=1, align="R")
        
        document.cell(w=85, h= 5.4, txt=str(inv_terms[4]), border='LR', fill=False, ln=0, align="L")
        #second tax
        stax_label=str(invoicedata_temp[39]) + '@' + str(invoicedata_temp[42]) + '%'
        document.cell(w=53, h= 5.4, txt=str(stax_label), border='L', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=str(invoicedata_temp[63]), border='R', fill=False, ln=1, align="R")
        
        document.cell(w=85, h= 5.4, txt=str(inv_terms[5]), border='LR', fill=False, ln=0, align="L")
        # third tax
        ttax_label=str(invoicedata_temp[40]) + '@' + str(invoicedata_temp[43]) + '%'
        document.cell(w=53, h= 5.4, txt=str(ttax_label), border='L', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=str(invoicedata_temp[64]), border='R', fill=False, ln=1, align="R")
        
        document.cell(w=85, h= 5.4, txt='', border='LR', fill=False, ln=0, align="L")
        #first tax on tax        
        ftot_label=str(invoicedata_temp[49]) + '@' + str(invoicedata_temp[52]) + '%'
        document.cell(w=53, h= 5.4, txt=str(ftot_label), border='L', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=str(invoicedata_temp[66]), border='R', fill=False, ln=1, align="R")       
        
        document.cell(w=85, h= 5.4, txt='', border='LR', fill=False, ln=0, align="L")
        #second tax on tax
        stot_label=str(invoicedata_temp[50]) + '@' + str(invoicedata_temp[53]) + '%'
        document.cell(w=35, h= 5.4, txt=str(stot_label), border='L', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=str(invoicedata_temp[67]), border='R', fill=False, ln=1, align="R")
        
        document.cell(w=85, h= 5.4, txt='', border='LR', fill=False, ln=0, align="L")
        # third tax on tax
        ttot_label=str(invoicedata_temp[51]) + '@' + str(invoicedata_temp[54]) + '%'
        document.cell(w=53, h= 5.4, txt=str(ttot_label), border='L', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=str(invoicedata_temp[68]), border='R', fill=False, ln=1, align="R")
        
        paymentmode = 'Payment mode: ' + invoicedata_temp[32]
        document.cell(w=85, h= 5.5, txt=str(paymentmode), border='TLB', fill=False, ln=0, align="L")
        #grand total       
        document.set_font("Times", style='B', size=12)
        document.cell(w=53, h= 5.5, txt='Total invoice value', border='TLB', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.5, txt=str(invoicedata_temp[71]), border='TRB', fill=False, ln=1, align="R")
        document.set_font("Times", size=11)
        
        document.cell(w=85, h= 5.4, txt='Total amount in words', border='LR', fill=False, ln=0, align="L")
        #headersign='For ' + str(invoicedata_temp[7])
        document.cell(w=0, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")
        
        #here is amount in words and sign
        amwords='One lac sixty thousand ninety only '
        document.cell(w=85, h= 5.4, txt=amwords, border='LR', fill=False, ln=0, align="L")        
        document.cell(w=0, h= 5.4, txt='', border='LR', fill=False, ln=1, align="L")
        
        amwords2='Seventy three lac sixty eight thousand ninety five only '
        document.cell(w=85, h= 5.4, txt=amwords2, border='LRB', fill=False, ln=0, align="L")        
        document.cell(w=0, h= 5.4, txt='Authorised signatory', border='LRB', fill=False, ln=1, align="R")
        
        
    def create_blankrow(self, document)    :
        document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
        document.cell(w=77, h= 5.4, txt='', border='LR', fill=False, ln=0, align="L")
        document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
        document.cell(w=15, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
        document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
        document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
        document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")    
        
   
   
    def create_irow(self, document, isome, invoicedata_temp, checker):
    
        iserial_temp=str(isome+1)
        iname_temp=str(invoicedata_temp[73][isome])
        iqtydisp_temp=str(invoicedata_temp[74][isome])+str(invoicedata_temp[80][isome])
        iprice_temp=str(invoicedata_temp[75][isome])
        idisc_temp=str(invoicedata_temp[76][isome])
        iamt_temp=str(invoicedata_temp[77][isome])
        ihsn_temp=str(invoicedata_temp[79][isome])
        iunit_temp=str(invoicedata_temp[80][isome])
        iqty_temp=str(invoicedata_temp[74][isome])
    
    
        if checker==1:      #everything is short     
            document.cell(w=8, h= 5.4, txt=iserial_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=77, h= 5.4, txt=iname_temp, border='LR', fill=False, ln=0, align="L")
            document.cell(w=18, h= 5.4, txt=ihsn_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=15, h= 5.4, txt=iqtydisp_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=17, h= 5.4, txt=iprice_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=13, h= 5.4, txt=idisc_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=22, h= 5.4, txt=iamt_temp, border='LR', fill=False, ln=1, align="R")
            
            rows_consumed=1

        elif checker==2: #only name is long
              
            iname_one=iname_temp[0:32]
            iname_two=iname_temp[32:]
            document.cell(w=8, h= 5.4, txt=iserial_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=77, h= 5.4, txt=iname_one, border='LR', fill=False, ln=0, align="L")
            document.cell(w=18, h= 5.4, txt=ihsn_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=15, h= 5.4, txt=iqtydisp_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=17, h= 5.4, txt=iprice_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=13, h= 5.4, txt=idisc_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=22, h= 5.4, txt=iamt_temp, border='LR', fill=False, ln=1, align="R")
                
            document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=77, h= 5.4, txt=iname_two, border='LR', fill=False, ln=0, align="L")
            document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=15, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")
            
            rows_consumed=2

        elif checker==3: #only qty is long            
            document.cell(w=8, h= 5.4, txt=iserial_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=77, h= 5.4, txt=iname_temp, border='LR', fill=False, ln=0, align="L")
            document.cell(w=18, h= 5.4, txt=ihsn_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=15, h= 5.4, txt=iqty_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=17, h= 5.4, txt=iprice_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=13, h= 5.4, txt=idisc_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=22, h= 5.4, txt=iamt_temp, border='LR', fill=False, ln=1, align="R")
                
            document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=77, h= 5.4, txt='', border='LR', fill=False, ln=0, align="L")
            document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=15, h= 5.4, txt=iunit_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")
            
            rows_consumed=2

        elif checker==4: #both are long
            iname_one=iname_temp[0:32]
            iname_two=iname_temp[32:]
            document.cell(w=8, h= 5.4, txt=iserial_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=77, h= 5.4, txt=iname_one, border='LR', fill=False, ln=0, align="L")
            document.cell(w=18, h= 5.4, txt=ihsn_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=15, h= 5.4, txt=iqty_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=17, h= 5.4, txt=iprice_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=13, h= 5.4, txt=idisc_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=22, h= 5.4, txt=iamt_temp, border='LR', fill=False, ln=1, align="R")
               
            document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=77, h= 5.4, txt=iname_two, border='LR', fill=False, ln=0, align="L")
            document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=15, h= 5.4, txt=iunit_temp, border='LR', fill=False, ln=0, align="C")
            document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
            document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")
             
            rows_consumed=2          
       
        return rows_consumed 
               
  
