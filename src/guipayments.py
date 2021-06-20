import sys
import gi
from submods import functions
from submods import dbmani
from submods import guicommon
from submods import guistatements
from submods import guiinwards
from submods import guieditinwards
from datetime import datetime

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class GtkPayments():
            
    
    def generatepage(self, mainwindow):
           
        paymentsmasterbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
                
        paymentsstack = Gtk.Stack()
        paymentsstack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        paymentsstack.set_transition_duration(1000)        
        
        #journalbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        #journal_ins=guijournal.GtkJournal()
        #journalholder=journal_ins.generatepage(mainwindow)
        #journalbox.pack_start(journalholder, False, False, 0)
        
        statementsbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        statementsins=guistatements.GtkStatements()
        sph=statementsins.generatepage(mainwindow) 
        statementsbox.pack_start(sph, False, False, 0)
        
        inwardsbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        inwardsins=guiinwards.GtkInwards()
        iph=inwardsins.generatepage(mainwindow) 
        inwardsbox.pack_start(iph, False, False, 0)
        
        editinwardsbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        editinwardsins=guieditinwards.GtkEditInwards()
        eiph=editinwardsins.generatepage(mainwindow) 
        editinwardsbox.pack_start(eiph, False, False, 0)
        
        #expensesbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        #expensesins=guiexpenses.GtkExpenses()
        #eph=expensesins.generatepage(mainwindow) 
        #expensesbox.pack_start(eph, False, False, 0)
               
        #paymentsstack.add_titled(journalbox, "journalbox", "Journal")
        paymentsstack.add_titled(statementsbox, "statementsmainbox", "Statements")
        paymentsstack.add_titled(inwardsbox, "inwardsmainbox", "Record inwards")
        paymentsstack.add_titled(editinwardsbox, "editinwardsmainbox", "Modify inwards")
        #paymentsstack.add_titled(expensesbox, "expensesmainbox", "Expenses")

        paymentsstack_switcher = Gtk.StackSwitcher()
        paymentsstack_switcher.set_stack(paymentsstack)
         
        paymentsmasterbox.pack_start(paymentsstack_switcher, False, False, 10)
        paymentsmasterbox.pack_start(paymentsstack, True, True, 10)
            
        return paymentsmasterbox
