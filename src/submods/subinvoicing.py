import sys
import gi
import os
import appdirs
from os.path import dirname
from pathlib import Path
from submods import functions
from submods import guicommon
from submods import guiprocessor
from submods import pdfsaleinvoice
from submods import printsihandler

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk



def print_invoice(invoicedata_temp):
    
    home_dir=Path.home()
    user_dir=str(home_dir)+'/ortealbilling_data'
    wd=user_dir + '/invoices'    
    if not os.path.exists(wd):
        os.makedirs(wd)
        print('Invoices directory missing, new folder created')      
    copies=guicommon.miscdbins.get('numberofinvcopies')
    pdfsi_ins=pdfsaleinvoice.PdfSI()
    if copies==2 or copies=='2':
        pdfsi_ins.printable_saleinvoice(invoicedata_temp[0], invoicedata_temp, 'Original for recipient', 'Original', wd)    
        pdfsi_ins.printable_saleinvoice(invoicedata_temp[0], invoicedata_temp, 'Duplicate for supplier', 'Duplicate', wd)  
    else:
        pdfsi_ins.printable_saleinvoice(invoicedata_temp[0], invoicedata_temp, 'Original for recipient', 'Original', wd)    
        pdfsi_ins.printable_saleinvoice(invoicedata_temp[0], invoicedata_temp, 'Duplicate for transporter', 'Duplicate', wd)  
        pdfsi_ins.printable_saleinvoice(invoicedata_temp[0], invoicedata_temp, 'Triplicate for supplier', 'Triplicate', wd)  
        
        
