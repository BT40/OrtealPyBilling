#to use this, install fpdf package by "pip3 install fpdf".

from fpdf import FPDF

class PDFD(FPDF):

    def header(self):
        self.set_font('Times', '', 11)
        # Move to the right
        self.cell(w=65)
        self.cell(w=30, h= 5.5, txt='TAX INVOICE', border= 0, ln=0, align='L', fill=False) #left aligned acc to cell
        self.cell(w=0, h= 5.5, txt='Original for recipient', border= 0, ln=1, align='R', fill=False) 
        
    #def footer(self):
        
        #self.set_y(-15) # Go to 1.5 cm from bottom
        # Select Arial 8
        #self.set_font('Times', '', 11) # Empty second parameter indicates normal, that is not bold, not underline (B, U capital)
        # Print centered page number
        #self.cell(0, 5.5, 'Page %s' % self.page_no(), 0, 1, 'C')

