from submods import functions
from submods import guicommon
from submods import statementprocessor
import sys
import gi
import operator

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkEditInwards():


    def generatepage(self, mainwindow):
        self.mainwindow=mainwindow
        einwmasterbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        view_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)         
        self.contentbox=self.generate_selector_box()   
        view_box.pack_start(self.contentbox, False, False, 0)       
        
        view_box.show_all()
        einwmasterbox.pack_start(view_box, False, False, True) 
          
        return einwmasterbox

    def generate_selector_box(self):                        
        sel_headerbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        
        ei_namelabel = Gtk.Label()
        ei_namelabel.set_markup("Select company name ")
       
        self.ei_nameentry = Gtk.Entry()
        self.ei_nameentry.set_width_chars(32)
        self.ei_nameentry.set_max_length(47)
        self.einame_completion = Gtk.EntryCompletion()
        self.einame_completion.set_model(guicommon.companyname_store)
        self.einame_completion.set_text_column(0)
        self.ei_nameentry.set_completion(self.einame_completion)   
        
        eindatelabel = Gtk.Label()
        eindatelabel.set_markup("Date of voucher/Ref no.")        
        self.eindate = Gtk.Entry()
        #self.eindate.set_text(functions.todaysdate_string)
        self.eindate.set_width_chars(10)
        self.eindate.set_max_length(10)
        self.eindate.set_halign(Gtk.Align.START)
        
        evoucherlabel = Gtk.Label()
        evoucherlabel.set_markup("Voucher/Ref no.")        
        self.ev = Gtk.Entry()
        self.ev.set_width_chars(24)
        self.ev.set_max_length(24)
        self.ev.set_halign(Gtk.Align.START)
        
        gridd = Gtk.Grid()
        #gridd.set_vexpand(False)
        gridd.set_margin_bottom(20)
        
        gridd.add(ei_namelabel)
        gridd.attach(self.ei_nameentry, 1, 0, 1, 1)
        gridd.attach(eindatelabel, 0, 6, 1, 1)
        gridd.attach(self.eindate, 1, 6, 1, 1)
        gridd.attach(evoucherlabel, 0, 5, 1, 1)
        gridd.attach(self.ev, 1, 5, 1, 1)
      
        buttonbox= Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        ei_editbutton = Gtk.Button.new_with_label("Modify or View")
        ei_deletebutton = Gtk.Button.new_with_label("Delete entry")
        ei_deletebutton.get_style_context().add_class("dangerbutton")
        ei_deletebutton.connect("clicked", self.delete_state_entry)
        buttonbox.pack_start(ei_editbutton, True, True, 0) 
        buttonbox.pack_start(ei_deletebutton, True, True, 0)         
        
        sel_headerbox.pack_start(gridd, False, False, 0)
        sel_headerbox.pack_start(buttonbox, False, False, 0)     
        
        return sel_headerbox    
        

    def generate_editable(self):
        inwmasterbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        
        inwheaderbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6) 
        #inwheaderbox.set_vexpand(False)
        #inwheaderbox.get_style_context().add_class("testarea") 
        
        gridd = Gtk.Grid()
        #gridd.set_vexpand(False)
        gridd.set_margin_bottom(20)
        
        forparty_label = Gtk.Label(label="Type and select party")
        forparty_label.set_width_chars(16)
        self.pnameentry = Gtk.Entry()
        self.pnameentry.set_width_chars(47)
        self.pnameentry.set_max_length(47)
        self.cname_completion = Gtk.EntryCompletion()
        self.cname_completion.set_model(guicommon.companyname_store)
        self.cname_completion.set_text_column(0)
        self.pnameentry.set_completion(self.cname_completion)  
        
        translabel = Gtk.Label(label="Select transaction")
        translabel.set_width_chars(32)
        
        
        self.tscombo = Gtk.ComboBoxText.new()
        translist=["Material purchased", "Payment received", "Credit note in" ]
        for ets in translist:
            self.tscombo.append_text(ets)        
        #self.tscombo.set_active(0)
        self.tscombo.set_hexpand(False)
        self.tscombo.set_halign(Gtk.Align.START)
        #self.tscombo.get_child().set_width_chars(24)  #if combobox new with entry
        #self.tscombo.get_child().set_max_length(24)   #if combobox new with entry
        
        amount_label = Gtk.Label(label="Amount")
        amount_label.set_width_chars(16)
        self.amountentry = Gtk.Entry()
        self.amountentry.set_width_chars(24)
        self.amountentry.set_max_length(24)
        self.amountentry.set_halign(Gtk.Align.START)
        
        indatelabel = Gtk.Label()
        indatelabel.set_markup("Date")
        
        self.indate = Gtk.Entry()
        self.indate.set_text(functions.todaysdate_string)
        self.indate.set_width_chars(10)
        self.indate.set_max_length(10)
        self.indate.set_halign(Gtk.Align.START)
        
        voucherlabel = Gtk.Label()
        voucherlabel.set_markup("Voucher/Ref no.")
        
        self.v = Gtk.Entry()
        self.v.set_width_chars(24)
        self.v.set_max_length(24)
        self.v.set_halign(Gtk.Align.START)
        
        comments_label = Gtk.Label(label="Comments")
        comments_label.set_width_chars(16)
        self.commentsentry = Gtk.Entry()
        self.commentsentry.set_width_chars(47)
        self.commentsentry.set_max_length(47)
        
        savebutton = Gtk.Button.new_with_label("Save")
        savebutton.get_style_context().add_class("suggested-action")
        savebutton.connect("clicked", self.generate_statement )
        savebutton.set_halign(Gtk.Align.CENTER) # to avoid expansion horizontally
        savebutton.get_child().set_width_chars(6)
        #savebutton.set_margin_left(20)
        
        resetbutton = Gtk.Button.new_with_label("Reset")
        #resetbutton.get_style_context().add_class("dangerbutton")
        resetbutton.connect("clicked", self.reset_fields )
        resetbutton.set_halign(Gtk.Align.CENTER) # to avoid expansion horizontally
        #resetbutton.set_margin_left(20)
        
        gridd.add(forparty_label)
        gridd.attach(self.pnameentry, 1, 0, 1, 1)
        gridd.attach(translabel, 0, 1, 1, 1)
        gridd.attach(self.tscombo, 1, 1, 1, 1)
        gridd.attach(amount_label, 0, 3, 1, 1)
        gridd.attach(self.amountentry, 1, 3, 1, 1)
        gridd.attach(indatelabel, 0, 4, 1, 1)
        gridd.attach(self.indate, 1, 4, 1, 1)
        gridd.attach(voucherlabel, 0, 5, 1, 1)
        gridd.attach(self.v, 1, 5, 1, 1)
        gridd.attach(comments_label, 0, 6, 1, 1)
        gridd.attach(self.commentsentry, 1, 6, 1, 1)
        #gridd.attach(savebutton, 1, 9, 1, 1)
        #gridd.attach(resetbutton, 2, 9, 1, 1)
        
        inwheaderbox.pack_start(gridd, False, False, 0)   
        
        h_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)    
        h_box.set_margin_top(10)
        h_box.set_margin_left(300)
        h_box.pack_start(savebutton, False, False, 0)   
        h_box.pack_start(resetbutton, False, False, 0)   
        
        view_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)               
        view_box.pack_start(inwheaderbox, False, False, 0)       
        view_box.pack_start(h_box, False, False, 0)   
        
        view_box.show_all()
        inwmasterbox.pack_start(view_box, False, False, True) 
          
        return inwmasterbox
        
    
    def reset_fields(self, button):       
        self.pnameentry.set_text("")   
        #self.tscombo.get_child().set_text("")  #only if combobox new with text
        self.amountentry.set_text("")  
        self.indate.set_text(functions.todaysdate_string)  
        self.v.set_text("")  
        self.commentsentry.set_text("")  
        
        
    def generate_statement(self, trigger):       
        partyname=str(self.pnameentry.get_text())   
        edate=str(self.indate.get_text())
        vnumber=str(self.v.get_text())
        creditamount=str(self.amountentry.get_text())  
        typetransaction=str(self.tscombo.get_active_text()) 
        comments=str(self.commentsentry.get_text())
        
        #date format checking mechanism, very basic
        date_chker=functions.check_date_format(edate)
        if date_chker=='valid':
            proceed_signal_date='y'
            
        else:
            proceed_signal_date='n'
            #print('date format incorrent')
            guicommon.simpledialogins.display_message(self.mainwindow, 'Error', 'Check date', 'Incorrect date format', '' )   
        #print(proceed_signal_date)
       
        checker=guicommon.companytableins.readrow(partyname)
        if checker=='not_found_row':
            proceed_signal_companyname='n'
            guicommon.simpledialogins.display_message(self.mainwindow, 'Error', 'Company not found in records', 'Check party name or create new before proceeding', '' )   
        else:
            proceed_signal_companyname='y'    
        
        # amount numbers checking mechanism          
        try:
            creditfloat=float(creditamount)
            proceed_signal_amount='y'
            
        except:
            proceed_signal_amount='n'
            guicommon.simpledialogins.display_message(self.mainwindow, 'Error', 'Check amount', 'Amount should contain only numbers', '' )   
            
        if proceed_signal_amount=='y' and proceed_signal_companyname=='y' and proceed_signal_date=='y':
            data_collection=[partyname, edate, vnumber, creditamount, typetransaction, comments]
            statementprocessor.create_in_statement_entry(data_collection, 'newinwards')
            self.reset_fields('triggermimic') 
            
        
   #se_collection=guicommon.statementstableins.readrow(selectedparty) 
        
    def delete_state_entry(self, button):        
        partyname=self.ei_nameentry.get_text()
        edate=self.eindate.get_text()
        vnumber=self.ev.get_text()
        statementprocessor.delete_statement_entry(partyname, edate, vnumber)
        
       
