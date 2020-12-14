# This file contains mechanism for printing sale invoice

from submods import functions
from submods import fpdfclass
from submods import guicommon

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
        document.set_draw_color(190, 9, 30)
        # border color, used for all drawing operations (lines, rectangles and cell borders)
        print('Initialized pdf printing')
        return document
        

    def printable_saleinvoice (self, invoicedate, invoicenumber, invoicedata_temp):
        invoiceid=invoicedate+"_"+invoicenumber
        invoice_filename=invoiceid+ '.pdf'
        invoice_output='udat/' + invoice_filename
        #print(invoice_output)
        
        document=self.some_initialisations()    
        #txt message  will displayed on pdf page  at the center.
        document.cell(w=0, h= 5.5, txt="Line 1:  Target 37 lines at 11 font", fill=True, ln=1, align="C")
        #Align is wrt cell, not page or margins
        #ln Indicates where current position should go after call. Possible values are:0- to the right, 1- beginning of next line, 2: below
        document.cell(w=0, h= 5.5, txt="Line 2: Some texi here to see line spacing.", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 3: gsgsg  hskjhs khksh ksks  wggs hgsss", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 4: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 5: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 6: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 7: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 8: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 9: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 10: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 11: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 12: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 13: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 14: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 15: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 16: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 17: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 18: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 19: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 20: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 21: Some texi here to see line spacing.", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 22: Some texi here to see line spacing.", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 23: gsgsg  hskjhs khksh ksks  wggs hgsss", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 24: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 25: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 26: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 27: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 28: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 29: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 30: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 31: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 32: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 33: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 34: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 35: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 36: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 37: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 38: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 39: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 40: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 41: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 42: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 43: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 44: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 45: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 46: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 47: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 48: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 49: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.cell(w=0, h=5.5, txt="Line 50: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        #document.cell(w=0, h=5.5, txt="Line 51: yuwoihs aoias saoiwp s iwj sa hdfgfgb yty hf gh", fill=True, ln=1, align="C")
        document.output(invoice_output)
        print('successfully printed')
