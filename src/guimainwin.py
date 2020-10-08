import sys
import gi
import guihome
import guiinvoicing
import guiinventory
import guicompany
import guimore
import time

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, applic): #applic is application instance
        super(MainWindow, self).__init__(title="Orteal Billing", application=applic, name="ortealbilling")        
        
        #self.set_default_size(280, 180)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(10)
        
        guihomeins=guihome.GtkHome()
        guiinvoicingins=guiinvoicing.GtkInvoicing()
        guiinventoryins=guiinventory.GtkInventory()
        guicompanyins=guicompany.GtkCompany() 
        guimoreins=guimore.GtkMore()       
        
        mainbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.add(mainbox)

        leftvbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        mainbox.add(leftvbox)
        
        rightvbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        mainbox.add(rightvbox)        

        stack = Gtk.Stack()
        stack.set_hexpand(True)
        stack.set_vexpand(True)
        rightvbox.pack_start(stack, True, True, 0)
        
        stacksidebar = Gtk.StackSidebar()
        stacksidebar.set_stack(stack)
        leftvbox.pack_start(stacksidebar, True, True, 0)
        
        homebox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        hph=guihomeins.generatepage() #hph home page holder
        homebox.add(hph)
        stack.add_titled(homebox, "homepage", "Home")
        
        invoicingbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        bph=guiinvoicingins.billingpage()
        invoicingbox.add(bph)
        stack.add_titled(invoicingbox, "billboxmain", "Invoicing") 
        #invoicingbox_pass=[invoicingbox, bph, guiinvoicingins]   
        
        #invoicingsw = Gtk.ScrolledWindow() #invoicing page scroll window
        #invoicingsw.add(invoicingbox)
        #stack.add_titled(invoicingsw, "billboxmainsw", "Invoicing")            
        
        inventorybox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        iph=guiinventoryins.generatepage(invoicingbox, bph, guiinvoicingins) #iph=inventory page holder
        inventorybox.add(iph)
        stack.add_titled(inventorybox, "inventorymain", "Inventory")
        #print("Inventory box loaded, now trying loading Create box")        
        
        companybox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)        
        cph=guicompanyins.generatepage(guiinvoicingins) # company page holder
        companybox.add(cph)
        stack.add_titled(companybox, "companyboxmain", "Company")        
        
        #paymentbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        #stack.add_titled(paymentbox, "paymentmain", "Payments")
        
        #ledgerbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        #stack.add_titled(ledgerbox, "ledgermain", "Ledger")
        
        #reportsbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        #stack.add_titled(reportsbox, "reportsboxmain", "Reports")              
        
        morebox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        mph=guimoreins.generatepage(applic) #mph=more page holder
        morebox.add(mph)
        stack.add_titled(morebox, "moremain", "More")
        
        style_provider = Gtk.CssProvider()      
        style_provider.load_from_path("submods/styl.css")
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
              
        #print("GUI creating done, reporting from main window")        
