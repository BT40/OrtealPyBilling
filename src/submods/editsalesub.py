import sys
import gi

from submods import functions
from submods import guicommon
from submods import guiprocessor

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk



def ini_other_variables(objinstant, fetched_details):
        objinstant.autoinvoice_numbering='no'
        objinstant.inv_prefix=''         
        objinstant.ewaybill=str(fetched_details[16])     
        objinstant.billcomments=str(fetched_details[56])  
        objinstant.furtherterms=str(fetched_details[33][5])                  
        objinstant.ship_name=fetched_details[25]  
        objinstant.ship_addline=(fetched_details[26])  
        objinstant.ship_state=(fetched_details[29])  
        objinstant.ship_statecode=(fetched_details[30])  
        objinstant.ship_phone=(fetched_details[28])  
        objinstant.ship_pin=(fetched_details[27])  
        objinstant.rcvalue=str(fetched_details[15])  
        objinstant.more_opened='yes'        
             
        objinstant.temp_basicamt=float(fetched_details[57])
        if fetched_details[60]=='':
            temp_othercharges=0
        else:    
            temp_othercharges=float(fetched_details[60])
            
        if fetched_details[58]=='':    
            temp_discountamt=0
        else:    
            temp_discountamt=float(fetched_details[58])
        objinstant.taxable_amount=float(fetched_details[57])+temp_othercharges-temp_discountamt
        
        if fetched_details[70]=='':
            objinstant.roundoff_amt =0
        else:    
            objinstant.roundoff_amt =float(fetched_details[70])
            
        objinstant.transmode=fetched_details[31]
        objinstant.invoicedata_temp = fetched_details

        objinstant.compchange_detector=fetched_details[18] #mechanism to detect company change after more pressed and change shipping accordingly
        
