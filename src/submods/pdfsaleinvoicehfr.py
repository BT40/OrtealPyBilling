# This file contains mechanism for printing sale invoice

from submods import functions
from submods import guicommon
from submods import checkersalepdf
from submods import amountwords
from fpdf import FPDF


class Pdfsihfr():        

    def create_header (self, invoicedata_temp, document, copyname):

        document.set_font('Times', '', 11)      
        document.cell(w=70)   # Move curser to the right using blank cell
        document.cell(w=30, h= 5.5, txt='TAX INVOICE', border= 0, ln=0, align='L', fill=False) #left aligned acc to cell
        document.cell(w=0, h= 5.5, txt=copyname, border= 0, ln=1, align='R', fill=False) 

        longmyname=invoicedata_temp[7]
        allsmallcapability_myname=30
        lettercapability_myname=checkersalepdf.calc_letters_accomodation_myname(longmyname, allsmallcapability_myname)
        
        if len(longmyname)>lettercapability_myname:
        
            lineone_myname=longmyname[0:lettercapability_myname]
            linetwo_myname=longmyname[lettercapability_myname:]
  
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
        document.cell(w=60, h= 5.5, txt=pos, border='LB', fill=False, ln=0, align="L")
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
        if invoicedata_temp[35]=='n':
            ftax_label=''
            ftax_amt='' 
        else:    
            ftax_label=str(invoicedata_temp[38]) + '@' + str(invoicedata_temp[41]) + '%'
            ftax_amt=str(invoicedata_temp[62])
        document.cell(w=53, h= 5.4, txt=str(ftax_label), border='L', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=ftax_amt, border='R', fill=False, ln=1, align="R")
        
        document.cell(w=85, h= 5.4, txt=str(inv_terms[4]), border='LR', fill=False, ln=0, align="L")
        #second tax
        if invoicedata_temp[36]=='n':
            stax_label=''
            stax_amt='' 
        else:    
            stax_label=str(invoicedata_temp[39]) + '@' + str(invoicedata_temp[42]) + '%'
            stax_amt=str(invoicedata_temp[63])
        document.cell(w=53, h= 5.4, txt=str(stax_label), border='L', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=stax_amt, border='R', fill=False, ln=1, align="R")
        
        document.cell(w=85, h= 5.4, txt=str(inv_terms[5]), border='LR', fill=False, ln=0, align="L")
        # third tax
        if invoicedata_temp[37]=='n':
            ttax_label='' 
            ttax_amt=''  
        else:    
            ttax_label=str(invoicedata_temp[40]) + '@' + str(invoicedata_temp[43]) + '%'
            ttax_amt=str(invoicedata_temp[64])
        document.cell(w=53, h= 5.4, txt=str(ttax_label), border='L', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=ttax_amt, border='R', fill=False, ln=1, align="R")
        
        bank_ac="Bank Ac no: " + str(inv_terms[6])
        if len(bank_ac)<16:
            bank_ac=''
        document.cell(w=85, h= 5.4, txt=bank_ac, border='LR', fill=False, ln=0, align="L")
        #first tax on tax       
        if invoicedata_temp[46]=='n':
            ftot_label=''
            ftot_amt=''
        else:     
            ftot_label=str(invoicedata_temp[49]) + '@' + str(invoicedata_temp[52]) + '%'
            ftot_amt=str(invoicedata_temp[66])
        document.cell(w=53, h= 5.4, txt=str(ftot_label), border='L', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=ftot_amt, border='R', fill=False, ln=1, align="R")       
        
        bankifsc="IFSC: " + str(inv_terms[7])
        if len(bankifsc)<10:
            bankifsc=''
        document.cell(w=85, h= 5.4, txt=bankifsc, border='LR', fill=False, ln=0, align="L")
        #second tax on tax
        if invoicedata_temp[47]=='n':
            stot_label=''
            stot_amt=''
        else:    
            stot_label=str(invoicedata_temp[50]) + '@' + str(invoicedata_temp[53]) + '%'
            stot_amt=str(invoicedata_temp[67])
        document.cell(w=35, h= 5.4, txt=str(stot_label), border='L', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=stot_amt, border='R', fill=False, ln=1, align="R")
        
        bankname=str(inv_terms[8])
        if len(bankname)<2:
            bankname=''
        document.cell(w=85, h= 5.4, txt=bankname, border='LR', fill=False, ln=0, align="L")
        # third tax on tax
        if invoicedata_temp[48]=='n':
            ttot_label=''
            ttot_amt=''
        else:    
            ttot_label=str(invoicedata_temp[51]) + '@' + str(invoicedata_temp[54]) + '%'
            ttot_amt=str(invoicedata_temp[68])
        document.cell(w=53, h= 5.4, txt=str(ttot_label), border='L', fill=False, ln=0, align="L")
        document.cell(w=0, h= 5.4, txt=ttot_amt, border='R', fill=False, ln=1, align="R")
        
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
        
        inv_grand_amount=invoicedata_temp[71]
        amwords=amountwords.amount_indian_currency(inv_grand_amount)
        if len(amwords)>48: #split in 2 lines if long
            amwords_line1=amwords[0:48] + '-'
            amwords_line2='-' + amwords[48:]
        else: #keep in one line
            amwords_line1=amwords  
            amwords_line2="" 
        #amwords='Rupees seven thousand eighty only '
        document.cell(w=85, h= 5.4, txt=amwords_line1, border='LR', fill=False, ln=0, align="L")        
        document.cell(w=0, h= 5.4, txt='', border='LR', fill=False, ln=1, align="L")
        
        document.cell(w=85, h= 5.4, txt=amwords_line2, border='LRB', fill=False, ln=0, align="L")        
        document.cell(w=0, h= 5.4, txt='Authorised signatory', border='LRB', fill=False, ln=1, align="R")
        
        
    def create_blankrow(self, document)    :
        document.cell(w=8, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
        document.cell(w=77, h= 5.4, txt='', border='LR', fill=False, ln=0, align="L")
        document.cell(w=18, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
        document.cell(w=15, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
        document.cell(w=17, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
        document.cell(w=13, h= 5.4, txt='', border='LR', fill=False, ln=0, align="C")
        document.cell(w=22, h= 5.4, txt='', border='LR', fill=False, ln=1, align="R")            
   
   
    def create_irow(self, document, isome, invoicedata_temp, checker, lettercapability):
    
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
              
            iname_one=iname_temp[0:lettercapability]
            iname_two=iname_temp[lettercapability:]
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
               
  
